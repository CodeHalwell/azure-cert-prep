# Lab 03: Build a RAG Solution with Azure AI Search

## 🎯 Lab Goal

Build an end-to-end Retrieval-Augmented Generation (RAG) solution that:

- Indexes your own documents using Azure AI Search
- Uses Azure OpenAI (or Azure AI Inference) to ground responses on that content
- Exposes a simple chat-style interface from a notebook or small app

By the end, you will understand how to combine vector search + LLMs safely and reliably—highly relevant for AI-102.

---

## ✅ Prerequisites

- Azure subscription with access to **Azure OpenAI** or **Azure AI Services**
- An **Azure AI Search** service (Basic or higher, with vector search enabled)
- A **storage location** for documents:
  - Either: a small folder of `.pdf`, `.docx`, or `.md` files you own
  - Or: sample content from Microsoft Learn you’ve exported locally
- Python 3.9+ and VS Code / dev environment

Recommended Python packages:

```bash
pip install azure-search-documents azure-identity openai python-dotenv tiktoken
```

> If you are using Azure AI Inference (new endpoint model), swap `openai` usage for the Azure AI Inference SDK patterns; conceptually the steps are the same.

---

## 🧱 High-Level Architecture

1. **Ingestion**
   - Chunk and embed documents.
   - Store vectors + metadata in Azure AI Search.
2. **Retrieval**
   - Accept a user question.
   - Retrieve top-k relevant chunks via vector/hybrid search.
3. **Augmented Generation**
   - Construct a prompt that includes retrieved context.
   - Send to the Azure OpenAI model.
   - Return grounded answer + citations.

---

## Step 1 – Create or Reuse Azure Resources

You can do this once and reuse across labs.

1. **Azure AI Search**
   - In the portal, create a **Search service** (e.g., `ai102-rag-search`).
   - Choose a Basic or Standard tier with **vector search** enabled.
2. **Azure OpenAI**
   - Create an **Azure OpenAI** resource (e.g., `ai102-openai`).
   - Deploy a chat model (e.g., `gpt-4o-mini` or similar) with a deployment name like `gpt-4o-mini-rag`.
3. **Key Vault (optional but recommended)**
   - Store your **search admin key** and **OpenAI key** as secrets.
   - In local dev, you can still use environment variables while learning.

---

## Step 2 – Set Up Environment and Configuration

Create a `.env` file in your lab folder (do not commit it to source control):

```env
AZURE_SEARCH_ENDPOINT=https://<your-search-service>.search.windows.net
AZURE_SEARCH_API_KEY=<admin-or-query-key>
AZURE_SEARCH_INDEX=ai102-rag-index

AZURE_OPENAI_ENDPOINT=https://<your-openai-resource>.openai.azure.com
AZURE_OPENAI_API_KEY=<your-openai-key>
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini-rag
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

In `config.py` (optional helper):

```python
from dotenv import load_dotenv
import os

load_dotenv()

AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_API_KEY = os.getenv("AZURE_SEARCH_API_KEY")
AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX", "ai102-rag-index")

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
```

---

## Step 3 – Create a Vector-Enabled Search Index

Use a notebook or simple Python script (`create_index.py`). The schema below is minimal but sufficient:

```python
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
	SearchIndex,
	SimpleField,
	SearchableField,
	VectorSearch,
	HnswParameters,
	VectorSearchProfile,
	VectorField,
)

from config import AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_API_KEY, AZURE_SEARCH_INDEX

credential = AzureKeyCredential(AZURE_SEARCH_API_KEY)
index_client = SearchIndexClient(AZURE_SEARCH_ENDPOINT, credential)

fields = [
	SimpleField(name="id", type="Edm.String", key=True),
	SearchableField(name="content", type="Edm.String", analyzer_name="en.lucene"),
	SimpleField(name="source", type="Edm.String"),
	VectorField(
		name="contentVector",
		searchable=True,
		dimensions=1536,  # match your embedding model dim
		vector_search_profile_name="default",
	),
]

vector_search = VectorSearch(
	algorithms=[HnswParameters(name="default-hnsw")],
	profiles=[VectorSearchProfile(name="default", algorithm_configuration_name="default-hnsw")],
)

index = SearchIndex(name=AZURE_SEARCH_INDEX, fields=fields, vector_search=vector_search)

index_client.create_or_update_index(index)
print("Index created or updated.")
```

> Use the right **dimensions** for your embedding model (e.g., `text-embedding-3-large` vs `small`). Check the model docs.

---

## Step 4 – Chunk, Embed, and Upload Documents

1. Place a few small documents in a `data/` folder.
2. Use OpenAI embeddings (or Azure AI Inference embeddings) to encode text.

Example (`ingest.py`):

```python
import os
import uuid
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from openai import AzureOpenAI
from config import (
	AZURE_SEARCH_ENDPOINT,
	AZURE_SEARCH_API_KEY,
	AZURE_SEARCH_INDEX,
	AZURE_OPENAI_ENDPOINT,
	AZURE_OPENAI_API_KEY,
	AZURE_OPENAI_API_VERSION,
)

client = AzureOpenAI(
	azure_endpoint=AZURE_OPENAI_ENDPOINT,
	api_key=AZURE_OPENAI_API_KEY,
	api_version=AZURE_OPENAI_API_VERSION,
)

search_client = SearchClient(
	AZURE_SEARCH_ENDPOINT,
	AZURE_SEARCH_INDEX,
	AzureKeyCredential(AZURE_SEARCH_API_KEY),
)

