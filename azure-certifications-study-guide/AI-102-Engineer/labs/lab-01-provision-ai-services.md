# Lab 01: Provision Azure AI Services

## 🎯 Lab Goal

Create and validate the core Azure resources you’ll use across AI‑102 labs:

- Azure AI Services (multi-service or individual resources)
- Azure AI Search (for RAG and enrichment)
- (Optional) Azure OpenAI / Azure AI Inference
- Supporting resource group, storage, and Key Vault

This lab focuses on doing this **cleanly and consistently**, so later labs can reuse the same foundation.

---

## ✅ Prerequisites

- Azure subscription with permissions to create resources
- Familiarity with the Azure Portal
- Azure CLI installed (optional but recommended)

---

## Step 1 – Plan Your Resource Topology

Decide the following (write this down in your notes):

- **Resource Group** name, e.g. `rg-ai102-labs`
- **Region** (pick one that supports Azure OpenAI and AI Search, e.g. `eastus` or `swedencentral`)
- **Naming convention**, e.g.: `ai102-<service>-<env>`

Keep everything for labs in the same resource group so you can delete it in one go.

---

## Step 2 – Create Resource Group and Storage

You can do this via portal or CLI.

### Using Azure CLI

```bash
az group create \
  --name rg-ai102-labs \
  --location eastus

az storage account create \
  --name ai102stor<unique> \
  --resource-group rg-ai102-labs \
  --location eastus \
  --sku Standard_LRS \
  --kind StorageV2
```

Record storage account name and resource group in your notes.

---

## Step 3 – Provision Azure AI Services

In the portal:

1. Go to **Create a resource → AI + Machine Learning → Azure AI services**.
2. Choose **Resource type**:
	- For labs, a **multi-service account** is usually enough.
3. Use:
	- Subscription: your subscription
	- Resource group: `rg-ai102-labs`
	- Region: same as above
	- Name: `ai102-aiservices`
4. Review + create.

After deployment:

- Go to the resource → **Keys and Endpoint**.
- Note the endpoint and one key (you’ll store them later).

---

## Step 4 – Provision Azure AI Search

1. In the portal, **Create a resource → Web → Azure AI Search**.
2. Configure:
	- Resource group: `rg-ai102-labs`
	- Name: `ai102-search-<unique>`
	- Region: same as your AI resources when possible
	- Pricing tier: `Basic` is fine for labs
3. After creating, go to the service:
	- **Keys**: copy an admin key
	- **Overview**: note the endpoint URL.

You’ll use this later for vector search and enrichment.

---

## Step 5 – (Optional) Provision Azure OpenAI

If your subscription has access:

1. **Create a resource → AI + Machine Learning → Azure OpenAI**.
2. Use the same resource group and region if available.
3. After deployment, go to **Model deployments**:
	- Deploy a chat model (e.g., `gpt-4o-mini`) with deployment name `gpt-4o-mini-chat`.
	- (Optional) Deploy an embedding model (e.g., `text-embedding-3-large`).

Record:

- Endpoint URL
- API key
- Deployment names

You will use these in the OpenAI and RAG labs.

---

## Step 6 – Add Key Vault for Secrets (Recommended)

1. Create a **Key Vault** in `rg-ai102-labs`.
2. Add the following secrets:
	- `ai-services-key`
	- `ai-services-endpoint`
	- `ai-search-key`
	- `ai-search-endpoint`
	- `openai-key` (if used)
	- `openai-endpoint`
3. Add your user and/or test app as **access policy** or use RBAC as appropriate.

For now you can still use env vars during development; Key Vault prepares you for production scenarios.

---

## Step 7 – Verify via Portal and Quick Test

Use the **Azure AI Studio**/portal experiences to confirm the services work:

1. Go to **ai.azure.com** (Azure AI Studio) and connect your Azure AI Services and OpenAI resources.
2. Run a quick text analysis or small chat completion in the built-in playground.
3. In **Azure AI Search**, confirm:
	- Service status is *Running*.
	- You can create a test index from sample data.

---

## ✅ Lab Checklist

- [ ] Resource group and storage account created
- [ ] Azure AI Services provisioned and keys recorded
- [ ] Azure AI Search created and keys/endpoint recorded
- [ ] (If available) Azure OpenAI resource + deployments created
- [ ] Key Vault configured with secrets (optional but recommended)
- [ ] Quick portal/Studio tests confirm resources are working

Keep your naming and notes handy; later labs assume these resources exist and are correctly configured.

