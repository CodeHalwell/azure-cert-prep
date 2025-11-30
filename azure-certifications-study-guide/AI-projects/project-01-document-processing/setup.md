# Project 01: Setup Guide

## 🔧 Subscription and Resource Group Setup

### Prerequisites

Before you begin, ensure you have:

1. **Azure Subscription** - [Create a free account](https://azure.microsoft.com/free/)
2. **Azure CLI** - [Install Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
3. **Terraform** - [Install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)
4. **Python 3.9+** - [Download Python](https://www.python.org/downloads/)
5. **Git** - [Install Git](https://git-scm.com/downloads)

---

## Step 1: Azure CLI Login

```bash
# Login to Azure
az login

# List available subscriptions
az account list --output table

# Set your active subscription
az account set --subscription "<subscription-id>"

# Verify the active subscription
az account show --output table
```

---

## Step 2: Register Required Resource Providers

Azure requires certain resource providers to be registered before creating resources:

```bash
# Register required providers
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Storage
az provider register --namespace Microsoft.KeyVault
az provider register --namespace Microsoft.Web

# Check registration status
az provider show --namespace Microsoft.CognitiveServices --query "registrationState"
```

---

## Step 3: Create Resource Group

```bash
# Set variables
RESOURCE_GROUP="rg-document-processing"
LOCATION="eastus"

# Create resource group
az group create \
  --name $RESOURCE_GROUP \
  --location $LOCATION \
  --tags Project="DocumentProcessing" Environment="Development"

# Verify creation
az group show --name $RESOURCE_GROUP --output table
```

---

## Step 4: Request Azure OpenAI Access (If Needed)

> ⚠️ Azure OpenAI requires approval. Request access before proceeding.

1. Go to [Azure OpenAI Access Request](https://aka.ms/oai/access)
2. Fill out the form with your subscription details
3. Wait for approval (typically 1-2 business days)

---

## Step 5: Configure Terraform Backend (Optional)

For production use, configure remote state storage:

```bash
# Create storage account for Terraform state
STORAGE_ACCOUNT="tfsatedocproc$RANDOM"
CONTAINER_NAME="tfstate"

az storage account create \
  --name $STORAGE_ACCOUNT \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --sku Standard_LRS

az storage container create \
  --name $CONTAINER_NAME \
  --account-name $STORAGE_ACCOUNT
```

---

## Step 6: Set Up Development Environment

### Create Python Virtual Environment

```bash
# Navigate to project directory
cd project-01-document-processing/src

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Create requirements.txt

```txt
azure-ai-documentintelligence==1.0.0b1
azure-storage-blob==12.19.0
azure-identity==1.15.0
azure-keyvault-secrets==4.7.0
openai==1.12.0
python-dotenv==1.0.0
pydantic==2.5.0
```

---

## Step 7: Deploy Infrastructure with Terraform

```bash
# Navigate to terraform directory
cd ../terraform

# Copy example variables file
cp terraform.tfvars.example terraform.tfvars

# Edit terraform.tfvars with your values
# Required values:
# - resource_group_name
# - location
# - project_name
# - environment

# Initialize Terraform
terraform init

# Preview the deployment
terraform plan

# Deploy resources
terraform apply
```

---

## Step 8: Configure Application Environment

After Terraform completes, set up your application:

```bash
# Get outputs from Terraform
terraform output

# Create .env file in src directory
cd ../src
cat > .env << EOF
# Azure Document Intelligence
AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT=$(terraform output -raw document_intelligence_endpoint)
AZURE_DOCUMENT_INTELLIGENCE_KEY=$(terraform output -raw document_intelligence_key)

# Azure OpenAI
AZURE_OPENAI_ENDPOINT=$(terraform output -raw openai_endpoint)
AZURE_OPENAI_API_KEY=$(terraform output -raw openai_key)
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o

# Azure Blob Storage
AZURE_STORAGE_CONNECTION_STRING=$(terraform output -raw storage_connection_string)
AZURE_STORAGE_CONTAINER_NAME=documents

# Azure Key Vault
AZURE_KEY_VAULT_URL=$(terraform output -raw key_vault_url)
EOF
```

---

## Step 9: Verify Setup

Run the verification script to ensure everything is configured:

```bash
python -c "
from config import settings
print('Configuration loaded successfully!')
print(f'Document Intelligence Endpoint: {settings.document_intelligence_endpoint}')
print(f'OpenAI Endpoint: {settings.openai_endpoint}')
print(f'Storage Container: {settings.storage_container_name}')
"
```

---

## 🔐 Security Best Practices

1. **Never commit secrets** - Use `.gitignore` for `.env` files
2. **Use Managed Identities** - When possible, use Azure Managed Identity
3. **Rotate keys regularly** - Set up key rotation in Key Vault
4. **Use RBAC** - Implement role-based access control

### Add to .gitignore

```gitignore
# Environment files
.env
.env.local
*.tfvars

# Terraform
.terraform/
*.tfstate
*.tfstate.backup

# Python
__pycache__/
venv/
*.pyc
```

---

## 🆘 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| "Subscription not found" | Run `az account set --subscription <id>` |
| "Provider not registered" | Run `az provider register --namespace <provider>` |
| "Quota exceeded" | Check regional quotas in Azure Portal |
| "OpenAI access denied" | Ensure access request was approved |

### Getting Help

- [Azure Support](https://azure.microsoft.com/en-us/support/)
- [Microsoft Q&A](https://learn.microsoft.com/en-us/answers/)
- [Stack Overflow - Azure](https://stackoverflow.com/questions/tagged/azure)

---

*Next: [Architecture Guide](./architecture.md)*
