# 09 — LangChain

A framework for building LLM applications by composing reusable components:
prompts, models, chains, tools, memory, and retrievers.

> 📦 **Course:** [LangChain: Chat with Your Data](https://www.deeplearning.ai/courses/langchain-chat-with-your-data) · ~16 hrs · Jul 23 – Jul 28

## 🎯 Learning Objectives

- Understand LangChain's core abstractions
- Compose prompts and models into chains (LCEL)
- Add memory for multi-turn conversations
- Connect tools and retrievers (RAG)
- Build a small end-to-end LLM application

## 🧩 Core Components

| Component | Purpose |
|-----------|---------|
| Models | Wrappers around LLMs / chat models |
| Prompts | Templated, reusable prompts |
| Chains (LCEL) | Compose steps with the `|` operator |
| Memory | Persist conversation state |
| Retrievers | Fetch context for RAG |
| Tools / Agents | Let the model call external functions |

## 🧪 Minimal Example

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("Explain {topic} simply.")
# chain = prompt | model | output_parser
# chain.invoke({"topic": "embeddings"})
```

## 📚 Recommended Resources

- LangChain documentation & "Introduction" tutorials
- LangChain Expression Language (LCEL) guide
