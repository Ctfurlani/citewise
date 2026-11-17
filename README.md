# Citewise

A RAG (retrieval-augmented generation) app: ask a question about a set of local
documents, and get an answer that cites the files it came from.

Right now Citewise is a **command-line tool**. The retrieval and answering
pipeline works end to end and is covered by tests and evals. The FastAPI
service, the React frontend and the infra are planned but not built yet.

## How it works

```
docs/*.md  ->  chunk  ->  ChromaDB (embeddings)
                            |
question  ->  vector search + BM25  ->  RRF fusion  ->  Claude rerank  ->  top 4 chunks
                                                                              |
                                                            Claude answers, citing sources
```

1. **Index** — each document is split into ~500-word chunks (50-word overlap)
   and stored in ChromaDB, which also holds the embeddings.
2. **Retrieve** — three modes, picked with `--mode`:
   - `vector` — embedding similarity only.
   - `hybrid` — embedding search *and* BM25 keyword search, merged by
     reciprocal rank fusion (RRF). RRF uses only the rank of each chunk, so the
     two scores never have to be put on a common scale.
   - `hybrid+rerank` (default) — hybrid, then the top 10 candidates are scored
     0–10 by a small Claude model (Haiku) that reads the question and each
     passage together.
3. **Answer** — the top chunks are passed to Claude as labelled
   `[source: file]` data blocks. The system prompt allows only facts from those
   blocks, requires `(source: file.md)` citations, and requires the exact reply
   `I don't know` when the context lacks the answer.

Framing documents as labelled data blocks is also a guardrail: a document that
contains text like "ignore all previous instructions" is presented as data, not
as an instruction. `api/tests/test_guardrails.py` tests this.

## Layout

| Path | What |
|---|---|
| `api/app/rag/simple_rag.py` | Indexing, retrieval, prompting, CLI entry point |
| `api/app/rag/hybrid.py` | BM25, vector search, reciprocal rank fusion |
| `api/app/rag/rerank.py` | Claude-based reranking of candidates |
| `api/data/docs/` | The document corpus (~55 Wikipedia-style notes on IR and ML) |
| `api/data/chroma_db/` | Local ChromaDB store (git-ignored, rebuilt on demand) |
| `api/tests/` | pytest suite; `live`-marked tests call the real API |
| `evals/run_eval.py` | Retrieval-only eval: recall@1/2/4 across all three modes |
| `evals/run_evals.py` | End-to-end eval: hit rate, MRR, citations, faithfulness |
| `evals/questions.jsonl` | 20 hard questions; `questions-easy.jsonl` has 20 easy ones |
| `web/`, `infra/`, `docs/` | Empty placeholders for the planned frontend and infra |

## Setup

Requires Python 3.12.

```powershell
cd api
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Then put your Claude API key in a `.env` file at the repo root (git-ignored,
never commit it):

```
ANTHROPIC_API_KEY=sk-ant-...
```

## Usage

From the `api/` directory, with the venv active:

```powershell
python -m app.rag.simple_rag "What is reciprocal rank fusion?"
```

Expected output: a short answer followed by citations, e.g.

```
Reciprocal rank fusion merges several ranked result lists by scoring each
document as 1 / (k + rank) ... (source: learning-to-rank.md)
```

The first run indexes the corpus and prints `Indexed N chunks from ...` before
answering. Later runs reuse the store.

Useful flags:

```powershell
python -m app.rag.simple_rag "..." --reindex        # re-read the docs
python -m app.rag.simple_rag "..." --mode vector    # skip BM25 and reranking
python -m app.rag.simple_rag "..." --mode hybrid    # skip reranking only
```

A question the docs do not cover should print exactly `I don't know`.

## Tests

From `api/`:

```powershell
pytest
```

Expected output: `22 passed, 3 deselected`. The three deselected ones are
marked `live` because they call the real Claude API and cost money. To run them
too:

```powershell
pytest -m live
```

## Evals

Tests check that the code works; evals measure how *well* retrieval and
answering do. Run both from the repo root.

Retrieval only — compares all three modes on recall. Only the rerank mode
calls the API:

```powershell
python evals/run_eval.py
```

Expected output: a header line with the question and chunk counts, then one
row per mode with hits and a percentage at each cutoff:

```
20 questions from questions.jsonl, N chunks indexed.

mode                   recall@1      recall@2      recall@4
vector            ..
hybrid            ..
hybrid+rerank     ..
```

Recall should rise from `vector` to `hybrid` to `hybrid+rerank`, and rise with
the cutoff within a row. That ordering is the point of the eval: it is what
shows the BM25 fusion and the reranker are earning their cost.

End to end — also answers each question and grades the answer. This calls the
API for every question, so start with the cheap smoke test:

```powershell
python evals/run_evals.py --no-judge --limit 3
```

Expected output: metrics for 3 questions (hit rate, MRR, citation checks) and a
JSON report written to `evals/results/`. `--no-judge` skips the LLM judge, which
halves the API calls. For a full graded run with a CI-style gate:

```powershell
python evals/run_evals.py --min-hit-rate 0.8
```

That exits 1 if the hit rate falls below 0.8, so it can be used as a build check.

## Roadmap

- FastAPI service wrapping the pipeline, with streaming answers
- React (Vite) chat frontend in `web/`
- Docker image, Kubernetes manifests and a Jenkinsfile in `infra/`
- Architecture notes and a learning log in `docs/`
