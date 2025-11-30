# Lab 02: Analyze Images with Azure AI Vision

## 🎯 Lab Goal

Use **Azure AI Vision** to analyze images and see how AI can:

- Describe what’s in a picture
- Tag objects and scenes

This is still fundamentals‑level; we’ll use portal demos or very light code.

---

## ✅ Prerequisites

- Azure subscription (or Microsoft Learn sandbox instructions from the course)
- Web browser

Optional (for code):

```bash
pip install azure-ai-vision-imageanalysis python-dotenv
```

---

## Option A – Portal / AI Studio Only (No Code)

1. Go to **Azure AI Studio** at [https://ai.azure.com](https://ai.azure.com).
2. Open a **Vision** or **Image analysis** playground.
3. Upload a sample photo (person, object, or landscape) or use a built‑in sample.
4. Observe and note:
   - The **caption** (short description)
   - The **tags** (keywords) the service generates
   - Any **detected objects**

Repeat with a second image (e.g., a different scene or product photo) and compare results.

If you are only doing AI‑900 at a conceptual level, this option is enough.

---

## Option B – Simple Code Example (Optional)

If you want to see the SDK in action, you can run a minimal script.

1. Create a `.env` file:

```env
AZURE_AI_SERVICE_ENDPOINT=https://<your-ai-services>.cognitiveservices.azure.com
AZURE_AI_SERVICE_KEY=<your-key>
```

2. Create `vision_demo.py`:

```python
import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis import ImageAnalysisClient, VisualFeatures


load_dotenv()

endpoint = os.getenv("AZURE_AI_SERVICE_ENDPOINT")
key = os.getenv("AZURE_AI_SERVICE_KEY")

client = ImageAnalysisClient(endpoint, AzureKeyCredential(key))


def analyze_image(path: str):
	with open(path, "rb") as f:
		image_data = f.read()

	result = client.analyze(
		image_data=image_data,
		visual_features=[VisualFeatures.CAPTION, VisualFeatures.TAGS],
	)

	print("Caption:", result.caption.text if result.caption else "(none)")

	print("Tags:")
	for tag in result.tags:
		print(f"- {tag.name} ({tag.confidence:.2f})")


if __name__ == "__main__":
	analyze_image("./sample-images/photo1.jpg")
```

3. Run:

```bash
python vision_demo.py
```

Observe how similar the results are to what you saw in the portal.

---

## ✅ Lab Checklist

- [ ] Ran at least one image through the Vision demo
- [ ] Observed caption and tags produced by the service
- [ ] Compared results for at least two different images
- [ ] (Optional) Ran the simple code example and compared to portal behavior

