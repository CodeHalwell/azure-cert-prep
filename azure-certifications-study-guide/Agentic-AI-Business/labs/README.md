# 🔬 AB-100 Labs Directory

## Overview

This directory contains hands-on lab exercises for the AB-100: Azure Agentic AI Business Solutions Architect certification.

---

## 📁 Lab Files Index

| Lab | File | Domain |
|-----|------|--------|
| Lab 01 | `lab-01-ai-assessment.md` | Plan AI Solutions |
| Lab 02 | `lab-02-ai-strategy.md` | Plan AI Solutions |
| Lab 03 | `lab-03-copilot-studio-basics.md` | Design AI Solutions |
| Lab 04 | `lab-04-generative-ai-agents.md` | Design AI Solutions |
| Lab 05 | `lab-05-azure-ai-foundry.md` | Design AI Solutions |
| Lab 06 | `lab-06-rag-implementation.md` | Deploy AI Solutions |
| Lab 07 | `lab-07-multi-agent.md` | Deploy AI Solutions |
| Lab 08 | `lab-08-mcp-integration.md` | Deploy AI Solutions |
| Lab 09 | `lab-09-monitoring.md` | Deploy AI Solutions |
| Lab 10 | `lab-10-governance.md` | Deploy AI Solutions |

---

## 🎯 Lab Objectives by Domain

### Plan AI Solutions (25-30%)

| Lab | Skills |
|-----|--------|
| Lab 01 | Assess business requirements, evaluate AI readiness, identify opportunities |
| Lab 02 | Define AI strategy, create governance framework, apply responsible AI |

### Design AI Solutions (25-30%)

| Lab | Skills |
|-----|--------|
| Lab 03 | Create agents in Copilot Studio, design topics, configure entities |
| Lab 04 | Add generative AI capabilities, implement plugins |
| Lab 05 | Use Azure AI Foundry, explore models, build prompt flows |

### Deploy AI Solutions (40-45%)

| Lab | Skills |
|-----|--------|
| Lab 06 | Implement RAG pattern, integrate Azure AI Search |
| Lab 07 | Design multi-agent orchestration, implement Semantic Kernel |
| Lab 08 | Build MCP servers, integrate tools and resources |
| Lab 09 | Configure monitoring, implement quality metrics |
| Lab 10 | Apply governance policies, configure content safety |

---

## 🛠️ Prerequisites

Before starting the labs, ensure you have:

| Requirement | Description |
|-------------|-------------|
| Microsoft 365 License | For Copilot Studio access |
| Azure Subscription | For Azure AI services |
| Copilot Studio Trial | 30-day trial available |
| VS Code | With AI extensions |
| Python 3.9+ | For SDK examples |

### Account Setup

```bash
# Install Azure CLI
# See https://learn.microsoft.com/en-us/cli/azure/install-azure-cli

# Login to Azure
az login

# Install Semantic Kernel
pip install semantic-kernel

# Install Azure AI SDKs
pip install azure-ai-inference
pip install azure-search-documents
```

---

## 📋 Lab Completion Checklist

### Weeks 1-2: Planning
- [ ] Lab 01: Complete AI assessment exercise
- [ ] Lab 02: Create AI strategy document

### Weeks 3-4: Design Basics
- [ ] Lab 03: Build first Copilot Studio agent
- [ ] Lab 04: Add generative AI capabilities

### Weeks 5-6: Advanced Design
- [ ] Lab 05: Create prompt flow in Azure AI Foundry
- [ ] Lab 06: Implement RAG solution

### Weeks 7-8: Deployment
- [ ] Lab 07: Build multi-agent system
- [ ] Lab 08: Create MCP integration

### Weeks 9-10: Operations
- [ ] Lab 09: Configure monitoring
- [ ] Lab 10: Implement governance

---

## 🔗 Lab Resources

### Copilot Studio

| Resource | Link |
|----------|------|
| Copilot Studio Portal | [Link](https://copilotstudio.microsoft.com/) |
| Documentation | [Link](https://learn.microsoft.com/en-us/microsoft-copilot-studio/) |
| Trial Sign-up | [Link](https://aka.ms/TryPVA) |

### Azure AI Foundry

| Resource | Link |
|----------|------|
| Azure AI Foundry | [Link](https://ai.azure.com/) |
| Documentation | [Link](https://learn.microsoft.com/en-us/azure/ai-studio/) |
| Samples | [Link](https://github.com/Azure-Samples/azureai-samples) |

### SDKs and Tools

| Resource | Link |
|----------|------|
| Semantic Kernel | [Link](https://github.com/microsoft/semantic-kernel) |
| Prompt Flow | [Link](https://github.com/microsoft/promptflow) |
| AutoGen | [Link](https://github.com/microsoft/autogen) |
| MCP | [Link](https://modelcontextprotocol.io/) |

---

## ⚠️ Important Notes

### Best Practices

1. **Start with planning labs** - Understand requirements before building
2. **Document your work** - Keep notes on design decisions
3. **Test thoroughly** - Validate agent behavior in all scenarios
4. **Monitor costs** - Track API usage and costs
5. **Apply responsible AI** - Consider ethics in all designs

### Common Challenges

| Challenge | Solution |
|-----------|----------|
| Rate limits | Implement retry logic and caching |
| Context length | Use summarization and chunking |
| Hallucinations | Implement RAG and grounding |
| Security | Apply least privilege and content filters |
| Cost management | Monitor usage, optimize prompts |

### Cleanup

After completing labs:

```bash
# Delete Azure resource groups
az group delete --name <resource-group-name> --yes --no-wait

# Review Copilot Studio agents for cleanup
# Remove test agents from Copilot Studio portal
```

---

## 📊 Lab Difficulty Levels

| Lab | Difficulty | Time |
|-----|------------|------|
| Lab 01 | ⭐ Beginner | 2 hours |
| Lab 02 | ⭐ Beginner | 2 hours |
| Lab 03 | ⭐⭐ Intermediate | 3 hours |
| Lab 04 | ⭐⭐ Intermediate | 3 hours |
| Lab 05 | ⭐⭐ Intermediate | 3 hours |
| Lab 06 | ⭐⭐⭐ Advanced | 4 hours |
| Lab 07 | ⭐⭐⭐ Advanced | 4 hours |
| Lab 08 | ⭐⭐⭐ Advanced | 4 hours |
| Lab 09 | ⭐⭐ Intermediate | 3 hours |
| Lab 10 | ⭐⭐ Intermediate | 3 hours |

**Total Lab Time: ~30 hours**

---

*Last updated: November 2025*
