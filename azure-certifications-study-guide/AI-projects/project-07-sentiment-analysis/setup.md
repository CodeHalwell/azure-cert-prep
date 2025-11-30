# Project 07: Setup Guide

## 🔧 Subscription and Resource Group Setup

### Prerequisites

1. **Azure Subscription**
2. **Azure CLI** installed
3. **Terraform** v1.0+
4. **Python 3.9+**
5. **Power BI Desktop** (optional, for dashboard)

---

## Step 1: Create Resource Group

```bash
az login
az group create --name rg-sentiment-analysis --location eastus
```

---

## Step 2: Deploy with Terraform

```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform apply
```

---

## Step 3: Test Language Service

Test in Language Studio:
1. Go to https://language.cognitive.azure.com/
2. Select "Sentiment Analysis"
3. Connect your resource
4. Test with sample text

---

## Step 4: Set Up Local Development

```bash
cd ../src
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

---

## Step 5: Configure Power BI (Optional)

1. Open Power BI Desktop
2. Get Data → Azure → Cosmos DB
3. Connect to your Cosmos DB account
4. Create visualizations

---

*Next: [Architecture Guide](./architecture.md)*
