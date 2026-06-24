# 07 — Hugging Face

Work with open-source models, datasets, and the `transformers` library.
Hugging Face is the hub for the open ML ecosystem.

> 📦 **Course:** [Open Source Models with Hugging Face](https://www.deeplearning.ai/courses/open-source-models-hugging-face) · ~20 hrs · Jul 2 – Jul 8

## 🎯 Learning Objectives

- Navigate the Hugging Face Hub (models, datasets, spaces)
- Run inference with the `transformers` `pipeline` API
- Load tokenizers and models directly
- Use the Inference API and authentication tokens
- Understand when to use open models vs. hosted APIs

## 🔐 Setup

```bash
pip install transformers datasets torch
# Optional, for the hosted Inference API:
# set HUGGINGFACEHUB_API_TOKEN in your .env
```

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
print(classifier("I love learning about AI!"))
```

## 🧩 Key Concepts

- **Pipelines** — high-level task APIs (classification, generation, etc.)
- **Tokenizers** — convert text ↔ tokens for a specific model
- **Model Hub** — thousands of pretrained checkpoints
- **Datasets** — load and stream training/eval data
- **Spaces** — host demos with Gradio / Streamlit

## 📚 Recommended Resources

- Hugging Face course (huggingface.co/learn)
- `transformers` documentation
