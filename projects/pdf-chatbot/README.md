# 📄 PDF Chatbot

Ask natural-language questions about your own PDF documents. A practical RAG
application that ties together embeddings, a vector store, and an LLM.

## 🎯 Goal

Upload one or more PDFs, then chat with them — getting answers grounded in the
document text, with citations.

## 🧱 Planned Architecture

```
PDF → extract text → chunk → embed → vector store
                                          │
User question → embed → retrieve top-k → prompt + context → LLM → answer
```

## 🛠️ Likely Stack

- PDF parsing: `pypdf`
- Embeddings: OpenAI / Sentence-Transformers
- Vector store: FAISS or Chroma
- Orchestration: LangChain
- UI: Streamlit (optional)

## 🔗 Modules Used

- 06 ChatGPT API · 07 Hugging Face · 08 RAG · 09 LangChain

## 🗺️ Status

> 🚧 Planned — to be built after completing modules 06–09.
