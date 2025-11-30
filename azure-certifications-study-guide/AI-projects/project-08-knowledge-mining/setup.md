# Project 08: Setup Guide

## 🔧 Setup

### Prerequisites
- Azure Subscription with OpenAI access
- Azure CLI, Terraform, Python 3.9+

### Quick Setup

```bash
# Login and create resource group
az login
az group create --name rg-knowledge-mining --location eastus

# Deploy infrastructure
cd terraform
cp terraform.tfvars.example terraform.tfvars
terraform init && terraform apply

# Set up Python environment
cd ../src
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Key Configuration

Create `.env` with Terraform outputs:
- AZURE_SEARCH_ENDPOINT
- AZURE_SEARCH_KEY
- AZURE_OPENAI_ENDPOINT
- AZURE_OPENAI_KEY
- AZURE_STORAGE_CONNECTION_STRING

---

*Next: [Architecture Guide](./architecture.md)*
