# Lab 04: Analyze Text with AI Language

## 🎯 Lab Goal

Use **Azure AI Language (Text Analytics)** to:

- Detect sentiment (positive/negative/mixed)
- Extract key phrases from customer feedback or reviews

All at a conceptual level suitable for AI‑900.

---

## ✅ Prerequisites

- Azure subscription or sandbox
- Short sample texts (customer reviews, feedback emails, etc.)

Optional for code:

```bash
pip install azure-ai-textanalytics python-dotenv
```

---

## Option A – Portal / AI Studio Demo

1. Open a **Language / Text Analytics** playground in Azure AI Studio.
2. Paste in a short review like:
   - "The app is easy to use and I’m very satisfied!"
3. Observe:
   - Overall **sentiment**
   - Any **key phrases** it highlights

Try a second review:

- "The service was slow and support never replied. Very disappointed."

Compare the detected sentiment and phrases.

---

## Option B – Simple Code Example (Optional)

1. Add to `.env`:

```env
AZURE_LANGUAGE_ENDPOINT=https://<your-ai-services>.cognitiveservices.azure.com
AZURE_LANGUAGE_KEY=<your-key>
```

2. Create `text_analytics_demo.py`:

```python
import os
from dotenv import load_dotenv
from azure.ai.textanalytics import TextAnalyticsClient, AzureKeyCredential


load_dotenv()

endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")
key = os.getenv("AZURE_LANGUAGE_KEY")

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

documents = [
	"The app is easy to use and I’m very satisfied!",
	"The service was slow and support never replied. Very disappointed.",
]


def analyze():
	sentiment_result = client.analyze_sentiment(documents)
	keyphrase_result = client.extract_key_phrases(documents)

	for i, doc in enumerate(sentiment_result):
		print(f"Review {i} sentiment: {doc.sentiment}")
		print("  Scores:", doc.confidence_scores)

	print("\nKey phrases:")
	for i, doc in enumerate(keyphrase_result):
		print(f"Review {i}:")
		for phrase in doc.key_phrases:
			print(" -", phrase)


if __name__ == "__main__":
	analyze()
```

3. Run the script and verify that the positive vs negative review is detected correctly.

---

## ✅ Lab Checklist

- [ ] Ran at least two reviews through a Text Analytics demo
- [ ] Observed sentiment and key phrases for positive vs negative text
- [ ] (Optional) Ran the simple code example
- [ ] Can explain one real‑world scenario where sentiment analysis is useful

