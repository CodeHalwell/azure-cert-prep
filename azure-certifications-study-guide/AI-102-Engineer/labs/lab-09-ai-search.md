# Lab 09: Implement Azure AI Search

## 🎯 Lab Goal

Create and query an Azure AI Search index that:

- Ingests structured/semi‑structured data
- Supports full‑text search, filters, and facets
- Prepares you for enrichment/RAG scenarios (building on later labs)

> This lab focuses on **classic search features**; vector/RAG was covered in Lab 03.

---

## ✅ Prerequisites

- Azure AI Search service from Lab 01
- Admin key + endpoint
- Python 3.9+ with:

```bash
pip install azure-search-documents python-dotenv
```

---

## Step 1 – Configure Environment

Update `.env`:

```env
AZURE_SEARCH_ENDPOINT=https://<your-search-service>.search.windows.net
AZURE_SEARCH_API_KEY=<admin-key>
AZURE_SEARCH_INDEX=ai102-products
```

---

## Step 2 – Define and Create the Index

```python
# search_index.py
import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchIndex, SimpleField, SearchableField


load_dotenv()

endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
key = os.getenv("AZURE_SEARCH_API_KEY")
index_name = os.getenv("AZURE_SEARCH_INDEX", "ai102-products")

client = SearchIndexClient(endpoint, AzureKeyCredential(key))

fields = [
	SimpleField(name="id", type="Edm.String", key=True),
	SearchableField(name="name", type="Edm.String", sortable=True, filterable=True),
	SearchableField(name="description", type="Edm.String"),
	SimpleField(name="category", type="Edm.String", filterable=True, facetable=True),
	SimpleField(name="price", type="Edm.Double", filterable=True, sortable=True, facetable=True),
]

index = SearchIndex(name=index_name, fields=fields)
client.create_or_update_index(index)
print("Index created/updated:", index_name)
```

Run this script to create the index.

---

## Step 3 – Upload Sample Documents

```python
# search_upload_docs.py
import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient


load_dotenv()

endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
key = os.getenv("AZURE_SEARCH_API_KEY")
index_name = os.getenv("AZURE_SEARCH_INDEX")

client = SearchClient(endpoint, index_name, AzureKeyCredential(key))

docs = [
	{
		"id": "1",
		"name": "Azure AI Fundamentals eBook",
		"description": "Introductory guide to Azure AI services.",
		"category": "Books",
		"price": 0.0,
	},
	{
		"id": "2",
		"name": "Contoso Vision Demo App",
		"description": "Sample app for computer vision demos.",
		"category": "Apps",
		"price": 29.0,
	},
	{
		"id": "3",
		"name": "Contoso Data Labeling Toolkit",
		"description": "Tooling to label data for Custom Vision and Language.",
		"category": "Tools",
		"price": 99.0,
	},
]

result = client.upload_documents(docs)
print("Uploaded:", len(result))
```

---

## Step 4 – Query the Index

```python
# search_query.py
import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient


load_dotenv()

endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
key = os.getenv("AZURE_SEARCH_API_KEY")
index_name = os.getenv("AZURE_SEARCH_INDEX")

client = SearchClient(endpoint, index_name, AzureKeyCredential(key))


def run_queries():
	print("\nFull-text search for 'vision':")
	for doc in client.search(search_text="vision"):
		print("-", doc["name"], "|", doc["description"])

	print("\nFilter category == 'Apps':")
	for doc in client.search(search_text="*", filter="category eq 'Apps'"):
		print("-", doc["name"], "|", doc["category"])

	print("\nFacet on category and price:")
	results = client.search(search_text="*", facets=["category", "price,values:0|50|100"])
	for facet in results.get_facets().get("category", []):
		print("Category facet:", facet)


if __name__ == "__main__":
	run_queries()
```

Run and observe search results, filters, and facets.

---

## Step 5 – Reflect on Design Choices

Consider and take notes on:

- Field types (searchable, filterable, sortable, facetable)
- When to use **indexes** vs **data sources + indexers**
- How this ties into RAG (Lab 03) and analytics

These topics show up frequently in AI‑102 and related data exams.

---

## ✅ Lab Checklist

- [ ] Azure AI Search endpoint + key configured
- [ ] Index schema designed and created
- [ ] Documents uploaded successfully
- [ ] Text search, filters, and facets executed
- [ ] Design trade‑offs and RAG ties documented

