# Lab 10: Document Intelligence – Forms and Invoices

## 🎯 Lab Goal

Use **Azure AI Document Intelligence** to extract structured data from semi‑structured documents such as forms and invoices.

You will:

- Call a prebuilt model (e.g., invoices/receipts)
- Inspect the extracted fields and tables
- Discuss when to use prebuilt vs custom models

---

## ✅ Prerequisites

- Azure AI Services with Document Intelligence enabled
- Endpoint + key
- Sample PDFs or images of invoices/receipts (use Microsoft samples if needed)

Install SDK:

```bash
pip install azure-ai-documentanalysis python-dotenv
```

---

## Step 1 – Configure Environment

Add to `.env`:

```env
AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT=https://<your-ai-services>.cognitiveservices.azure.com
AZURE_DOCUMENT_INTELLIGENCE_KEY=<your-key>
```

---

## Step 2 – Analyze a Prebuilt Invoice

```python
# document_invoice.py
import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentanalysis import DocumentAnalysisClient


load_dotenv()

endpoint = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT")
key = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_KEY")

client = DocumentAnalysisClient(endpoint, AzureKeyCredential(key))


def analyze_invoice(path: str):
	with open(path, "rb") as f:
		poller = client.begin_analyze_document("prebuilt-invoice", document=f)
	result = poller.result()

	for doc in result.documents:
		print("Invoice fields:")
		for name, field in doc.fields.items():
			print(f"- {name}: {field.value if field.value else field.content} (conf {field.confidence:.2f})")

		print("\nLine items:")
		items = doc.fields.get("Items")
		if items and items.value:
			for item in items.value:
				desc = item.value.get("Description")
				qty = item.value.get("Quantity")
				amt = item.value.get("Amount")
				print(
					"  -", desc.value if desc else None,
					"qty=", qty.value if qty else None,
					"amount=", amt.value if amt else None,
				)


if __name__ == "__main__":
	sample_path = "./sample-docs/invoice1.pdf"
	analyze_invoice(sample_path)
```

Run and inspect the extracted fields and line items.

---

## Step 3 – Try Prebuilt Receipt or General Document

Change the model ID to test different prebuilt models, e.g.:

- `"prebuilt-receipt"`
- `"prebuilt-document"` (for general docs)

Observe differences in:

- Field names
- Accuracy and confidence scores

---

## Step 4 – Reflect on Custom vs Prebuilt

Consider:

- When prebuilt invoices/receipts are enough
- When you’d need a **custom model** (unique layout, domain‑specific fields)
- Data labeling and retraining implications

Take notes – these decisions appear in scenario questions.

---

## ✅ Lab Checklist

- [ ] Document Intelligence endpoint + key configured
- [ ] Prebuilt invoice model called from code
- [ ] Fields and line items inspected
- [ ] At least one other prebuilt model tested (receipt/general)
- [ ] Pros/cons of prebuilt vs custom models documented

