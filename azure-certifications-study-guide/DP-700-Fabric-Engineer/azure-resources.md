# 🔧 DP-700 Fabric Resources Reference

Resource-focused view of Microsoft Fabric and related services for DP-700.

---

## 📋 Table of Contents

1. Fabric Workspaces & Capacities
2. Lakehouses, Warehouses, and OneLake
3. Data Engineering
   - Dataflows Gen2
   - Data Pipelines
   - Notebooks & Spark
4. Semantic Models & BI
   - Semantic models
   - Power BI items in Fabric
5. Security & Governance
   - Workspaces roles
   - Row-level security (RLS)
   - Sensitivity labels

---

# 1. Fabric Workspaces & Capacities

## 1.1 Workspaces

- Logical containers for Fabric items (lakehouses, warehouses, reports, etc.)

### Built-in

- Role-based permissions (Viewer, Contributor, Member, Admin)
- Integration with OneLake and capacities

### Requires Customization

- Workspace-per-domain vs per-project vs per-environment strategy
- Separation between **development**, **test**, and **production** workspaces

---

## 1.2 Capacities

- Fabric capacity SKUs (F, P, etc.) govern performance & concurrency

### Built-in

- Automatic resource management within capacity

### Requires Customization

- Capacity sizing, scaling, and assignment to workspaces
- Multi-tenant designs and chargeback models

---

# 2. Lakehouses, Warehouses, OneLake

## 2.1 Lakehouse

- Delta table–based storage on OneLake
- Combines capabilities of data lake + warehouse-style queries

### Built-in

- Tables, shortcuts, files area
- SQL and Spark access

### Requires Customization

- Table partitioning and folder structure
- Medallion architecture (bronze/silver/gold) implementation

---

## 2.2 Warehouse

- SQL-first experience in Fabric

### Built-in

- T-SQL endpoint
- Integration with Power BI semantic models

### Requires Customization

- Schema design, indexing, and partitioning

---

## 2.3 OneLake

- Single logical data lake for Fabric
- Shortcuts to external storage (ADLS, S3)

### Built-in

- Unified security and governance

### Requires Customization

- Shortcut strategy (local vs external data)

---

# 3. Data Engineering

## 3.1 Dataflows Gen2

- Low-code ETL using Power Query

### Built-in

- Connectors to many sources
- Incremental refresh support

### Requires Customization

- Dataflow layering (staging vs curated)

---

## 3.2 Data Pipelines

- Orchestration akin to Azure Data Factory

### Built-in

- Activities for copy, notebooks, stored procedures, etc.
- Triggers (schedule, event-based)

### Requires Customization

- Pipeline orchestration patterns
- Error handling/retry logic

---

## 3.3 Notebooks & Spark

- Collaborative notebooks with Spark clusters

### Built-in

- Auto-scaling compute (within capacity)
- Support for Python, SQL, Scala

### Requires Customization

- Environment and library management
- Job scheduling patterns

---

# 4. Semantic Models & BI

## 4.1 Semantic Models

- Tabular models used by Power BI and Fabric

### Built-in

- Direct Lake, Import, and DirectQuery modes

### Requires Customization

- Star schema modeling
- Aggregation tables

---

# 5. Security & Governance

## 5.1 Workspace Roles

- Viewer, Contributor, Member, Admin with specific privileges

## 5.2 RLS & Sensitivity Labels

- Row-level security on semantic models
- Sensitivity labels flow into Office apps

---

*Last updated: November 2025*