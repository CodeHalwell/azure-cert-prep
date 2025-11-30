# Lab 05: Image Analysis with Azure AI Vision

## 🎯 Lab Goal

Use **Azure AI Vision** to analyze images, extracting:

- Tags and descriptions
- Objects and their bounding boxes
- Text (OCR) where applicable

You’ll call the service via SDK/REST and understand typical use cases and limitations.

---

## ✅ Prerequisites

- **Azure AI Services** resource with Vision enabled (from Lab 01)
- Endpoint + key for your AI Services resource
- Python 3.9+ (or .NET, but examples below use Python)

Install packages:

```bash
pip install azure-ai-vision-imageanalysis python-dotenv
```

---

## Step 1 – Configure Environment

Add to `.env`:

```env
AZURE_AI_SERVICE_ENDPOINT=https://<your-ai-services>.cognitiveservices.azure.com
AZURE_AI_SERVICE_KEY=<your-key>
```

---

## Step 2 – Call Image Analysis API

```python
# vision_image_analysis.py
import os
from dotenv import load_dotenv
from azure.ai.vision.imageanalysis import (
	ImageAnalysisClient,
	VisualFeatures,
)
from azure.core.credentials import AzureKeyCredential


load_dotenv()

endpoint = os.getenv("AZURE_AI_SERVICE_ENDPOINT")
key = os.getenv("AZURE_AI_SERVICE_KEY")

client = ImageAnalysisClient(
	endpoint=endpoint,
	credential=AzureKeyCredential(key),
)


def analyze_image(path: str):
	with open(path, "rb") as f:
		image_data = f.read()

	result = client.analyze(
		image_data=image_data,
		visual_features=[
			VisualFeatures.TAGS,
			VisualFeatures.CAPTION,
			VisualFeatures.OBJECTS,
			VisualFeatures.READ,
		],
	)

	print("Caption:", result.caption.text if result.caption else "-None-")

	print("\nTags:")
	for tag in result.tags:
		print(f"- {tag.name} (confidence {tag.confidence:.2f})")

	print("\nObjects:")
	for obj in result.objects:
		r = obj.bounding_box
		print(f"- {obj.name} at [{r.x}, {r.y}, {r.w}, {r.h}] (conf {obj.confidence:.2f})")

	if result.read is not None:
		print("\nText:")
		for block in result.read.blocks:
			for line in block.lines:
				print(line.text)


if __name__ == "__main__":
	test_image = "./sample-images/contoso-street.png"  # ensure this exists
	analyze_image(test_image)
```

Run:

```bash
python vision_image_analysis.py
```

Observe the caption, tags, objects, and extracted text.

---

## Step 3 – Try Different Images and Options

Test images such as:

- A product photo (good for tagging and captioning)
- A street scene (objects and text from signs)
- A document or receipt (text extraction)

Adjust:

- `VisualFeatures` list to limit features for performance/cost
- Error handling for unsupported or very large images

---

## Step 4 – Discuss Use Cases and Limitations

Take notes on:

- When to use **AI Vision** vs **Document Intelligence**
- Privacy considerations (faces, license plates, PII on documents)
- Throughput/cost: batch processing vs one‑off calls

These are common design‑level questions in AI‑102.

---

## ✅ Lab Checklist

- [ ] Azure AI Services Vision endpoint + key configured
- [ ] SDK call implemented to analyze local image
- [ ] Captions, tags, objects, and text successfully retrieved
- [ ] Behaviors observed for different image types
- [ ] Notes captured on appropriate use cases and limitations

