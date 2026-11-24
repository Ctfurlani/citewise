"""HTTP tests for the API. No Claude calls: retrieval and generation are faked."""

import os
from collections.abc import AsyncIterator

# The app builds an AsyncAnthropic client at startup, which needs a key to
# exist. Set a dummy one when .env has not provided a real one.
os.environ.setdefault("ANTHROPIC_API_KEY", "test-key")

import pytest
from fastapi.testclient import TestClient

from app import main

CHUNKS = [
    ("bm25.md", "BM25 ranks documents by term frequency and document length."),
    ("tf-idf.md", "TF-IDF weights a term by how rare it is across the corpus."),
]
ANSWER = "BM25 is a ranking function (source: bm25.md)."


async def fake_answer(client: object, question: str, chunks: list[tuple[str, str]]) -> str:
    return ANSWER


async def fake_stream(
    client: object, question: str, chunks: list[tuple[str, str]]
) -> AsyncIterator[str]:
    for piece in ("BM25 is ", "a ranking function (source: bm25.md)."):
        yield piece


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch) -> TestClient:
    monkeypatch.setattr(main, "retrieve", lambda *args, **kwargs: CHUNKS)
    monkeypatch.setattr(main, "answer", fake_answer)
    monkeypatch.setattr(main, "stream_answer", fake_stream)
    with TestClient(main.app) as test_client:
        yield test_client


def test_health_is_ok(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ask_returns_answer_and_only_cited_sources(client: TestClient) -> None:
    response = client.post("/ask", json={"question": "What is BM25?"})

    assert response.status_code == 200
    body = response.json()
    assert body["answer"] == ANSWER
    assert [source["source"] for source in body["sources"]] == ["bm25.md"]
    assert body["sources"][0]["snippet"].startswith("BM25 ranks documents")


def test_ask_rejects_an_empty_question(client: TestClient) -> None:
    response = client.post("/ask", json={"question": ""})

    assert response.status_code == 422


def test_ask_stream_sends_tokens_then_sources_then_done(client: TestClient) -> None:
    response = client.post("/ask/stream", json={"question": "What is BM25?"})

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/event-stream")
    body = response.text
    assert body.count("event: token") == 2
    assert '"text": "BM25 is "' in body
    assert body.index("event: token") < body.index("event: sources") < body.index("event: done")
    assert '"source": "bm25.md"' in body
