# 🔧 AB-100 Agentic AI Resources Reference

Reference for Azure and Microsoft resources relevant to the Agentic AI Business Solutions Architect (AB-100, preview).

---

## 📋 Table of Contents

1. Azure OpenAI & Azure AI Studio
2. Agent Orchestration & Tools
   - Prompt Flow
   - Function Calling & Tooling
   - MCP (Model Context Protocol) at a high level
3. Data & Retrieval
   - Azure AI Search
   - Vector Stores & RAG
   - Enterprise data sources (Fabric, Cosmos DB, SQL, SharePoint)
4. Integration Channels
   - Web apps & APIs
   - Teams, M365 Copilot extensibility
5. Governance & Responsible AI
   - Content Safety
   - Policy & access control

---

# 1. Azure OpenAI & Azure AI Studio

## 1.1 Azure OpenAI

- Same base capabilities as AI-102 but with emphasis on **agentic patterns**

### Built-in

- GPT-4/4o reasoning models
- Function calling, JSON mode
- Content safety hooks

### Requires Customization

- Agent orchestration logic (what tools to call, when)
- Prompt engineering for multi-step workflows

---

## 1.2 Azure AI Studio

- Primary canvas for building generative AI and agent experiences

### Built-in

- Prompt flow
- Model catalog
- Evaluation tools

### Requires Customization

- Flow design, tool graph, and integration points

---

# 2. Agent Orchestration & Tools

## 2.1 Prompt Flow

- Visual and code-first experience to orchestrate models, tools, and control logic

### Built-in

- Node types for LLM calls, Python code, HTTP calls, conditional logic

### Requires Customization

- Defining tool interfaces, error handling, retries, and fallbacks

---

## 2.2 Function Calling & Tooling

- Mechanism to let models call structured tools/APIs

### Requires Customization

- Tool schemas, security, and rate limiting

---

## 2.3 MCP (Model Context Protocol) – High Level

- Standard for connecting tools and data to AI agents
- Not an Azure product itself, but relevant for **extensibility** and **integration** patterns

---

# 3. Data & Retrieval

## 3.1 Azure AI Search & Vector Stores

- As in AI-102, but focused on **retrieval-augmented generation (RAG)** patterns

### Built-in

- Hybrid search, semantic ranking, vector search

### Requires Customization

- Chunking strategies, index schema, ranking profiles

---

## 3.2 Enterprise Data Sources

- Connectors to Fabric, Cosmos DB, SQL DB, SharePoint, and others

### Design Points

- Data freshness vs indexing cost
- Security trimming and per-user data filters

---

# 4. Integration Channels

## 4.1 Web Apps & APIs

- Host agent front-ends and backends via App Service, Container Apps, Functions

## 4.2 Teams & M365 Extensibility

- Build agent experiences as Teams apps or Copilot plugins

---

# 5. Governance & Responsible AI

## 5.1 Content Safety

- Text and image moderation, jailbreak protection, groundedness checks

## 5.2 Policy & Access Control

- Enforce data boundaries using Entra ID, RBAC, and application permissions

---

*Last updated: November 2025*