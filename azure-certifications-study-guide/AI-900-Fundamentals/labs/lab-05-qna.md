# Lab 05: Create a Q&A Solution

## 🎯 Lab Goal

Create a simple **question‑and‑answer experience** that can answer questions based on FAQ‑style content.

For AI‑900, we’ll focus on the **concepts** using Azure AI Studio, not detailed coding.

---

## ✅ Prerequisites

- Azure subscription or sandbox
- A small FAQ document (or copy a few Q&A pairs into a text file)

---

## Step 1 – Prepare Some FAQ Content

Create a short FAQ in a file, for example:

```text
Q: What are your support hours?
A: Our support team is available 24/7.

Q: How can I reset my password?
A: Click "Forgot password" on the sign‑in page and follow the instructions.

Q: Do you offer a free trial?
A: Yes, we offer a 14‑day free trial for new users.
```

Save it as `faq.txt` or similar.

---

## Step 2 – Create a Q&A Experience in Azure AI Studio

1. Go to Azure AI Studio and create a new **Q&A** or **chat over your data** style project (names may vary over time).
2. Upload your `faq.txt` (or other FAQ file) as a **data source**.
3. Wait for the content to be indexed.

---

## Step 3 – Ask Questions

In the playground/chat interface:

1. Ask: "What are your support hours?"
2. Ask: "How do I reset my password?"
3. Ask a question that is **not** in the FAQ and see how the system responds.

Observe:

- How answers closely follow your FAQ wording
- How it behaves when the answer does not exist

---

## Step 4 – Tweak the Behavior (Optional)

- Adjust any **answer style** or **grounding** settings (if available)
- Try more natural questions like:
	- "Can I try it for free first?"
	- "Is support always online?"

Notice that even if wording changes, it still finds the relevant FAQ.

---

## ✅ Lab Checklist

- [ ] Created a small FAQ file or document
- [ ] Uploaded it to a Q&A / chat‑over‑data experience in Azure AI Studio
- [ ] Asked multiple questions and saw answers grounded in the FAQ
- [ ] Observed what happens when you ask a question that isn’t covered

