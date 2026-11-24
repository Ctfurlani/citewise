"""FastAPI app: ask questions about the indexed documents, with citations."""

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from functools import partial

import anthropic
import chromadb
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from starlette.concurrency import run_in_threadpool

from app.rag.generate import answer, select_sources, sse, stream_answer
from app.rag.simple_rag import API_DIR, CHROMA_DIR, COLLECTION, retrieve
from app.schemas import AskRequest, AskResponse

log = logging.getLogger(__name__)

NO_DOCS = "I don't know (no documents indexed)."
# Browsers and proxies buffer by default, which holds back the stream.
SSE_HEADERS = {"Cache-Control": "no-cache", "X-Accel-Buffering": "no"}


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Open the Chroma collection and the Claude client once per process."""
    load_dotenv(API_DIR.parent / ".env")
    chroma = chromadb.PersistentClient(path=str(CHROMA_DIR))
    app.state.collection = chroma.get_or_create_collection(COLLECTION)
    app.state.claude = anthropic.AsyncAnthropic()
    yield
    await app.state.claude.close()


app = FastAPI(title="Citewise", lifespan=lifespan)


@app.get("/health")
async def health() -> dict[str, str]:
    """Liveness check: no retrieval, no model call."""
    return {"status": "ok"}


async def _retrieve(request: Request, ask: AskRequest) -> list[tuple[str, str]]:
    """Run the blocking retrieval (Chroma, BM25, rerank) off the event loop."""
    call = partial(retrieve, request.app.state.collection, ask.question, mode=ask.mode)
    return await run_in_threadpool(call)


@app.post("/ask", response_model=AskResponse)
async def ask(ask: AskRequest, request: Request) -> AskResponse:
    """Answer a question from the indexed documents and list the sources."""
    chunks = await _retrieve(request, ask)
    if not chunks:
        return AskResponse(answer=NO_DOCS, sources=[])
    text = await answer(request.app.state.claude, ask.question, chunks)
    return AskResponse(answer=text, sources=select_sources(text, chunks))


async def _ask_events(request: Request, ask: AskRequest) -> AsyncIterator[str]:
    """Stream the answer as `token` events, then one `sources` event, then `done`."""
    chunks = await _retrieve(request, ask)
    if not chunks:
        yield sse("token", {"text": NO_DOCS})
        yield sse("sources", {"sources": []})
        yield sse("done", {})
        return

    parts: list[str] = []
    try:
        async for text in stream_answer(request.app.state.claude, ask.question, chunks):
            parts.append(text)
            yield sse("token", {"text": text})
    except Exception:
        # The 200 and the headers are already sent, so errors travel as an event.
        log.exception("streaming answer failed")
        yield sse("error", {"message": "generation failed"})
        return

    # Citations only exist once the whole answer is in, so sources come last.
    sources = select_sources("".join(parts), chunks)
    yield sse("sources", {"sources": [s.model_dump() for s in sources]})
    yield sse("done", {})


@app.post("/ask/stream")
async def ask_stream(ask: AskRequest, request: Request) -> StreamingResponse:
    """Same answer as /ask, streamed as server-sent events."""
    return StreamingResponse(
        _ask_events(request, ask),
        media_type="text/event-stream",
        headers=SSE_HEADERS,
    )
