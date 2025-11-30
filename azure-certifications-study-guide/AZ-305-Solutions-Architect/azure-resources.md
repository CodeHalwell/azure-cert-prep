# 🔧 AZ-305 Azure Resources Reference

Comprehensive reference for Azure services and building blocks used in AZ-305 solution designs: what they do, built-in capabilities, limits, and when customization is required.

---

## 📋 Table of Contents

1. Identity, Security & Governance
   - Microsoft Entra ID
   - RBAC, Management Groups, Policy, Blueprints/Bicep
   - Key Vault
2. Networking & Connectivity
   - Virtual Networks, Subnets, Peering
   - Private Link, VPN, ExpressRoute, DNS
   - Application Gateway, Front Door, Azure Firewall, WAF, DDoS
3. Compute & Container Platforms
   - Virtual Machines & Scale Sets
   - App Service
   - Azure Kubernetes Service (AKS)
   - Azure Functions & Event-based compute
4. Data & Storage
   - Storage Accounts (Blob, Files, Tables, Queues)
   - SQL Database / SQL Managed Instance
   - Cosmos DB
   - Caching (Azure Cache for Redis)
5. Integration & Messaging
   - Service Bus
   - Event Grid
   - Event Hubs
6. Monitoring, Resilience & Cost
   - Azure Monitor & Log Analytics
   - Backup & Site Recovery
   - Availability Zones & Sets
   - Cost Management + Advisor

---

# 1. Identity, Security & Governance

## 1.1 Microsoft Entra ID

High-level behavior is as described in AZ-104, but AZ-305 focuses on design tradeoffs.

### What You Can Do

- Implement **single sign-on** across SaaS and custom apps
- Design **tenant and directory structure** (single vs multi-tenant)
- Choose between **cloud-only**, **hybrid (AD Connect)**, or **B2B/B2C** scenarios
- Enforce **Conditional Access** and **Zero Trust** principles

### Built-in Capabilities

- Multi-tenant cloud directory, basic user/group management
- SSO to thousands of SaaS apps
- Conditional Access, MFA, passwordless
- Device registration / join, basic security defaults

### Requires Customization / Design

- Tenant topology (single vs multiple tenants, B2B trust)
- Identity lifecycle (HR-driven provisioning, Just-in-Time access)
- Hybrid identity architecture (AD Connect, Cloud Sync, PTA vs PHS)
- Delegated admin and least-privilege using custom roles and PIM

### Key Constraints & Limits (Design Impact)

- Directory and subscription limits (objects, role assignments)
- Cross-tenant collaboration restrictions & access reviews

---

## 1.2 Management Groups, RBAC, Policy, Infrastructure as Code

### Management Groups

**Purpose:** Hierarchical governance above subscriptions.

- Apply policies and RBAC across **all child subscriptions**
- Segment environments: `Root → Corp → Prod / NonProd → Department`
- Built-in, no extra cost

### Azure Policy

**What It Does:** Enforce or audit configuration at scale.

- **Built-in:** Many policy definitions (e.g., require tags, allowed locations)
- **Custom:** JSON-based policies for org-specific rules
- **Effects:** `Deny`, `Audit`, `Append`, `DeployIfNotExists`

**Limitations & Design Considerations**
- Complex nested policies can affect deployment performance
- Must plan for **exemptions** to avoid blocking essential operations

### RBAC

- Same core as AZ-104 but AZ-305 emphasizes **least privilege architecture**
- Use **management group/subscription/RG** scopes to align with organizational model

### Infrastructure as Code (Bicep/ARM/Terraform)

- **Built-in:** Native Bicep/ARM support in Azure
- Use for **repeatable, versioned deployments**, multi-region patterns
- Customization is effectively **mandatory** for production-grade designs

---

## 1.3 Key Vault

### What You Can Do

- Store **secrets**, **keys**, and **certificates** securely
- Use **Managed Identity** for apps to access secrets without embedded credentials
- Use **Key Vault-backed encryption** (Database TDE, Disk, Storage, App Config)

### Built-in Capabilities

- Soft-delete and purge protection (recommended for production)
- Integration with many PaaS services
- RBAC or access policies for control

### Requires Customization

- Network isolation: private endpoints, firewall rules
- Key rotation policies (automatic vs manual)
- Multi-region strategy (per-region vaults vs cross-region)

