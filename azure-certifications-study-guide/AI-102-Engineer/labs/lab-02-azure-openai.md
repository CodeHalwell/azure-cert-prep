# Lab 02: Implement Azure OpenAI

## 🎯 Lab Goal

Connect to Azure OpenAI (or Azure AI Inference) from code and implement a small **chat completion** and **embedding** workflow you can reuse in later labs (RAG, agents, tools).

---

## ✅ Prerequisites

- Completed **Lab 01** (resource provisioning)
- An Azure OpenAI resource with at least:
  - One chat model deployment (e.g., `gpt-4o-mini-chat`)
  - One embedding model (e.g., `text-embedding-3-large`)
- Python 3.9+ and `openai` package installed:

```bash
pip install openai python-dotenv
```

> If you’re using the new Azure AI Inference SDK, the patterns are very similar; AI‑102 focuses on concepts, not a single SDK.

---

## Step 1 – Configure Environment Variables

Create or update your `.env` file for this lab:

```env
AZURE_OPENAI_ENDPOINT=https://<your-openai-resource>.openai.azure.com
AZURE_OPENAI_API_KEY=<your-openai-key>
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_CHAT_DEPLOYMENT=gpt-4o-mini-chat
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-large
```

In `openai_client.py`:

```python
import os
from dotenv import load_dotenv
from openai import AzureOpenAI


load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
AZURE_OPENAI_CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")


client = AzureOpenAI(
	azure_endpoint=AZURE_OPENAI_ENDPOINT,
	api_key=AZURE_OPENAI_API_KEY,
	api_version=AZURE_OPENAI_API_VERSION,
)


def chat(prompt: str) -> str:
	response = client.chat.completions.create(
		model=AZURE_OPENAI_CHAT_DEPLOYMENT,
		messages=[
			{"role": "system", "content": "You are a helpful Azure AI assistant."},
			{"role": "user", "content": prompt},
		],
		temperature=0.7,
		max_tokens=512,
	)
	return response.choices[0].message.content


def embed(text: str) -> list[float]:
	response = client.embeddings.create(
		model=AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
		input=[text],
	)
	return response.data[0].embedding


if __name__ == "__main__":
	print("Chat test:")
	print(chat("Give me 3 ideas for Azure AI apps."))

	print("\nEmbedding length:")
	emb = embed("Azure AI is great for building intelligent apps.")
	print(len(emb))
```

Run:

```bash
python openai_client.py
```

Verify you get a sensible chat response and an embedding vector length that matches your model’s spec.

---

## Step 2 – Experiment with System Prompts and Parameters

Modify the `chat` function to:

- Use a more restrictive **system message** (e.g., “Answer in 2 concise bullet points”).
- Compare `temperature = 0.0` vs `0.9`.

Questions to try:

- “Explain Azure AI Search in simple terms for a non‑technical audience.”
- “List 5 ways to secure an Azure AI solution.”

Observe how temperature and max tokens affect:

- Creativity vs determinism
- Response length
- Consistency between runs

These behaviors are frequently tested conceptually in AI‑102.

---

## Step 3 – Implement a Simple Chat Loop

In `chat_loop.py`:

```python
from openai_client import chat


def main():
	print("Azure OpenAI Chat – type 'exit' to quit")
	while True:
		user = input("You: ")
		if user.lower() in {"exit", "quit"}:
			break
		answer = chat(user)
		print("Assistant:\n", answer, "\n")


if __name__ == "__main__":
	main()
```

Use this loop to get comfortable with basic chat interactions before adding tools, grounding, or agents in later labs.

---

## Step 4 – Add Basic Safety Controls

Discuss and (optionally) implement:

- A simple **input filter** that rejects obviously harmful requests.
- A maxima on `max_tokens` and defensive checks on response size.
- Logging of prompts and responses to help with offline evaluation.

> For the exam, you should be able to describe how you’d integrate **Azure AI Content Safety** or built‑in safety filters even if you don’t wire them here.

---

## ✅ Lab Checklist

- [ ] `.env` configured with OpenAI endpoint, key, and deployments
- [ ] Python client created and able to send chat and embedding requests
- [ ] System prompt and temperature experiments performed
- [ ] Simple REPL-like chat loop implemented
- [ ] Basic safety and logging considerations discussed/noted

You will reuse the `chat` and `embed` helpers in later labs (RAG, agents, tools). Keep them in a shared utility module if possible.

