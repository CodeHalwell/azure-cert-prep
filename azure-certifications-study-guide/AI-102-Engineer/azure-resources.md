# 🔧 AI-102 Azure Resources Reference

## Complete Guide to Azure AI Services for AI Engineers

This document provides in-depth technical reference for all Azure resources covered in the AI-102 exam.

---

## 📋 Table of Contents

1. [Azure AI Services Architecture](#azure-ai-services-architecture)
2. [Azure AI Vision - Advanced](#azure-ai-vision-advanced)
3. [Azure AI Language - Advanced](#azure-ai-language-advanced)
4. [Azure AI Speech - Advanced](#azure-ai-speech-advanced)
5. [Azure OpenAI Service - Advanced](#azure-openai-service-advanced)
6. [Azure AI Search](#azure-ai-search)
7. [Azure AI Document Intelligence - Advanced](#azure-ai-document-intelligence-advanced)
8. [Azure AI Content Safety](#azure-ai-content-safety)
9. [Responsible AI Tools](#responsible-ai-tools)

---

# Azure AI Services Architecture

## Deployment Options

| Option | Description | Use Case |
|--------|-------------|----------|
| **Multi-service resource** | Single endpoint for all services | Simplified management |
| **Single-service resource** | Dedicated resource per service | Isolation, separate billing |
| **Container deployment** | Run on-premises/edge | Data residency, offline |
| **Connected containers** | Containers with cloud billing | Hybrid scenarios |

## Authentication Methods

| Method | Use Case | Security Level |
|--------|----------|----------------|
| **Subscription key** | Simple scenarios | Basic |
| **Azure AD token** | Enterprise apps | High |
| **Managed Identity** | Azure-hosted apps | Highest |

### Key Rotation Best Practices

```
┌─────────────────────────────────────────────────────────────┐
│                   Key Rotation Strategy                      │
├─────────────────────────────────────────────────────────────┤
│  1. Generate Key 2 (while using Key 1)                       │
│  2. Update all apps to use Key 2                             │
│  3. Regenerate Key 1                                         │
│  4. Store Key 1 for next rotation                            │
└─────────────────────────────────────────────────────────────┘
```

## Network Security

| Feature | Description | Configuration |
|---------|-------------|---------------|
| **Private endpoints** | VNet connectivity | Create private endpoint |
| **Service endpoints** | VNet routing | Enable on subnet |
| **IP firewall** | Restrict by IP | Configure allowed IPs |
| **Disable public access** | Private only | Toggle in portal |

---

# Azure AI Vision - Advanced

## Image Analysis 4.0

### Capabilities Matrix

| Feature | API Version | Notes |
|---------|-------------|-------|
| Captions | 4.0 | Dense captions available |
| Tags | 4.0 | Confidence scores |
| Objects | 4.0 | Bounding boxes |
| People | 4.0 | Detection only (face API separate) |
| Smart crops | 4.0 | Aspect ratio targeting |
| Read (OCR) | 4.0 | Unified with Document Intelligence |

### Custom Vision

| Model Type | Training Time | Min Images |
|------------|---------------|------------|
| Classification (multiclass) | 1-2 hours | 5 per tag |
| Classification (multilabel) | 1-2 hours | 5 per tag |
| Object Detection | 2-4 hours | 15 per tag |
| Compact models (export) | 1-2 hours | 5 per tag |

### Export Options (Compact Models)

| Platform | Format | Use Case |
|----------|--------|----------|
| TensorFlow | .pb | General edge |
| CoreML | .mlmodel | iOS apps |
| ONNX | .onnx | Windows, cross-platform |
| Dockerfile | Container | Edge devices |
| Vision AI Dev Kit | Custom | IoT cameras |

### Limitations Deep Dive

| Limitation | Standard | Workaround |
|------------|----------|------------|
| Image size | 4 MB | Resize before upload |
| Batch processing | 1 image/call | Parallelize calls |
| Custom Vision projects | 100 per resource | Create additional resources |
| Tags per project | 500 | Consolidate tags |
| Training images | 100,000 per project | Multiple projects |

---

# Azure AI Language - Advanced

## Conversational Language Understanding (CLU)

### Intent and Entity Design

| Component | Best Practice | Limit |
|-----------|--------------|-------|
| Intents | 15-30 per project | 500 max |
| Entities | Keep focused | 100 per project |
| Utterances | 15-30 per intent | 25,000 total |
| Synonyms | Use for variations | 20,000 total |

### Entity Types

| Type | Description | Use Case |
|------|-------------|----------|
| **Learned** | ML-extracted | Custom entities |
| **List** | Exact match | Fixed options |
| **Prebuilt** | Built-in extractors | Date, number, etc. |
| **Regex** | Pattern matching | IDs, codes |

### Custom NER Configuration

```
┌─────────────────────────────────────────────────────────────┐
│                Custom NER Training                           │
├─────────────────────────────────────────────────────────────┤
│  Data Requirements:                                          │
│  ├── Minimum: 10 labeled documents                          │
│  ├── Recommended: 50+ documents                              │
│  ├── Entity instances: 10+ per entity type                  │
│  └── Format: JSON with entity spans                         │
├─────────────────────────────────────────────────────────────┤
│  Training Configuration:                                     │
│  ├── Automatic split: 80% train / 20% test                  │
│  ├── Evaluation: Precision, Recall, F1                      │
│  └── Deployment: Create deployment for inference            │
└─────────────────────────────────────────────────────────────┘
```

## Custom Text Classification

| Type | Use Case | Output |
|------|----------|--------|
| **Single-label** | One category per document | Single class |
| **Multi-label** | Multiple categories | Array of classes |

### Training Requirements

| Requirement | Single-label | Multi-label |
|-------------|--------------|-------------|
| Min classes | 2 | 2 |
| Min docs per class | 10 | 10 |
| Recommended | 200+ total | 200+ total |

---

# Azure AI Speech - Advanced

## Custom Speech Models

### When to Customize

| Scenario | Solution | Effort |
|----------|----------|--------|
| Industry jargon | Phrase list | Low |
| Accent/dialect | Custom acoustic model | High |
| Domain terms | Custom language model | Medium |
| Noisy environment | Custom acoustic model | High |

### Custom Speech Training Data

| Data Type | Purpose | Format |
|-----------|---------|--------|
| Plain text | Language model | .txt files |
| Audio + transcripts | Acoustic model | .wav + .txt |
| Pronunciation | Custom pronunciations | .txt with phonemes |
| Structured text | Domain adaptation | .txt files |

### Audio Requirements

| Requirement | Specification |
|-------------|---------------|
| Format | WAV (PCM, 16-bit) |
| Sample rate | 8 kHz or 16 kHz |
| Channels | Mono |
| Duration | 10 sec - 60 sec per file |
| Total duration | Min 30 minutes |

## Custom Neural Voice

### Voice Creation Process

| Step | Description | Time |
|------|-------------|------|
| 1. Data collection | Record voice talent | Days-weeks |
| 2. Data preparation | Clean and format audio | Hours |
| 3. Training | Submit for training | 24-48 hours |
| 4. Evaluation | Test voice quality | Hours |
| 5. Deployment | Create endpoint | Minutes |

### Requirements

| Requirement | Details |
|-------------|---------|
| Audio quality | Studio quality, low noise |
| Duration | 1-2 hours of speech |
| Consent | Written consent from talent |
| Review | Microsoft approval required |

---

# Azure OpenAI Service - Advanced

## Model Comparison

| Model | Context | Speed | Cost | Use Case |
|-------|---------|-------|------|----------|
| GPT-4o | 128K | Fast | $$$ | Complex reasoning |
| GPT-4 | 8K/32K | Medium | $$$ | Complex tasks |
| GPT-3.5-Turbo | 16K | Fast | $ | General tasks |
| text-embedding-3 | N/A | Fast | ¢ | Vector search |

## Fine-Tuning

### When to Fine-Tune

| Scenario | Solution | Fine-tuning? |
|----------|----------|--------------|
| Follow specific format | Prompt engineering | No |
| Use company terminology | RAG + prompts | No |
| Consistent persona | System message | No |
| Specialized task patterns | Fine-tuning | Yes |
| Reduce prompt length | Fine-tuning | Yes |

### Fine-Tuning Process

| Step | Description | Notes |
|------|-------------|-------|
| 1. Prepare data | JSONL format | Min 10 examples |
| 2. Upload data | Via API or portal | Validation applied |
| 3. Create job | Submit training | Hours to complete |
| 4. Evaluate | Test model | Compare to base |
| 5. Deploy | Create deployment | Separate quota |

### Data Format

```json
{"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
```

## RAG (Retrieval-Augmented Generation)

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      RAG Pipeline                            │
├─────────────────────────────────────────────────────────────┤
│  User Query                                                  │
│      ↓                                                       │
│  1. Generate Embeddings (text-embedding-3)                  │
│      ↓                                                       │
│  2. Vector Search (Azure AI Search)                         │
│      ↓                                                       │
│  3. Retrieve Top K Documents                                 │
│      ↓                                                       │
│  4. Augment Prompt with Context                             │
│      ↓                                                       │
│  5. Generate Response (GPT-4)                               │
│      ↓                                                       │
│  Response with Citations                                     │
└─────────────────────────────────────────────────────────────┘
```

### On Your Data Configuration

| Data Source | Setup | Indexing |
|-------------|-------|----------|
| Azure Blob Storage | Connect container | Automatic |
| Azure AI Search | Connect existing index | Pre-indexed |
| URL | Provide URLs | Crawl and index |
| Local files | Upload in portal | Automatic |

---

# Azure AI Search

## Overview

| Attribute | Details |
|-----------|---------|
| **Type** | PaaS - Search service |
| **Purpose** | Full-text and vector search |
| **Integration** | Azure OpenAI, AI Services |
| **Pricing** | By tier (Free, Basic, Standard) |

## Features

| Feature | Description | Built-in |
|---------|-------------|----------|
| Full-text search | BM25 ranking | ✅ Yes |
| Vector search | Semantic similarity | ✅ Yes |
| Hybrid search | Combined ranking | ✅ Yes |
| Semantic ranking | AI-powered re-ranking | ✅ Yes |
| Faceted navigation | Filter categories | ✅ Yes |
| Autocomplete | Query suggestions | ✅ Yes |

## Skillsets (AI Enrichment)

### Built-in Skills

| Skill | Purpose | AI Service |
|-------|---------|------------|
| OCR | Extract text from images | AI Vision |
| Key phrase extraction | Identify key terms | AI Language |
| Entity recognition | Extract entities | AI Language |
| Language detection | Identify language | AI Language |
| Sentiment | Analyze sentiment | AI Language |
| Image analysis | Describe images | AI Vision |
| Translation | Translate content | Translator |

### Custom Skills

| Type | Description | Use Case |
|------|-------------|----------|
| Web API skill | Call custom endpoint | Custom logic |
| Azure Function | Serverless processing | Complex transforms |
| Azure ML skill | Call ML model | Predictions |

## Index Design

| Field Type | Searchable | Filterable | Sortable | Facetable |
|------------|------------|------------|----------|-----------|
| Edm.String | ✅ | ✅ | ✅ | ✅ |
| Collection(Edm.String) | ✅ | ✅ | ❌ | ✅ |
| Edm.Int32/64 | ❌ | ✅ | ✅ | ✅ |
| Edm.Boolean | ❌ | ✅ | ✅ | ✅ |
| Edm.DateTimeOffset | ❌ | ✅ | ✅ | ✅ |
| Collection(Edm.Single) | Vector | ❌ | ❌ | ❌ |

## Limitations

| Limitation | Free | Basic | S1 |
|------------|------|-------|-----|
| Indexes | 3 | 15 | 50 |
| Documents | 10,000 | 1M | 15M/partition |
| Storage | 50 MB | 2 GB | 25 GB/partition |
| Indexers | 3 | 15 | 50 |
| Skillsets | 3 | 15 | 50 |

---

# Azure AI Document Intelligence - Advanced

## Model Selection Guide

| Model | Use Case | Accuracy | Customization |
|-------|----------|----------|---------------|
| Prebuilt Invoice | Standard invoices | High | None needed |
| Prebuilt Receipt | Store receipts | High | None needed |
| Custom extraction | Unique forms | Varies | Training required |
| Custom classification | Route documents | High | Training required |
| Composed model | Multiple form types | Varies | Combine models |

## Custom Model Training

### Requirements

| Requirement | Details |
|-------------|---------|
| Min documents | 5 (recommended: 50+) |
| File formats | PDF, JPEG, PNG, BMP, TIFF |
| File size | Max 500 MB |
| Labeling | Manual in Document Intelligence Studio |

### Training Process

| Step | Description |
|------|-------------|
| 1. Create project | Define in studio |
| 2. Upload documents | Training samples |
| 3. Label documents | Mark fields |
| 4. Train model | Submit training |
| 5. Evaluate | Review accuracy |
| 6. Deploy | Use model endpoint |

## Composed Models

```
┌─────────────────────────────────────────────────────────────┐
│                    Composed Model                            │
├─────────────────────────────────────────────────────────────┤
│  Incoming Document                                           │
│       ↓                                                      │
│  Classifier (automatic routing)                              │
│       ↓                                                      │
│  ├── Invoice Model (if invoice detected)                    │
│  ├── Receipt Model (if receipt detected)                    │
│  └── Custom Form Model (if custom form)                     │
│       ↓                                                      │
│  Extracted Fields                                            │
└─────────────────────────────────────────────────────────────┘
```

---

# Azure AI Content Safety

## Overview

| Attribute | Details |
|-----------|---------|
| **Purpose** | Detect harmful content |
| **Integration** | Azure OpenAI, apps |
| **Categories** | Hate, Violence, Sexual, Self-harm |
| **Severity** | 0-6 scale |

## Features

| Feature | Description | Customization |
|---------|-------------|---------------|
| Text moderation | Analyze text | Threshold configuration |
| Image moderation | Analyze images | Threshold configuration |
| Prompt shields | Block jailbreaks | Built-in |
| Groundedness detection | Check factual accuracy | Built-in |
| Protected material | Detect copyrighted content | Built-in |

## Severity Levels

| Level | Severity | Typical Action |
|-------|----------|----------------|
| 0 | Safe | Allow |
| 2 | Low | Allow with warning |
| 4 | Medium | Block or review |
| 6 | High | Block |

---

# Responsible AI Tools

## Fairness Assessment

| Tool | Purpose | Integration |
|------|---------|-------------|
| Fairlearn | Detect bias | Azure ML |
| Error Analysis | Find failure modes | Azure ML |
| InterpretML | Explain predictions | Azure ML |

## Azure ML Responsible AI Dashboard

| Component | Purpose |
|-----------|---------|
| Error Analysis | Identify error patterns |
| Model Overview | Performance metrics |
| Data Explorer | Data distribution |
| Feature Importance | What drives predictions |
| Counterfactuals | What-if analysis |
| Causal Analysis | Causal relationships |

---

## 📊 Integration Patterns

| Pattern | Services | Use Case |
|---------|----------|----------|
| Intelligent search | AI Search + OpenAI + AI Services | Enterprise search |
| Document processing | Document Intelligence + OpenAI | Automation |
| Conversational AI | OpenAI + AI Language + Speech | Voice assistants |
| Content moderation | Content Safety + OpenAI | Safe AI apps |

---

*Last updated: November 2025*
