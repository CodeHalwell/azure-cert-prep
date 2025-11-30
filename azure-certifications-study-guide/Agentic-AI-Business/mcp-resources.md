# 🔌 Model Context Protocol (MCP) Resources

## Overview

The Model Context Protocol (MCP) is an open standard for connecting AI agents to external tools, data, and services. Understanding MCP is essential for the AB-100 certification.

---

## 🎯 What is MCP?

MCP provides a standardized way for AI agents to:

1. **Access Tools** - Execute functions and actions
2. **Read Resources** - Access data and documents
3. **Use Prompts** - Leverage reusable prompt templates
4. **Manage Context** - Maintain conversation state

```
┌─────────────────────────────────────────────────────────────┐
│                      AI Application                          │
│                    (Host/Client)                             │
└───────────────────────────┬─────────────────────────────────┘
                            │
                    ┌───────▼───────┐
                    │  MCP Protocol │
                    └───────┬───────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
┌───────▼────────┐ ┌────────▼───────┐ ┌─────────▼──────┐
│  MCP Server 1  │ │  MCP Server 2  │ │  MCP Server 3  │
│  (Database)    │ │  (Search)      │ │  (Actions)     │
└────────────────┘ └────────────────┘ └────────────────┘
```

---

## 📊 MCP Components

### 1. Tools

Tools are functions that agents can call to perform actions.

| Aspect | Description |
|--------|-------------|
| **Definition** | Named functions with typed parameters |
| **Invocation** | Agent requests tool execution |
| **Response** | Tool returns results to agent |
| **Examples** | Search, calculate, create, update |

**Tool Schema Example:**
```json
{
  "name": "search_documents",
  "description": "Search for documents by query",
  "inputSchema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search query"
      },
      "limit": {
        "type": "integer",
        "description": "Maximum results",
        "default": 10
      }
    },
    "required": ["query"]
  }
}
```

### 2. Resources

Resources are data that agents can read.

| Aspect | Description |
|--------|-------------|
| **Definition** | Named data sources with URIs |
| **Access** | Agent requests resource content |
| **Types** | Documents, databases, APIs |
| **Updates** | Resources can notify of changes |

**Resource Types:**
| Type | Description | Example |
|------|-------------|---------|
| Static | Fixed content | Configuration files |
| Dynamic | Content changes | Database records |
| Streaming | Real-time updates | Event streams |

### 3. Prompts

Prompts are reusable templates for agent instructions.

| Aspect | Description |
|--------|-------------|
| **Definition** | Named prompt templates |
| **Parameters** | Customizable placeholders |
| **Purpose** | Consistent agent behavior |

### 4. Sampling

Sampling allows servers to request LLM completions.

| Aspect | Description |
|--------|-------------|
| **Purpose** | Server-initiated AI requests |
| **Control** | Human-in-the-loop approval |
| **Use Cases** | Complex reasoning, validation |

---

## 🏗️ MCP Architecture Patterns

### Single Server Pattern

Simple integration with one MCP server.

```
┌───────────────┐       ┌───────────────┐
│    Client     │◄─────►│  MCP Server   │
│  (AI Agent)   │       │  (Database)   │
└───────────────┘       └───────────────┘
```

### Multi-Server Pattern

Multiple MCP servers for different capabilities.

```
                    ┌───────────────────────┐
                    │       AI Agent        │
                    │      (Client)         │
                    └───────────┬───────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
┌───────▼───────┐       ┌───────▼───────┐       ┌───────▼───────┐
│  File Server  │       │ Search Server │       │ Action Server │
│    (MCP)      │       │    (MCP)      │       │    (MCP)      │
└───────────────┘       └───────────────┘       └───────────────┘
```

### Gateway Pattern

Centralized gateway for MCP server management.

```
┌───────────────┐       ┌───────────────┐       ┌───────────────┐
│    Client     │◄─────►│   Gateway     │◄─────►│  MCP Server 1 │
│  (AI Agent)   │       │   (Routing,   │◄─────►│  MCP Server 2 │
└───────────────┘       │    Auth)      │◄─────►│  MCP Server 3 │
                        └───────────────┘       └───────────────┘
```

---

## 🔐 MCP Security

### Authentication

| Method | Description |
|--------|-------------|
| **API Keys** | Simple token-based auth |
| **OAuth** | Standard OAuth 2.0 flows |
| **Managed Identity** | Azure managed identities |

### Authorization

