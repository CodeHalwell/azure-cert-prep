# Lab 04: Work with Azure Blob Storage

## 🎯 Lab Goal

Use the **Azure Blob Storage SDK** to:

- Create containers and upload blobs
- Download and list blobs
- Set metadata and access tiers

This supports the **Develop solutions that use Blob storage** domain of AZ‑204.

---

## ✅ Prerequisites

- Azure subscription
- Python 3.9+ with `azure-storage-blob` package

```bash
pip install azure-storage-blob python-dotenv
```

---

## Step 1 – Create a Storage Account

```bash
az group create --name rg-az204-blob --location eastus

az storage account create \
  --name staz204blob<unique> \
  --resource-group rg-az204-blob \
  --sku Standard_LRS
```

Get the connection string and add to `.env`:

```bash
az storage account show-connection-string \
  --name staz204blob<unique> \
  --resource-group rg-az204-blob \
  --query connectionString -o tsv
```

---

## Step 2 – Create a Container and Upload Blobs

```python
import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()
conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
blob_service = BlobServiceClient.from_connection_string(conn_str)

# Create container
container = blob_service.create_container("mycontainer")

# Upload blob
blob_client = blob_service.get_blob_client("mycontainer", "sample.txt")
with open("sample.txt", "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print("Blob uploaded!")
```

---

## Step 3 – List and Download Blobs

```python
container_client = blob_service.get_container_client("mycontainer")

# List blobs
for blob in container_client.list_blobs():
    print(f"Blob: {blob.name}")

# Download blob
download = blob_client.download_blob()
print(download.readall().decode("utf-8"))
```

---

## Step 4 – Set Metadata and Access Tier

```python
# Set metadata
blob_client.set_blob_metadata({"author": "az204", "project": "lab"})

# Get metadata
props = blob_client.get_blob_properties()
print(props.metadata)

# Set access tier
blob_client.set_standard_blob_tier("Cool")
```

---

## Cleanup

```bash
az group delete --name rg-az204-blob --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created a storage account
- [ ] Created a container and uploaded blobs using SDK
- [ ] Listed and downloaded blobs programmatically
- [ ] Set blob metadata and access tier
- [ ] Cleaned up resources
