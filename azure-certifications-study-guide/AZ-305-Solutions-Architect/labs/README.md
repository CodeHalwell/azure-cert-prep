# 🔬 AZ-305 Labs Directory

## Overview

This directory contains architecture design exercises for the AZ-305: Designing Microsoft Azure Infrastructure Solutions certification.

---

## 📁 Lab Files Index

| Lab | File | Domain |
|-----|------|--------|
| Lab 01 | `lab-01-identity-governance.md` | Identity & Governance |
| Lab 02 | `lab-02-monitoring-logging.md` | Identity & Governance |
| Lab 03 | `lab-03-storage-design.md` | Data Storage |
| Lab 04 | `lab-04-database-design.md` | Data Storage |
| Lab 05 | `lab-05-backup-dr.md` | Business Continuity |
| Lab 06 | `lab-06-high-availability.md` | Business Continuity |
| Lab 07 | `lab-07-compute-design.md` | Infrastructure |
| Lab 08 | `lab-08-network-design.md` | Infrastructure |
| Lab 09 | `lab-09-app-architecture.md` | Infrastructure |
| Lab 10 | `lab-10-migration-design.md` | Infrastructure |

---

## 🎯 Lab Objectives by Domain

### Identity, Governance, and Monitoring (25-30%)

| Lab | Architecture Focus |
|-----|-------------------|
| Lab 01 | Design identity solutions, Entra ID architecture, Conditional Access |
| Lab 02 | Design monitoring solutions, Log Analytics workspace, Application Insights |

### Data Storage Solutions (20-25%)

| Lab | Architecture Focus |
|-----|-------------------|
| Lab 03 | Design storage solutions, redundancy, access tiers, data protection |
| Lab 04 | Design database solutions, SQL vs. NoSQL selection, Cosmos DB |

### Business Continuity (15-20%)

| Lab | Architecture Focus |
|-----|-------------------|
| Lab 05 | Design backup solutions, disaster recovery with ASR |
| Lab 06 | Design high availability, availability zones, load balancing |

### Infrastructure Solutions (30-35%)

| Lab | Architecture Focus |
|-----|-------------------|
| Lab 07 | Design compute solutions, VM vs. containers vs. PaaS |
| Lab 08 | Design network solutions, hub-spoke, hybrid connectivity |
| Lab 09 | Design application architecture, microservices, messaging |
| Lab 10 | Design migration strategies, Azure Migrate, assessment |

---

## 🛠️ Prerequisites

Before starting the labs, ensure you have:

| Requirement | Description |
|-------------|-------------|
| Azure Subscription | Free account or existing subscription |
| Azure Architecture Center | Familiarity with reference architectures |
| Visio or Draw.io | For creating architecture diagrams |
| AZ-104 knowledge | Administrator-level understanding |

### Recommended Tools

| Tool | Purpose |
|------|---------|
| Azure Portal | Resource deployment and configuration |
| Azure CLI / PowerShell | Automation and scripting |
| VS Code | Template development |
| Visio / Draw.io | Architecture diagrams |

---

## 📋 Architecture Design Process

### Step 1: Gather Requirements

| Category | Questions to Ask |
|----------|-----------------|
| Business | What are the business objectives? |
| Technical | What are the technical constraints? |
| Compliance | What regulations apply? |
| Budget | What is the budget? |
| Timeline | What is the timeline? |

### Step 2: Design Solution

| Activity | Deliverable |
|----------|-------------|
| Select services | Service selection matrix |
| Design architecture | Architecture diagram |
| Plan networking | Network topology |
| Plan security | Security architecture |
| Calculate costs | Cost estimate |

### Step 3: Validate Design

| Validation | Criteria |
|------------|----------|
| Well-Architected Review | All 5 pillars |
| Security review | Zero Trust principles |
| Cost optimization | Within budget |
| Scalability | Meets growth requirements |

---

## 📊 Lab Completion Checklist

### Weeks 1-3: Identity & Governance
- [ ] Lab 01: Design identity solution for enterprise
- [ ] Lab 02: Design comprehensive monitoring strategy

### Weeks 4-5: Data Storage
- [ ] Lab 03: Design data storage architecture
- [ ] Lab 04: Design database solution

### Week 6: Business Continuity
- [ ] Lab 05: Design backup and DR strategy
- [ ] Lab 06: Design high availability architecture

### Weeks 7-9: Infrastructure
- [ ] Lab 07: Design compute architecture
- [ ] Lab 08: Design network architecture
- [ ] Lab 09: Design application architecture
- [ ] Lab 10: Design migration strategy

---

## 🔗 Additional Resources

| Resource | Link |
|----------|------|
| Azure Architecture Center | [Link](https://learn.microsoft.com/en-us/azure/architecture/) |
| Reference Architectures | [Link](https://learn.microsoft.com/en-us/azure/architecture/browse/) |
| Well-Architected Framework | [Link](https://learn.microsoft.com/en-us/azure/well-architected/) |
| Cloud Adoption Framework | [Link](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/) |
| Azure Pricing Calculator | [Link](https://azure.microsoft.com/pricing/calculator/) |

---

## ⚠️ Design Guidelines

### Best Practices

1. **Start with requirements** - Don't jump to solutions
2. **Consider trade-offs** - Cost vs. performance vs. security
3. **Use reference architectures** - Don't reinvent the wheel
4. **Document decisions** - Explain why, not just what
5. **Review with Well-Architected Framework** - All 5 pillars

### Common Pitfalls

| Pitfall | How to Avoid |
|---------|--------------|
| Over-engineering | Start simple, scale as needed |
| Under-estimating costs | Use pricing calculator early |
| Ignoring security | Build security in from the start |
| Single points of failure | Design for failure |
| Vendor lock-in | Consider portability requirements |

---

*Last updated: November 2025*
