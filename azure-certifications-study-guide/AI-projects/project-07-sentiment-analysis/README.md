# Project 07: Sentiment Analysis Dashboard

![Azure](https://img.shields.io/badge/Azure-Language%20Service-0078D4?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=flat-square)
![Duration](https://img.shields.io/badge/Duration-3--4%20hours-brightgreen?style=flat-square)

## 🎯 Project Overview

Build a sentiment analysis dashboard that analyzes customer feedback in real-time using Azure AI Language and visualizes insights with Power BI.

### What You'll Build

- Text sentiment analysis API
- Opinion mining for aspect-based sentiment
- Real-time feedback processing
- Analytics dashboard
- Trend analysis and reporting

### Skills You'll Learn

- Azure AI Language Service
- Sentiment analysis APIs
- Opinion mining
- Power BI integration
- Data visualization

---

## 📦 Azure Resources Required

| Resource | SKU/Tier | Purpose |
|----------|----------|---------|
| Azure AI Language | S | Sentiment analysis |
| Azure Functions | Consumption | API endpoints |
| Azure Cosmos DB | Serverless | Data storage |
| Azure Event Hubs | Basic | Real-time streaming |

### Estimated Monthly Cost

- **Development/Testing**: $15-30/month
- **Production (low volume)**: $40-80/month

---

## 🏗️ Architecture

```mermaid
graph TB
    subgraph "Data Sources"
        A[Customer Reviews]
        B[Social Media]
        C[Support Tickets]
    end
    
    subgraph "Processing"
        D[Azure Functions]
        E[Language Service]
        E --> F[Sentiment Score]
        E --> G[Opinion Mining]
        E --> H[Key Phrases]
    end
    
    subgraph "Storage"
        I[(Cosmos DB)]
        J[Aggregated Data]
    end
    
    subgraph "Visualization"
        K[Power BI]
        L[Dashboard]
        M[Reports]
    end
    
    A & B & C --> D --> E
    F & G & H --> I
    I --> K --> L & M
    
    style E fill:#e8f5e9
```

---

## 📁 Project Structure

```
project-07-sentiment-analysis/
├── README.md
├── setup.md
├── architecture.md
├── checklist.md
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── sentiment_analyzer.py
│   ├── function_app.py
│   └── requirements.txt
└── terraform/
    ├── main.tf
    ├── variables.tf
    ├── outputs.tf
    └── terraform.tfvars.example
```

---

## 🚀 Quick Start

### 1. Deploy Infrastructure

```bash
cd terraform
terraform init && terraform apply
```

### 2. Test Sentiment Analysis

```bash
curl -X POST http://localhost:7071/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product! It exceeded my expectations."}'
```

---

## 🔗 Related Resources

- [Azure AI Language Documentation](https://learn.microsoft.com/en-us/azure/ai-services/language-service/)
- [Sentiment Analysis API](https://learn.microsoft.com/en-us/azure/ai-services/language-service/sentiment-opinion-mining/)
- [Power BI Documentation](https://learn.microsoft.com/en-us/power-bi/)

---

*Last updated: November 2025*
