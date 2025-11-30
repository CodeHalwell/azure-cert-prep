# Lab 02: Create and Configure a Lakehouse

## 🎯 Lab Goal

Create and configure a **Fabric Lakehouse**:

- Create a lakehouse
- Upload and organize data
- Query data with SQL endpoint

This supports the **Implement and manage lakehouse** domain of DP‑700.

---

## ✅ Prerequisites

- Microsoft Fabric workspace from Lab 01
- Sample data files (CSV, Parquet)

---

## Step 1 – Create a Lakehouse

1. Open your Fabric workspace.
2. Click **+ New → Lakehouse**.
3. Name: `sales_lakehouse`
4. Click **Create**.

---

## Step 2 – Understand Lakehouse Structure

```
sales_lakehouse/
├── Tables/           # Managed Delta tables
│   ├── customers
│   └── orders
├── Files/            # Unmanaged files
│   ├── raw/
│   └── staging/
└── SQL endpoint      # T-SQL queries
```

| Folder | Purpose |
|--------|--------|
| Tables | Delta tables with schema, queryable via SQL |
| Files | Raw files (CSV, JSON, Parquet) for staging |

---

## Step 3 – Upload Files to Lakehouse

### Via UI:

1. In the lakehouse, expand **Files**.
2. Click **... → Upload → Upload files**.
3. Select local CSV or Parquet files.
4. Create folders (e.g., `raw/customers/`).

### Via Shortcut:

1. Click **... → New shortcut**.
2. Choose source:
   - Azure Data Lake Storage Gen2
   - Amazon S3
   - Google Cloud Storage
3. Configure connection and path.

---

## Step 4 – Create a Managed Table from Files

### From CSV:

1. Navigate to a CSV file in Files.
2. Click **... → Load to Tables → New table**.
3. Configure:
   - **Table name**: `customers`
   - **File type**: Delimited
   - **First row as header**: Yes
4. Click **Load**.

### From Spark Notebook:

```python
# Read CSV from Files
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("Files/raw/customers.csv")

# Write as managed Delta table
df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("customers")
```

---

## Step 5 – Query with SQL Endpoint

1. Click **SQL endpoint** (top-right).
2. Write T-SQL queries:

```sql
SELECT TOP 10 *
FROM customers;

SELECT 
    Country,
    COUNT(*) as CustomerCount,
    SUM(TotalPurchases) as TotalSales
FROM customers
GROUP BY Country
ORDER BY TotalSales DESC;
```

3. Save queries for reuse.

---

## Step 6 – Create Views

```sql
CREATE VIEW vw_high_value_customers AS
SELECT *
FROM customers
WHERE TotalPurchases > 10000;
```

Views appear under the SQL endpoint schema.

---

## Step 7 – Explore Table Properties

1. In the lakehouse, click a table.
2. View:
   - **Schema** – Column names and types
   - **Preview** – Sample data
   - **History** – Delta table versions

### Via Spark:

```python
# View table history
spark.sql("DESCRIBE HISTORY customers").show()

# View table properties
spark.sql("DESCRIBE EXTENDED customers").show(truncate=False)
```

---

## Step 8 – Configure Lakehouse Permissions

1. Go to lakehouse settings.
2. Configure:
   - **OneLake data access roles** for fine-grained permissions
   - **SQL endpoint permissions** for T-SQL access

---

## ✅ Lab Checklist

- [ ] Created a Fabric lakehouse
- [ ] Understood Tables vs. Files structure
- [ ] Uploaded files and created shortcuts
- [ ] Created managed Delta tables from files
- [ ] Queried data using SQL endpoint
- [ ] Created views for common queries
- [ ] Explored table history and properties
