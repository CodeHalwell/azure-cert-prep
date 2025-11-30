# 📖 DP-700 Study Guide

## Microsoft Fabric Data Engineer Associate

This study guide covers all skills measured in the DP-700 exam.

---

# Domain 1: Implement and Manage Analytics Solution (25-30%)

## 1.1 Microsoft Fabric Architecture

### OneLake Concept

```
┌─────────────────────────────────────────────────────────────┐
│                         OneLake                              │
│              (Single unified data lake)                      │
├─────────────────────────────────────────────────────────────┤
│  ┌───────────┐  ┌───────────┐  ┌───────────┐               │
│  │ Lakehouse │  │ Warehouse │  │  KQL DB   │               │
│  │   (Delta) │  │   (SQL)   │  │  (Kusto)  │               │
│  └───────────┘  └───────────┘  └───────────┘               │
│                                                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              Shortcuts (References)                    │  │
│  │  Azure Storage | ADLS Gen2 | S3 | Other Lakehouses    │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Workspace Configuration

| Element | Purpose |
|---------|---------|
| **Capacity** | Compute resources for workspaces |
| **Workspace** | Container for Fabric items |
| **Domain** | Logical grouping of workspaces |
| **Lakehouse** | Delta-based data storage |

---

## 1.2 Lakehouse Architecture

### Medallion Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Medallion Architecture                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────┐      ┌─────────┐      ┌─────────┐             │
│  │ Bronze  │ ───► │ Silver  │ ───► │  Gold   │             │
│  │  (Raw)  │      │(Cleansed│      │(Business│             │
│  │         │      │ Conformed)     │ Ready)  │             │
│  └─────────┘      └─────────┘      └─────────┘             │
│                                                              │
│  Landing zone     Validated,       Aggregated,              │
│  Raw data         deduplicated     modeled                  │
│  All formats      Delta tables     Star schema              │
└─────────────────────────────────────────────────────────────┘
```

### Delta Lake Features

| Feature | Description |
|---------|-------------|
| **ACID transactions** | Reliable data operations |
| **Time travel** | Query historical data versions |
| **Schema enforcement** | Prevent bad data |
| **Z-Ordering** | Optimize file layout |
| **V-Order** | Fabric-specific optimization |

---

## 1.3 Security

### Workspace Roles

| Role | Permissions |
|------|-------------|
| **Admin** | Full control, manage access |
| **Member** | Create, edit, delete items |
| **Contributor** | Create and edit items |
| **Viewer** | View items only |

### Item-Level Permissions

| Permission | Scope |
|------------|-------|
| Read | View data and metadata |
| Write | Modify data |
| Reshare | Grant access to others |
| All | Full control |

### Row-Level Security (RLS)

```sql
-- Create security role
CREATE ROLE SalesRegion

-- Define filter
CREATE SECURITY POLICY RegionFilter
ADD FILTER PREDICATE dbo.fn_securitypredicate(Region)
ON dbo.Sales
```

---

# Domain 2: Ingest and Transform Data (30-35%)

## 2.1 Data Pipelines

### Copy Activity

| Source | Supported |
|--------|-----------|
| Azure Blob Storage | ✓ |
| Azure Data Lake | ✓ |
| SQL Database | ✓ |
| REST APIs | ✓ |
| Files (CSV, JSON, Parquet) | ✓ |

### Pipeline Patterns

```
┌─────────────────────────────────────────────────────────────┐
│                   Orchestration Pipeline                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────┐    ┌────────┐    ┌────────┐    ┌────────┐      │
│  │ Copy   │───►│Notebook│───►│ Copy   │───►│Semantic│      │
│  │Activity│    │Activity│    │Activity│    │ Model  │      │
│  └────────┘    └────────┘    └────────┘    │Refresh │      │
│                                             └────────┘      │
│                                                              │
│  Parameters: @pipeline().parameters.sourceDate              │
│  Variables: @variables('processedCount')                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 2.2 Notebooks (Spark)

### PySpark Transformations

```python
# Read Delta table
df = spark.read.format("delta").load("Tables/bronze_sales")

