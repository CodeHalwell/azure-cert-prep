# 🔬 AI-102 Hands-On Labs

## Lab Overview

These hands-on labs provide practical experience with Azure AI services covered in the AI-102 exam. Each lab includes step-by-step instructions and code samples.

---

## Lab Prerequisites

Before starting the labs:

1. **Azure Subscription** - Free trial or paid subscription
2. **Development Environment**:
   - Visual Studio Code
   - Python 3.8+ or .NET 6+
   - Azure CLI installed
3. **Azure Resources**:
   - Azure AI Services account
   - Azure OpenAI access (request separately)
   - Azure AI Search service

---

## Lab Index

| Lab # | Title | Duration | Difficulty | Skills |
|-------|-------|----------|------------|--------|
| 01 | [Provision Azure AI Services](./labs/lab-01-provision-ai-services.md) | 30 min | 🟢 Easy | Planning & Management |
| 02 | [Implement Azure OpenAI](./labs/lab-02-azure-openai.md) | 60 min | 🟡 Medium | Generative AI |
| 03 | [Build RAG Solution](./labs/lab-03-rag-solution.md) | 90 min | 🔴 Advanced | Gen AI + Search |
| 04 | [Create AI Agents](./labs/lab-04-ai-agents.md) | 60 min | 🔴 Advanced | Agentic Solutions |
| 05 | [Image Analysis](./labs/lab-05-image-analysis.md) | 45 min | 🟢 Easy | Computer Vision |
| 06 | [Custom Vision](./labs/lab-06-custom-vision.md) | 60 min | 🟡 Medium | Computer Vision |
| 07 | [Text Analytics](./labs/lab-07-text-analytics.md) | 45 min | 🟢 Easy | NLP |
| 08 | [Speech Services](./labs/lab-08-speech-services.md) | 45 min | 🟡 Medium | NLP |
| 09 | [Azure AI Search](./labs/lab-09-ai-search.md) | 75 min | 🟡 Medium | Knowledge Mining |
| 10 | [Document Intelligence](./labs/lab-10-document-intelligence.md) | 60 min | 🟡 Medium | Information Extraction |

---

## Lab 1: Provision Azure AI Services

### Objective
Create and configure Azure AI Services for use in AI solutions.

### Steps

1. **Create Resource Group**
```bash
az group create --name ai102-labs --location eastus
```

2. **Create AI Services Account**
```bash
az cognitiveservices account create \
    --name myaiservices \
    --resource-group ai102-labs \
    --kind CognitiveServices \
    --sku S0 \
    --location eastus
```

3. **Get Keys and Endpoint**
```bash
az cognitiveservices account keys list \
    --name myaiservices \
    --resource-group ai102-labs

az cognitiveservices account show \
    --name myaiservices \
    --resource-group ai102-labs \
    --query "properties.endpoint"
```

4. **Configure Managed Identity**
```bash
az cognitiveservices account identity assign \
    --name myaiservices \
    --resource-group ai102-labs
```

---

## Lab 2: Implement Azure OpenAI

### Objective
Deploy and use Azure OpenAI models for text generation.

### Prerequisites
- Approved Azure OpenAI access
- Azure subscription

### Steps

1. **Create Azure OpenAI Resource**
```bash
az cognitiveservices account create \
    --name myopenai \
    --resource-group ai102-labs \
    --kind OpenAI \
    --sku S0 \
    --location eastus
```

2. **Deploy a Model**
```bash
az cognitiveservices account deployment create \
    --name myopenai \
    --resource-group ai102-labs \
    --deployment-name gpt-4o \
    --model-name gpt-4o \
    --model-version "2024-05-13" \
    --model-format OpenAI \
    --sku-capacity 10 \
    --sku-name Standard
```

3. **Use the Model (Python)**
```python
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="your-api-key",
    api_version="2024-02-01",
    azure_endpoint="https://myopenai.openai.azure.com"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain Azure AI services in 3 sentences."}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
```

4. **Experiment with Parameters**
- Try different temperature values (0.0 - 2.0)
- Adjust max_tokens
- Test system prompts

---

## Lab 3: Build RAG Solution

### Objective
Implement Retrieval Augmented Generation with Azure AI Search and Azure OpenAI.

