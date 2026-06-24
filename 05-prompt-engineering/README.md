# 05 — Prompt Engineering

Learn to communicate with LLMs effectively. Good prompts are the cheapest,
fastest way to improve output quality.

> 📦 **Course:** [AI Prompting for Everyone](https://learn.deeplearning.ai/courses/ai-prompting-for-everyone) · ~8 hrs · Jun 29 – Jun 30

## 🎯 Learning Objectives

- Write clear, specific, and well-structured prompts
- Apply zero-shot, few-shot, and chain-of-thought techniques
- Use roles, delimiters, and output format instructions
- Reduce hallucination and increase reliability
- Iterate systematically on prompts

## 🧩 Core Techniques

| Technique | Idea |
|-----------|------|
| Zero-shot | Ask directly with no examples |
| Few-shot | Provide a few input/output examples |
| Chain-of-thought | Ask the model to reason step by step |
| Role prompting | "You are an expert ..." |
| Structured output | Request JSON / Markdown / tables |
| Delimiters | Use `"""` or `<tags>` to separate sections |

## ✅ Best Practices

- Be specific about the task, audience, and format
- Show, don't just tell — provide examples
- Break complex tasks into steps
- Ask for the format you want (and validate it)
- Iterate: test, observe, refine

## 📝 Example

```text
You are a helpful assistant.
Summarize the text below in exactly 3 bullet points.

Text:
"""
<your text here>
"""
```

## 📚 Recommended Resources

- Prompt engineering guides from major model providers
- learnprompting.org
