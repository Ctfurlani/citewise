"""End-to-end eval: retrieve, answer, then score retrieval and the answer.

Scores four things per question:

- retrieval  hit rate and MRR, by checking whether the expected source file
             shows up in the retrieved chunks and at which rank (deterministic)
- citations  whether every file the answer cites was actually in the context,
             and whether the expected source is among them (deterministic)
- faithfulness  whether every claim in the answer is supported by the context,
                judged by a Claude model that sees only context and answer

Writes a JSON report to evals/results/ and exits 1 if a --min-* gate fails,
so CI can use it as a check.

Usage:
    python evals/run_evals.py --no-judge --limit 3      # cheap smoke test
    python evals/run_evals.py --min-hit-rate 0.8        # full run

Every question calls the answer model, and by default the judge model too, so
a run costs money. --no-judge halves the calls; --limit shortens the run.
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

EVALS_DIR = Path(__file__).resolve().parent
API_DIR = EVALS_DIR.parent / "api"
sys.path.insert(0, str(API_DIR))

import anthropic  # noqa: E402
import chromadb  # noqa: E402
from dotenv import load_dotenv  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402

from app.rag.simple_rag import (  # noqa: E402
    CHROMA_DIR,
    COLLECTION,
    DOCS_DIR,
    MODEL,
    answer,
    build_context,
    cited_sources,
    index,
    load_docs,
    retrieve,
)

DEFAULT_QUESTIONS = EVALS_DIR / "questions.jsonl"
RESULTS_DIR = EVALS_DIR / "results"
JUDGE_MODEL = "claude-sonnet-5-5"

JUDGE_SYSTEM = """You grade one answer produced by a retrieval system.

You are given the question, the context blocks the system retrieved, and the
answer it wrote. Each context block starts with a [source: file] header.

Grade only grounding, never whether the answer matches your own knowledge:

- supported: true only if every factual claim in the answer can be traced to
  the context. An answer that says it does not know, when the context really
  does not contain the answer, counts as supported.
- citation_supports: true only if every (source: file) citation in the answer
  points at a context block that actually backs the claim it is attached to.
  An answer with no citations and no factual claims counts as true; an answer
  with factual claims and no citation is false.
- reason: one short sentence naming the worst problem, or "ok".
"""


class Verdict(BaseModel):
    """The judge's grading of one answer."""

    supported: bool = Field(description="every claim is traceable to the context")
    citation_supports: bool = Field(description="every citation backs the claim it marks")
    reason: str = Field(description="one short sentence, or 'ok'")


def load_questions(path: Path) -> list[dict[str, str]]:
    """Read one JSON object per non-empty line."""
    lines = (line.strip() for line in path.read_text(encoding="utf-8").splitlines())
    return [json.loads(line) for line in lines if line]


def first_rank(sources: list[str], expected: str) -> int:
    """Return the 1-based rank of the first chunk from `expected`, or 0 if absent."""
    for rank, source in enumerate(sources, start=1):
        if source == expected:
            return rank
    return 0


def judge(question: str, chunks: list[tuple[str, str]], text: str, model: str) -> Verdict:
    """Ask a Claude model whether the answer is grounded in the context."""
    client = anthropic.Anthropic()
    prompt = (
        f"Question: {question}\n\n"
        f"Context:\n\n{build_context(chunks)}\n\n"
        f"Answer:\n\n{text}"
    )
    response = client.messages.parse(
        model=model,
        max_tokens=2000,
        output_config={"effort": "low"},
        system=JUDGE_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
        output_format=Verdict,
    )
    parsed = response.parsed_output
    if parsed is None:
        return Verdict(supported=False, citation_supports=False, reason="judge returned no verdict")
    return parsed


def evaluate_one(
    collection, question: dict[str, str], top_k: int, mode: str, judge_model: str | None
) -> dict:
    """Run one question through the pipeline and score it."""
    expected = question["expected_source"]
    chunks = retrieve(collection, question["question"], k=top_k, mode=mode)
    sources = [source for source, _ in chunks]
    retrieved = set(sources)

    row: dict = {
        "question": question["question"],
        "expected_source": expected,
        "retrieved_sources": sources,
        "rank": first_rank(sources, expected),
        "answer": None,
        "cited": [],
        "citation_subset": None,
        "citation_expected": None,
        "judge": None,
    }
    if not chunks:
        return row

    text = answer(question["question"], chunks)
    cited = cited_sources(text)
    row["answer"] = text
    row["cited"] = cited
    # No citation at all counts as a failure: the answer is unattributable.
    row["citation_subset"] = bool(cited) and all(name in retrieved for name in cited)
    row["citation_expected"] = expected in cited

    if judge_model:
        verdict = judge(question["question"], chunks, text, judge_model)
        row["judge"] = verdict.model_dump()
    return row


