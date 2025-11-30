# Project 03: Setup Guide

## 🔧 Subscription and Resource Group Setup

### Prerequisites

1. **Azure Subscription**
2. **Azure CLI** and **Azure Functions Core Tools**
3. **Terraform** v1.0+
4. **Python 3.9+**

---

## Step 1: Install Azure Functions Core Tools

```bash
# Windows (winget)
winget install Microsoft.AzureFunctionsCoreTools

# macOS
brew install azure-functions-core-tools@4

# Linux
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo apt-get update
sudo apt-get install azure-functions-core-tools-4
```

---

## Step 2: Create Resource Group

```bash
az login
az group create --name rg-translation-service --location eastus
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

## Step 4: Set Up Local Development

```bash
cd ../src
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
cp local.settings.json.example local.settings.json
# Edit with Terraform outputs
```

---

## Step 5: Run Locally

```bash
func start
```

---

## Step 6: Deploy to Azure

```bash
func azure functionapp publish <function-app-name>
```

---

*Next: [Architecture Guide](./architecture.md)*
