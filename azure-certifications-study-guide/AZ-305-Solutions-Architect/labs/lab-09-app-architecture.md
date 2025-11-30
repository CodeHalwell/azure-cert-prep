# Lab 09: Design Application Architecture

## 🎯 Lab Goal

Design **application architecture** patterns:

- Evaluate monolith vs. microservices
- Design messaging and event-driven patterns
- Plan API management strategy

This supports the **Design infrastructure solutions** domain of AZ‑305.

---

## ✅ Prerequisites

- Azure subscription
- Understanding of application architecture patterns

---

## Scenario

Contoso is modernizing their e-commerce platform:
- Decompose monolith into microservices
- Implement async communication between services
- Expose APIs to partners and mobile apps
- Handle 10,000 orders/hour at peak

---

## Step 1 – Evaluate Architecture Patterns

### Monolith vs. Microservices:

| Factor | Monolith | Microservices |
|--------|----------|---------------|
| Complexity | Low | High |
| Deployment | Single unit | Independent |
| Scaling | Scale entire app | Scale per service |
| Team structure | Single team | Service teams |
| Data management | Shared database | Database per service |

### Recommendation:

**Strangler Fig pattern** – Gradually extract microservices:

```
Phase 1: Extract Orders service
Phase 2: Extract Inventory service
Phase 3: Extract Notifications service
Phase 4: Decompose remaining monolith
```

---

## Step 2 – Design Microservices Communication

### Synchronous vs. Asynchronous:

| Pattern | Use Case | Azure Service |
|---------|----------|---------------|
| Sync (HTTP) | Real-time queries | API Management |
| Async (Queue) | Decoupled operations | Service Bus Queue |
| Pub/Sub | Fan-out events | Event Grid / Service Bus Topics |
| Streaming | High-volume data | Event Hubs |

### Service Communication Design:

```
Order Placed
    │
    ├── Event Grid ──→ Inventory Service (sync decrement)
    │
    ├── Service Bus Queue ──→ Payment Service (async)
    │
    └── Event Grid ──→ Notification Service (email/SMS)
```

---

## Step 3 – Design Messaging Architecture

### Service Bus Design:

```bash
az servicebus namespace create \
  --name sb-contoso \
  --resource-group rg-messaging \
  --sku Premium

az servicebus queue create \
  --name orders \
  --namespace-name sb-contoso \
  --resource-group rg-messaging \
  --max-delivery-count 10 \
  --lock-duration PT5M
```

### Dead Letter Handling:

```
Main Queue ──→ Consumer
    │
    └── (failures) ──→ Dead Letter Queue ──→ Alert + Manual Review
```

### Event Grid for Events:

```bash
az eventgrid topic create \
  --name eg-orders \
  --resource-group rg-messaging \
  --location eastus

az eventgrid event-subscription create \
  --name sub-inventory \
  --source-resource-id <topic-id> \
  --endpoint <function-url>
```

---

## Step 4 – Design API Management

### API Layers:

```
External Clients
       │
   API Management (policies, rate limiting)
       │
   ┌───┴───┬───────┬───────┐
   │       │       │       │
 Orders  Products Inventory Users
 (Container Apps / Functions)
```

### API Management Policies:

| Policy | Purpose |
|--------|--------|
| Rate limiting | Protect backends |
| JWT validation | Authentication |
| Caching | Reduce backend calls |
| Transformation | Request/response mapping |
| CORS | Cross-origin support |

---

## Step 5 – Design Document

```markdown
# Application Architecture – Contoso E-commerce

## 1. Service Decomposition
| Service | Responsibility | Technology |
|---------|----------------|------------|
| Orders | Order lifecycle | Container Apps |
| Inventory | Stock management | Container Apps |
| Products | Catalog | Functions |
| Payments | Payment processing | Container Apps |
| Notifications | Email/SMS | Functions |

## 2. Communication Patterns
- Sync: HTTPS between services (via APIM internally)
- Async: Service Bus for order processing
- Events: Event Grid for cross-service notifications

## 3. Data Strategy
- Database per service (Cosmos DB for Orders, SQL for Inventory)
- Event sourcing for audit trail
- Saga pattern for distributed transactions

## 4. API Strategy
- External: API Management with OAuth 2.0
- Internal: Dapr service invocation
- Partner: API subscriptions with rate limits

## 5. Resilience
- Circuit breaker (Polly/.NET)
- Retry with exponential backoff
- Bulkhead isolation
```

---

## ✅ Lab Checklist

- [ ] Evaluated monolith vs. microservices tradeoffs
- [ ] Designed service communication patterns
- [ ] Planned messaging architecture with Service Bus/Event Grid
- [ ] Created API management strategy
- [ ] Documented application architecture