| Level | Control |
|-------|---------|
| **Server** | Which servers can agent access? |
| **Tool** | Which tools can agent call? |
| **Resource** | Which resources can agent read? |
| **Data** | What data can be returned? |

### Security Best Practices

| Practice | Description |
|----------|-------------|
| **Least privilege** | Grant minimum required access |
| **Input validation** | Validate all tool inputs |
| **Output filtering** | Filter sensitive data |
| **Audit logging** | Log all MCP interactions |
| **Rate limiting** | Prevent abuse |

---

## 🛠️ Implementing MCP

### Building an MCP Server

**Key Steps:**
1. Define capabilities (tools, resources, prompts)
2. Implement protocol handlers
3. Add security controls
4. Deploy and register

### MCP with Azure Services

| Azure Service | MCP Integration |
|---------------|-----------------|
| Azure AI Search | Search tools/resources |
| Cosmos DB | Database resources |
| Azure Functions | Custom tools |
| Azure Storage | Document resources |
| Key Vault | Secure configuration |

### Example: Search Tool Implementation

```python
# Conceptual MCP tool implementation
class SearchTool:
    name = "search_documents"
    description = "Search Azure AI Search index"
    
    def execute(self, query: str, limit: int = 10):
        # Connect to Azure AI Search
        # Execute query
        # Return results
        pass
```

---

## 📋 MCP Use Cases

### Enterprise Knowledge Base

```
User Query → Agent → MCP Search Tool → Azure AI Search
                                              │
                                              ▼
                                        Documents
                                              │
                                              ▼
                             Agent synthesizes response
```

### Multi-System Automation

```
User Request → Orchestrator Agent
                     │
        ┌────────────┼────────────┐
        │            │            │
   CRM Tool     ERP Tool    Email Tool
   (Salesforce) (SAP)      (Outlook)
        │            │            │
        └────────────┼────────────┘
                     │
              Combined Action
```

### Data Analysis Pipeline

```
Analysis Request → Agent
                     │
        ┌────────────┼────────────┐
        │            │            │
   Data Tool    Compute Tool  Viz Tool
   (SQL)        (Python)      (Charts)
        │            │            │
        └────────────┼────────────┘
                     │
           Analysis Results
```

---

## 🎓 Learning Resources

### Official Documentation

| Resource | Link |
|----------|------|
| MCP Specification | [Link](https://modelcontextprotocol.io/) |
| MCP GitHub | [Link](https://github.com/modelcontextprotocol) |
| Azure MCP Integration | [Link](https://learn.microsoft.com/en-us/azure/) |

### Tutorials and Guides

| Resource | Description |
|----------|-------------|
| MCP Quickstart | Getting started with MCP |
| Building MCP Servers | Server implementation guide |
| MCP with Azure | Azure integration patterns |
| Security Guide | MCP security best practices |

### Sample Implementations

| Sample | Description |
|--------|-------------|
| File System Server | Access local files via MCP |
| Database Server | Query databases via MCP |
| API Gateway Server | Access REST APIs via MCP |
| Search Server | Azure AI Search via MCP |

---

## ✅ MCP Checklist for AB-100

### Core Concepts
- [ ] Understand MCP components (tools, resources, prompts)
- [ ] Know MCP communication patterns
- [ ] Understand server vs. client roles

### Architecture
- [ ] Design single-server integrations
- [ ] Design multi-server architectures
- [ ] Implement gateway patterns

### Security
- [ ] Implement authentication
- [ ] Configure authorization
- [ ] Apply security best practices

### Implementation
- [ ] Build MCP servers for Azure services
- [ ] Integrate with AI agents
- [ ] Monitor and troubleshoot

---

## 🔗 Quick Reference

### MCP Message Types

| Type | Direction | Purpose |
|------|-----------|---------|
| `initialize` | Client → Server | Start session |
| `tools/list` | Client → Server | Get available tools |
| `tools/call` | Client → Server | Execute a tool |
| `resources/list` | Client → Server | Get resources |
| `resources/read` | Client → Server | Read resource |
| `prompts/list` | Client → Server | Get prompts |
| `prompts/get` | Client → Server | Get prompt content |
| `sampling/create` | Server → Client | Request completion |

### Common Tool Categories

| Category | Examples |
|----------|----------|
| **Search** | Document search, web search |
| **Data** | Database queries, API calls |
| **Action** | Send email, create record |
| **Compute** | Calculate, transform, analyze |
| **Integration** | CRM, ERP, productivity apps |

---

*Last updated: November 2025*
