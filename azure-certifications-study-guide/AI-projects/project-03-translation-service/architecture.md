# Project 03: Architecture Guide

## 🏗️ System Architecture

### High-Level Architecture

```mermaid
graph TB
    subgraph "Client Applications"
        A[Web App]
        B[Mobile App]
        C[API Client]
    end
    
    subgraph "Azure Functions"
        D[HTTP Trigger - /translate]
        E[HTTP Trigger - /speech-to-text]
        F[HTTP Trigger - /text-to-speech]
        G[Blob Trigger - Batch]
    end
    
    subgraph "Azure AI Services"
        H[Azure Translator]
        I[Speech Service]
    end
    
    subgraph "Storage"
        J[(Blob Storage)]
        K[Audio Files]
        L[Translated Results]
    end
    
    A & B & C --> D & E & F
    D --> H
    E --> I --> H
    F --> H --> I
    G --> J --> H --> L
    
    style H fill:#e8f5e9
    style I fill:#fff3e0
```

---

## API Endpoints

### POST /api/translate

Translate text between languages.

```json
// Request
{
  "text": "Hello, how are you?",
  "from": "en",
  "to": ["es", "fr", "de"]
}

// Response
{
  "translations": [
    {"language": "es", "text": "Hola, ¿cómo estás?"},
    {"language": "fr", "text": "Bonjour, comment allez-vous?"},
    {"language": "de", "text": "Hallo, wie geht es Ihnen?"}
  ]
}
```

### POST /api/speech-to-text

Convert audio to text with translation.

### POST /api/text-to-speech

Convert text to spoken audio.

---

## Data Flow

```mermaid
sequenceDiagram
    participant Client
    participant Function as Azure Function
    participant Translator
    participant Speech
    
    Client->>Function: POST /translate
    Function->>Translator: Translate text
    Translator-->>Function: Translated text
    Function-->>Client: JSON response
    
    Client->>Function: POST /speech-to-text
    Function->>Speech: Recognize speech
    Speech-->>Function: Transcribed text
    Function->>Translator: Translate
    Translator-->>Function: Translated text
    Function-->>Client: JSON response
```

---

## Supported Languages

Azure Translator supports 100+ languages including:

| Category | Languages |
|----------|-----------|
| Major | English, Spanish, French, German, Chinese, Japanese |
| European | Italian, Portuguese, Dutch, Polish, Russian |
| Asian | Korean, Hindi, Thai, Vietnamese, Indonesian |
| Middle Eastern | Arabic, Hebrew, Turkish, Persian |

---

*Next: [Implementation Checklist](./checklist.md)*
