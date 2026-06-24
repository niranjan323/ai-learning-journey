# 🤖 AI Agent

An autonomous, tool-using agent that plans, acts, and iterates toward a goal —
the capstone project of this journey.

## 🎯 Goal

Build an agent that, given a goal, can reason about steps, call tools
(search, calculator, retrieval, APIs), observe results, and continue until done.

## 🧱 Planned Architecture

```
Goal → ┌─────────┐   ┌────────┐   ┌─────────┐
       │ reason  │──►│  act   │──►│ observe │──┐
       └─────────┘   └────────┘   └─────────┘  │
            ▲                                   │
            └───────────── loop ────────────────┘
                         │ done
                         ▼
                      Final answer
```

## 🛠️ Likely Stack

- Control flow: LangGraph (stateful agent loop)
- Tools: web search, calculator, retriever, custom functions
- Memory: short-term context + vector store for long-term
- Model: Claude / GPT with tool calling

## 🔗 Modules Used

- 09 LangChain · 10 LangGraph · 11 Agentic AI (and 08 RAG for memory)

## 🗺️ Status

> 🚧 Planned — the final capstone, built after completing all modules.
