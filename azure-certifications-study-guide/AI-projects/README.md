# 🚀 Azure AI Projects - Hands-On Implementation Guide

![Azure AI](https://img.shields.io/badge/Azure-AI%20Projects-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)
![Last Updated](https://img.shields.io/badge/Last%20Updated-November%202025-green?style=for-the-badge)
![Projects](https://img.shields.io/badge/Projects-10-orange?style=for-the-badge)

A comprehensive collection of 10 end-to-end Azure AI projects with step-by-step instructions, Python code, infrastructure diagrams, and Terraform configurations.

---

## 📋 Project Overview

Each project includes:

| Component | Description |
|-----------|-------------|
| 📖 **README.md** | Project overview and learning objectives |
| 🛠️ **setup.md** | Subscription and resource group setup instructions |
| 🐍 **src/** | Python code with implementation logic |
| 📊 **architecture.md** | Infrastructure diagrams (Mermaid) |
| 🏗️ **terraform/** | Infrastructure as Code for Azure resources |
| ✅ **checklist.md** | Step-by-step implementation guide |

---

## 🎯 Projects List

| # | Project | Azure Services | Difficulty | Duration |
|---|---------|----------------|------------|----------|
| 01 | [Intelligent Document Processing](./project-01-document-processing/) | Document Intelligence, OpenAI, Blob Storage | 🟡 Medium | 4-6 hours |
| 02 | [AI-Powered Customer Service Bot](./project-02-customer-service-bot/) | Azure Bot Service, OpenAI, Language Understanding | 🟡 Medium | 6-8 hours |
| 03 | [Real-time Translation Service](./project-03-translation-service/) | Translator, Speech Services, Functions | 🟢 Easy | 3-4 hours |
| 04 | [Content Moderation System](./project-04-content-moderation/) | Content Safety, OpenAI, Event Grid | 🟡 Medium | 4-5 hours |
| 05 | [Visual Search Engine](./project-05-visual-search/) | Computer Vision, AI Search, Custom Vision | 🟡 Medium | 5-7 hours |
| 06 | [Predictive Maintenance Solution](./project-06-predictive-maintenance/) | Machine Learning, IoT Hub, Stream Analytics | 🔴 Advanced | 8-10 hours |
| 07 | [Sentiment Analysis Dashboard](./project-07-sentiment-analysis/) | Language Service, Power BI, Functions | 🟢 Easy | 3-4 hours |
| 08 | [AI Knowledge Mining System](./project-08-knowledge-mining/) | AI Search, OpenAI, Document Intelligence | 🔴 Advanced | 8-10 hours |
| 09 | [Multi-modal AI Assistant](./project-09-multimodal-assistant/) | OpenAI GPT-4o, Speech, Vision | 🔴 Advanced | 8-10 hours |
| 10 | [AI-Powered Anomaly Detection](./project-10-anomaly-detection/) | Anomaly Detector, Stream Analytics, Event Hubs | 🟡 Medium | 5-7 hours |

---

## ✅ Prerequisites

Before starting any project, ensure you have:

### Azure Requirements
- Active Azure subscription (Free tier works for most projects)
- Azure CLI installed and configured
- Terraform installed (v1.0+)
- Python 3.9 or higher

### Development Environment
- Visual Studio Code (recommended)
- Git installed
- Python virtual environment capability

### Knowledge Prerequisites
- Basic Python programming
- Familiarity with Azure Portal
- Understanding of REST APIs

---

## 🏁 Getting Started

### 1. Set Up Your Azure Environment

```bash
# Login to Azure
az login

# Set your subscription
az account set --subscription "<your-subscription-id>"

# Verify
az account show
```

### 2. Create a Base Resource Group

```bash
# Create resource group for all projects
az group create \
  --name rg-ai-projects \
  --location eastus
```

### 3. Clone This Repository

```bash
git clone <repository-url>
cd azure-certifications-study-guide/AI-projects
```

### 4. Choose a Project and Follow Instructions

Each project folder contains:
- `README.md` - Start here for project overview
- `setup.md` - Detailed setup instructions
- `checklist.md` - Step-by-step implementation guide

---

## 💰 Cost Considerations

| Tier | Monthly Cost Estimate | Suitable Projects |
|------|----------------------|-------------------|
| Free Tier | $0 | Projects 03, 07 |
| Basic | $50-100 | Projects 01, 02, 04, 05, 10 |
| Standard | $100-300 | Projects 06, 08, 09 |

> 💡 **Tip**: Use the Terraform `terraform destroy` command after completing each project to avoid unexpected charges.

---

## 🔗 Related Certifications

These projects align with the following Azure certifications:

| Certification | Related Projects |
|---------------|------------------|
| AI-900 | All projects (fundamentals) |
| AI-102 | Projects 01-10 (implementation) |
| DP-100 | Projects 06, 10 |
| AZ-204 | Projects 02, 03, 07 |

---

## 📚 Learning Path

### Beginner Path (4-5 hours)
1. Start with **Project 03: Translation Service**
2. Move to **Project 07: Sentiment Analysis**

### Intermediate Path (10-15 hours)
1. **Project 01: Document Processing**
2. **Project 05: Visual Search**
3. **Project 04: Content Moderation**

### Advanced Path (20+ hours)
1. **Project 08: Knowledge Mining**
2. **Project 06: Predictive Maintenance**
3. **Project 09: Multi-modal Assistant**

---

## 🛠️ Common Terraform Commands

```bash
# Initialize Terraform
terraform init

# Preview changes
terraform plan

# Apply infrastructure
terraform apply

# Destroy resources (cleanup)
terraform destroy
```

---

## 🤝 Contributing

Contributions are welcome! Please see the main repository [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

---

*Last updated: November 2025*
