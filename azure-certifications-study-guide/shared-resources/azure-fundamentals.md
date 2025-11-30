# ☁️ Azure Fundamentals Reference

## Overview

This reference covers fundamental Azure concepts that apply across all Azure certifications.

---

## 🌐 Azure Global Infrastructure

### Regions

Azure operates in 60+ regions worldwide.

| Geography | Regions | Examples |
|-----------|---------|----------|
| Americas | 12+ | East US, West US, Brazil South |
| Europe | 10+ | North Europe, West Europe, UK South |
| Asia Pacific | 15+ | East Asia, Southeast Asia, Australia East |
| Middle East & Africa | 5+ | UAE North, South Africa North |

### Availability Zones

| Concept | Description |
|---------|-------------|
| **Definition** | Physically separate datacenters within a region |
| **Count** | Minimum 3 zones per enabled region |
| **Purpose** | High availability and disaster recovery |
| **Latency** | <2ms between zones |

### Region Pairs

| Concept | Description |
|---------|-------------|
| **Definition** | Two regions within same geography |
| **Purpose** | Disaster recovery and data residency |
| **Example** | East US ↔ West US |
| **Updates** | Sequential updates to prevent dual outages |

---

## 📦 Azure Resource Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│                  Microsoft Entra ID Tenant                   │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                    Management Groups                         │
│           (Optional hierarchy for governance)                │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                      Subscriptions                           │
│              (Billing and access boundary)                   │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                    Resource Groups                           │
│             (Logical containers for resources)               │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                        Resources                             │
│            (VMs, storage, databases, etc.)                   │
└─────────────────────────────────────────────────────────────┘
```

### Management Groups

| Purpose | Description |
|---------|-------------|
| Organize | Group subscriptions hierarchically |
| Govern | Apply policies across subscriptions |
| Access | Manage access at scale |
| Compliance | Enforce organizational standards |

### Subscriptions

| Type | Purpose |
|------|---------|
| **Pay-As-You-Go** | Standard consumption-based |
| **Enterprise Agreement** | Large organization contracts |
| **CSP** | Partner-managed subscriptions |
| **Free** | Trial and learning |
| **Dev/Test** | Discounted development pricing |

### Resource Groups

| Best Practice | Description |
|---------------|-------------|
| Lifecycle | Group resources that share lifecycle |
| Application | Group by application or workload |
| Environment | Separate dev, test, prod |
| Region | Consider regional placement |

---

## 🔐 Identity and Access

### Microsoft Entra ID (Azure AD)

| Feature | Description |
|---------|-------------|
| **Users** | Individual identity accounts |
| **Groups** | Collections of users |
| **Applications** | Service principals and managed identities |
| **Roles** | Permissions assignments |

### Authentication Methods

| Method | Security Level | Use Case |
|--------|---------------|----------|
| Password only | Low | Legacy systems |
| MFA (SMS) | Medium | Basic additional security |
| MFA (Authenticator) | High | Recommended for users |
| Passwordless | Very High | Modern security |
| Managed Identity | Very High | Azure resources |

### Azure RBAC

| Level | Scope | Example |
|-------|-------|---------|
| **Owner** | Full access | Subscription admins |
| **Contributor** | Manage, no access mgmt | Developers |
| **Reader** | View only | Auditors |
| **Custom** | Specific permissions | Specialized roles |

**Scope Hierarchy:**
```
Management Group → Subscription → Resource Group → Resource
      ↓                ↓               ↓             ↓
   (Inherited)    (Inherited)    (Inherited)    (Direct)
