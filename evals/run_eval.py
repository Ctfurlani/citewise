"""Measure retrieval quality: how often the expected source is retrieved.

Runs every question in questions.jsonl through three retrieval modes and
prints recall at each cutoff. Only the rerank mode calls the Claude API.
"""

import json
import sys
from pathlib import Path

EVALS_DIR = Path(__file__).resolve().parent
API_DIR = EVALS_DIR.parent / "api"
sys.path.insert(0, str(API_DIR))

import chromadb  # noqa: E402
from dotenv import load_dotenv  # noqa: E402

from app.rag.hybrid import hybrid_search, vector_search  # noqa: E402
from app.rag.rerank import RERANK_CANDIDATES, rerank  # noqa: E402
from app.rag.simple_rag import CHROMA_DIR, COLLECTION, DOCS_DIR, index, load_docs  # noqa: E402

DEFAULT_QUESTIONS = EVALS_DIR / "questions.jsonl"
TOP_K = 4
CUTOFFS = (1, 2, 4)
MODES = ("vector", "hybrid", "hybrid+rerank")


def load_questions(path: Path) -> list[dict[str, str]]:
    """Read one JSON object per non-empty line."""
    lines = (line.strip() for line in path.read_text(encoding="utf-8").splitlines())
    return [json.loads(line) for line in lines if line]


def top_sources(collection, question: str, mode: str) -> list[str]:
    """Return the source file names of the top TOP_K chunks for one mode."""
    if mode == "vector":
        chunks = vector_search(collection, question, TOP_K)
    elif mode == "hybrid":
        chunks = hybrid_search(collection, question)[:TOP_K]
    elif mode == "hybrid+rerank":
        chunks = rerank(question, hybrid_search(collection, question)[:RERANK_CANDIDATES], TOP_K)
    else:
        raise ValueError(f"unknown mode: {mode}")
    return [chunk.source for chunk in chunks]


def main() -> None:
    load_dotenv(API_DIR.parent / ".env")
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    collection = client.get_or_create_collection(COLLECTION)
    if collection.count() == 0:
        print(f"Indexed {index(collection, load_docs(DOCS_DIR))} chunks.")

    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_QUESTIONS
    questions = load_questions(path)
    total = len(questions)
    print(f"{total} questions from {path.name}, {collection.count()} chunks indexed.\n")
    print(f"{'mode':<16}" + "".join(f"{'recall@' + str(n):>14}" for n in CUTOFFS))

    for mode in MODES:
        ranked = [top_sources(collection, q["question"], mode) for q in questions]
        cells = ""
        for cutoff in CUTOFFS:
            hits = sum(
                q["expected_source"] in sources[:cutoff]
                for q, sources in zip(questions, ranked)
            )
            cells += f"{hits:>6}/{total:<3}{hits / total if total else 0:>5.0%}"
        print(f"{mode:<16}{cells}")


if __name__ == "__main__":
    main()
