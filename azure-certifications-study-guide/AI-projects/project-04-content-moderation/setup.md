# Project 04: Setup Guide

## 🔧 Subscription and Resource Group Setup

### Prerequisites

1. **Azure Subscription**
2. **Azure CLI** and **Azure Functions Core Tools**
3. **Terraform** v1.0+
4. **Python 3.9+**

---

## Step 1: Register Providers

```bash
az login
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.EventGrid
```

---

## Step 2: Create Resource Group

```bash
az group create --name rg-content-moderation --location eastus
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

## Step 4: Test Content Safety

Test in Content Safety Studio:
1. Go to https://contentsafety.cognitive.azure.com/
2. Connect your resource
3. Test with sample content

---

*Next: [Architecture Guide](./architecture.md)*
