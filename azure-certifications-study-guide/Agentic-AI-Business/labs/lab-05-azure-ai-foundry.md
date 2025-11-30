# Lab 05: Exploring Azure AI Studio (Foundry)

## 🎯 Lab Goal

Get hands-on with **Azure AI Studio (Foundry)** to:

- Explore the model catalog
- Deploy or use a model in a playground
- Understand prompt flows / workflows at a high level

This supports the **Design AI solutions** domain for AB‑100.

---

## ✅ Prerequisites

- Azure subscription with access to Azure AI Studio: https://ai.azure.com/
- Permissions to create AI resources (or use a sandbox/demo environment)

No code is strictly required, though familiarity with prompts is helpful.

---

## Step 1 – Explore the Model Catalog

1. Go to https://ai.azure.com/ and sign in.
2. Open the **Model catalog**.
3. Filter by:
	- Provider (e.g., Azure OpenAI, Meta, Mistral, etc. depending on what’s available)
	- Task type (chat completion, embeddings, image generation, etc.)
4. For 3–5 models, note:
	- Name and provider
	- Primary task (chat, vision, embeddings, etc.)
	- Key differences or notes relevant for business use

Capture this in a small table or notes.

---

## Step 2 – Open a Chat Playground

1. Choose a GPT‑like model (e.g., a chat completion model) from the catalog.
2. Open it in a **Playground**.
3. Set a system message similar to what you designed in Lab 04.
4. Run 3–5 test prompts related to the Contoso scenario.

Observe:

- Response quality and style
- How changes in the system message affect behavior

---

## Step 3 – Explore Prompt Flow / Workflows (Conceptual)

Depending on what’s available in your AI Studio version:

1. Look for **Prompt flow**, **Workflows**, or similar features.
2. Open an example or template if available.
3. Identify:
	- Inputs (user queries, data sources)
	- Model steps (LLM calls, tools)
	- Outputs (final answer, classification, etc.)

Sketch (on paper or in notes) how a simple workflow for **customer FAQ + order status** might look using prompt flows.

---

## Step 4 – Connect to Data (Conceptual)

1. In AI Studio, locate **Data** or **Connections**.
2. Review how you would:
	- Attach a data source (e.g., Azure Blob Storage, Azure AI Search index)
	- Use it for grounding/RAG
3. You do not have to fully implement RAG here—that is the focus of Lab 06—but understand the configuration surfaces.

---

## Step 5 – Review Monitoring / Usage (High-Level)

1. Look for any **Monitoring**, **Usage**, or **Cost** views associated with the model or project.
2. Note what metrics are visible (e.g., number of calls, tokens, latency).

This prepares you for Labs 09–10 (monitoring and governance).

---

## ✅ Lab Checklist

- [ ] Explored the Azure AI Studio model catalog and noted several model options
- [ ] Opened a chat playground and tested prompts using a GPT‑style model
- [ ] Reviewed or sketched how prompt flows/workflows are structured
- [ ] Understood at a high level how to connect data sources for grounding
- [ ] Located or conceptualized where monitoring/usage insights appear