### Limitations

- Request rate limits (per vault, per region)
- Per-vault object limits (secrets/keys/certs)

---

# 2. Networking & Connectivity

## 2.1 Virtual Network, Subnets, Peering

### What You Can Do

- Design **hub-and-spoke** or **mesh** topologies
- Segment workloads via subnets and NSGs
- Use **VNet peering** (intra-/cross-region) to connect VNets

### Built-in Capabilities

- Private IP address space (RFC1918)
- System routing, DNS, basic DDoS protection
- VNet peering with **low latency** and **no bandwidth cap** (within limits)

### Requires Customization

- Detailed CIDR planning to avoid address conflicts
- Route tables and UDRs for custom traffic paths
- DNS architecture (Azure DNS Private Zones vs custom DNS)

### Limitations

- Max VNets, subnets, peerings per VNet
- UDR limits per route table

---

## 2.2 Private Link & Service Endpoints

### Private Link

**What It Does:** Private access to PaaS services over private IP in your VNet.

- **Built-in:** Private endpoint support for Storage, SQL, Key Vault, Web Apps, etc.
- **Security:** Traffic stays on Microsoft backbone; can disable public access

**Customization / Design Choices**
- How many private endpoints vs using **Private Link service** for your own apps
- DNS configuration (Private DNS Zones required for many services)

### Service Endpoints

**What It Does:** Secures traffic to PaaS over optimized route, but still uses public IPs.

- Easier to configure, but less strict than Private Link

---

## 2.3 Application Gateway, Front Door, Azure Firewall, WAF, DDoS

### Application Gateway

- **Layer 7 load balancer** with path-based routing and SSL offload
- **Built-in:** WAF option, autoscaling in v2 SKUs
- Use when you need:
  - App-aware routing (URL-based)
  - Per-application WAF rules

### Azure Front Door

- **Global entry point (anycast)** with CDN-like capabilities
- Intelligent routing, SSL offload, WAF
- Use when:
  - Global scale / latency optimization is required
  - You need multi-region active-active front-ends

### Azure Firewall

- **Stateful L3/L4 firewall** with central management, FQDN filtering, threat intelligence
- Use for **central hub** firewalling in hub-and-spoke

### DDoS Protection

- **Built-in:** Basic on all endpoints
- **Standard (paid):** When app is internet-facing and critical, provides advanced telemetry and protection with cost coverage

### Design Tradeoffs

| Scenario | Service Choice |
|----------|----------------|
| Single-region web app with WAF | App Gateway WAF |
| Global multi-region web app | Front Door + App Gateway |
| Centralized traffic inspection | Azure Firewall in hub |

---

## 2.4 VPN & ExpressRoute

### VPN Gateway

- IPSec tunnels over internet
- **Use for:** Smaller or cost-sensitive hybrid setups, branch offices

### ExpressRoute

- Private, dedicated connectivity
- **Use for:** High throughput, low latency, strict data sovereignty/compliance

### Limitations & Design Points

- VPN throughput caps by SKU; consider **active-active** for HA
- ExpressRoute has **peering types** (private, Microsoft, M365)

---

# 3. Compute & Container Platforms

## 3.1 Virtual Machines & Scale Sets

Summary behavior similar to AZ-104, but AZ-305 focuses on **when to choose VMs**:

- Required when:
  - Legacy workloads, custom OS
  - Special hardware requirements
  - Full control of OS/networking

- Design considerations:
  - **Availability sets** vs **Availability Zones**
  - Backup & DR strategy
  - Image management (shared image gallery)

---

## 3.2 App Service

### What You Can Do

- Host **web apps, APIs, and background jobs** without managing OS

### Built-in

- Auto-scale
- Deployment slots
- Managed platform patching
- Integration with Entra ID and Key Vault

### Requires Customization

- VNet integration / private endpoints for backend dependencies
- Custom health checks and deployment strategies (blue-green/canary)

### Limitations

- Limited access to underlying OS and networking stack
- Some networking features require **Premium** or higher tiers

---

## 3.3 Azure Kubernetes Service (AKS)

### What You Can Do

- Run containerized microservices
- Control deployment, scaling, networking at cluster and pod level

### Built-in

