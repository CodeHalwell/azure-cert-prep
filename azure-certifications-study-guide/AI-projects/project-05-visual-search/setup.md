# Project 05: Setup Guide

## 🔧 Subscription and Resource Group Setup

### Prerequisites

1. **Azure Subscription**
2. **Azure CLI** installed
3. **Terraform** v1.0+
4. **Python 3.9+**

---

## Step 1: Register Providers

```bash
az login
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Search
```

---

## Step 2: Create Resource Group

```bash
az group create --name rg-visual-search --location eastus
```

---

## Step 3: Deploy with Terraform

```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform apply
```

---

## Step 4: Create AI Search Index

The search index with vector field needs to be created:

```bash
python src/create_index.py
```

---

## Step 5: Set Up Development Environment

```bash
cd src
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

---

*Next: [Architecture Guide](./architecture.md)*
