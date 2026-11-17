# Citewise

Citewise is a RAG application. A user asks a question, the app retrieves the
most relevant chunks from a document set, and Claude answers using only those
chunks, citing the source file names.

The backend is Python 3.12 with FastAPI. Retrieval combines ChromaDB for vector
search with BM25 for keyword search. The frontend is a React app built with
Vite, using a streaming chat interface.