### Architecture
```
Documents → Azure AI Search (Index) → Retrieval → Azure OpenAI → Response
```

### Steps

1. **Create AI Search Service**
```bash
az search service create \
    --name myaisearch \
    --resource-group ai102-labs \
    --sku Basic \
    --location eastus
```

2. **Create Index with Vector Field**
```python
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    HnswAlgorithmConfiguration
)

index_client = SearchIndexClient(endpoint, credential)

fields = [
    SearchField(name="id", type=SearchFieldDataType.String, key=True),
    SearchField(name="content", type=SearchFieldDataType.String, searchable=True),
    SearchField(
        name="content_vector",
        type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
        searchable=True,
        vector_search_dimensions=1536,
        vector_search_profile_name="my-vector-profile"
    )
]

vector_search = VectorSearch(
    algorithms=[HnswAlgorithmConfiguration(name="my-hnsw")],
    profiles=[...]
)

index = SearchIndex(name="documents", fields=fields, vector_search=vector_search)
index_client.create_index(index)
```

3. **Upload Documents with Embeddings**
```python
from openai import AzureOpenAI

def get_embedding(text):
    response = openai_client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding

documents = [
    {
        "id": "1",
        "content": "Azure AI services provide...",
        "content_vector": get_embedding("Azure AI services provide...")
    }
]

search_client.upload_documents(documents)
```

4. **Implement RAG Query**
```python
def rag_query(user_query):
    # Get query embedding
    query_vector = get_embedding(user_query)
    
    # Search for relevant documents
    results = search_client.search(
        search_text=user_query,
        vector_queries=[
            VectorizedQuery(
                vector=query_vector,
                k_nearest_neighbors=3,
                fields="content_vector"
            )
        ],
        select=["content"]
    )
    
    # Build context
    context = "\n".join([doc["content"] for doc in results])
    
    # Generate response
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"Answer based on this context:\n{context}"},
            {"role": "user", "content": user_query}
        ]
    )
    
    return response.choices[0].message.content
```

---

## Lab 4: Create AI Agents

### Objective
Build an AI agent with tool-calling capabilities.

### Steps

1. **Define Agent Tools**
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_documents",
            "description": "Search internal documents for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Perform mathematical calculations",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "Math expression"}
                },
                "required": ["expression"]
            }
        }
    }
]
```

2. **Implement Tool Functions**
```python
def execute_tool(name, arguments):
    if name == "search_documents":
        return search_documents(arguments["query"])
    elif name == "calculate":
        return str(eval(arguments["expression"]))
    return "Unknown tool"
```

3. **Build Agent Loop**
```python
def run_agent(user_message):
    messages = [
        {"role": "system", "content": "You are a helpful agent with access to tools."},
        {"role": "user", "content": user_message}
    ]
    
    while True:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=tools
        )
        
        assistant_message = response.choices[0].message
        
        if assistant_message.tool_calls:
            messages.append(assistant_message)
            
            for tool_call in assistant_message.tool_calls:
                result = execute_tool(
                    tool_call.function.name,
                    json.loads(tool_call.function.arguments)
                )
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })
        else:
            return assistant_message.content
```

---

## Lab 5-10: Additional Labs

Detailed guides for labs 5-10 are available in the [labs/](./labs/) directory:

- **Lab 05**: Image analysis with Azure AI Vision
- **Lab 06**: Train custom object detection models
- **Lab 07**: Text analytics and entity recognition
- **Lab 08**: Speech-to-text and text-to-speech
- **Lab 09**: Azure AI Search with skillsets
- **Lab 10**: Document Intelligence for forms

---

## Lab Solutions

Complete solutions for all labs are available in the GitHub repository:

🔗 [AI-102 Lab Solutions](https://github.com/MicrosoftLearning/mslearn-ai-services)

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| 401 Unauthorized | Check API key configuration |
| 429 Rate Limited | Reduce request frequency or increase quota |
| Resource not found | Verify endpoint URL and resource name |
| Model not deployed | Deploy model in Azure OpenAI Studio |

### Getting Help

- [Microsoft Q&A](https://learn.microsoft.com/en-us/answers/products/)
- [Stack Overflow - Azure](https://stackoverflow.com/questions/tagged/azure)
- [Azure AI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/)

---

*Last updated: November 2025*
