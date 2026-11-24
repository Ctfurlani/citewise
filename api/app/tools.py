"""Tools Claude may call during /ask.

A tool is just a JSON schema sent with the request. Claude never runs code:
it asks for a tool by name, this module runs the function, and the caller
sends the result back (see app/rag/generate.py for that loop).
"""

from datetime import UTC, datetime
from typing import Any

from anthropic.types import ToolParam

DATE_TOOL: ToolParam = {
    "name": "get_current_date",
    "description": (
        "Return today's date as an ISO 8601 date in UTC, e.g. 2026-11-24. "
        "Use it when the question mentions today, now, this year, or asks how "
        "long ago something happened."
    ),
    "input_schema": {
        "type": "object",
        "properties": {},
        "required": [],
        "additionalProperties": False,
    },
    "strict": True,
}

TOOLS: list[ToolParam] = [DATE_TOOL]


def get_current_date() -> str:
    """Return today's UTC date, e.g. "2026-11-24"."""
    return datetime.now(UTC).date().isoformat()


def run_tool(name: str, params: dict[str, Any]) -> str:
    """Run the tool Claude asked for and return its output as text."""
    if name == "get_current_date":
        return get_current_date()
    raise ValueError(f"unknown tool: {name}")
