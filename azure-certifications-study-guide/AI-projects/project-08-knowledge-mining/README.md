# Project 08: AI Knowledge Mining System

![Azure](https://img.shields.io/badge/Azure-AI%20Search-0078D4?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-Advanced-red?style=flat-square)
![Duration](https://img.shields.io/badge/Duration-8--10%20hours-red?style=flat-square)

## 🎯 Project Overview

Build an enterprise knowledge mining system that extracts insights from unstructured documents using Azure AI Search, Document Intelligence, and OpenAI.

### What You'll Build

- Document ingestion pipeline
- AI-powered content extraction
- Semantic search with vector embeddings
- Question-answering over documents
- Knowledge graph visualization

### Skills You'll Learn

- Azure AI Search with skillsets
- Azure Document Intelligence
- Azure OpenAI for embeddings and QA
- Knowledge extraction patterns
- RAG (Retrieval Augmented Generation)

---

## 📦 Azure Resources Required

| Resource | SKU/Tier | Purpose |
|----------|----------|---------|
| Azure AI Search | Standard | Search and indexing |
| Azure Document Intelligence | S0 | Document processing |
| Azure OpenAI | S0 | Embeddings and QA |
| Azure Blob Storage | Standard | Document storage |
| Azure Functions | Consumption | Processing pipeline |

### Estimated Monthly Cost

- **Development/Testing**: $100-180/month
- **Production**: $300-500/month

---

## 🏗️ Architecture

```mermaid
graph TB
    subgraph "Document Ingestion"
        A[Documents] --> B[Blob Storage]
        B --> C[Indexer]
    end
    
    subgraph "AI Enrichment"
        C --> D[Skillset]
        D --> E[Document Intelligence]
        D --> F[Entity Recognition]
        D --> G[Key Phrase Extraction]
        D --> H[OpenAI Embeddings]
    end
    
    subgraph "Search Index"
        E & F & G & H --> I[AI Search Index]
        I --> J[Vector Fields]
        I --> K[Text Fields]
        I --> L[Facets]
    end
    
    subgraph "Query"
        M[User Query] --> N[Semantic Search]
        N --> O[RAG Pipeline]
        O --> P[OpenAI]
        P --> Q[Answer]
    end
    
    I --> N
    
    style D fill:#e8f5e9
    style P fill:#fff3e0
```

---

## 📁 Project Structure

```
project-08-knowledge-mining/
├── README.md
├── setup.md
├── architecture.md
├── checklist.md
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── ingestion.py
│   ├── search_service.py
│   ├── rag_pipeline.py
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
cd terraform && terraform init && terraform apply
```

### 2. Index Documents

```bash
python src/ingestion.py --folder ./documents
```

### 3. Query Knowledge Base

```bash
python src/rag_pipeline.py --query "What are the key policies?"
```

---

## 🔗 Related Resources

- [Azure AI Search Skillsets](https://learn.microsoft.com/en-us/azure/search/cognitive-search-concept-intro)
- [RAG with Azure](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)

---

*Last updated: November 2025*
