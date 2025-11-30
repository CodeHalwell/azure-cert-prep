# Project 06: Setup Guide

## 🔧 Subscription and Resource Group Setup

### Prerequisites

1. **Azure Subscription** with ML and IoT access
2. **Azure CLI** and **Azure ML CLI extension**
3. **Terraform** v1.0+
4. **Python 3.9+** with Azure ML SDK

---

## Step 1: Install Azure ML CLI Extension

```bash
az extension add -n ml
```

---

## Step 2: Register Providers

```bash
az login
az provider register --namespace Microsoft.MachineLearningServices
az provider register --namespace Microsoft.Devices
az provider register --namespace Microsoft.StreamAnalytics
```

---

## Step 3: Create Resource Group

```bash
az group create --name rg-predictive-maintenance --location eastus
```

---

## Step 4: Deploy with Terraform

```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform apply
```

---

## Step 5: Set Up ML Workspace

```bash
# Connect to workspace
az ml workspace show --name <workspace-name> -g rg-predictive-maintenance

# Create compute cluster
az ml compute create --name cpu-cluster --type AmlCompute --min-instances 0 --max-instances 4
```

---

## Step 6: Prepare Training Data

Sample sensor data format:

```csv
timestamp,device_id,temperature,vibration,pressure,operational_hours,failure
2025-01-01 00:00:00,device001,65.2,0.42,101.3,1200,0
2025-01-01 00:01:00,device001,65.5,0.43,101.4,1200,0
```

---

*Next: [Architecture Guide](./architecture.md)*
