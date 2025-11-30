# Project 05: Architecture Guide

## 🏗️ System Architecture

### Visual Search Pipeline

```mermaid
graph TB
    subgraph "Image Ingestion"
        A[Upload Image] --> B[Blob Storage]
        B --> C[Event Grid Trigger]
    end
    
    subgraph "Feature Extraction"
        C --> D[Computer Vision]
        D --> E[Image Embeddings]
        D --> F[Visual Tags]
        D --> G[Object Detection]
        D --> H[OCR Text]
    end
    
    subgraph "Indexing"
        E & F & G & H --> I[AI Search Index]
        I --> J[Vector Field]
        I --> K[Metadata Fields]
    end
    
    subgraph "Search"
        L[Query Image] --> M[Get Embedding]
        M --> N[Vector Search]
        N --> O[K-NN Results]
        
        P[Text Query] --> Q[Hybrid Search]
        Q --> O
    end
    
    style D fill:#e3f2fd
    style I fill:#e8f5e9
```

---

## Image Embedding Process

```mermaid
sequenceDiagram
    participant App
    participant Vision as Computer Vision
    participant Search as AI Search
    participant Storage as Blob Storage
    
    App->>Storage: Upload image
    Storage-->>App: Blob URL
    App->>Vision: Get image embedding
    Vision-->>App: 1024-dim vector
    App->>Vision: Analyze image
    Vision-->>App: Tags, objects, text
    App->>Search: Index document
    Search-->>App: Document ID
```

---

## Index Schema

```json
{
  "name": "visual-search-index",
  "fields": [
    {"name": "id", "type": "Edm.String", "key": true},
    {"name": "imageUrl", "type": "Edm.String"},
    {"name": "embedding", "type": "Collection(Edm.Single)", 
     "dimensions": 1024, "vectorSearchProfile": "default"},
    {"name": "tags", "type": "Collection(Edm.String)", "searchable": true},
    {"name": "objects", "type": "Collection(Edm.String)", "searchable": true},
    {"name": "text", "type": "Edm.String", "searchable": true},
    {"name": "uploadedAt", "type": "Edm.DateTimeOffset"}
  ]
}
```

---

## Search Modes

### 1. Pure Vector Search
Find visually similar images using embedding similarity.

### 2. Hybrid Search
Combine vector similarity with keyword matching on tags/objects.

### 3. Tag-based Search
Search by specific tags or detected objects.

---

*Next: [Implementation Checklist](./checklist.md)*
