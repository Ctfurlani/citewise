"""Tests for the pure chunking logic in simple_rag."""

from app.rag.simple_rag import chunk


def test_chunk_short_text_is_one_chunk() -> None:
    assert chunk("a b c", size=500, overlap=50) == ["a b c"]


def test_chunk_empty_text_is_no_chunks() -> None:
    assert chunk("   ") == []


def test_chunk_respects_size_and_overlap() -> None:
    words = [str(i) for i in range(1000)]
    chunks = chunk(" ".join(words), size=500, overlap=50)

    # Steps of 450 words: 0-499, 450-949, 900-999.
    assert [len(c.split()) for c in chunks] == [500, 500, 100]
    assert chunks[0].split()[0] == "0"
    assert chunks[1].split()[0] == "450"


def test_chunk_overlap_repeats_boundary_words() -> None:
    chunks = chunk(" ".join(str(i) for i in range(120)), size=100, overlap=10)
    first_tail = chunks[0].split()[-10:]
    second_head = chunks[1].split()[:10]

    assert first_tail == second_head
