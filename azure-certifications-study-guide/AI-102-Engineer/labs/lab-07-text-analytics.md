# Lab 07: Text Analytics and Language Capabilities

## 🎯 Lab Goal

Use Azure AI Language (Text Analytics) to:

- Detect language and sentiment
- Extract key phrases and named entities
- Understand when to choose prebuilt Language features vs LLM prompts

---

## ✅ Prerequisites

- Azure AI Services resource (Language enabled)
- Endpoint + key
- Python 3.9+ with:

```bash
pip install azure-ai-textanalytics python-dotenv
```

---

## Step 1 – Configure Environment

Update `.env`:

```env
AZURE_LANGUAGE_ENDPOINT=https://<your-ai-services>.cognitiveservices.azure.com
AZURE_LANGUAGE_KEY=<your-key>
```

---

## Step 2 – Call Text Analytics APIs

```python
# language_text_analytics.py
import os
from dotenv import load_dotenv
from azure.ai.textanalytics import TextAnalyticsClient, AzureKeyCredential


load_dotenv()

endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")
key = os.getenv("AZURE_LANGUAGE_KEY")

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))


documents = [
	"I love using Azure AI – it makes building intelligent apps much easier!",
	"The service was slow and the documentation was confusing.",
]


def analyze_sentiment():
	response = client.analyze_sentiment(documents=documents)
	for idx, doc in enumerate(response):
		print(f"Doc {idx} sentiment: {doc.sentiment}")
		print("  Scores:")
		print("   positive=", doc.confidence_scores.positive)
		print("   neutral =", doc.confidence_scores.neutral)
		print("   negative=", doc.confidence_scores.negative)


def key_phrases():
	response = client.extract_key_phrases(documents=documents)
	for idx, doc in enumerate(response):
		print(f"Doc {idx} key phrases:")
		for phrase in doc.key_phrases:
			print(" -", phrase)


def entities():
	response = client.recognize_entities(documents=documents)
	for idx, doc in enumerate(response):
		print(f"Doc {idx} entities:")
		for ent in doc.entities:
			print(f" - {ent.text} ({ent.category}) conf={ent.confidence_score:.2f}")


if __name__ == "__main__":
	analyze_sentiment()
	print("\n---\n")
	key_phrases()
	print("\n---\n")
	entities()
```

Run the script and observe outputs.

---

## Step 3 – Experiment and Reflect

Try:

- Text in different languages
- Longer product reviews or support tickets

Reflect on:

- When prebuilt Language features are sufficient (e.g., simple sentiment dashboards)
- When you’d prefer an LLM with a custom prompt or fine‑tuning

---

## ✅ Lab Checklist

- [ ] Language endpoint and key configured
- [ ] Sentiment, key phrase, and entity extraction tested
- [ ] Notes captured on prebuilt vs LLM-based approaches and their trade‑offs

