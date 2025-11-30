# Lab 06: Optimize Delta Tables in OneLake

## 🎯 Lab Goal

Optimize **Delta tables** for performance:

- Apply OPTIMIZE and VACUUM commands
- Configure partitioning and Z-ordering
- Monitor table health

This supports the **Optimize and maintain data** domain of DP‑700.

---

## ✅ Prerequisites

- Fabric lakehouse with Delta tables
- Tables with significant data volume

---

## Step 1 – Understand Delta Table Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| Small files | Many small writes | OPTIMIZE |
| Old versions | Frequent updates | VACUUM |
| Slow queries | No partitioning | Partition/Z-order |
| Large scans | Poor predicates | Z-order |

---

## Step 2 – Analyze Table Health

```python
# View table details
spark.sql("DESCRIBE DETAIL sales").show(truncate=False)

# View file statistics
spark.sql("DESCRIBE EXTENDED sales").show(truncate=False)

# Count files
from delta.tables import DeltaTable

dt = DeltaTable.forName(spark, "sales")
print(f"Files: {dt.toDF().rdd.getNumPartitions()}")

# View history
spark.sql("DESCRIBE HISTORY sales").show(truncate=False)
```

---

## Step 3 – Optimize Small Files

```python
# Basic optimize (compact files)
spark.sql("OPTIMIZE sales")

# Optimize with Z-ordering on frequently filtered columns
spark.sql("OPTIMIZE sales ZORDER BY (CustomerID, OrderDate)")

# Optimize specific partitions
spark.sql("OPTIMIZE sales WHERE OrderYear = 2024")
```

### When to Optimize:

- After large batch ingestions
- When query performance degrades
- Regularly scheduled (e.g., nightly)

---

## Step 4 – Vacuum Old Versions

```python
# Check current retention
print(spark.conf.get("spark.databricks.delta.retentionDurationCheck.enabled"))

# Vacuum files older than 7 days (default)
spark.sql("VACUUM sales")

# Vacuum with custom retention (minimum 7 days recommended)
spark.sql("VACUUM sales RETAIN 168 HOURS")  # 7 days

# Dry run to see what would be deleted
spark.sql("VACUUM sales DRY RUN")
```

> **Warning**: VACUUM removes time travel capability for deleted versions.

---

## Step 5 – Configure Partitioning

### Create Partitioned Table:

```python
df.write.format("delta") \
    .partitionBy("OrderYear", "OrderMonth") \
    .saveAsTable("partitioned_sales")
```

### Partitioning Best Practices:

| Do | Don't |
|----|---------|
| Partition on frequently filtered columns | Over-partition (too many small partitions) |
| Use low-cardinality columns | Partition on high-cardinality (e.g., CustomerID) |
| Align with query patterns | Change partition scheme on existing table |

---

## Step 6 – Apply Z-Ordering

Z-ordering colocates related data for faster queries.

```python
# Z-order on frequently used filter/join columns
spark.sql("OPTIMIZE sales ZORDER BY (ProductID, CustomerID)")
```

### Z-Order Best Practices:

- Choose columns used in WHERE clauses
- Maximum 4 columns recommended
- Re-run after significant data changes

---

## Step 7 – Configure Auto-Optimization

```python
# Enable optimized writes (auto-coalesce small files on write)
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")

# Enable auto-compact (periodic compaction)
spark.conf.set("spark.microsoft.delta.autoCompact.enabled", "true")

# Set target file size (128MB default)
spark.conf.set("spark.microsoft.delta.optimizeWrite.fileSize", "134217728")
```

### Set at Table Level:

```python
spark.sql("""
    ALTER TABLE sales SET TBLPROPERTIES (
        'delta.autoOptimize.optimizeWrite' = 'true',
        'delta.autoOptimize.autoCompact' = 'true'
    )
""")
```

---

## Step 8 – Monitor and Maintain

### Create Maintenance Notebook:

```python
# List all tables needing optimization
tables = spark.sql("SHOW TABLES").collect()

for table in tables:
    table_name = table.tableName
    print(f"Optimizing {table_name}...")
    
    # Optimize
    spark.sql(f"OPTIMIZE {table_name}")
    
    # Vacuum
    spark.sql(f"VACUUM {table_name} RETAIN 168 HOURS")
    
    print(f"Completed {table_name}")
```

### Schedule via Pipeline:

1. Create pipeline with Notebook activity.
2. Schedule to run nightly/weekly.
3. Monitor execution in pipeline runs.

---

## ✅ Lab Checklist

- [ ] Analyzed table health and file statistics
- [ ] Optimized tables to compact small files
- [ ] Applied Z-ordering for query performance
- [ ] Vacuumed old versions to reclaim storage
- [ ] Configured partitioning strategy
- [ ] Enabled auto-optimization settings
- [ ] Created maintenance routine
