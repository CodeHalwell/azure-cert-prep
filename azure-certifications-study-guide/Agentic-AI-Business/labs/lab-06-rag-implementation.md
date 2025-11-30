# Lab 06: Implementing a RAG Pattern with Azure AI Search

## 🎯 Lab Goal

Design (and optionally prototype) a **Retrieval-Augmented Generation (RAG)** solution using:

- Azure AI Search (for indexing and retrieval)
- An LLM (e.g., Azure OpenAI) for response generation

This directly supports the **Deploy AI solutions** domain of AB‑100.

> Note: This lab can be done conceptually (architecture + design) or, if you prefer, with light code based on the AI‑102 RAG lab already in this repo.

---

## ✅ Prerequisites

- Familiarity with the Contoso scenario and your chosen use case (e.g., customer FAQ & policies)
- Access to Azure Search (Azure AI Search) and an LLM in Azure AI Studio (for hands-on)

---

## Step 1 – Clarify the RAG Use Case

Select a focused use case, such as:

- "Answer customer questions based on Contoso’s return and shipping policies"

Define:

- Types of questions users will ask
- Documents or data sources to ground answers (policy PDFs, FAQ pages, etc.)

---

## Step 2 – Design the RAG Architecture

Sketch or describe the flow:

1. User asks a question
2. System embeds the question (vectorization)
3. Azure AI Search performs vector (and possibly keyword) search
4. Top N passages are returned
5. LLM is prompted with user question + retrieved passages
6. LLM generates a grounded answer, citing sources

Draw this as a simple diagram or bullet list and label components.

---

## Step 3 – Plan the Search Index

Define an index schema suitable for your documents:

- Fields such as:
	- `id` (key)
	- `title`
	- `content`
	- `category` (e.g., "returns", "shipping")
	- `embedding` (vector field)

Decide:

- Chunking strategy (by paragraph, section, etc.)
- Indexing schedule (one‑off vs continuous)

You can reference the detailed implementation from the AI‑102 RAG lab in this repo for inspiration.

---

## Step 4 – Configure Retrieval and Prompting (Conceptual or Hands-On)

Conceptual (required):

- Describe how you will:
	- Retrieve top `k` passages from Azure AI Search
	- Insert passages into a **system or assistant** message as context
	- Instruct the model to **only answer from provided content** and say "I don’t know" otherwise

Example high-level prompt pattern:

> You are a support agent for Contoso. Use ONLY the information in the CONTEXT section to answer. If the answer is not in the context, say you don’t know and suggest contacting human support.

Hands-on (optional):

- Reuse or adapt the Python scripts from the AI‑102 RAG lab (index creation, ingestion, and query) with a smaller set of Contoso documents.

---

## Step 5 – Evaluate and Iterate

For at least 5 sample questions:

- Predict what documents should be retrieved
- Check whether your RAG design would surface them
- Identify potential failure modes:
	- Missing data
	- Poor chunking
	- Ambiguous questions

Document 3–5 improvements you would make (e.g., better metadata, synonyms, multi‑step prompts).

---

## ✅ Lab Checklist

- [ ] Selected a focused RAG use case for Contoso
- [ ] Designed an end‑to‑end RAG architecture with Azure AI Search + LLM
- [ ] Planned an index schema and chunking strategy
- [ ] Defined how retrieval results are injected into the LLM prompt
- [ ] (Optional) Implemented or adapted a small hands-on RAG prototype
- [ ] Identified potential failure modes and improvement ideas

