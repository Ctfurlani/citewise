"""Async answer generation: one grounded call, a tool loop, and streaming.

simple_rag.answer is the synchronous version used by the CLI. The API needs
async, so these functions take an anthropic.AsyncAnthropic client.
"""

import json
from collections.abc import AsyncIterator, Iterable
from typing import Any

from anthropic import AsyncAnthropic
from anthropic.types import ContentBlock, MessageParam, ToolResultBlockParam

from app.rag.simple_rag import MODEL, SYSTEM, build_context, cited_sources
from app.schemas import Source
from app.tools import TOOLS, run_tool

MAX_TOKENS = 2000
# Cap on request/tool rounds, so a model that keeps calling tools cannot spin.
MAX_STEPS = 4
SNIPPET_CHARS = 300

TOOL_NOTE = """
You also have tools. A fact a tool returns counts as context: you may use it
and cite it as (source: tool name).
"""
SYSTEM_WITH_TOOLS = SYSTEM + TOOL_NOTE


def _question_message(question: str, chunks: list[tuple[str, str]]) -> MessageParam:
    """Build the user turn: the retrieved chunks as data, then the question."""
    context = build_context(chunks)
    return {"role": "user", "content": f"Context:\n\n{context}\n\nQuestion: {question}"}


def _text_of(blocks: Iterable[ContentBlock]) -> str:
    """Join the text blocks of a response, ignoring thinking and tool blocks."""
    return "\n".join(block.text for block in blocks if block.type == "text")


def _tool_results(blocks: Iterable[ContentBlock]) -> list[ToolResultBlockParam]:
    """Run every tool Claude asked for and return one result block per call.

    All results go back in a single user message. A failing tool returns an
    error result rather than being dropped: an unanswered tool_use block makes
    the next request invalid.
    """
    results: list[ToolResultBlockParam] = []
    for block in blocks:
        if block.type != "tool_use":
            continue
        params: dict[str, Any] = block.input if isinstance(block.input, dict) else {}
        try:
            content, is_error = run_tool(block.name, params), False
        except Exception as exc:  # a broken tool must still produce a result
            content, is_error = f"tool failed: {exc}", True
        results.append(
            {
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": content,
                "is_error": is_error,
            }
        )
    return results


async def answer(
    client: AsyncAnthropic,
    question: str,
    chunks: list[tuple[str, str]],
    *,
    model: str = MODEL,
) -> str:
    """Answer the question from the chunks, letting Claude call tools first.

    The loop: send the history, and if the reply stops with "tool_use", append
    that assistant turn plus the tool results and send everything again. The
    API is stateless, so the full history goes out every round.
    """
    messages: list[MessageParam] = [_question_message(question, chunks)]
    for _ in range(MAX_STEPS):
        response = await client.messages.create(
            model=model,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_WITH_TOOLS,
            tools=TOOLS,
            messages=messages,
        )
        if response.stop_reason != "tool_use":
            return _text_of(response.content)
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": _tool_results(response.content)})
    raise RuntimeError(f"tool loop did not finish within {MAX_STEPS} steps")


async def stream_answer(
    client: AsyncAnthropic,
    question: str,
    chunks: list[tuple[str, str]],
    *,
    model: str = MODEL,
) -> AsyncIterator[str]:
    """Yield the answer text as it is generated. No tools on this path."""
    async with client.messages.stream(
        model=model,
        max_tokens=MAX_TOKENS,
        system=SYSTEM,
        messages=[_question_message(question, chunks)],
    ) as stream:
        async for text in stream.text_stream:
            yield text


def select_sources(answer_text: str, chunks: list[tuple[str, str]]) -> list[Source]:
    """Return the retrieved chunks the answer cited, in citation order.

    Falls back to every retrieved chunk when the answer cited nothing, so the
    caller can always show what the answer was based on.
    """
    best: dict[str, str] = {}
    for source, text in chunks:  # keeps retrieval order, best chunk per source
        best.setdefault(source, text)
    cited = [name for name in cited_sources(answer_text) if name in best]
    names = cited or list(best)
    return [Source(source=name, snippet=best[name][:SNIPPET_CHARS]) for name in names]


def sse(event: str, data: dict[str, Any]) -> str:
    """Format one server-sent event: a named event and a JSON data line."""
    return f"event: {event}\ndata: {json.dumps(data)}\n\n"
