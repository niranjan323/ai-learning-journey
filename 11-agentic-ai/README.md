# 11 — Agentic AI

The capstone topic: autonomous agents that **plan, use tools, observe results,
and iterate** toward a goal — with minimal human intervention.

> 📦 **Course:** [Agentic AI](https://www.deeplearning.ai/courses/agentic-ai) · ~16 hrs · Aug 4 – Aug 7

## 🎯 Learning Objectives

- Define what makes a system "agentic"
- Implement the reason → act → observe loop
- Equip agents with tools (search, code, APIs, retrieval)
- Add memory and planning
- Coordinate multiple agents
- Understand safety, guardrails, and evaluation

## 🧩 Key Concepts

- **Agent loop** — perceive → reason → act → observe → repeat
- **Tool use** — function/tool calling to interact with the world
- **Planning** — decomposing goals into steps
- **Memory** — short-term (context) and long-term (vector store)
- **Multi-agent systems** — specialized agents collaborating
- **Guardrails** — limits, approvals, and human-in-the-loop

## 🏗️ Common Patterns

- **ReAct** — interleave reasoning and acting
- **Plan-and-execute** — plan first, then carry out steps
- **Reflection** — critique and improve own output
- **Supervisor / worker** — an orchestrator delegates to sub-agents

## 🔗 Builds On

- 09 LangChain (tools, chains)
- 10 LangGraph (stateful control flow)
- 08 RAG (long-term memory / retrieval)

## 📚 Recommended Resources

- ReAct paper (Yao et al., 2022)
- LangGraph & Anthropic agent-building guides
