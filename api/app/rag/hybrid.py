"""Hybrid retrieval: BM25 keyword search fused with ChromaDB vector search."""

import re
from dataclasses import dataclass

from chromadb.api.models.Collection import Collection
from rank_bm25 import BM25Okapi

RRF_K = 60
_WORD = re.compile(r"[a-z0-9]+")


@dataclass(frozen=True)
class Chunk:
    """One indexed piece of a document."""

    id: str
    source: str
    text: str


def tokenize(text: str) -> list[str]:
    """Lowercase the text and keep only alphanumeric words."""
    return _WORD.findall(text.lower())


def all_chunks(collection: Collection) -> list[Chunk]:
    """Read every chunk out of the collection, in a stable order.

    Chroma is the single source of truth, so the BM25 index and the vector
    index always cover exactly the same chunks.
    """
    result = collection.get(include=["documents", "metadatas"])
    chunks = [
        Chunk(id=cid, source=str(meta["source"]), text=doc)
        for cid, doc, meta in zip(result["ids"], result["documents"], result["metadatas"])
    ]
    return sorted(chunks, key=lambda c: c.id)


def bm25_search(chunks: list[Chunk], question: str, k: int) -> list[Chunk]:
    """Return the k best chunks for the question by BM25 keyword score."""
    if not chunks:
        return []
    bm25 = BM25Okapi([tokenize(c.text) for c in chunks])
    scores = bm25.get_scores(tokenize(question))
    ranked = sorted(zip(scores, chunks), key=lambda pair: (-pair[0], pair[1].id))
    return [chunk for _, chunk in ranked[:k]]


def vector_search(collection: Collection, question: str, k: int) -> list[Chunk]:
    """Return the k nearest chunks for the question by embedding similarity."""
    count = collection.count()
    if count == 0:
        return []
    result = collection.query(query_texts=[question], n_results=min(k, count))
    return [
        Chunk(id=cid, source=str(meta["source"]), text=doc)
        for cid, doc, meta in zip(
            result["ids"][0], result["documents"][0], result["metadatas"][0]
        )
    ]


def reciprocal_rank_fusion(ranked_lists: list[list[Chunk]], k: int = RRF_K) -> list[Chunk]:
    """Merge several ranked lists into one by reciprocal rank fusion.

    A chunk at 1-based rank r in a list contributes 1 / (k + r) to its score.
    Only ranks are used, so BM25 scores and cosine distances never have to be
    put on a common scale.
    """
    scores: dict[str, float] = {}
    seen: dict[str, Chunk] = {}
    for ranked in ranked_lists:
        for rank, chunk in enumerate(ranked, start=1):
            scores[chunk.id] = scores.get(chunk.id, 0.0) + 1.0 / (k + rank)
            seen.setdefault(chunk.id, chunk)
    order = sorted(scores.items(), key=lambda pair: (-pair[1], pair[0]))
    return [seen[cid] for cid, _ in order]


def hybrid_search(collection: Collection, question: str, candidates: int = 20) -> list[Chunk]:
    """Return chunks ranked by RRF over vector search and BM25 search."""
    vector = vector_search(collection, question, candidates)
    keyword = bm25_search(all_chunks(collection), question, candidates)
    return reciprocal_rank_fusion([vector, keyword])
