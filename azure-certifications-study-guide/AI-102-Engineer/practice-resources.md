# 🧪 AI-102 Practice Resources

## Official Practice Assessment

### Free Microsoft Practice Assessment
Microsoft provides a free practice assessment that mirrors the actual exam format.

🔗 **[Take the Free Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-102/practice/assessment?assessment-type=practice&assessmentId=61)**

| Feature | Details |
|---------|---------|
| Questions | 50+ questions |
| Format | Multiple choice, drag-and-drop, case studies |
| Time | Unlimited |
| Retakes | Unlimited |
| Cost | Free |

---

## Hands-On Lab Platforms

### Microsoft Learn Labs

These exercises are built into the Microsoft Learn modules:

| Lab | Description | Duration |
|-----|-------------|----------|
| Create Azure AI Services | Provision and configure | 30 min |
| Analyze images | Image analysis API | 45 min |
| Extract text with OCR | Document reading | 30 min |
| Analyze text | Language service | 45 min |
| Build Q&A solution | Knowledge base | 60 min |
| Deploy Azure OpenAI | Model deployment | 45 min |
| Implement RAG | Search + OpenAI | 90 min |

### GitHub Labs

| Repository | Description |
|------------|-------------|
| [AI-102 Labs](https://github.com/MicrosoftLearning/mslearn-ai-services) | Official course labs |
| [Azure OpenAI Demo](https://github.com/Azure-Samples/azure-search-openai-demo) | Complete RAG solution |
| [AI Samples](https://github.com/Azure-Samples/cognitive-services-quickstart-code) | Service quickstarts |

---

## Practice Projects

### Project 1: Build a RAG Chatbot (4-6 hours)

Build a complete RAG solution using Azure AI Search and Azure OpenAI:

**Components:**
- Azure AI Search with vector index
- Azure OpenAI GPT-4 model
- Document ingestion pipeline
- Chat interface

**Skills Tested:**
- Index configuration
- Vector embeddings
- Prompt engineering
- RAG pattern implementation

🔗 [Tutorial](https://learn.microsoft.com/en-us/azure/search/search-get-started-rag)

### Project 2: Custom Vision Object Detection (2-3 hours)

Train a custom object detection model:

**Components:**
- Custom Vision project
- Image labeling
- Model training
- API consumption

**Skills Tested:**
- Model training workflow
- Evaluation metrics
- Deployment and testing

### Project 3: Multi-language Q&A Bot (3-4 hours)

Build a question-answering solution with translation:

**Components:**
- Azure AI Language Q&A
- Translator service
- Bot Framework integration
- Multi-turn conversations

---

## Study Questions by Domain

### Domain 1: Plan and Manage Azure AI Solutions (20-25%)

**Sample Questions:**

1. **You need to deploy an Azure AI service that can be used offline. What should you use?**
   - A) Azure AI Services multi-service account
   - B) Container deployment ✓
   - C) Azure Functions
   - D) Virtual machine

2. **Which authentication method is recommended for production Azure AI services?**
   - A) API keys stored in code
   - B) API keys in environment variables
   - C) Managed identity ✓
   - D) SAS tokens

3. **You need to ensure AI-generated content doesn't include harmful material. What should you configure?**
   - A) Rate limiting
   - B) Content filtering ✓
   - C) Token limits
   - D) Temperature settings

---

### Domain 2: Implement Generative AI Solutions (15-20%)

**Sample Questions:**

1. **You're implementing RAG with Azure AI Search. Which search type provides the best semantic relevance?**
   - A) Full-text search only
   - B) Vector search only
   - C) Hybrid search with semantic ranking ✓
   - D) Filter-based search

2. **What is the purpose of the temperature parameter in Azure OpenAI?**
   - A) Controls request timeout
   - B) Controls randomness in responses ✓
   - C) Sets maximum tokens
   - D) Configures model version

3. **You need to reduce hallucinations in an Azure OpenAI model. What approach should you use?**
   - A) Increase temperature
   - B) Use few-shot prompting only
   - C) Implement RAG with grounding data ✓
   - D) Increase max tokens

4. **Which prompt engineering technique shows the model examples of desired output?**
   - A) Zero-shot prompting
   - B) Few-shot prompting ✓
   - C) Chain-of-thought
   - D) System prompting

---

### Domain 3: Implement Agentic Solutions (5-10%)

**Sample Questions:**

1. **You're building a multi-agent solution. Which component manages communication between agents?**
   - A) Agent tools
   - B) Orchestrator ✓
   - C) Prompt template
   - D) Model router

