# Lab 01: Set Up an Azure ML Workspace

## 🎯 Lab Goal

Create and configure an **Azure Machine Learning workspace**:

- Create workspace with required resources
- Configure the Python SDK
- Explore the workspace components

This supports the **Manage Azure Machine Learning resources** domain of DP‑100.

---

## ✅ Prerequisites

- Azure subscription
- Python 3.9+ installed locally

---

## Step 1 – Create Azure ML Workspace via Portal

1. Go to **Azure Portal → Create a resource → Machine Learning**.
2. Configure:
   - **Workspace name**: `mlw-dp100-lab`
   - **Resource group**: Create new or select existing
   - **Region**: Select nearest region
   - **Storage account**: Create new (auto-generated)
   - **Key vault**: Create new (auto-generated)
   - **Application insights**: Create new (auto-generated)
   - **Container registry**: None (created on first use)
3. Click **Review + create → Create**.

---

## Step 2 – Create Workspace via CLI

```bash
# Install ML extension
az extension add -n ml

# Create resource group
az group create --name rg-dp100 --location eastus

# Create workspace
az ml workspace create \
  --name mlw-dp100-lab \
  --resource-group rg-dp100 \
  --location eastus
```

---

## Step 3 – Install Python SDK

```bash
pip install azure-ai-ml azure-identity
```

---

## Step 4 – Connect to Workspace from Python

```python
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

# Get workspace details
subscription_id = "<your-subscription-id>"
resource_group = "rg-dp100"
workspace_name = "mlw-dp100-lab"

# Connect to workspace
ml_client = MLClient(
    DefaultAzureCredential(),
    subscription_id,
    resource_group,
    workspace_name
)

print(f"Connected to workspace: {ml_client.workspace_name}")
```

---

## Step 5 – Explore Workspace Components

### List Compute Targets:

```python
for compute in ml_client.compute.list():
    print(f"{compute.name}: {compute.type}")
```

### List Data Assets:

```python
for data in ml_client.data.list():
    print(f"{data.name} (v{data.version})")
```

### List Environments:

```python
for env in ml_client.environments.list():
    print(f"{env.name}: {env.latest_version}")
```

---

## Step 6 – Access Azure ML Studio

1. Go to [ml.azure.com](https://ml.azure.com).
2. Select your workspace.
3. Explore:
   - **Notebooks** – Jupyter environment
   - **Compute** – Compute instances and clusters
   - **Data** – Datasets and datastores
   - **Jobs** – Training runs
   - **Models** – Registered models
   - **Endpoints** – Deployed models

---

## Step 7 – Create config.json (Optional)

For local development, create a config file:

```json
{
    "subscription_id": "<your-subscription-id>",
    "resource_group": "rg-dp100",
    "workspace_name": "mlw-dp100-lab"
}
```

Then connect using:

```python
ml_client = MLClient.from_config(DefaultAzureCredential())
```

---

## Cleanup

```bash
az group delete --name rg-dp100 --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created Azure ML workspace via portal or CLI
- [ ] Installed the Azure ML Python SDK v2
- [ ] Connected to workspace from Python
- [ ] Explored workspace components via SDK
- [ ] Accessed Azure ML Studio
