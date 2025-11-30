# 📖 AZ-305 Study Guide

## Designing Microsoft Azure Infrastructure Solutions

This comprehensive study guide covers all skills measured in the AZ-305 exam, updated for April 2025.

---

## 📊 Exam Overview

| Attribute | Details |
|-----------|---------|
| **Total Questions** | 40-60 |
| **Duration** | 120 minutes |
| **Passing Score** | 700/1000 |
| **Question Types** | Multiple choice, case studies, drag-and-drop |

---

# Domain 1: Design Identity, Governance, and Monitoring (25-30%)

## 1.1 Design Solutions for Logging and Monitoring

### Azure Monitor

| Component | Purpose |
|-----------|---------|
| **Metrics** | Numerical data about resource performance |
| **Logs** | Detailed records stored in Log Analytics |
| **Alerts** | Proactive notifications based on conditions |
| **Dashboards** | Visualizations of key metrics |
| **Workbooks** | Interactive reports and analysis |

### Log Analytics Workspace Design

**Key Considerations:**
- Centralized vs. distributed workspaces
- Data residency requirements
- Access control requirements
- Cost management (data retention, ingestion)
- Integration with other services

### Application Insights

| Feature | Use Case |
|---------|----------|
| Request tracking | Monitor API/web requests |
| Dependency tracking | External service calls |
| Exception logging | Error tracking and analysis |
| Performance monitoring | Response times, throughput |
| Availability tests | Synthetic monitoring |

### Monitoring Strategy Design

```
Application Layer
    └── Application Insights
Infrastructure Layer
    └── Azure Monitor (Metrics/Logs)
Security Layer
    └── Microsoft Defender for Cloud
Business Layer
    └── Custom dashboards and alerts
```

---

## 1.2 Design Authentication and Authorization Solutions

### Microsoft Entra ID (Azure AD)

| Identity Type | Use Case |
|---------------|----------|
| Cloud-only | New organizations, no on-premises AD |
| Hybrid | Sync with on-premises AD |
| B2B | External partners and vendors |
| B2C | Consumer-facing applications |

### Authentication Methods

| Method | Security Level | User Experience |
|--------|---------------|-----------------|
| Password only | Low | Simple |
| MFA (SMS/Voice) | Medium | Moderate friction |
| MFA (Authenticator) | High | Low friction |
| Passwordless (FIDO2) | Very High | Excellent |
| Passwordless (Windows Hello) | Very High | Excellent |

### Conditional Access

**Key Components:**
- **Assignments:** Users, groups, cloud apps
- **Conditions:** Sign-in risk, device state, location
- **Access controls:** Grant, block, require MFA

**Common Policies:**
1. Require MFA for admins
2. Block legacy authentication
3. Require compliant devices
4. Location-based access

### Privileged Identity Management (PIM)

| Feature | Purpose |
|---------|---------|
| Just-in-time access | Temporary role activation |
| Approval workflows | Require approval for sensitive roles |
| Access reviews | Periodic review of role assignments |
| Audit logs | Track all privileged activities |

---

## 1.3 Design Governance

### Management Groups

```
Root Management Group
├── Production
│   ├── US Region
│   └── EU Region
├── Development
│   └── All Dev Subscriptions
└── Sandbox
    └── Experimental Projects
```

### Azure Policy

| Policy Type | Purpose |
|-------------|---------|
| **Audit** | Log non-compliance |
| **Deny** | Prevent non-compliant deployments |
| **Append** | Add required tags or settings |
| **DeployIfNotExists** | Auto-remediate resources |

**Common Initiatives:**
- Allowed locations
- Allowed VM SKUs
- Required tags
- Enforce encryption
- Network security

### Azure Blueprints

| Component | Purpose |
|-----------|---------|
| Role assignments | Standard RBAC setup |
| Policy assignments | Governance policies |
| ARM templates | Standard resources |
| Resource groups | Organizational structure |

### Naming and Tagging Strategy

**Naming Convention Example:**
```
{resource-type}-{workload}-{environment}-{region}-{instance}
vm-web-prod-eastus-001
```

**Required Tags:**
| Tag | Purpose |
|-----|---------|
| Environment | prod, dev, test |
| Owner | Team or individual |
| CostCenter | Billing allocation |
| Project | Business project |

---

# Domain 2: Design Data Storage Solutions (20-25%)

## 2.1 Design Data Storage Solutions

### Storage Account Types

| Type | Use Case | Performance |
|------|----------|-------------|
| Standard GPv2 | General purpose | Standard |
| Premium Block Blob | High-performance blob | Premium |
| Premium File Shares | Enterprise file shares | Premium |
| Premium Page Blob | VM disks | Premium |

