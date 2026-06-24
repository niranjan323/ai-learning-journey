# 🧩 RAG Assistant

A general-purpose retrieval-augmented Q&A assistant over a custom knowledge base
(docs, notes, wikis, or mixed sources).

## 🎯 Goal

Build a reusable assistant that ingests a folder of documents and answers
questions about them with grounded, cited responses.

## 🧱 Planned Architecture

```
Knowledge base (md / txt / pdf) → ingestion pipeline → vector store
                                                            │
        Query → retriever → reranker (optional) → LLM → grounded answer
```

## 🛠️ Likely Stack

- Loaders: LangChain document loaders
- Embeddings + vector store: Chroma / FAISS
- Orchestration: LangChain (and LangGraph for control flow)
- Interface: CLI or Streamlit

## 🔗 Modules Used

- 08 RAG · 09 LangChain · 10 LangGraph

## 🗺️ Status

> 🚧 Planned — extends the PDF Chatbot into a multi-source assistant.
