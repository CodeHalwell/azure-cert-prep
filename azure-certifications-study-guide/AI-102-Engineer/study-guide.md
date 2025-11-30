# 📖 AI-102 Study Guide

## Exam Overview

**Exam AI-102: Designing and Implementing a Microsoft Azure AI Solution**

This comprehensive study guide covers all skills measured on the AI-102 exam as of April 30, 2025.

---

## Audience Profile

As a Microsoft Azure AI engineer, you build, manage, and deploy AI solutions that leverage Azure AI. Your responsibilities include:

- Requirements definition and design
- Development and deployment
- Integration and maintenance
- Performance tuning and monitoring

**Required Skills:**
- Python or C# programming
- REST APIs and SDKs
- Image/video/NLP processing
- Knowledge mining and generative AI
- Responsible AI principles

---

## Skills Measured (April 30, 2025)

### 1. Plan and Manage an Azure AI Solution (20-25%)

#### 1.1 Select the Appropriate Azure AI Foundry Services

| Solution Type | Recommended Service |
|--------------|---------------------|
| Generative AI | Azure OpenAI, Azure AI Foundry |
| Computer Vision | Azure AI Vision, Custom Vision |
| NLP | Azure AI Language |
| Speech | Azure AI Speech |
| Information Extraction | Azure AI Document Intelligence |
| Knowledge Mining | Azure AI Search |

**Key Decisions:**
- [ ] Match business requirements to AI services
- [ ] Consider cost, latency, and scalability
- [ ] Evaluate managed vs. custom solutions

#### 1.2 Plan, Create and Deploy an Azure AI Foundry Service

**Planning for Responsible AI:**
```
1. Identify potential harms
2. Measure impact of harms
3. Mitigate harms
4. Deploy responsibly
5. Monitor and improve
```

**Deployment Options:**

| Option | Use Case |
|--------|----------|
| Azure AI Foundry Hub | Centralized AI development |
| Azure AI Services | Direct API access |
| Container Deployment | Edge/offline scenarios |
| Custom Endpoints | Specialized requirements |

**SDK and API Integration:**
- Azure SDK for Python/C#
- REST API endpoints
- Azure AI SDKs
- CI/CD pipeline integration

#### 1.3 Manage, Monitor, and Secure an Azure AI Foundry Service

| Task | Tools/Methods |
|------|---------------|
| Monitoring | Azure Monitor, Application Insights |
| Cost Management | Azure Cost Management, Budgets |
| Key Management | Azure Key Vault, Managed Identity |
| Authentication | Microsoft Entra ID, RBAC |

#### 1.4 Implement AI Solutions Responsibly

**Content Safety Features:**
- Content filtering
- Prompt shields
- Harm detection
- Blocklists

**Governance Framework:**
- Define AI governance policies
- Implement content filters
- Monitor for abuse
- Document compliance

---

### 2. Implement Generative AI Solutions (15-20%)

#### 2.1 Build Generative AI Solutions with Azure AI Foundry

**Azure AI Foundry Components:**

| Component | Purpose |
|-----------|---------|
| Hub | Central governance and management |
| Project | Development workspace |
| Models | AI model catalog and deployment |
| Prompt Flow | Orchestration and testing |
| Evaluations | Model performance metrics |

**RAG Pattern Implementation:**

```
User Query → Embedding → Vector Search → Context Retrieval → LLM → Response
```

**Key RAG Components:**
- Azure AI Search for knowledge base
- Embeddings for semantic search
- Azure OpenAI for generation
- Prompt templates for consistency

#### 2.2 Use Azure OpenAI in Foundry Models

**Available Models:**

| Model | Capabilities |
|-------|--------------|
| GPT-4o | Multimodal, advanced reasoning |
| GPT-4 | Text generation, code, analysis |
| GPT-3.5 Turbo | Fast, cost-effective generation |
| DALL-E 3 | Image generation |
| Whisper | Speech transcription |
| Embeddings | Text similarity, search |

**Prompt Engineering Techniques:**
- Zero-shot prompting
- Few-shot prompting
- Chain-of-thought reasoning
- System message design
- Temperature and top-p tuning

#### 2.3 Optimize and Operationalize Generative AI

**Performance Parameters:**
| Parameter | Effect |
|-----------|--------|
| Temperature | Controls randomness (0-2) |
| Top-p | Nucleus sampling threshold |
| Max tokens | Response length limit |
| Frequency penalty | Reduces repetition |
| Presence penalty | Encourages topic diversity |

**Deployment Best Practices:**
- [ ] Configure scaling rules
- [ ] Implement retry logic
- [ ] Enable tracing and logging
- [ ] Monitor token usage
- [ ] Implement model reflection

---

### 3. Implement an Agentic Solution (5-10%)

#### 3.1 Create Custom Agents

**Agent Types:**

| Type | Description |
|------|-------------|
| Task Agent | Completes specific tasks |
| Autonomous Agent | Acts independently |
| Prompt/Response Agent | Interactive conversation |
| Multi-Agent | Coordinated agent teams |

**Building with Azure AI Foundry Agent Service:**

```python
# Example: Create agent with tools
agent = AgentBuilder()
    .with_model("gpt-4o")
    .with_tools([search_tool, calculator_tool])
    .with_instructions("You are a helpful assistant...")
    .build()
```