### Blob Storage Tiers

| Tier | Access Frequency | Cost Model |
|------|------------------|------------|
| Hot | Frequently accessed | Higher storage, lower access |
| Cool | Infrequently (30+ days) | Lower storage, higher access |
| Cold | Rarely (90+ days) | Lower storage, higher access |
| Archive | Rarely (180+ days) | Lowest storage, highest access |

### Redundancy Options

| Option | Durability | Availability | Use Case |
|--------|------------|--------------|----------|
| LRS | 11 9's | Single datacenter | Dev/test |
| ZRS | 12 9's | Single region, 3 zones | Production |
| GRS | 16 9's | Two regions | Disaster recovery |
| GZRS | 16 9's | Primary: 3 zones, Secondary | Critical workloads |

---

## 2.2 Design Database Solutions

### Database Selection Guide

| Requirement | Recommended Service |
|-------------|-------------------|
| Relational, SQL Server | Azure SQL Database |
| Relational, open source | Azure Database for PostgreSQL/MySQL |
| NoSQL, global distribution | Azure Cosmos DB |
| Data warehouse | Azure Synapse Analytics |
| In-memory caching | Azure Cache for Redis |

### Azure SQL Database Options

| Option | Use Case | Management |
|--------|----------|------------|
| Single Database | Individual applications | Fully managed |
| Elastic Pool | Multiple databases, shared resources | Fully managed |
| Managed Instance | Lift-and-shift SQL Server | Near-full compatibility |
| SQL Server on VMs | Full control needed | Self-managed |

### Azure Cosmos DB

| API | Use Case |
|-----|----------|
| Core (SQL) | Document store, most flexibility |
| MongoDB | MongoDB compatibility |
| Cassandra | Wide-column store |
| Gremlin | Graph database |
| Table | Key-value store |

**Consistency Levels (Strong to Eventual):**
1. Strong
2. Bounded Staleness
3. Session
4. Consistent Prefix
5. Eventual

---

## 2.3 Design Data Integration

### Azure Data Factory

| Component | Purpose |
|-----------|---------|
| Linked Services | Connections to data sources |
| Datasets | Data structures |
| Pipelines | Orchestration of activities |
| Activities | Data movement/transformation |
| Triggers | Schedule or event-based execution |

### Data Integration Patterns

| Pattern | Use Case |
|---------|----------|
| ETL | Transform before loading |
| ELT | Load then transform in destination |
| Real-time streaming | Event-driven processing |
| Batch processing | Scheduled large-scale processing |

---

# Domain 3: Design Business Continuity Solutions (15-20%)

## 3.1 Design Backup and Recovery Solutions

### Azure Backup

| Workload | Backup Method |
|----------|---------------|
| Azure VMs | VM-level backup |
| Azure Files | File share snapshots |
| SQL in VMs | SQL-aware backup |
| Azure SQL | Automatic backups |
| On-premises | MARS agent, DPM, MABS |

### Backup Policies

| Element | Consideration |
|---------|---------------|
| Frequency | Daily, weekly, monthly |
| Retention | How long to keep backups |
| Instant restore | Keep snapshots for fast recovery |
| Cross-region | Copy to secondary region |

---

## 3.2 Design High Availability Solutions

### Availability Options

| Option | Protection Level | SLA |
|--------|-----------------|-----|
| Single VM (Premium SSD) | None | 99.9% |
| Availability Set | Rack/Update failure | 99.95% |
| Availability Zone | Datacenter failure | 99.99% |
| Multi-region | Region failure | >99.99% |

### Load Balancing Solutions

| Service | Layer | Scope | Use Case |
|---------|-------|-------|----------|
| Azure Load Balancer | L4 | Regional | VM distribution |
| Application Gateway | L7 | Regional | Web app routing |
| Azure Front Door | L7 | Global | Global web apps |
| Traffic Manager | DNS | Global | DNS-based routing |

---

## 3.3 Design Disaster Recovery

### Azure Site Recovery

| Scenario | Source | Target |
|----------|--------|--------|
| Azure to Azure | Primary region | Secondary region |
| VMware to Azure | On-premises VMware | Azure |
| Hyper-V to Azure | On-premises Hyper-V | Azure |
| Physical to Azure | Physical servers | Azure |

### RTO and RPO Considerations

| Term | Definition | Factors |
|------|------------|---------|
| **RTO** | Recovery Time Objective | How quickly to recover |
| **RPO** | Recovery Point Objective | Acceptable data loss |

---

# Domain 4: Design Infrastructure Solutions (30-35%)

## 4.1 Design Compute Solutions

### Compute Selection Guide