# Transformations
df_cleaned = (df
    .filter(col("amount") > 0)
    .dropDuplicates(["transaction_id"])
    .withColumn("processed_date", current_date())
)

# Write to Silver layer
df_cleaned.write.format("delta").mode("overwrite").save("Tables/silver_sales")
```

### Common Operations

| Operation | Method |
|-----------|--------|
| Filter rows | `.filter()`, `.where()` |
| Select columns | `.select()` |
| Add columns | `.withColumn()` |
| Rename columns | `.withColumnRenamed()` |
| Group and aggregate | `.groupBy().agg()` |
| Join tables | `.join()` |
| Remove duplicates | `.dropDuplicates()` |

---

## 2.3 Dataflows Gen2

### Power Query Features

| Feature | Use Case |
|---------|----------|
| **Merge queries** | Join data sources |
| **Append queries** | Union data sources |
| **Pivot/Unpivot** | Reshape data |
| **Group by** | Aggregate data |
| **Custom columns** | Calculated fields |

### Incremental Refresh

| Element | Purpose |
|---------|---------|
| RangeStart | Filter start date |
| RangeEnd | Filter end date |
| Detect changes | Only process new data |

---

# Domain 3: Monitor and Optimize (20-25%)

## 3.1 Performance Optimization

### Storage Optimization

| Technique | Benefit |
|-----------|---------|
| **V-Order** | Optimized for Fabric queries |
| **Z-Ordering** | Clustered file layout |
| **Partitioning** | Reduce data scanned |
| **Compaction** | Combine small files |

### Optimize Commands

```sql
-- Optimize table with V-Order
OPTIMIZE sales_table VORDER

-- Z-Order by column
OPTIMIZE sales_table ZORDER BY (region, date)

-- Compact small files
OPTIMIZE sales_table WHERE date > '2025-01-01'

-- Clean up old files
VACUUM sales_table RETAIN 168 HOURS
```

---

## 3.2 Monitoring

### Capacity Metrics

| Metric | Description |
|--------|-------------|
| CU utilization | Compute unit usage |
| Throttling | Operations delayed |
| Memory usage | Active memory consumption |
| Queued operations | Waiting operations |

### Spark Monitoring

| View | Information |
|------|-------------|
| Job history | Completed and running jobs |
| Stage details | Task distribution |
| Metrics | Duration, data processed |
| Logs | Error messages, warnings |

---

# Domain 4: Semantic Models (15-20%)

## 4.1 Data Modeling

### Star Schema

```
          ┌─────────────┐
          │ DimCustomer │
          └──────┬──────┘
                 │
┌─────────┐     │     ┌─────────┐
│ DimDate │────►│◄────│DimProduct│
└─────────┘     │     └─────────┘
                │
          ┌─────▼─────┐
          │FactSales  │
          └───────────┘
```

### Relationship Types

| Type | Cardinality |
|------|-------------|
| One-to-Many | Most common (Dim→Fact) |
| Many-to-Many | Bridge tables |
| One-to-One | Rare, use carefully |

---

## 4.2 DAX Basics

### Common Measures

```dax
// Total Sales
Total Sales = SUM(FactSales[Amount])

// Year-to-Date
YTD Sales = TOTALYTD(SUM(FactSales[Amount]), DimDate[Date])

// Same Period Last Year
SPLY = CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(DimDate[Date])
)

// Growth %
Growth % = DIVIDE([Total Sales] - [SPLY], [SPLY])
```

---

## ✅ Study Checklist

### Domain 1: Analytics Solution
- [ ] Configure workspaces and capacities
- [ ] Create and manage Lakehouses
- [ ] Implement medallion architecture
- [ ] Configure security and RLS

### Domain 2: Ingest & Transform
- [ ] Build data pipelines
- [ ] Write Spark transformations
- [ ] Create Dataflows Gen2
- [ ] Implement incremental refresh

### Domain 3: Monitor & Optimize
- [ ] Monitor capacity metrics
- [ ] Optimize Delta tables
- [ ] Troubleshoot Spark jobs

### Domain 4: Semantic Models
- [ ] Design star schema
- [ ] Create relationships
- [ ] Write DAX measures

---

*Last updated: November 2025*
