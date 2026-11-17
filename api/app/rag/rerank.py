"""Rerank merged retrieval results with a small Claude model.

The retriever is fast but only approximately relevant. Reranking reads the
question and each candidate chunk together and scores them, which catches
chunks that merely share keywords or sit nearby in embedding space.
"""

import anthropic
from pydantic import BaseModel, Field

from app.rag.hybrid import Chunk

RERANK_MODEL = "claude-haiku-5-5"
RERANK_CANDIDATES = 10

INSTRUCTIONS = """Score how well each numbered passage answers the question.

Use a 0-10 scale: 10 means the passage directly answers the question, 0 means
it is unrelated. Judge each passage on its own. Return one score per passage,
using the passage numbers exactly as given.
"""


class PassageScore(BaseModel):
    """One passage's relevance score, keyed by its position in the prompt."""

    index: int = Field(description="the passage number, starting at 0")
    relevance: int = Field(description="relevance from 0 (unrelated) to 10 (direct answer)")


class Ranking(BaseModel):
    """The model's scores for every passage it was shown."""

    scores: list[PassageScore]


def _prompt(question: str, chunks: list[Chunk]) -> str:
    """Build the user message listing the question and the numbered passages."""
    passages = "\n\n".join(f"[{i}] {chunk.text}" for i, chunk in enumerate(chunks))
    return f"Question: {question}\n\nPassages:\n\n{passages}"


def rerank(
    question: str,
    chunks: list[Chunk],
    top_k: int = 4,
    model: str = RERANK_MODEL,
) -> list[Chunk]:
    """Return the top_k chunks for the question, reordered by Claude's scores.

    Only the first RERANK_CANDIDATES chunks are sent. Any chunk the model does
    not score keeps a score of 0 and stays behind the ones it did score.
    """
    candidates = chunks[:RERANK_CANDIDATES]
    if len(candidates) <= 1:
        return candidates[:top_k]

    client = anthropic.Anthropic()
    response = client.messages.parse(
        model=model,
        max_tokens=2000,
        output_config={"effort": "low"},
        system=INSTRUCTIONS,
        messages=[{"role": "user", "content": _prompt(question, candidates)}],
        output_format=Ranking,
    )
    scored = response.parsed_output.scores if response.parsed_output else []
    return apply_scores(candidates, scored, top_k)


def apply_scores(
    chunks: list[Chunk],
    scores: list[PassageScore],
    top_k: int,
) -> list[Chunk]:
    """Sort chunks by their score, highest first, keeping the original order on ties."""
    by_index = {s.index: s.relevance for s in scores if 0 <= s.index < len(chunks)}
    ranked = sorted(
        enumerate(chunks),
        key=lambda pair: (-by_index.get(pair[0], 0), pair[0]),
    )
    return [chunk for _, chunk in ranked[:top_k]]