| Requirement | Service |
|-------------|---------|
| Full OS control | Virtual Machines |
| Containerized workloads | AKS, Container Apps |
| Web applications | App Service |
| Event-driven, short-running | Azure Functions |
| Batch processing | Azure Batch |

### Virtual Machine Sizing

| Series | Use Case |
|--------|----------|
| B-series | Burstable, dev/test |
| D-series | General purpose |
| E-series | Memory optimized |
| F-series | Compute optimized |
| N-series | GPU workloads |

### Azure Kubernetes Service (AKS)

| Component | Purpose |
|-----------|---------|
| Node pools | Groups of VMs running workloads |
| Ingress controller | External traffic routing |
| Service mesh | Service-to-service communication |
| KEDA | Event-driven autoscaling |

### Azure App Service

| Plan Tier | Use Case |
|-----------|----------|
| Free/Shared | Development only |
| Basic | Low-traffic production |
| Standard | Production with autoscale |
| Premium | High-performance |
| Isolated | Enterprise, private networking |

---

## 4.2 Design Network Solutions

### Virtual Network Design

```
Hub VNet (10.0.0.0/16)
├── GatewaySubnet (10.0.0.0/27)
├── AzureFirewallSubnet (10.0.1.0/26)
├── ManagementSubnet (10.0.2.0/24)
└── SharedServicesSubnet (10.0.3.0/24)

Spoke VNet 1 (10.1.0.0/16)
├── WebTier (10.1.1.0/24)
├── AppTier (10.1.2.0/24)
└── DataTier (10.1.3.0/24)
```

### Network Connectivity

| Scenario | Solution |
|----------|----------|
| VNet to VNet (same region) | VNet Peering |
| VNet to VNet (cross-region) | Global VNet Peering |
| On-premises to Azure (low cost) | VPN Gateway |
| On-premises to Azure (high perf) | ExpressRoute |
| Multi-region connectivity | Virtual WAN |

### Network Security

| Service | Purpose |
|---------|---------|
| NSG | Subnet/NIC level filtering |
| Azure Firewall | Centralized network security |
| WAF | Web application protection |
| DDoS Protection | Volumetric attack protection |
| Private Link | Private connectivity to PaaS |

---

## 4.3 Design Application Architecture

### Microservices Patterns

| Pattern | Purpose |
|---------|---------|
| API Gateway | Single entry point |
| Service Discovery | Locate services dynamically |
| Circuit Breaker | Handle failures gracefully |
| Saga | Distributed transactions |
| CQRS | Separate read/write models |

### Messaging Solutions

| Service | Use Case |
|---------|----------|
| Service Bus | Enterprise messaging |
| Event Grid | Event routing |
| Event Hubs | High-throughput streaming |
| Queue Storage | Simple queuing |

### Caching Strategies

| Strategy | Use Case |
|----------|----------|
| Azure Cache for Redis | Session state, caching |
| Azure CDN | Static content delivery |
| Azure Front Door | Edge caching |

---

## 4.4 Design Migrations

### Migration Strategies (6 R's)

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| Rehost | Lift and shift | Quick migration |
| Replatform | Minor changes | Optimize for cloud |
| Refactor | Rearchitect | Maximize cloud benefits |
| Rebuild | Rewrite | Complete modernization |
| Replace | SaaS adoption | Standard capabilities |
| Retain | Keep on-premises | Not ready to migrate |

### Azure Migrate

| Tool | Purpose |
|------|---------|
| Discovery and assessment | Identify and assess workloads |
| Server Migration | Migrate VMs to Azure |
| Database Migration Service | Migrate databases |
| Web app migration assistant | Migrate web apps |

---

## ✅ Study Checklist

### Domain 1: Identity, Governance, Monitoring
- [ ] Understand Azure Monitor components
- [ ] Design Log Analytics workspace architecture
- [ ] Configure Application Insights
- [ ] Design Entra ID solutions
- [ ] Implement Conditional Access policies
- [ ] Configure Privileged Identity Management
- [ ] Design management group hierarchy
- [ ] Create Azure Policy initiatives

### Domain 2: Data Storage
- [ ] Select appropriate storage types
- [ ] Design storage redundancy
- [ ] Choose database solutions
- [ ] Design Cosmos DB consistency levels
- [ ] Plan data integration with Data Factory

### Domain 3: Business Continuity
- [ ] Design backup strategies
- [ ] Plan disaster recovery with ASR
- [ ] Design high availability architectures
- [ ] Calculate composite SLAs

### Domain 4: Infrastructure
- [ ] Select compute solutions
- [ ] Design AKS architectures
- [ ] Plan hub-spoke network topology
- [ ] Design hybrid connectivity
- [ ] Implement network security
- [ ] Plan migration strategies

---

*Last updated: November 2025*