**Advanced Agent Frameworks:**
- Semantic Kernel
- AutoGen
- LangChain

**Multi-Agent Orchestration:**
- Agent routing
- Task delegation
- Conversation management
- State synchronization

#### 3.2 Test and Deploy Agents

- Unit testing for agent behaviors
- Integration testing with tools
- Performance optimization
- Production deployment patterns

---

### 4. Implement Computer Vision Solutions (10-15%)

#### 4.1 Analyze Images

**Azure AI Vision Capabilities:**

| Feature | Description |
|---------|-------------|
| Image Analysis | Tags, captions, objects |
| OCR | Text extraction |
| Face Detection | Facial analysis |
| Spatial Analysis | Video analytics |

**API Request Parameters:**
- Visual features selection
- Model version
- Language preferences
- Analysis options

#### 4.2 Implement Custom Vision Models

**Model Types:**
| Type | Use Case |
|------|----------|
| Image Classification | Categorize images |
| Object Detection | Locate objects with bounding boxes |
| Multi-label Classification | Multiple tags per image |

**Training Workflow:**
```
1. Create project
2. Upload and label images
3. Train model
4. Evaluate metrics
5. Publish endpoint
6. Consume in application
```

#### 4.3 Analyze Videos

**Azure AI Video Indexer:**
- Face identification
- Speech transcription
- Topic extraction
- Sentiment analysis
- Scene detection

---

### 5. Implement Natural Language Processing Solutions (15-20%)

#### 5.1 Analyze and Translate Text

| Capability | Description |
|------------|-------------|
| Key Phrase Extraction | Important phrases |
| Entity Recognition | Named entities |
| Sentiment Analysis | Emotional tone |
| Language Detection | Identify language |
| PII Detection | Personal information |
| Translation | Multi-language support |

#### 5.2 Process and Translate Speech

**Speech Service Capabilities:**

| Feature | Description |
|---------|-------------|
| Speech-to-Text | Audio transcription |
| Text-to-Speech | Voice synthesis |
| Speech Translation | Real-time translation |
| Custom Speech | Domain-specific models |
| Intent Recognition | Understand purpose |

**SSML (Speech Synthesis Markup Language):**
```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis">
    <voice name="en-US-JennyNeural">
        <prosody rate="medium" pitch="high">
            Hello, how can I help you?
        </prosody>
    </voice>
</speak>
```

#### 5.3 Implement Custom Language Models

**Conversational Language Understanding (CLU):**
- Define intents
- Create entities
- Add utterances
- Train and evaluate
- Deploy endpoints

**Question Answering:**
- Create knowledge base
- Import sources (URLs, files)
- Add Q&A pairs
- Multi-turn conversations
- Active learning

---

### 6. Implement Knowledge Mining and Information Extraction (15-20%)

#### 6.1 Implement Azure AI Search

**Core Concepts:**

| Component | Description |
|-----------|-------------|
| Index | Searchable data store |
| Indexer | Automated data ingestion |
| Data Source | Connection to data |
| Skillset | AI enrichment pipeline |
| Semantic Ranker | AI-powered relevance |

**Search Query Types:**
- Full-text search
- Vector search
- Hybrid search (text + vector)
- Semantic ranking

**Vector Search Implementation:**
```python
# Generate embeddings
embedding = openai.embeddings.create(
    model="text-embedding-ada-002",
    input="search query"
)

# Vector search
results = search_client.search(
    search_text=None,
    vector_queries=[VectorizedQuery(
        vector=embedding.data[0].embedding,
        k_nearest_neighbors=5,
        fields="content_vector"
    )]
)
```

#### 6.2 Implement Azure AI Document Intelligence

**Prebuilt Models:**

| Model | Use Case |
|-------|----------|
| Read | General OCR |
| Layout | Document structure |
| Invoice | Invoice processing |
| Receipt | Receipt extraction |
| ID Document | Identity documents |
| Business Card | Contact information |

**Custom Models:**
- Train with your documents
- Compose multiple models
- Define custom fields

#### 6.3 Extract Information with Azure AI Content Understanding

**New capabilities (2025):**
- OCR pipelines for images/documents
- Document summarization
- Classification and attribute detection
- Entity, table, and image extraction
- Multi-modal content processing

---

## Exam Preparation Resources

### Official Resources

| Resource | Link |
|----------|------|
| Exam Page | [AI-102](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/) |
| Study Guide | [Study Guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-102) |
| Practice Assessment | [Free Practice Test](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-102/practice/assessment?assessment-type=practice&assessmentId=61) |
| Learning Path | [AI-102 Training](https://learn.microsoft.com/en-us/credentials/certifications/exams/AI-102#two-ways-to-prepare) |

### Sample Repositories

- [Azure Search OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo)
- [AI Samples](https://github.com/Azure-Samples/cognitive-services-quickstart-code)
- [Azure AI Studio Samples](https://github.com/Azure-Samples/aistudio-python-quickstart-sample)

---

## Exam Tips

1. **Focus on Azure AI Foundry** - The exam has shifted toward Foundry services
2. **Know RAG patterns** - Understand retrieval augmented generation deeply
3. **Practice with agents** - New section on agentic solutions
4. **Understand responsible AI** - Content safety and governance
5. **Hands-on experience** - Build real solutions before the exam

---

*Last updated: November 2025*
