# 10 — LangGraph

Build **stateful**, graph-based LLM workflows. Where LangChain composes linear
chains, LangGraph models applications as graphs with nodes, edges, loops, and
shared state — ideal for agents that need control flow.

> 📦 **Course:** [Long-Term Agentic Memory with LangGraph](https://www.deeplearning.ai/courses/long-term-agentic-memory-with-langgraph) · ~16 hrs · Jul 29 – Aug 3

## 🎯 Learning Objectives

- Model an application as a graph of nodes and edges
- Manage shared, typed state across steps
- Add conditional edges, branches, and loops
- Build cyclic agent workflows (reason → act → observe)
- Add human-in-the-loop checkpoints

## 🧩 Key Concepts

- **State** — a shared, typed object passed between nodes
- **Nodes** — units of work (call a model, run a tool, transform state)
- **Edges** — define which node runs next
- **Conditional edges** — branch based on state
- **Cycles** — loop until a stopping condition is met
- **Checkpointing** — persist and resume runs

## 🔄 Mental Model

```
        ┌──────────┐
        │  reason  │◄──────────────┐
        └────┬─────┘               │
             ▼                      │
        ┌──────────┐    not done    │
        │   act    │────────────────┘
        └────┬─────┘
             ▼ done
        ┌──────────┐
        │  finish  │
        └──────────┘
```

## 📚 Recommended Resources

- LangGraph documentation & quickstart
- LangGraph agent / multi-agent tutorials