- Managed control plane (no cost)
- Integration with Azure CNI/Calico, Managed Identity, Azure Monitor
- Basic upgrades, node pools

### Requires Customization

- Ingress controller (App Gateway Ingress Controller, Nginx, etc.)
- CI/CD pipelines, GitOps
- Pod security policies, network policies
- Observability toolchain (Prometheus/Grafana/OpenTelemetry)

### Limitations

- Node pool and node count limits
- Complexity overhead vs App Service / Functions

---

## 3.4 Azure Functions & Event-based Compute

### What You Can Do

- Build serverless APIs and background processing
- Trigger from HTTP, timers, queues, Event Grid, Event Hubs, etc.

### Built-in

- Auto-scaling (Consumption/Premium)
- Bindings for many services
- Integrated logging via Application Insights

### Requires Customization

- Cold start mitigation (Premium plan, pre-warmed instances)
- VNet integration and private endpoints
- Durable Functions for orchestrations

---

# 4. Data & Storage

## 4.1 Storage Accounts (Blob, Files, Tables, Queues)

Full technical breakdown is in AZ-104; for AZ-305 focus on **design decisions**:

- **Blob:** Object storage for unstructured data, data lakes (with hierarchical namespace)
- **Files:** Lift-and-shift file shares (SMB/NFS)
- **Tables:** Simple NoSQL key-value data
- **Queues:** Simple message queues for decoupling components

### Key Design Points

- Replication (LRS/ZRS/GRS/GZRS) aligned to **RPO/RTO** and compliance
- Access tiers (Hot/Cool/Cold/Archive) based on usage patterns
- Security (Private Link, firewall, encryption with customer-managed keys)

---

## 4.2 Azure SQL Database & SQL Managed Instance

### What They Do

| Service | Description | Typical Use |
|---------|-------------|-------------|
| SQL Database | PaaS single DB / pools | Modern apps |
| SQL Managed Instance | Near full SQL Server compatibility | Lift and shift |

### Built-in

- Automated backups & point-in-time restore
- High availability (zone redundant options)
- Security (TDE, auditing, threat detection)

### Requires Customization

- Network isolation (VNet integration / private endpoints)
- Geo-replication and DR strategy
- Elastic pools for many small databases

---

## 4.3 Cosmos DB

### What It Does

- Globally distributed, multi-model NoSQL database
- APIs: Core (SQL), Mongo, Cassandra, Gremlin, Table

### Built-in

- Multi-region writes/reads
- 99.999% availability with SLAs for latency, throughput, consistency

### Design Choices

- Consistency levels (Strong, Bounded Staleness, Session, Consistent Prefix, Eventual)
- Partitioning strategy (logical partition keys)
- Provisioned vs serverless vs autoscale throughput

---

## 4.4 Azure Cache for Redis

### What It Does

- In-memory cache for performance and scalability

### Built-in

- Multi-tenant managed Redis
- Clustering and persistence options (tier-dependent)

### Requires Customization

- Cache key design and eviction strategy
- HA and geo-replication configuration

---

# 5. Integration & Messaging

## 5.1 Service Bus

- Enterprise-grade messaging (queues & topics)
- Ordered delivery, sessions, dead-lettering, transactions

### Use Cases

- Decouple microservices
- Integration between on-prem and cloud

---

## 5.2 Event Grid

- Event routing service based on **pub/sub**
- React to events from Azure services or custom sources

### Use Cases

- Serverless event-driven architectures
- Storage events (blob created/deleted), subscription events

---

## 5.3 Event Hubs

- Big data streaming platform
- High-throughput event ingestion (telemetry, logs)

### Use Cases

- Ingest events for analytics (Stream Analytics, Fabric, Databricks)

---

# 6. Monitoring, Resilience & Cost

## 6.1 Azure Monitor & Log Analytics

- Central logging and metric platform
- Use **Application Insights** for application-level telemetry

## 6.2 Availability & DR

- Zones vs Availability Sets vs Multi-region
- Backup (Azure Backup) vs replication (GRS/GZRS) vs geo-replication

## 6.3 Cost Management & Advisor

- Built-in **Cost Management** for budgets and alerts
- Azure Advisor for cost, performance, security, and reliability recommendations

---

*Last updated: November 2025*