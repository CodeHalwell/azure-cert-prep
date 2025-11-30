# 📖 AI-900 Study Guide

## Exam Overview

**Exam AI-900: Microsoft Azure AI Fundamentals**

This study guide covers all skills measured on the AI-900 exam. Use this as your primary reference for exam preparation.

---

## Skills Measured (As of May 2, 2025)

### 1. Describe Artificial Intelligence Workloads and Considerations (15-20%)

#### 1.1 Identify Features of Common AI Workloads

| Workload Type | Description | Azure Services |
|--------------|-------------|----------------|
| **Computer Vision** | Analyze and understand visual data from images and videos | Azure AI Vision, Custom Vision |
| **Natural Language Processing** | Process and understand human language | Azure AI Language, Translator |
| **Document Processing** | Extract information from documents | Azure AI Document Intelligence |
| **Generative AI** | Create new content (text, images, code) | Azure OpenAI Service |

**Key Concepts to Master:**
- [ ] Identify when to use computer vision workloads
- [ ] Identify natural language processing workloads
- [ ] Identify document processing workloads
- [ ] Identify features of generative AI workloads

#### 1.2 Identify Guiding Principles for Responsible AI

Microsoft's **Six Principles of Responsible AI:**

| Principle | Description |
|-----------|-------------|
| **Fairness** | AI systems should treat all people fairly |
| **Reliability & Safety** | AI systems should perform reliably and safely |
| **Privacy & Security** | AI systems should be secure and respect privacy |
| **Inclusiveness** | AI systems should empower everyone |
| **Transparency** | AI systems should be understandable |
| **Accountability** | People should be accountable for AI systems |

**Study Resources:**
- [Microsoft Responsible AI Principles](https://www.microsoft.com/ai/responsible-ai)
- [Responsible AI Guidelines](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai)

---

### 2. Describe Fundamental Principles of Machine Learning on Azure (15-20%)

#### 2.1 Identify Common Machine Learning Techniques

| Technique | Use Case | Example |
|-----------|----------|---------|
| **Regression** | Predict continuous numerical values | Housing prices, sales forecasting |
| **Classification** | Categorize data into discrete classes | Spam detection, disease diagnosis |
| **Clustering** | Group similar data points | Customer segmentation |
| **Deep Learning** | Complex pattern recognition | Image recognition, language translation |

**The Transformer Architecture:**
- Foundation for modern language models
- Uses attention mechanisms
- Powers models like GPT and BERT

#### 2.2 Core Machine Learning Concepts

**Features and Labels:**
- **Features**: Input variables (predictors)
- **Labels**: Output variables (what we're predicting)

**Training and Validation:**
- **Training dataset**: Used to teach the model
- **Validation dataset**: Used to evaluate model performance
- Split typically: 70-80% training, 20-30% validation

#### 2.3 Azure Machine Learning Capabilities

| Capability | Description |
|------------|-------------|
| **Automated ML** | Automatically select algorithms and hyperparameters |
| **Designer** | Visual drag-and-drop ML pipeline creation |
| **Compute Resources** | Scalable compute for training and inference |
| **Model Registry** | Store and version ML models |
| **Endpoints** | Deploy models as web services |

---

### 3. Describe Features of Computer Vision Workloads on Azure (15-20%)

#### 3.1 Common Computer Vision Solutions

| Solution Type | Description | Azure Service |
|--------------|-------------|---------------|
| **Image Classification** | Categorize images into predefined classes | Custom Vision |
| **Object Detection** | Locate and identify objects in images | Azure AI Vision |
| **Face Detection/Analysis** | Detect and analyze human faces | Azure AI Face |
| **OCR** | Extract text from images | Azure AI Vision, Document Intelligence |
| **Spatial Analysis** | Analyze people's movement in physical spaces | Azure AI Vision |

#### 3.2 Azure AI Vision Capabilities

- **Image Analysis**: Tags, captions, object detection
- **Optical Character Recognition (OCR)**: Extract printed and handwritten text
- **Spatial Analysis**: Video analytics for physical spaces
- **Face Detection**: Detect faces and facial attributes

---

### 4. Describe Features of Natural Language Processing Workloads on Azure (15-20%)

#### 4.1 Key NLP Concepts

| Concept | Description |
|---------|-------------|
| **Tokenization** | Breaking text into words, phrases, or sentences |
| **Stemming/Lemmatization** | Reducing words to their root form |
| **Named Entity Recognition** | Identifying entities (people, places, dates) |
| **Sentiment Analysis** | Determining emotional tone |
| **Key Phrase Extraction** | Identifying important phrases |

#### 4.2 Azure AI Language Services

| Service | Capability |
|---------|------------|
| **Text Analytics** | Sentiment, key phrases, entities |
| **Language Understanding** | Intent recognition, entity extraction |
| **Translator** | Text translation between languages |
| **Question Answering** | Build Q&A knowledge bases |
| **Conversational Language Understanding** | Custom NLU models |

#### 4.3 Azure AI Speech Services

| Service | Capability |
|---------|------------|
| **Speech-to-Text** | Convert spoken audio to text |
| **Text-to-Speech** | Convert text to natural-sounding speech |
| **Speech Translation** | Real-time speech translation |
| **Speaker Recognition** | Identify speakers by their voice |

---

### 5. Describe Features of Generative AI Workloads on Azure (20-25%)

#### 5.1 Generative AI Concepts

| Concept | Description |
|---------|-------------|
| **Large Language Models (LLMs)** | AI models trained on vast text data |
| **Prompts** | Instructions given to AI models |
| **Tokens** | Units of text processed by the model |
| **Completions** | Text generated by the model |
| **Temperature** | Controls randomness in outputs |
| **Embeddings** | Numerical representations of text |

#### 5.2 Azure OpenAI Service

**Available Models:**

| Model Family | Capabilities |
|-------------|--------------|
| **GPT-4/GPT-4o** | Advanced reasoning, code generation, multimodal |
| **GPT-3.5** | Text generation, conversation |
| **DALL-E** | Image generation from text |
| **Whisper** | Speech-to-text transcription |
| **Embeddings** | Text similarity, search |

**Responsible AI Features:**
- Content filtering
- Abuse monitoring
- Model deployment controls

#### 5.3 Grounding and RAG

**Retrieval Augmented Generation (RAG):**
- Combines LLM capabilities with custom data
- Reduces hallucinations
- Provides up-to-date information

---

## Exam Preparation Checklist

### Before the Exam:

- [ ] Complete all Microsoft Learn modules
- [ ] Take the free practice assessment
- [ ] Review all study guide topics
- [ ] Practice with Azure AI services (free tier)
- [ ] Explore the exam sandbox
- [ ] Get comfortable with question formats

### Exam Day Tips:

1. **Read questions carefully** - Pay attention to keywords like "MOST," "BEST," "NOT"
2. **Manage your time** - ~1 minute per question
3. **Flag uncertain questions** - Review them at the end
4. **Trust your preparation** - Don't second-guess too much

---

## Additional Resources

| Resource | Link |
|----------|------|
| Microsoft Learn AI-900 Path | [Link](https://learn.microsoft.com/en-us/training/paths/get-started-with-artificial-intelligence-on-azure/) |
| AI-900 Practice Assessment | [Link](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-900/practice/assessment?assessment-type=practice&assessmentId=26) |
| Azure AI Documentation | [Link](https://learn.microsoft.com/en-us/azure/ai-services/) |
| Responsible AI Guidelines | [Link](https://www.microsoft.com/ai/responsible-ai) |

---

*Last updated: November 2025*
