# Project 01: Architecture Guide

## 🏗️ System Architecture

This document provides a detailed explanation of the Intelligent Document Processing architecture.

---

## High-Level Architecture

```mermaid
graph TB
    subgraph "Input Layer"
        A[📄 Documents] --> B[Upload API]
        A1[PDF Files]
        A2[Images]
        A3[Invoices]
        A4[Forms]
        A1 & A2 & A3 & A4 --> A
    end
    
    subgraph "Storage Layer"
        B --> C[(Azure Blob Storage)]
        C --> |Raw Documents| C1[input-container]
        C --> |Processed| C2[output-container]
    end
    
    subgraph "Processing Layer"
        C1 --> D[Azure Document Intelligence]
        D --> |Layout Analysis| D1[Text Extraction]
        D --> |Prebuilt Models| D2[Invoice/Receipt]
        D --> |Custom Models| D3[Custom Forms]
        
        D1 & D2 & D3 --> E[Extracted Data JSON]
    end
    
    subgraph "AI Enhancement Layer"
        E --> F[Azure OpenAI]
        F --> |Summarization| F1[Document Summary]
        F --> |Entity Extraction| F2[Key Entities]
        F --> |Classification| F3[Document Type]
    end
    
    subgraph "Security Layer"
        G[Azure Key Vault]
        G --> |API Keys| D
        G --> |API Keys| F
        G --> |Connection Strings| C
    end
    
    subgraph "Output Layer"
        F1 & F2 & F3 --> H[Structured Output]
        H --> I[API Response]
        H --> C2
    end
    
    style D fill:#fff3e0
    style F fill:#e8f5e9
    style G fill:#fce4ec
```

---

## Component Details

### 1. Azure Blob Storage

**Purpose**: Store input documents and processed outputs

| Container | Purpose | Access Level |
|-----------|---------|--------------|
| `input-documents` | Raw uploaded documents | Private |
| `processed-documents` | Extracted data and summaries | Private |
| `archive` | Long-term storage | Private (Cool tier) |

**Configuration**:
```hcl
# Lifecycle management
lifecycle_rule {
  action { type = "Delete" }
  condition { age = 90 }
}
```

---

### 2. Azure Document Intelligence

**Purpose**: Extract text, tables, and structured data from documents

**Models Used**:

| Model | Use Case | Features |
|-------|----------|----------|
| `prebuilt-layout` | General documents | Text, tables, structure |
| `prebuilt-invoice` | Invoice processing | Vendor, amounts, line items |
| `prebuilt-receipt` | Receipt processing | Merchant, total, items |
| `prebuilt-document` | General extraction | Key-value pairs, entities |

**API Flow**:
```mermaid
sequenceDiagram
    participant App
    participant DocIntel as Document Intelligence
    participant Storage as Blob Storage
    
    App->>Storage: Upload document
    Storage-->>App: Blob URL
    App->>DocIntel: Analyze document (URL)
    DocIntel->>Storage: Fetch document
    DocIntel-->>App: Operation ID
    App->>DocIntel: Get result (polling)
    DocIntel-->>App: Extracted data (JSON)
```

---

### 3. Azure OpenAI

**Purpose**: Enhance extracted data with AI capabilities

**Deployment Configuration**:

| Model | Deployment Name | Use Case |
|-------|-----------------|----------|
| GPT-4o | `gpt-4o-docproc` | Summarization, analysis |
| text-embedding-3-large | `embedding-docproc` | Vector search (optional) |

**Prompt Engineering**:

```python
SYSTEM_PROMPT = """
You are a document analysis assistant. Given extracted document text,
provide:
1. A concise summary (2-3 sentences)
2. Key entities (people, organizations, dates, amounts)
3. Document classification (invoice, contract, report, etc.)

Respond in JSON format.
"""
```

---

### 4. Azure Key Vault

**Purpose**: Secure storage for secrets and API keys

**Secrets Stored**:

| Secret Name | Purpose |
|-------------|---------|
| `document-intelligence-key` | Document Intelligence API key |
| `openai-api-key` | OpenAI API key |
| `storage-connection-string` | Blob Storage connection |

**Access Pattern**:
```mermaid
graph LR
    A[Application] --> |Managed Identity| B[Key Vault]
    B --> |Secret| C[Document Intelligence]
    B --> |Secret| D[OpenAI]
    B --> |Secret| E[Blob Storage]
```

---

## Data Flow

### Document Processing Pipeline

```mermaid
flowchart LR
    A[Upload] --> B[Store]
    B --> C[Extract]
    C --> D[Enhance]
    D --> E[Output]
    
    subgraph Details
        B --> |Blob Storage| B1[Generate SAS URL]
        C --> |Doc Intelligence| C1[Text + Tables]
        D --> |OpenAI| D1[Summary + Entities]
        E --> |API| E1[JSON Response]
    end
```

### Processing Steps

1. **Upload**: Client uploads document via REST API
2. **Store**: Document saved to Blob Storage with metadata
3. **Extract**: Document Intelligence analyzes the document
4. **Enhance**: OpenAI provides summaries and insights
5. **Output**: Structured JSON returned to client

---

## Security Architecture

```mermaid
graph TB
    subgraph "Public Zone"
        A[Client] --> |HTTPS| B[API Gateway]
    end
    
    subgraph "Application Zone"
        B --> C[Azure Functions]
        C --> |Managed Identity| D[Key Vault]
    end
    
    subgraph "Data Zone"
        C --> |Private Endpoint| E[Blob Storage]
        C --> |Private Endpoint| F[Document Intelligence]
        C --> |Private Endpoint| G[OpenAI]
    end
    
    subgraph "Security Controls"
        H[Azure AD] --> C
        I[Network Security Groups]
        J[Azure Firewall]
    end
    
    style D fill:#fce4ec
    style H fill:#e3f2fd
```

---

## Scalability Considerations

### Horizontal Scaling

| Component | Scaling Strategy |
|-----------|-----------------|
| Blob Storage | Auto-scaling (no limit) |
| Document Intelligence | Concurrent requests (S0: 15 TPS) |
| OpenAI | TPM/RPM limits per deployment |
| Functions | Consumption plan auto-scale |

### Rate Limiting

```python
# Rate limiting configuration
RATE_LIMITS = {
    "document_intelligence": 15,  # Transactions per second
    "openai_gpt4": 10000,         # Tokens per minute
    "openai_requests": 100,       # Requests per minute
}
```

---

## Monitoring and Observability

```mermaid
graph LR
    A[Application] --> B[Application Insights]
    A --> C[Azure Monitor]
    
    B --> D[Custom Metrics]
    B --> E[Request Traces]
    B --> F[Exceptions]
    
    C --> G[Resource Metrics]
    C --> H[Alerts]
    C --> I[Dashboards]
```

### Key Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| Processing Time | End-to-end latency | > 30 seconds |
| Error Rate | Failed requests | > 5% |
| Queue Depth | Pending documents | > 100 |
| API Usage | OpenAI token consumption | > 80% quota |

---

## Cost Optimization

### Resource Tiers

| Environment | Document Intelligence | OpenAI | Storage |
|-------------|----------------------|--------|---------|
| Development | F0 (Free) | PTU Dev | LRS |
| Staging | S0 | Standard | LRS |
| Production | S0 | PTU | GRS |

### Cost Reduction Strategies

1. **Use F0 tier** for development and testing
2. **Implement caching** for repeated document analysis
3. **Batch processing** to optimize API calls
4. **Lifecycle policies** for storage cleanup

---

*Next: [Implementation Checklist](./checklist.md)*
