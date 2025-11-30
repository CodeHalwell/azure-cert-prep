# Lab 06: Explore Azure OpenAI

## 🎯 Lab Goal

Use **Azure OpenAI** (or Azure AI Inference) in a **playground** to experiment with:

- Chatting with a large language model (LLM)
- Seeing how prompts and system messages change the behavior

This is a **conceptual** lab – no coding required, with an optional small code sample.

---

## ✅ Prerequisites

- Azure subscription with access to Azure OpenAI or an equivalent LLM in Azure AI Studio

Optional for code:

```bash
pip install openai python-dotenv
```

---

## Step 1 – Open the Chat Playground

1. In Azure AI Studio, open a **Chat** playground using an available GPT‑style model.
2. Note the fields:
   - **System message** (instructions for the model)
   - **User message** (your questions)

---

## Step 2 – Try Basic Conversations

1. Ask: "Explain cloud computing to me like I’m new to IT."
2. Ask: "Summarize the key benefits of Azure in 3 bullet points."

Observe how the model responds in natural language.

---

## Step 3 – Change the System Message

1. Set the system message to:

   "You are a helpful Azure tutor who explains concepts in simple language."

2. Ask again:
   - "What is Azure Machine Learning?"

3. Change the system message to:

   "You are a strict technical reviewer. Be brief and precise."

4. Ask the same question.

Compare how the answers differ.

---

## Optional – Very Small Code Sample

If you want to see the code side, create `.env`:

```env
AZURE_OPENAI_ENDPOINT=https://<your-openai-resource>.openai.azure.com
AZURE_OPENAI_KEY=<your-key>
AZURE_OPENAI_DEPLOYMENT=<your-chat-model-deployment-name>
``` 

Create `openai_simple_chat.py`:

```python
import os
from dotenv import load_dotenv
from openai import AzureOpenAI


load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
key = os.getenv("AZURE_OPENAI_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

client = AzureOpenAI(azure_endpoint=endpoint, api_key=key, api_version="2024-02-15-preview")


def ask(question: str):
	response = client.chat.completions.create(
		model=deployment,
		messages=[
			{"role": "system", "content": "You are a helpful Azure tutor."},
			{"role": "user", "content": question},
		],
		max_tokens=150,
	)

	print(response.choices[0].message.content)


if __name__ == "__main__":
	ask("Explain AI services in Azure in simple terms.")
```

Run:

```bash
python openai_simple_chat.py
```

---

## ✅ Lab Checklist

- [ ] Opened a chat playground with an LLM in Azure AI Studio
- [ ] Ran at least two basic questions and reviewed responses
- [ ] Experimented with different system messages and saw how behavior changes
- [ ] (Optional) Ran the small Python chat sample with Azure OpenAI

