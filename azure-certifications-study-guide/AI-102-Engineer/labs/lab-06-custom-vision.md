# Lab 06: Build a Custom Vision Model

## 🎯 Lab Goal

Create and use a **Custom Vision** (Image Classification) model to:

- Train on your own labeled images
- Evaluate performance
- Call the model from code for prediction

---

## ✅ Prerequisites

- Azure subscription with access to **Custom Vision** via Azure AI services
- A small dataset of labeled images (or sample data from Microsoft docs)
- Azure portal access

---

## Step 1 – Create a Custom Vision Project

1. Navigate to the **Custom Vision** portal (linked from Azure AI Studio or docs).
2. Sign in with your Azure account.
3. Create a **New Project**:
   - Name: `ai102-customvision-demo`
   - Resource group: `rg-ai102-labs`
   - Type: `Classification`
   - Classification type: `Multiclass` (one tag per image) for this lab
   - Domains: choose an appropriate domain (e.g., `General`)

---

## Step 2 – Upload and Tag Images

1. Prepare at least **10–15 images per class**.
2. Upload images to the project.
3. Create tags (e.g., `cat`, `dog` or `logoA`, `logoB`).
4. Assign the correct tag(s) to each image.

> You don’t need a large dataset for the lab; the goal is to understand the workflow.

---

## Step 3 – Train and Evaluate the Model

1. Click **Train** → choose `Quick Training`.
2. Wait for training to complete.
3. Review metrics:
   - Precision, recall, mAP
   - Per‑tag performance
4. Inspect a few **Sample images** and predictions in the portal.

Discuss:

- What would you do if one class has much lower precision?
- How would you handle class imbalance?

---

## Step 4 – Publish the Model

1. In **Performance** tab, choose the best iteration.
2. Click **Publish**:
   - Name: `ai102-customvision-model`
   - Prediction resource: select your Azure AI resource
3. Copy the **Prediction URL** and **Prediction key** from the portal.

---

## Step 5 – Call the Model from Code

Install the prediction SDK if desired, or use raw HTTP.

Example (HTTP via Python):

```python
# customvision_predict.py
import os
import requests
from dotenv import load_dotenv


load_dotenv()

PREDICTION_KEY = os.getenv("CUSTOMVISION_PREDICTION_KEY")
PREDICTION_ENDPOINT = os.getenv("CUSTOMVISION_PREDICTION_ENDPOINT")  # full URL


def predict_image(path: str):
	with open(path, "rb") as f:
		image_data = f.read()

	headers = {
		"Prediction-Key": PREDICTION_KEY,
		"Content-Type": "application/octet-stream",
	}

	response = requests.post(PREDICTION_ENDPOINT, headers=headers, data=image_data)
	response.raise_for_status()

	result = response.json()
	for prediction in result.get("predictions", []):
		print(f"Tag: {prediction['tagName']}, prob: {prediction['probability']:.2f}")


if __name__ == "__main__":
	test_image = "./sample-images/test1.jpg"
	predict_image(test_image)
```

Update `.env`:

```env
CUSTOMVISION_PREDICTION_KEY=<prediction-key>
CUSTOMVISION_PREDICTION_ENDPOINT=<prediction-url>
```

Run the script and confirm that predictions match your expectations.

---

## Step 6 – Reflect on Production Considerations

Think about:

- When to choose **Custom Vision** vs prebuilt Vision models
- Data labeling effort and retraining cadence
- Versioning models and rollback strategies
- Latency and throughput requirements

These are common scenario questions in AI‑102.

---

## ✅ Lab Checklist

- [ ] Custom Vision project created
- [ ] Images uploaded and tagged
- [ ] Model trained and metrics reviewed
- [ ] Best iteration published to a prediction endpoint
- [ ] Code successfully calls the prediction endpoint and interprets results