```

---

## 💾 Core Azure Services

### Compute

| Service | Type | Use Case |
|---------|------|----------|
| Virtual Machines | IaaS | Full OS control |
| App Service | PaaS | Web applications |
| Azure Functions | Serverless | Event-driven code |
| Azure Kubernetes Service | Containers | Container orchestration |
| Container Instances | Containers | Simple containers |
| Azure Batch | Batch | HPC workloads |

### Storage

| Service | Type | Use Case |
|---------|------|----------|
| Blob Storage | Object | Unstructured data |
| File Storage | File | File shares |
| Queue Storage | Queue | Message queuing |
| Table Storage | NoSQL | Key-value data |
| Disk Storage | Block | VM disks |

### Networking

| Service | Purpose | Layer |
|---------|---------|-------|
| Virtual Network | Isolation | Network |
| Load Balancer | Distribution | Layer 4 |
| Application Gateway | Web routing | Layer 7 |
| Azure DNS | Name resolution | DNS |
| VPN Gateway | Hybrid connectivity | Network |
| ExpressRoute | Private connectivity | Network |

### Databases

| Service | Type | Use Case |
|---------|------|----------|
| Azure SQL | Relational | SQL Server workloads |
| Cosmos DB | NoSQL | Global distribution |
| Azure MySQL | Relational | MySQL workloads |
| Azure PostgreSQL | Relational | PostgreSQL workloads |
| Redis Cache | In-memory | Caching |

---

## 💰 Cost Management

### Pricing Factors

| Factor | Impact |
|--------|--------|
| **Region** | Prices vary by region |
| **Tier** | Different service tiers |
| **Reserved** | 1-3 year commitments |
| **Spot** | Discounted spare capacity |
| **Hybrid Benefit** | Use existing licenses |

### Cost Tools

| Tool | Purpose |
|------|---------|
| Pricing Calculator | Estimate costs |
| TCO Calculator | Compare on-prem vs cloud |
| Cost Management | Monitor and optimize |
| Azure Advisor | Cost recommendations |

### Cost Optimization Strategies

| Strategy | Savings |
|----------|---------|
| Right-sizing | 20-30% |
| Reserved Instances | Up to 72% |
| Spot VMs | Up to 90% |
| Auto-shutdown | Variable |
| Hybrid Benefit | 40%+ |

---

## 🛡️ Security Fundamentals

### Defense in Depth

```
┌─────────────────────────────────────────────────────────────┐
│                       Physical Security                      │
├─────────────────────────────────────────────────────────────┤
│                    Identity & Access                         │
├─────────────────────────────────────────────────────────────┤
│                       Perimeter                              │
├─────────────────────────────────────────────────────────────┤
│                        Network                               │
├─────────────────────────────────────────────────────────────┤
│                        Compute                               │
├─────────────────────────────────────────────────────────────┤
│                       Application                            │
├─────────────────────────────────────────────────────────────┤
│                          Data                                │
└─────────────────────────────────────────────────────────────┘
```

### Security Services

| Service | Purpose |
|---------|---------|
| Microsoft Defender for Cloud | Security posture |
| Azure Firewall | Network security |
| Key Vault | Secrets management |
| DDoS Protection | Attack protection |
| Azure Information Protection | Data classification |

---

## 📊 Governance

### Azure Policy

| Effect | Description |
|--------|-------------|
| **Audit** | Log non-compliance |
| **Deny** | Block non-compliant resources |
| **Append** | Add required configurations |
| **DeployIfNotExists** | Auto-remediate |
| **Modify** | Add, update, or remove properties |

### Blueprints

| Component | Purpose |
|-----------|---------|
| Role assignments | Standard RBAC |
| Policy assignments | Governance policies |
| ARM templates | Resource deployment |
| Resource groups | Organizational structure |

### Compliance

| Standard | Description |
|----------|-------------|
| SOC | Service Organization Controls |
| ISO 27001 | Information security |
| HIPAA | Healthcare data |
| GDPR | EU data protection |
| FedRAMP | US government |

---

## 📈 Monitoring

### Azure Monitor Components

| Component | Purpose |
|-----------|---------|
| **Metrics** | Numerical performance data |
| **Logs** | Text-based activity data |
| **Alerts** | Proactive notifications |
| **Dashboards** | Visualizations |
| **Workbooks** | Interactive reports |

### Log Analytics

| Concept | Description |
|---------|-------------|
| Workspace | Central repository for logs |
| KQL | Query language for logs |
| Tables | Structured log data |
| Retention | How long data is kept |

---

## 🔗 Quick Reference Links

### Documentation

| Resource | Link |
|----------|------|
| Azure Documentation | [Link](https://learn.microsoft.com/en-us/azure/) |
| Azure Architecture Center | [Link](https://learn.microsoft.com/en-us/azure/architecture/) |
| Azure Pricing | [Link](https://azure.microsoft.com/pricing/) |
| Azure Status | [Link](https://status.azure.com/) |

### Tools

| Resource | Link |
|----------|------|
| Azure Portal | [Link](https://portal.azure.com) |
| Azure CLI | [Link](https://learn.microsoft.com/en-us/cli/azure/) |
| Azure PowerShell | [Link](https://learn.microsoft.com/en-us/powershell/azure/) |
| Azure Mobile | App Store / Play Store |

---

*Last updated: November 2025*
