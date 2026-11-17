"""Tests for the pure retrieval logic in hybrid: tokenizing, BM25, and RRF."""

from app.rag.hybrid import Chunk, bm25_search, reciprocal_rank_fusion, tokenize

CHUNKS = [
    Chunk(id="a:0", source="a.md", text="Chunks overlap by fifty words."),
    Chunk(id="b:0", source="b.md", text="The frontend is a React app built with Vite."),
    Chunk(id="c:0", source="c.md", text="Nothing relevant here at all."),
    Chunk(id="d:0", source="d.md", text="Filler text for ranking tests."),
]


def test_tokenize_lowercases_and_drops_punctuation() -> None:
    assert tokenize("Vite, React-Router 7!") == ["vite", "react", "router", "7"]


def test_tokenize_empty_text_is_no_tokens() -> None:
    assert tokenize("  ,.! ") == []


def test_bm25_ranks_the_matching_chunk_first() -> None:
    assert bm25_search(CHUNKS, "which build tool does React use", k=4)[0].id == "b:0"


def test_bm25_respects_k() -> None:
    assert len(bm25_search(CHUNKS, "overlap", k=2)) == 2


def test_bm25_on_empty_corpus_is_empty() -> None:
    assert bm25_search([], "anything", k=4) == []


def test_rrf_prefers_a_chunk_ranked_well_by_both_lists() -> None:
    a, b, c, d = CHUNKS
    # b is 2nd in both (2/62 = 0.03226); a is 1st then last (1/61 + 1/64 = 0.03202).
    merged = reciprocal_rank_fusion([[a, b, c, d], [d, b, c, a]])

    assert merged[0].id == "b:0"
    assert {chunk.id for chunk in merged} == {"a:0", "b:0", "c:0", "d:0"}


def test_rrf_scores_use_rank_only() -> None:
    a, b = CHUNKS[0], CHUNKS[1]
    # Appearing 1st in both lists beats appearing 1st in one and last in none.
    assert reciprocal_rank_fusion([[a, b], [a, b]])[0].id == "a:0"


def test_rrf_deduplicates_across_lists() -> None:
    a = CHUNKS[0]
    assert [chunk.id for chunk in reciprocal_rank_fusion([[a], [a]])] == ["a:0"]


def test_rrf_of_no_lists_is_empty() -> None:
    assert reciprocal_rank_fusion([]) == []


def test_apply_scores_sorts_by_relevance() -> None:
    from app.rag.rerank import PassageScore, apply_scores

    a, b, c, d = CHUNKS
    scores = [
        PassageScore(index=0, relevance=1),
        PassageScore(index=1, relevance=9),
        PassageScore(index=2, relevance=5),
        PassageScore(index=3, relevance=0),
    ]

    assert [x.id for x in apply_scores([a, b, c, d], scores, top_k=2)] == ["b:0", "c:0"]


def test_apply_scores_keeps_unscored_chunks_last_in_original_order() -> None:
    from app.rag.rerank import PassageScore, apply_scores

    a, b, c = CHUNKS[:3]
    ranked = apply_scores([a, b, c], [PassageScore(index=2, relevance=7)], top_k=3)

    assert [x.id for x in ranked] == ["c:0", "a:0", "b:0"]


def test_apply_scores_ignores_out_of_range_indexes() -> None:
    from app.rag.rerank import PassageScore, apply_scores

    a, b = CHUNKS[:2]
    scores = [PassageScore(index=99, relevance=10), PassageScore(index=1, relevance=4)]

    assert [x.id for x in apply_scores([a, b], scores, top_k=2)] == ["b:0", "a:0"]
