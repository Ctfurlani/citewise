"""Minimal RAG pipeline: index local docs in ChromaDB, answer questions with Claude."""

import argparse
import re
from pathlib import Path

import anthropic
import chromadb
from chromadb.api.models.Collection import Collection
from dotenv import load_dotenv

from app.rag.hybrid import hybrid_search, vector_search
from app.rag.rerank import RERANK_CANDIDATES, rerank

API_DIR = Path(__file__).resolve().parents[2]
DOCS_DIR = API_DIR / "data" / "docs"
CHROMA_DIR = API_DIR / "data" / "chroma_db"
COLLECTION = "docs"
MODEL = "claude-sonnet-5"

# Matches the citation format the system prompt asks for: "(source: notes.md)".
CITATION = re.compile(r"\(source:\s*([^)]+?)\s*\)", re.IGNORECASE)

SYSTEM = """You answer questions using only the context blocks given by the user.

Rules:
- Use only facts present in the context. Never use outside knowledge.
- Cite the source file names you used, like (source: notes.md).
- If the context does not contain the answer, reply exactly: I don't know
"""


def load_docs(docs_dir: Path) -> list[tuple[str, str]]:
    """Return (file name, text) for every .md and .txt file in docs_dir."""
    paths = sorted(p for p in docs_dir.iterdir() if p.suffix in {".md", ".txt"})
    return [(p.name, p.read_text(encoding="utf-8")) for p in paths]


def chunk(text: str, size: int = 500, overlap: int = 50) -> list[str]:
    """Split text into ~`size`-word chunks that overlap by `overlap` words."""
    words = text.split()
    if not words:
        return []
    step = size - overlap
    return [" ".join(words[i : i + size]) for i in range(0, len(words), step)]


def index(collection: Collection, docs: list[tuple[str, str]]) -> int:
    """Add every chunk of every doc to the collection. Returns chunk count."""
    ids: list[str] = []
    texts: list[str] = []
    metadatas: list[dict[str, str]] = []
    for name, text in docs:
        for i, piece in enumerate(chunk(text)):
            ids.append(f"{name}:{i}")
            texts.append(piece)
            metadatas.append({"source": name})
    if ids:
        collection.upsert(ids=ids, documents=texts, metadatas=metadatas)
    return len(ids)


def retrieve(
    collection: Collection, question: str, k: int = 4, mode: str = "hybrid+rerank"
) -> list[tuple[str, str]]:
    """Return the k best (source file name, chunk text) pairs for the question.

    Modes: "vector" (embeddings only), "hybrid" (embeddings fused with BM25),
    "hybrid+rerank" (hybrid, then scored by a small Claude model).
    """
    if mode == "vector":
        chunks = vector_search(collection, question, k)
    elif mode == "hybrid":
        chunks = hybrid_search(collection, question)[:k]
    elif mode == "hybrid+rerank":
        chunks = rerank(question, hybrid_search(collection, question)[:RERANK_CANDIDATES], k)
    else:
        raise ValueError(f"unknown mode: {mode}")
    return [(chunk.source, chunk.text) for chunk in chunks]


def cited_sources(text: str) -> list[str]:
    """Return the file names cited in an answer, in order, without duplicates."""
    seen: list[str] = []
    for match in CITATION.findall(text):
        for name in (part.strip() for part in match.split(",")):
            if name and name not in seen:
                seen.append(name)
    return seen


def build_context(chunks: list[tuple[str, str]]) -> str:
    """Frame the retrieved chunks as labelled data blocks for the prompt.

    Every chunk gets a "[source: name]" header so the model can cite it, and so
    document text is presented to the model as data, not as instructions.
    """
    return "\n\n".join(f"[source: {source}]\n{text}" for source, text in chunks)


def answer(question: str, chunks: list[tuple[str, str]]) -> str:
    """Ask Claude the question, grounded in the retrieved chunks."""
    context = build_context(chunks)
    client = anthropic.Anthropic()
    response = client.messages.create(
        model=MODEL,
        max_tokens=2000,
        system=SYSTEM,
        messages=[{"role": "user", "content": f"Context:\n\n{context}\n\nQuestion: {question}"}],
    )
    return "\n".join(block.text for block in response.content if block.type == "text")


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask a question about the local docs.")
    parser.add_argument("question", help="the question to answer")
    parser.add_argument("--reindex", action="store_true", help="re-read and re-index the docs")
    parser.add_argument(
        "--mode",
        default="hybrid+rerank",
        choices=["vector", "hybrid", "hybrid+rerank"],
        help="how to retrieve chunks (default: hybrid+rerank)",
    )
    args = parser.parse_args()

    load_dotenv(API_DIR.parent / ".env")
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    collection = client.get_or_create_collection(COLLECTION)

    if args.reindex or collection.count() == 0:
        count = index(collection, load_docs(DOCS_DIR))
        print(f"Indexed {count} chunks from {DOCS_DIR}.")

    chunks = retrieve(collection, args.question, mode=args.mode)
    if not chunks:
        print("I don't know (no documents indexed).")
        return
    print(answer(args.question, chunks))


if __name__ == "__main__":
    main()