def chunk_text(text: str, max_tokens: int = 400) -> list[str]:
	# Simple naïve chunk by sentences; in production, use a tokenizer-based splitter.
	sentences = text.split(". ")
	chunks, buffer = [], ""
	for s in sentences:
		if len(buffer) + len(s) < max_tokens * 3:  # rough proxy
			buffer += s + ". "
		else:
			chunks.append(buffer.strip())
			buffer = s + ". "
	if buffer:
		chunks.append(buffer.strip())
	return chunks


def embed(texts: list[str]) -> list[list[float]]:
	response = client.embeddings.create(
		model="text-embedding-3-large",  # or your deployed embedding model
		input=texts,
	)
	return [d.embedding for d in response.data]


def ingest_file(path: str, source: str):
	with open(path, "r", encoding="utf-8") as f:
		text = f.read()

	chunks = chunk_text(text)
	vectors = embed(chunks)

	docs = []
	for chunk, vec in zip(chunks, vectors):
		docs.append(
			{
				"id": str(uuid.uuid4()),
				"content": chunk,
				"source": source,
				"contentVector": vec,
			}
		)

	search_client.upload_documents(docs)
	print(f"Uploaded {len(docs)} chunks from {source}")


if __name__ == "__main__":
	data_dir = "data"
	for filename in os.listdir(data_dir):
		if not filename.endswith(".md"):
			continue
		ingest_file(os.path.join(data_dir, filename), source=filename)
```

Run `python ingest.py` and verify in the Azure portal that documents appear in your index.

---

## Step 5 – Implement RAG Query Flow

Now you’ll:

1. Accept a natural language question.
2. Retrieve the most relevant chunks via vector search.
3. Build a prompt that includes those chunks.
4. Call the chat model to generate an answer.

Example (`rag_chat.py`):

```python
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from openai import AzureOpenAI
from config import (
	AZURE_SEARCH_ENDPOINT,
	AZURE_SEARCH_API_KEY,
	AZURE_SEARCH_INDEX,
	AZURE_OPENAI_ENDPOINT,
	AZURE_OPENAI_API_KEY,
	AZURE_OPENAI_DEPLOYMENT,
	AZURE_OPENAI_API_VERSION,
)

search_client = SearchClient(
	AZURE_SEARCH_ENDPOINT,
	AZURE_SEARCH_INDEX,
	AzureKeyCredential(AZURE_SEARCH_API_KEY),
)

llm = AzureOpenAI(
	azure_endpoint=AZURE_OPENAI_ENDPOINT,
	api_key=AZURE_OPENAI_API_KEY,
	api_version=AZURE_OPENAI_API_VERSION,
)


def search_documents(query: str, k: int = 5):
	# Vector-only search using an embedding of the query
	query_embedding = llm.embeddings.create(
		model="text-embedding-3-large",
		input=[query],
	).data[0].embedding

	results = search_client.search(
		search_text="",  # empty because we use pure vector
		vector=query_embedding,
		top_k=k,
		vector_fields="contentVector",
	)

	chunks = []
	for r in results:
		chunks.append({"content": r["content"], "source": r["source"]})
	return chunks


def build_prompt(question: str, docs: list[dict]) -> str:
	context_parts = []
	for d in docs:
		context_parts.append(f"Source: {d['source']}\n{d['content']}")

	context = "\n\n".join(context_parts)
	system = (
		"You are an AI assistant that answers questions strictly based on the provided context. "
		"If the answer is not in the context, say you don't know."
	)

	return system + "\n\nContext:\n" + context + "\n\nQuestion: " + question


def answer_question(question: str) -> str:
	docs = search_documents(question, k=5)
	prompt = build_prompt(question, docs)

	response = llm.chat.completions.create(
		model=AZURE_OPENAI_DEPLOYMENT,
		messages=[{"role": "user", "content": prompt}],
		temperature=0.2,
	)

	answer = response.choices[0].message.content
	return answer


if __name__ == "__main__":
	while True:
		q = input("\nAsk a question (or 'exit'): ")
		if q.lower() in {"exit", "quit"}:
			break
		print("\nAnswer:\n", answer_question(q))
```

> For AI-102, be ready to explain how you would swap **pure vector** for **hybrid** search (add `search_text` and scoring profiles) and how to adjust temperature and system prompts for reliability.

---

## Step 6 – Test and Validate

1. Ask questions clearly covered by your documents and confirm the answer is grounded.
2. Ask questions *not* covered and confirm the model responds with “I don’t know” or equivalent.
3. Inspect Azure AI Search metrics and logs.
4. (Optional) Log each interaction (question, retrieved docs, answer) for later evaluation.

### Things to Observe

- Does increasing `k` (number of retrieved docs) improve quality or add noise?
- How often does the model hallucinate when context is weak?
- What happens when documents are very long vs well-chunked?

---

## 🔐 Security and Governance Considerations

- **Data residency**: Ensure your search and OpenAI resources are in compliant regions.
- **PII**: Avoid indexing sensitive data in training labs; use synthetic or sanitized samples.
- **Access control**: Use managed identities and Key Vault in production.
- **Cost control**: Limit max tokens, throttle ingestion, and clean up resources when done.

---

## ✅ Lab Checklist

- [ ] Azure AI Search service created and index defined
- [ ] Azure OpenAI (or Azure AI Inference) deployment configured
- [ ] Documents chunked, embedded, and uploaded to index
- [ ] RAG query flow implemented and tested
- [ ] Behaviors for in-scope vs out-of-scope questions verified
- [ ] Notes captured on improvements (chunking, prompt design, hybrid search)

Use this lab as a foundation for later AI-102 labs (agents, tools, and multi-turn orchestration) by reusing the same RAG backing store.