def mean(values: list[float]) -> float:
    """Average, or 0.0 for an empty list."""
    return sum(values) / len(values) if values else 0.0


def aggregate(rows: list[dict], top_k: int) -> dict[str, float | int]:
    """Reduce the per-question rows to the report metrics."""
    ranks = [row["rank"] for row in rows]
    metrics: dict[str, float | int] = {
        "n": len(rows),
        "hit_rate": mean([float(0 < rank <= top_k) for rank in ranks]),
        "hit_rate_at_1": mean([float(rank == 1) for rank in ranks]),
        "mrr": mean([1.0 / rank if rank else 0.0 for rank in ranks]),
        "citation_subset": mean([float(bool(row["citation_subset"])) for row in rows]),
        "citation_expected": mean([float(bool(row["citation_expected"])) for row in rows]),
    }
    judged = [row["judge"] for row in rows if row["judge"]]
    if judged:
        metrics["faithfulness"] = mean([float(v["supported"]) for v in judged])
        metrics["citation_supports"] = mean([float(v["citation_supports"]) for v in judged])
    return metrics


def parse_args() -> argparse.Namespace:
    """Read the command line."""
    parser = argparse.ArgumentParser(description="Score the RAG pipeline end to end.")
    parser.add_argument("--questions", type=Path, default=DEFAULT_QUESTIONS)
    parser.add_argument(
        "--mode", default="hybrid+rerank", choices=["vector", "hybrid", "hybrid+rerank"]
    )
    parser.add_argument("--top-k", type=int, default=4, help="chunks retrieved per question")
    parser.add_argument("--limit", type=int, help="only run the first N questions")
    parser.add_argument("--judge-model", default=JUDGE_MODEL, help="model that grades answers")
    parser.add_argument(
        "--no-judge",
        action="store_true",
        help="skip the LLM judge: retrieval and citation metrics only (cheaper)",
    )
    parser.add_argument(
        "--min-hit-rate", type=float, default=0.0, help="exit 1 if hit rate is below this"
    )
    parser.add_argument(
        "--min-faithfulness", type=float, help="exit 1 if faithfulness is below this"
    )
    return parser.parse_args()


def write_report(report: dict) -> Path:
    """Save the report under evals/results/ and return its path."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    stamp = report["run"]["started_at"].replace(":", "").replace("-", "")
    path = RESULTS_DIR / f"{stamp}.json"
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def print_rows(rows: list[dict]) -> None:
    """Print one line per question so failures are easy to spot."""
    print(f"{'rank':>4}  {'cite':>4}  {'faith':>5}  question")
    for row in rows:
        verdict = row["judge"]
        faith = "-" if verdict is None else ("ok" if verdict["supported"] else "FAIL")
        cite = "ok" if row["citation_subset"] and row["citation_expected"] else "FAIL"
        rank = row["rank"] or "-"
        print(f"{rank:>4}  {cite:>4}  {faith:>5}  {row['question'][:70]}")


def main() -> None:
    args = parse_args()
    load_dotenv(API_DIR.parent / ".env")
    judge_model = None if args.no_judge else args.judge_model

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    collection = client.get_or_create_collection(COLLECTION)
    if collection.count() == 0:
        print(f"Indexed {index(collection, load_docs(DOCS_DIR))} chunks.")

    questions = load_questions(args.questions)
    if args.limit:
        questions = questions[: args.limit]
    print(
        f"{len(questions)} questions from {args.questions.name}, mode={args.mode}, "
        f"top_k={args.top_k}, judge={judge_model or 'off'}\n"
    )

    rows = [
        evaluate_one(collection, question, args.top_k, args.mode, judge_model)
        for question in questions
    ]
    metrics = aggregate(rows, args.top_k)

    report = {
        "run": {
            "started_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "questions_file": str(args.questions),
            "mode": args.mode,
            "top_k": args.top_k,
            "answer_model": MODEL,
            "judge_model": judge_model,
        },
        "metrics": metrics,
        "questions": rows,
    }
    path = write_report(report)

    print_rows(rows)
    print()
    for name, value in metrics.items():
        print(f"{name:<20}{value:.0%}" if isinstance(value, float) else f"{name:<20}{value}")
    print(f"\nReport: {path}")

    failures = []
    if metrics["hit_rate"] < args.min_hit_rate:
        failures.append(f"hit_rate {metrics['hit_rate']:.0%} < {args.min_hit_rate:.0%}")
    if args.min_faithfulness is not None:
        faithfulness = metrics.get("faithfulness")
        if faithfulness is None:
            failures.append("--min-faithfulness needs the judge, but it was off")
        elif faithfulness < args.min_faithfulness:
            failures.append(f"faithfulness {faithfulness:.0%} < {args.min_faithfulness:.0%}")

    if failures:
        print("FAIL: " + "; ".join(failures))
        sys.exit(1)
    print("PASS")


if __name__ == "__main__":
    main()
