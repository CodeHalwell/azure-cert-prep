# Lab 05: Build an App with Azure Cosmos DB

## 🎯 Lab Goal

Use the **Azure Cosmos DB SDK** to:

- Create a database and container
- Perform CRUD operations
- Query with SQL API

This supports the **Develop solutions that use Azure Cosmos DB** domain of AZ‑204.

---

## ✅ Prerequisites

- Azure subscription
- Python 3.9+ with `azure-cosmos` package

```bash
pip install azure-cosmos python-dotenv
```

---

## Step 1 – Create a Cosmos DB Account

```bash
az group create --name rg-az204-cosmos --location eastus

az cosmosdb create \
  --name cosmos-az204-<unique> \
  --resource-group rg-az204-cosmos \
  --kind GlobalDocumentDB \
  --default-consistency-level Session
```

Get the endpoint and key:

```bash
az cosmosdb keys list \
  --name cosmos-az204-<unique> \
  --resource-group rg-az204-cosmos
```

Add to `.env`:

```
COSMOS_ENDPOINT=https://cosmos-az204-<unique>.documents.azure.com:443/
COSMOS_KEY=<your-primary-key>
```

---

## Step 2 – Create Database and Container

```python
import os
from dotenv import load_dotenv
from azure.cosmos import CosmosClient, PartitionKey

load_dotenv()
client = CosmosClient(os.getenv("COSMOS_ENDPOINT"), os.getenv("COSMOS_KEY"))

# Create database
database = client.create_database_if_not_exists("ProductsDB")

# Create container with partition key
container = database.create_container_if_not_exists(
    id="Items",
    partition_key=PartitionKey(path="/category"),
    offer_throughput=400
)
print("Container created!")
```

---

## Step 3 – Insert Documents

```python
items = [
    {"id": "1", "name": "Widget", "category": "electronics", "price": 25.00},
    {"id": "2", "name": "Gadget", "category": "electronics", "price": 50.00},
    {"id": "3", "name": "Book", "category": "books", "price": 15.00}
]

for item in items:
    container.upsert_item(item)

print("Items inserted!")
```

---

## Step 4 – Query Documents

```python
query = "SELECT * FROM c WHERE c.category = @category"
params = [{"name": "@category", "value": "electronics"}]

results = container.query_items(
    query=query,
    parameters=params,
    enable_cross_partition_query=True
)

for item in results:
    print(f"{item['name']}: ${item['price']}")
```

---

## Step 5 – Update and Delete Documents

```python
# Read item
item = container.read_item(item="1", partition_key="electronics")

# Update
item["price"] = 30.00
container.replace_item(item=item, body=item)

# Delete
container.delete_item(item="3", partition_key="books")

print("Update and delete complete!")
```

---

## Cleanup

```bash
az group delete --name rg-az204-cosmos --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created a Cosmos DB account
- [ ] Created a database and container with partition key
- [ ] Inserted documents using the SDK
- [ ] Queried documents with SQL API
- [ ] Updated and deleted documents
- [ ] Cleaned up resources
