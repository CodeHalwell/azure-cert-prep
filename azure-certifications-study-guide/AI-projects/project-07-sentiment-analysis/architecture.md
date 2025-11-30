# Project 07: Architecture Guide

## 🏗️ System Architecture

### Sentiment Analysis Pipeline

```mermaid
graph LR
    A[Text Input] --> B[Language Service]
    B --> C{Analysis Type}
    C -->|Sentiment| D[Positive/Negative/Neutral]
    C -->|Opinion| E[Aspect + Sentiment]
    C -->|Key Phrases| F[Important Terms]
    D & E & F --> G[Cosmos DB]
    G --> H[Power BI]
```

---

## API Response Structure

### Sentiment Analysis

```json
{
  "documents": [{
    "id": "1",
    "sentiment": "positive",
    "confidenceScores": {
      "positive": 0.95,
      "neutral": 0.03,
      "negative": 0.02
    },
    "sentences": [{
      "sentiment": "positive",
      "text": "I love this product!",
      "confidenceScores": {...}
    }]
  }]
}
```

### Opinion Mining

```json
{
  "documents": [{
    "id": "1",
    "sentences": [{
      "targets": [{
        "text": "battery life",
        "sentiment": "positive",
        "confidenceScores": {...}
      }],
      "assessments": [{
        "text": "excellent",
        "sentiment": "positive"
      }]
    }]
  }]
}
```

---

## Data Model

```mermaid
erDiagram
    FEEDBACK {
        string id
        string text
        string source
        datetime timestamp
    }
    ANALYSIS {
        string id
        string feedback_id
        string sentiment
        float positive_score
        float negative_score
        float neutral_score
    }
    OPINION {
        string id
        string analysis_id
        string target
        string target_sentiment
        string assessment
    }
    
    FEEDBACK ||--|| ANALYSIS : has
    ANALYSIS ||--o{ OPINION : contains
```

---

## Dashboard Metrics

| Metric | Description |
|--------|-------------|
| Sentiment Score | Average sentiment over time |
| Volume | Number of feedbacks processed |
| Trend | Sentiment change over periods |
| Topics | Most mentioned aspects |
| Alerts | Negative sentiment spikes |

---

*Next: [Implementation Checklist](./checklist.md)*
