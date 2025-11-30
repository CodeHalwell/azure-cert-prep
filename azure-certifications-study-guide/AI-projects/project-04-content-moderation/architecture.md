# Project 04: Architecture Guide

## 🏗️ System Architecture

### Content Moderation Flow

```mermaid
graph TB
    subgraph "Input Processing"
        A[Content Input] --> B{Content Type}
        B -->|Text| C[Text Analyzer]
        B -->|Image| D[Image Analyzer]
    end
    
    subgraph "Azure Content Safety"
        C --> E[Text Moderation API]
        D --> F[Image Moderation API]
        
        E --> G[Hate Speech Detection]
        E --> H[Violence Detection]
        E --> I[Sexual Content Detection]
        E --> J[Self-Harm Detection]
        
        F --> K[Inappropriate Images]
        F --> L[Violence Detection]
    end
    
    subgraph "Decision Engine"
        G & H & I & J --> M{Severity Check}
        K & L --> M
        M -->|Safe| N[Approve]
        M -->|Review| O[Human Review Queue]
        M -->|Block| P[Auto-Block]
    end
    
    subgraph "Custom Rules"
        Q[Blocklists]
        R[Custom Categories]
        Q & R --> M
    end
    
    style E fill:#fce4ec
    style F fill:#fce4ec
```

---

## Severity Levels

Azure Content Safety returns severity scores (0-7) for each category:

| Level | Score | Action |
|-------|-------|--------|
| Safe | 0-1 | Auto-approve |
| Low | 2-3 | Log only |
| Medium | 4-5 | Flag for review |
| High | 6-7 | Auto-block |

---

## API Response Structure

```json
{
  "categoriesAnalysis": [
    {
      "category": "Hate",
      "severity": 0
    },
    {
      "category": "Violence", 
      "severity": 2
    },
    {
      "category": "Sexual",
      "severity": 0
    },
    {
      "category": "SelfHarm",
      "severity": 0
    }
  ],
  "blocklistsMatch": [],
  "decision": "approve"
}
```

---

## Custom Blocklist Management

```mermaid
sequenceDiagram
    participant Admin
    participant API
    participant ContentSafety
    participant Storage
    
    Admin->>API: Add term to blocklist
    API->>ContentSafety: Create/Update blocklist
    ContentSafety-->>API: Confirmation
    API->>Storage: Log change
    
    Note over ContentSafety: Future content checks against blocklist
```

---

*Next: [Implementation Checklist](./checklist.md)*
