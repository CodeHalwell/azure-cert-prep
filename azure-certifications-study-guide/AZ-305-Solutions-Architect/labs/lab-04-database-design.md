# Lab 04: Design Database Architecture

## 🎯 Lab Goal

Design a **database architecture** for enterprise workloads:

- Select appropriate database services
- Design for scalability and high availability
- Plan data consistency and partitioning

This supports the **Design data storage solutions** domain of AZ‑305.

---

## ✅ Prerequisites

- Azure subscription
- Understanding of relational and NoSQL databases

---

## Scenario

Contoso needs databases for:
- E-commerce orders (transactional, relational) – 5M transactions/day
- Product catalog (semi-structured, global read) – 1M products
- Session state (key-value, low latency) – 10K concurrent users
- Reporting (analytics, complex queries)

---

## Step 1 – Select Database Services

| Requirement | Service | Justification |
|-------------|---------|---------------|
| Orders | Azure SQL Database | ACID, complex queries |
| Product catalog | Cosmos DB | Global distribution, flexible schema |
| Session state | Azure Cache for Redis | Sub-millisecond latency |
| Reporting | Azure Synapse Analytics | Large-scale analytics |

---

## Step 2 – Design SQL Database Architecture

### Tier Selection:

| Tier | Use Case |
|------|----------|
| Basic/Standard | Dev/Test |
| Premium | High IOPS, in-memory OLTP |
| Hyperscale | Large databases, fast scaling |
| Business Critical | Low latency, built-in HA |

### High Availability:

```
Production: Business Critical
├── Primary replica (read-write)
├── Secondary replica (read-only)
└── Secondary replica (read-only)
```

### Geo-replication:

```bash
az sql db replica create \
  --name orders-db \
  --resource-group rg-primary \
  --server sql-contoso-primary \
  --partner-server sql-contoso-secondary \
  --partner-resource-group rg-secondary
```

---

## Step 3 – Design Cosmos DB Architecture

### Consistency Levels:

| Level | Use Case |
|-------|----------|
| Strong | Financial transactions |
| Bounded Staleness | Leaderboards with lag tolerance |
| Session | User-specific consistency |
| Eventual | Highest throughput, product views |

### Partition Strategy for Product Catalog:

```
Partition Key: /categoryId
- Electronics: categoryId = "electronics"
- Clothing: categoryId = "clothing"
```

> Choose partition key with high cardinality and even distribution.

### Multi-region Write:

```bash
az cosmosdb update \
  --name cosmos-contoso \
  --resource-group rg-data \
  --enable-multiple-write-locations true
```

---

## Step 4 – Design Caching Strategy

### Redis Cache Tiers:

| Tier | Features |
|------|----------|
| Basic | No SLA, dev only |
| Standard | Replicated, SLA |
| Premium | Clustering, geo-replication |
| Enterprise | Redis modules, active geo-replication |

### Caching Patterns:

- **Cache-aside**: Application manages cache
- **Write-through**: Updates cache and database
- **Write-behind**: Updates cache, async database write

---

## Step 5 – Design Document

```markdown
# Database Architecture – Contoso Ltd.

## 1. Service Selection
| Workload | Service | Tier |
|----------|---------|------|
| Orders | Azure SQL | Business Critical |
| Products | Cosmos DB | Autoscale |
| Sessions | Redis | Premium P1 |
| Analytics | Synapse | Dedicated SQL Pool |

## 2. High Availability
- SQL: Auto-failover groups (RPO < 5s, RTO < 30s)
- Cosmos DB: Multi-region with automatic failover
- Redis: Zone redundancy

## 3. Security
- Private endpoints for all databases
- TDE enabled for SQL
- Customer-managed keys
- Entra ID authentication

## 4. Scaling Strategy
- SQL: Elastic pools for multi-tenant
- Cosmos DB: Autoscale RU/s
- Synapse: Pause when not in use
```

---

## ✅ Lab Checklist

- [ ] Selected appropriate database service for each workload
- [ ] Designed SQL Database high availability with geo-replication
- [ ] Planned Cosmos DB partition strategy and consistency level
- [ ] Designed caching layer with appropriate patterns
- [ ] Documented database architecture
