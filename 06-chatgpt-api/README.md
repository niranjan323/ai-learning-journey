# 06 — ChatGPT API

Move from the chat UI to code. Call the OpenAI / Chat Completions API
programmatically and build your first AI-powered scripts.

> 📦 **Course:** [ChatGPT Prompt Engineering / Building Systems](https://www.deeplearning.ai/courses/chatgpt-building-system) · ~4 hrs · Jul 1

## 🎯 Learning Objectives

- Authenticate securely with an API key (via `.env`)
- Make chat completion requests
- Control output with temperature, max tokens, and system messages
- Handle streaming responses
- Manage cost, rate limits, and errors

## 🔐 Setup

```bash
cp ../.env.example ../.env     # add OPENAI_API_KEY
pip install openai python-dotenv
```

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain RAG in one sentence."},
    ],
)
print(response.choices[0].message.content)
```

## 🧩 Key Concepts

- **Roles** — `system`, `user`, `assistant`
- **Inference parameters** — temperature, top_p, max_tokens
- **Streaming** — receive tokens as they're generated
- **Function / tool calling** — let the model call your code
- **Cost awareness** — tokens in + tokens out

> 💡 Note: this repo also targets **Claude** via the `anthropic` SDK and
> `ANTHROPIC_API_KEY`. The latest Claude models include Opus 4.8 and Sonnet 4.6.

## 📚 Recommended Resources

- OpenAI API reference & cookbook
- Anthropic API documentation
