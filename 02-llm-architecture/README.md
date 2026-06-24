# 02 — LLM Architecture

Understand what is happening *inside* a large language model: how text becomes tokens,
how attention works, and why the transformer architecture changed everything.

> 📦 **Course:** [How Transformer LLMs Work](https://learn.deeplearning.ai/courses/how-transformer-llms-work) · ~4 hrs · Jun 11 – Jun 16

## 🎯 Learning Objectives

- Explain tokenization and embeddings
- Describe the transformer architecture (encoder/decoder)
- Understand self-attention and multi-head attention
- Know the difference between pre-training and inference
- Read and sketch an LLM data flow diagram

## 📁 Contents

| Folder | Purpose |
|--------|---------|
| `notes/` | Concept notes (attention, tokenization, etc.) |
| `diagrams/` | Architecture sketches and diagrams |

## 🧩 Key Concepts

- **Tokenization** — splitting text into tokens (sub-word units)
- **Embeddings** — turning tokens into vectors
- **Positional encoding** — giving the model a sense of order
- **Self-attention** — weighing the relevance of every token to every other
- **Transformer block** — attention + feed-forward + normalization
- **Decoding** — generating the next token, one at a time

## 📚 Recommended Resources

- *"Attention Is All You Need"* (Vaswani et al., 2017)
- The Illustrated Transformer (Jay Alammar)
- 3Blue1Brown — Neural networks / transformers series
