# Lab 03: Read Text with OCR

## 🎯 Lab Goal

Use Azure AI to **read text from images or scanned documents** (Optical Character Recognition – OCR).

---

## ✅ Prerequisites

- Azure subscription or Learn sandbox
- Sample image that contains clear printed text (e.g., a sign, poster, or document)

Optional for code:

```bash
pip install azure-ai-vision-imageanalysis python-dotenv
```

---

## Option A – Portal / AI Studio Demo

1. In **Azure AI Studio** or the Vision demos, choose a **Read text** / OCR playground.
2. Upload a sample image with text.
3. Observe:
   - Extracted text
   - Any bounding boxes or line structure shown

Try a second image with:

- Smaller text
- Different font or background

Note where the model struggles (e.g., very low contrast or angled text).

---

## Option B – Simple Code Example (Optional)

1. Ensure `.env` has your AI endpoint and key (as in Lab 02).
2. Create `ocr_demo.py`:

```python
import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis import ImageAnalysisClient, VisualFeatures


load_dotenv()

endpoint = os.getenv("AZURE_AI_SERVICE_ENDPOINT")
key = os.getenv("AZURE_AI_SERVICE_KEY")

client = ImageAnalysisClient(endpoint, AzureKeyCredential(key))


def read_text(path: str):
	with open(path, "rb") as f:
		image_data = f.read()

	result = client.analyze(
		image_data=image_data,
		visual_features=[VisualFeatures.READ],
	)

	print("Recognized text:")
	if result.read is not None:
		for block in result.read.blocks:
			for line in block.lines:
				print(line.text)


if __name__ == "__main__":
	read_text("./sample-images/text1.png")
```

3. Run:

```bash
python ocr_demo.py
```

Compare the raw text output to the original image.

---

## ✅ Lab Checklist

- [ ] Ran at least one image through an OCR demo
- [ ] Observed how printed text is extracted
- [ ] Noted conditions that help/hurt accuracy (font size, contrast, angle)
- [ ] (Optional) Ran the simple OCR code example

