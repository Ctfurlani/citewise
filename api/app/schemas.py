"""Request and response shapes for the HTTP API.

Pydantic validates incoming JSON against these models, so a bad request is
rejected with a 422 before any retrieval or model call happens.
"""

from typing import Literal

from pydantic import BaseModel, Field

Mode = Literal["vector", "hybrid", "hybrid+rerank"]


class Source(BaseModel):
    """One document the answer cited."""

    source: str = Field(description="file name of the document, e.g. bm25.md")
    snippet: str = Field(description="the start of the chunk the answer used")


class AskRequest(BaseModel):
    """A question about the indexed documents."""

    question: str = Field(min_length=1, max_length=2000)
    mode: Mode = "hybrid+rerank"


class AskResponse(BaseModel):
    """The answer plus the documents it cited."""

    answer: str
    sources: list[Source]
