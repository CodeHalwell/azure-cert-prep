# 🔧 AZ-204 Azure Resources Reference

Developer-centric reference for all key Azure services in AZ-204: what they do, built-in features, limits, and when you must customize.

---

## 📋 Table of Contents

1. Compute Platforms
   - App Service
   - Azure Functions
   - Azure Container Apps & AKS (developer view)
2. Data & Storage
   - Storage Accounts (Blob, Queue, Table)
   - Cosmos DB
   - Azure SQL Database
3. Messaging & Eventing
   - Service Bus
   - Event Grid
   - Event Hubs
4. Identity & Security
   - Microsoft Entra ID (App registrations)
   - Managed Identities
   - Key Vault
5. Monitoring & Configuration
   - Application Insights
   - Azure Monitor
   - App Configuration & Feature Flags

---

# 1. Compute Platforms

## 1.1 Azure App Service (Web Apps / API Apps)

### What You Can Do

- Host **.NET, Node.js, Python, Java, PHP** web apps and APIs
- Use deployment slots for **blue-green** rollouts
- Configure CI/CD from GitHub, Azure DevOps, etc.

### Built-in Features

| Feature | Included | Notes |
|---------|----------|-------|
| Managed runtime & OS | ✅ | No server management |
| Auto-scale | ✅ | Based on metrics/schedule |
| Authentication/Authorization | ✅ | Easy Entra ID integration |
| Deployment slots | ✅ (Standard+) | Swap with warm-up |
| Custom domains & SSL | ✅ | Free managed certs |
| Logging & diagnostics | ✅ | Integrated with Azure Monitor |

### Requires Customization

- VNet integration / private endpoints to reach backends
- Health check endpoints and custom probes
- Scaling rules (CPU, memory, queue length)
- Startup scripts, containerization for non-standard stacks

### Key Limits

- Max size of deployment package (2 GB via ZIP)
- # of apps per plan limited by compute capacity
- Scale out limits by SKU (e.g., up to 30 instances in Premium)

---

## 1.2 Azure Functions

### What You Can Do

- Build **serverless APIs** and background jobs
- Trigger from HTTP, timers, queues, Service Bus, Event Grid, Event Hubs, Cosmos DB, etc.

### Hosting Plans

| Plan | Billing | Scale | Use Case |
|------|---------|-------|----------|
| Consumption | Per execution | Auto, event-driven | Spiky workloads |
| Premium | Pre-warmed cores | Predictable | VNet, long-running |
| Dedicated | App Service plan | Manual/auto | Always-on APIs |

### Built-in Features

- Rich trigger and binding model
- Integrated logging with Application Insights
- Managed identity support
- Durable Functions for orchestrations and stateful workflows

### Requires Customization

- **Cold start mitigation**: Premium plan or warm-up strategies
- **Binding configuration** in `function.json` or attributes
- Custom retry policies for triggers (Service Bus, Event Grid, etc.)
- VNet and private endpoint integration for secure backends

### Limits

- Max execution time (Consumption: 5–10 minutes default; extendable via host.json but bounded)
- Size of payload for some triggers (e.g., HTTP, Queues)

---

## 1.3 Containers (Container Apps & AKS)

For AZ-204 you mostly need **developer-level understanding**.

### Azure Container Apps

- Serverless containers, autoscale based on KEDA metrics (HTTP, queue length, custom)
- Built-in Dapr integration for microservices patterns
- Good for APIs, background workers, event-driven workloads

### AKS (Developer View)

- Kubernetes cluster for containerized workloads
- You focus on **Dockerfiles, manifests/Helm, and app code**
- Platform team typically manages cluster-level concerns

---

# 2. Data & Storage

## 2.1 Azure Storage (Blob, Queue, Table)

### Blob Storage

- **What:** Object storage for files, images, documents, static assets
- **Built-in:**
  - Multi-tier (Hot/Cool/Cold/Archive)
  - Versioning, soft delete
  - Static website hosting

