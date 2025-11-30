# 🔧 AI-900 Azure Resources Reference

## Complete Guide to Azure AI Services for AI-900 Exam

This document provides detailed explanations of all Azure resources referenced in the AI-900 exam.

---

## 📋 Table of Contents

1. [Azure AI Services (Cognitive Services)](#azure-ai-services)
2. [Azure Machine Learning](#azure-machine-learning)
3. [Azure OpenAI Service](#azure-openai-service)
4. [Azure AI Studio](#azure-ai-studio)
5. [Azure Bot Service](#azure-bot-service)

---

# Azure AI Services

## Overview

Azure AI Services (formerly Cognitive Services) provides pre-built AI capabilities through REST APIs and SDKs.

| Attribute | Details |
|-----------|---------|
| **Type** | PaaS - Pre-built AI APIs |
| **Deployment** | Multi-region, single or multi-service |
| **Pricing** | Pay-per-call, commitment tiers available |
| **SLA** | 99.9% availability |

---

## 1. Azure AI Vision

### What It Does

| Capability | Description |
|------------|-------------|
| **Image Analysis** | Extract visual features, objects, brands, faces |
| **OCR** | Extract printed and handwritten text |
| **Spatial Analysis** | Analyze people movement in video |
| **Face Detection** | Detect and analyze faces (age, emotion, glasses) |
| **Custom Vision** | Train custom image classifiers |

### Built-in Features

| Feature | Included | Notes |
|---------|----------|-------|
| Object detection | ✅ Yes | 10,000+ objects recognized |
| Brand detection | ✅ Yes | 2,000+ logos |
| OCR (86 languages) | ✅ Yes | Print and handwriting |
| Adult content detection | ✅ Yes | Configurable levels |
| Image categorization | ✅ Yes | 86 categories |
| Color analysis | ✅ Yes | Dominant, accent colors |
| Thumbnail generation | ✅ Yes | Smart cropping |

### Customization Options

| Customization | How | Use Case |
|---------------|-----|----------|
| **Custom Vision** | Upload labeled images, train model | Product defect detection |
| **Custom categories** | Train with your images | Industry-specific classification |
| **Custom object detection** | Label and train | Specific object recognition |

### Limitations

| Limitation | Details |
|------------|---------|
| Image size | Max 4 MB |
| Image dimensions | Min 50x50, Max 16,000x16,000 |
| File formats | JPEG, PNG, GIF, BMP |
| Rate limits | Varies by tier (10-30 TPS) |
| Face API restrictions | Limited access, requires approval |

### Pricing Tiers

| Tier | Rate | Best For |
|------|------|----------|
| Free | 20 calls/min, 5K/month | Development |
| S1 | $1.00 per 1,000 calls | Production |
| Commitment | Discounted bulk | High volume |

---

## 2. Azure AI Language

### What It Does

| Capability | Description |
|------------|-------------|
| **Sentiment Analysis** | Detect positive/negative/neutral sentiment |
| **Key Phrase Extraction** | Identify main talking points |
| **Named Entity Recognition** | Extract people, places, organizations |
| **Language Detection** | Identify language of text |
| **Text Summarization** | Generate summaries of documents |
| **Question Answering** | Build FAQ bots from documents |

### Built-in Features

| Feature | Languages | Notes |
|---------|-----------|-------|
| Sentiment analysis | 20+ | Document and sentence level |
| Key phrases | 20+ | Automatic extraction |
| Named entities | 10+ | Person, location, org, date |
| Language detection | 120+ | Automatic identification |
| PII detection | 10+ | SSN, credit cards, etc. |
| Health entities | English | Medical terminology |

### Customization Options

| Customization | Capability | Effort |
|---------------|------------|--------|
| **Custom NER** | Train entity extraction | Medium - requires labeled data |
| **Custom classification** | Text categorization | Medium - requires examples |
| **Custom question answering** | FAQ from your content | Low - upload documents |
| **Conversational Language Understanding** | Intent and entity extraction | Medium - define intents |

### Limitations

| Limitation | Details |
|------------|---------|
| Document size | Max 5,120 characters per document |
| Batch size | Max 1,000 documents |
| Custom training data | Min 10 examples per class |
| Languages | Varies by feature |

---

## 3. Azure AI Speech

### What It Does

| Capability | Description |
|------------|-------------|
| **Speech-to-Text** | Convert audio to text |
| **Text-to-Speech** | Convert text to natural speech |
| **Speech Translation** | Real-time speech translation |
| **Speaker Recognition** | Identify speakers by voice |
| **Pronunciation Assessment** | Score pronunciation accuracy |

### Built-in Features

| Feature | Included | Notes |
|---------|----------|-------|
| Real-time transcription | ✅ Yes | Streaming support |
| Batch transcription | ✅ Yes | For recorded audio |
| Neural voices | ✅ Yes | 400+ voices, 140+ languages |
| SSML support | ✅ Yes | Fine-tune speech output |
| Keyword spotting | ✅ Yes | Wake word detection |
| Diarization | ✅ Yes | Identify multiple speakers |

### Customization Options

| Customization | Purpose | Effort |
|---------------|---------|--------|
| **Custom Speech** | Improve recognition for domain | High - requires audio + transcripts |
| **Custom Voice** | Create branded voice | High - requires voice samples |
| **Custom Keywords** | Custom wake words | Low - define keywords |
| **Phrase lists** | Improve specific terms | Low - add phrases |

### Limitations

| Limitation | Details |
|------------|---------|
| Audio formats | WAV, MP3, OGG, FLAC |
| Audio duration | Streaming: real-time; Batch: 2 hours |
| Sample rate | 8 kHz to 48 kHz |
| Custom Voice | Requires approval process |

---

## 4. Azure AI Translator

### What It Does

| Capability | Description |
|------------|-------------|
| **Text Translation** | Translate text between 100+ languages |
| **Document Translation** | Translate entire documents |
| **Custom Translator** | Domain-specific translation |
| **Transliteration** | Convert scripts |

### Built-in Features

| Feature | Included | Notes |
|---------|----------|-------|
| 100+ languages | ✅ Yes | Continuously expanding |
| Auto language detection | ✅ Yes | Automatic source detection |
| Dictionary lookup | ✅ Yes | Alternative translations |
| Profanity filtering | ✅ Yes | Configurable |
| Document formats | ✅ Yes | Word, PDF, PowerPoint, Excel |

### Customization Options

| Customization | Purpose | Effort |
|---------------|---------|--------|
| **Custom Translator** | Industry-specific terminology | Medium - requires parallel data |
| **Glossary** | Enforce specific translations | Low - define terms |

### Limitations

| Limitation | Details |
|------------|---------|
| Text length | 50,000 characters per request |
| Document size | 40 MB per document |
| Custom training | Min 10,000 parallel sentences |
| Rate limits | Varies by tier |

---

## 5. Azure AI Document Intelligence

### What It Does

| Capability | Description |
|------------|-------------|
| **Form Recognition** | Extract key-value pairs from forms |
| **Invoice Processing** | Extract invoice data |
| **Receipt Processing** | Extract receipt information |
| **ID Document Reading** | Extract passport/ID data |
| **Custom Models** | Train on your document types |

### Built-in (Prebuilt) Models

| Model | Extracts | Accuracy |
|-------|----------|----------|
| **Invoice** | Vendor, dates, amounts, line items | High |
| **Receipt** | Merchant, date, total, items | High |
| **ID Document** | Name, DOB, address, ID number | High |
| **Business Card** | Name, company, phone, email | High |
| **W-2** | Tax form fields | High |
| **Health Insurance** | Member info, coverage | High |

### Customization Options

| Customization | When to Use | Effort |
|---------------|-------------|--------|
| **Custom extraction** | Unique document types | Medium - label 5+ samples |
| **Composed models** | Multiple form types | Medium - combine models |
| **Custom classification** | Route to correct model | Medium - label samples |

### Limitations

| Limitation | Details |
|------------|---------|
| File size | Max 500 MB |
| Pages | Max 2,000 pages |
| File formats | PDF, JPEG, PNG, BMP, TIFF |
| Training samples | Min 5 labeled documents |

---

# Azure Machine Learning

## Overview

Azure Machine Learning is a cloud platform for building, training, and deploying ML models.

| Attribute | Details |
|-----------|---------|
| **Type** | PaaS - ML Platform |
| **Deployment** | Workspace-based |
| **Pricing** | Compute + storage costs |
| **Interfaces** | Studio, SDK, CLI |

### What It Does

| Capability | Description |
|------------|-------------|
| **Automated ML** | Automatically find best model |
| **Designer** | Drag-and-drop ML pipelines |
| **Notebooks** | Jupyter notebooks in cloud |
| **MLflow** | Track experiments and models |
| **Responsible AI** | Fairness, explainability tools |

### Built-in Features

| Feature | Included | Notes |
|---------|----------|-------|
| AutoML | ✅ Yes | Classification, regression, forecasting |
| Compute clusters | ✅ Yes | CPU and GPU options |
| Model registry | ✅ Yes | Version control for models |
| Endpoints | ✅ Yes | Real-time and batch |
| Data labeling | ✅ Yes | ML-assisted labeling |
| Feature store | ✅ Yes | Reusable features |

### Customization Options

| Customization | Purpose | Effort |
|---------------|---------|--------|
| **Custom environments** | Specific packages | Low - define requirements |
| **Custom compute** | Specific hardware | Low - configure VM |
| **Custom pipelines** | Complex workflows | High - define steps |
| **Bring your own model** | Use existing models | Medium - package model |

### Limitations

| Limitation | Details |
|------------|---------|
| AutoML time | Max 6 hours per run |
| Compute | Subject to subscription quotas |
| Dataset size | Limited by storage account |
| Concurrent runs | Based on compute capacity |

---

# Azure OpenAI Service

## Overview

Azure OpenAI provides access to OpenAI's powerful language models.

| Attribute | Details |
|-----------|---------|
| **Type** | PaaS - Generative AI |
| **Access** | Requires approval |
| **Pricing** | Per 1,000 tokens |
| **Models** | GPT-4, GPT-3.5, DALL-E, Whisper |

### What It Does

| Capability | Description |
|------------|-------------|
| **Text Generation** | Generate human-like text |
| **Code Generation** | Write and explain code |
| **Image Generation** | Create images from text (DALL-E) |
| **Embeddings** | Vector representations for search |
| **Speech-to-Text** | Transcription (Whisper) |

### Built-in Features

| Feature | Included | Notes |
|---------|----------|-------|
| GPT-4/4o models | ✅ Yes | Latest reasoning capabilities |
| GPT-3.5 Turbo | ✅ Yes | Fast, cost-effective |
| DALL-E 3 | ✅ Yes | Image generation |
| Content filtering | ✅ Yes | Safety filters enabled |
| Function calling | ✅ Yes | Structured outputs |

### Customization Options

| Customization | Purpose | Effort |
|---------------|---------|--------|
| **Fine-tuning** | Domain-specific behavior | High - requires training data |
| **System prompts** | Control model behavior | Low - configure prompts |
| **RAG patterns** | Ground with your data | Medium - build pipeline |
| **On Your Data** | Chat with documents | Low - connect data sources |

### Limitations

| Limitation | Details |
|------------|---------|
| Token limits | Varies by model (4K-128K) |
| Rate limits | Tokens per minute (TPM) |
| Content filtering | Cannot be fully disabled |
| Region availability | Limited regions |
| Access | Requires approval application |

---

# Azure AI Studio

## Overview

Azure AI Studio is the unified platform for building generative AI applications.

| Attribute | Details |
|-----------|---------|
| **Type** | Development Platform |
| **Access** | General availability |
| **Pricing** | Based on resources used |
| **Focus** | Generative AI apps |

### What It Does

| Capability | Description |
|------------|-------------|
| **Prompt Engineering** | Design and test prompts |
| **Model Catalog** | Browse and deploy models |
| **Playground** | Test models interactively |
| **Evaluation** | Assess model quality |
| **Deployment** | Deploy to endpoints |

### Built-in Features

| Feature | Included | Notes |
|---------|----------|-------|
| Model catalog | ✅ Yes | OpenAI, Hugging Face, Meta |
| Prompt flow | ✅ Yes | Build AI workflows |
| Evaluation metrics | ✅ Yes | Groundedness, relevance |
| Content safety | ✅ Yes | Built-in moderation |
| Vector search | ✅ Yes | Azure AI Search integration |

---

# Azure Bot Service

## Overview

Azure Bot Service enables building conversational AI bots.

| Attribute | Details |
|-----------|---------|
| **Type** | PaaS - Bot Framework |
| **Channels** | Teams, Web, Slack, etc. |
| **Pricing** | Free and Standard tiers |
| **Languages** | C#, JavaScript, Python |

### What It Does

| Capability | Description |
|------------|-------------|
| **Bot hosting** | Host and manage bots |
| **Channel integration** | Connect to messaging platforms |
| **Bot Framework SDK** | Build custom bots |
| **Composer** | Visual bot authoring |

### Built-in Features

| Feature | Included | Notes |
|---------|----------|-------|
| Multi-channel | ✅ Yes | 10+ channels |
| Authentication | ✅ Yes | OAuth support |
| Direct Line | ✅ Yes | Custom channel |
| Analytics | ✅ Yes | Basic metrics |

### Customization

| Customization | Purpose | Effort |
|---------------|---------|--------|
| **Custom dialogs** | Conversation flows | Medium - code required |
| **Custom channels** | New platforms | High - implement protocol |
| **Skill bots** | Modular capabilities | Medium - design skills |

---

## 📊 Quick Reference: When to Use What

| Need | Service | Built-in or Custom |
|------|---------|-------------------|
| Extract text from images | AI Vision (OCR) | Built-in |
| Analyze sentiment | AI Language | Built-in |
| Transcribe audio | AI Speech | Built-in |
| Translate documents | Translator | Built-in |
| Process invoices | Document Intelligence | Built-in |
| Detect custom objects | Custom Vision | Custom |
| Industry-specific NLP | Custom Language | Custom |
| Generate text/code | Azure OpenAI | Built-in + prompts |
| Build FAQ bot | AI Language Q&A | Custom |
| Train ML model | Azure ML AutoML | Custom |

---

*Last updated: November 2025*