2. **Which framework can be used to build complex AI agents in Azure?**
   - A) Azure Functions
   - B) Semantic Kernel ✓
   - C) Azure Logic Apps
   - D) Power Automate

3. **An autonomous agent needs to perform actions without user approval. What must you configure?**
   - A) System prompt
   - B) Tool permissions and guardrails ✓
   - C) Model temperature
   - D) Token limits

---

### Domain 4: Implement Computer Vision Solutions (10-15%)

**Sample Questions:**

1. **You need to detect custom objects not available in the pre-built models. What should you use?**
   - A) Azure AI Vision image analysis
   - B) Custom Vision object detection ✓
   - C) Form Recognizer
   - D) Video Indexer

2. **Which metric measures the proportion of actual positive cases correctly identified?**
   - A) Precision
   - B) Recall ✓
   - C) F1 Score
   - D) Accuracy

3. **You need to extract text from handwritten forms. Which service should you use?**
   - A) Computer Vision Read API ✓
   - B) Custom Vision
   - C) Video Indexer
   - D) Speech to Text

---

### Domain 5: Implement NLP Solutions (15-20%)

**Sample Questions:**

1. **You need to build a custom intent classification model. Which service should you use?**
   - A) Text Analytics
   - B) Conversational Language Understanding ✓
   - C) Translator
   - D) Speech Service

2. **Which SSML element controls the speaking rate?**
   - A) `<voice>`
   - B) `<prosody>` ✓
   - C) `<audio>`
   - D) `<speak>`

3. **You need to detect personally identifiable information in text. Which feature should you use?**
   - A) Key phrase extraction
   - B) Named entity recognition
   - C) PII detection ✓
   - D) Sentiment analysis

4. **A knowledge base needs to support follow-up questions. What feature enables this?**
   - A) Active learning
   - B) Multi-turn conversations ✓
   - C) Chit-chat
   - D) Synonyms

---

### Domain 6: Knowledge Mining and Information Extraction (15-20%)

**Sample Questions:**

1. **You need to enrich documents during indexing with AI-generated content. What should you create?**
   - A) Data source
   - B) Indexer
   - C) Skillset ✓
   - D) Index

2. **Which Azure AI Search feature uses AI to improve search relevance?**
   - A) Filters
   - B) Facets
   - C) Semantic ranking ✓
   - D) Scoring profiles

3. **You need to extract data from invoices at scale. Which Document Intelligence approach is best?**
   - A) Custom model
   - B) Prebuilt invoice model ✓
   - C) Layout model
   - D) Read model

4. **To store enriched content for analysis outside the search index, you should create:**
   - A) Data source
   - B) Knowledge store ✓
   - C) Custom skill
   - D) Synonym map

---

## Code Samples

### Python: Azure OpenAI with RAG

```python
from azure.search.documents import SearchClient
from openai import AzureOpenAI

# Initialize clients
search_client = SearchClient(
    endpoint=search_endpoint,
    index_name="documents",
    credential=credential
)

openai_client = AzureOpenAI(
    api_key=api_key,
    api_version="2024-02-01",
    azure_endpoint=openai_endpoint
)

# Search for relevant context
def get_context(query: str) -> str:
    results = search_client.search(
        search_text=query,
        top=5,
        query_type="semantic",
        semantic_configuration_name="my-config"
    )
    return "\n".join([doc["content"] for doc in results])

# Generate response
def generate_response(query: str) -> str:
    context = get_context(query)
    
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"Answer based on this context:\n{context}"},
            {"role": "user", "content": query}
        ],
        temperature=0.7
    )
    
    return response.choices[0].message.content
```

### Python: Custom Vision Prediction

```python
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint, credentials)

with open("image.jpg", "rb") as image:
    results = predictor.detect_image(
        project_id, 
        published_name, 
        image
    )

for prediction in results.predictions:
    if prediction.probability > 0.5:
        print(f"{prediction.tag_name}: {prediction.probability:.2%}")
        print(f"  Box: {prediction.bounding_box}")
```

---

## Exam Day Preparation

### Final Week Checklist

- [ ] Complete all practice assessments
- [ ] Review incorrect answers deeply
- [ ] Re-read study guide for weak areas
- [ ] Practice with Azure services hands-on
- [ ] Review code patterns and SDKs

### Exam Environment

- Ensure stable internet connection
- Use the exam sandbox to familiarize yourself
- Have valid ID ready
- Clear your workspace (for proctored exams)

### Time Management

- ~2 minutes per question average
- Flag complex questions for review
- Don't spend too long on any single question
- Review flagged questions at the end

---

*Last updated: November 2025*
