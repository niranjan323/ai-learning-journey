# 08 — Retrieval-Augmented Generation (RAG)

Give LLMs access to your own data. RAG retrieves relevant context from a
knowledge base and feeds it to the model so answers are grounded and current.

> 📦 **Course:** [Retrieval Augmented Generation (RAG)](https://www.deeplearning.ai/courses/retrieval-augmented-generation-rag) · ~40 hrs · Jul 9 – Jul 22

## 🎯 Learning Objectives

- Explain why and when to use RAG
- Build a document ingestion pipeline (load → chunk → embed → store)
- Use a vector database for similarity search
- Retrieve relevant context and inject it into a prompt
- Evaluate and reduce hallucination

## 🔄 The RAG Pipeline

```
Documents → Chunking → Embeddings → Vector Store
                                         │
User question → Embed → Similarity search┘ → Top-k chunks
                                         │
              Prompt (question + context) → LLM → Grounded answer
```

## 🧩 Key Concepts

- **Chunking** — splitting documents into retrievable pieces
- **Embeddings** — vector representations of text
- **Vector store** — FAISS, Chroma, Pinecone, etc.
- **Similarity search** — cosine / dot-product nearest neighbors
- **Context window management** — fitting retrieved chunks in the prompt
- **Citations** — pointing back to source documents

## 🛠️ Common Tools

- Vector stores: FAISS, Chroma
- Embeddings: OpenAI, Sentence-Transformers
- Orchestration: LangChain (module 09)

## 📚 Recommended Resources

- LangChain RAG tutorials
- "Retrieval-Augmented Generation" (Lewis et al., 2020)
