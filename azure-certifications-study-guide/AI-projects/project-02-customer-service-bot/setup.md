# Project 02: Setup Guide

## 🔧 Subscription and Resource Group Setup

### Prerequisites

1. **Azure Subscription** with Bot Service access
2. **Azure CLI** installed
3. **Terraform** v1.0+
4. **Python 3.9+**
5. **Bot Framework Emulator** (for local testing)

---

## Step 1: Register Azure Bot Service Provider

```bash
az login
az account set --subscription "<subscription-id>"

# Register Bot Service provider
az provider register --namespace Microsoft.BotService
az provider register --namespace Microsoft.Web
az provider register --namespace Microsoft.DocumentDB
```

---

## Step 2: Create Resource Group

```bash
az group create \
  --name rg-customer-bot \
  --location eastus \
  --tags Project="CustomerServiceBot" Environment="Development"
```

---

## Step 3: Deploy with Terraform

```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your values

terraform init
terraform plan
terraform apply
```

---

## Step 4: Configure Bot Registration

After Terraform deployment:

1. Go to Azure Portal → Bot Services
2. Note the Bot Application ID and Password
3. Configure messaging endpoint URL

---

## Step 5: Set Up Development Environment

```bash
cd ../src
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

pip install -r requirements.txt
cp .env.example .env
# Edit .env with values from Terraform outputs
```

---

## Step 6: Test Locally

```bash
python app.py
# Open Bot Framework Emulator
# Connect to http://localhost:3978/api/messages
```

---

## 🔐 Security Notes

- Store Bot secret in Key Vault
- Use Managed Identity for production
- Enable authentication for Teams/Slack channels

---

*Next: [Architecture Guide](./architecture.md)*