**Developer Considerations**
- Choose correct **access tier** and **content type**
- Use **SAS tokens** or **managed identity** for secure access
- Use **client-side retry policies** for transient failures

### Queue Storage

- Simple message queue for decoupling
- Max message size: 64 KB (base) / up to 256 KB (with base64)
- At-least-once delivery; you must handle duplicates and poison messages

### Table Storage

- Key-value NoSQL store
- PartitionKey/RowKey determine performance and scalability

---

## 2.2 Cosmos DB

### What You Can Do

- Globally distributed NoSQL database with multiple APIs

### Built-in Features

| Feature | Notes |
|---------|-------|
| Multi-region replication | Automatic failover |
| Five consistency levels | Tunable per request |
| Autoscale throughput | PAYG scaling |
| SLAs | For latency, availability, throughput, consistency |

### Requires Customization

- Partition key design based on access patterns
- Throughput model (provisioned/auto/serverless)
- Index policy customization to optimize costs

### Limits

- 20 GB logical partition limit
- RU/s and storage quotas per container/account

---

## 2.3 Azure SQL Database

### What You Can Do

- Managed relational database for transactional workloads

### Built-in

- Automatic backups & PITR
- TDE encryption, auditing
- Basic performance tuning (Query Store, auto-tuning)

### Requires Customization

- Connection resiliency & retry logic
- Elastic pools for multi-tenant SaaS
- Geo-replication for DR

---

# 3. Messaging & Eventing

## 3.1 Service Bus

### What You Can Do

- Reliable enterprise messaging using **queues** and **topics/subscriptions**

### Built-in Features

- Dead-letter queues, sessions, duplicate detection, transactions

### Requires Customization

- Queue/topic hierarchy and naming
- Auto-complete vs manual-complete semantics in SDK
- Retry and backoff strategies

---

## 3.2 Event Grid

### What You Can Do

- Lightweight **pub/sub event routing** service

### Built-in Sources & Handlers

- Storage, Resource Groups, Event Hubs, custom topics
- Handlers: Functions, Logic Apps, WebHooks, Queues, etc.

### Design Points

- Event schema (CloudEvents vs Event Grid schema)
- Filtering by subject and event type
- Dead-letter configuration

---

## 3.3 Event Hubs

- High-throughput event ingestion
- Partitioned consumer model
- Integrates with Stream Analytics, Fabric, Databricks

---

# 4. Identity & Security

## 4.1 Microsoft Entra ID App Registrations

### What You Can Do

- Register applications for OAuth 2.0 / OpenID Connect
- Define **API permissions** (Microsoft Graph, custom APIs)
- Configure **redirect URIs**, **certificates/secrets**

### Built-in

- Token issuance (ID, access, refresh)
- App roles and scopes

### Requires Customization

- Multi-tenant vs single-tenant app design
- Permission grant model (delegated vs application permissions)
- Token lifetime & claims via **token configuration**

---

## 4.2 Managed Identities

### System-assigned

- Tied to a single resource (App Service, Functions, VM, etc.)
- Lifecycle bound to the resource

### User-assigned

- Standalone identity that can be attached to multiple resources

### Use Cases

- Access Key Vault, Storage, SQL, Service Bus without secrets

---

## 4.3 Key Vault

- As in AZ-104/AZ-305, but focus on **developer usage** via SDKs
- Secret retrieval using managed identity
- Client-side encryption scenarios

---

# 5. Monitoring & Configuration

## 5.1 Application Insights

### What You Can Do

- Collect application-level telemetry: requests, dependencies, exceptions, traces, metrics

### Built-in

- Automatic instrumentation for many runtimes
- Live Metrics, Application Map, Failures, Performance views

### Requires Customization

- Custom events and metrics
- Sampling configuration to control costs
- Distributed tracing across services

---

## 5.2 Azure Monitor & Log Analytics

- Platform logs and metrics for your resources
- KQL queries for advanced diagnostics

---

## 5.3 App Configuration & Feature Flags

- Central config store for key-values
- First-class feature flag support
- Designed for **12-factor** application practices

---

*Last updated: November 2025*