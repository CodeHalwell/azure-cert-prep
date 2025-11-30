# Lab 04: Transform Data with Spark Notebooks

## 🎯 Lab Goal

Use **Spark notebooks** for data transformation:

- Write PySpark code for transformations
- Work with Delta tables
- Optimize Spark jobs

This supports the **Transform and prepare data** domain of DP‑700.

---

## ✅ Prerequisites

- Fabric workspace with lakehouse
- Sample data in lakehouse

---

## Step 1 – Create a Notebook

1. Open your lakehouse.
2. Click **Open notebook → New notebook**.
3. The notebook automatically connects to the lakehouse.

---

## Step 2 – Read Data from Lakehouse

```python
# Read from managed table
df = spark.read.table("raw_sales")
display(df)

# Read from Files folder
df_csv = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("Files/raw/sales/*.csv")

# Read Delta files directly
df_delta = spark.read.format("delta").load("Tables/raw_sales")
```

---

## Step 3 – Transform Data with PySpark

```python
from pyspark.sql.functions import col, when, year, month, sum, avg

# Filter and clean
df_clean = df.filter(col("OrderAmount") > 0) \
             .dropna(subset=["CustomerId", "OrderDate"]) \
             .dropDuplicates(["OrderId"])

# Add calculated columns
df_enhanced = df_clean.withColumn(
    "OrderYear", year(col("OrderDate"))
).withColumn(
    "OrderMonth", month(col("OrderDate"))
).withColumn(
    "Category", 
    when(col("OrderAmount") > 1000, "High")
    .when(col("OrderAmount") > 100, "Medium")
    .otherwise("Low")
)

display(df_enhanced)
```

---

## Step 4 – Aggregate Data

```python
# Monthly sales summary
monthly_sales = df_enhanced.groupBy("OrderYear", "OrderMonth") \
    .agg(
        sum("OrderAmount").alias("TotalSales"),
        avg("OrderAmount").alias("AvgOrderValue"),
        count("OrderId").alias("OrderCount")
    ) \
    .orderBy("OrderYear", "OrderMonth")

display(monthly_sales)

# Customer summary
customer_summary = df_enhanced.groupBy("CustomerId") \
    .agg(
        sum("OrderAmount").alias("LifetimeValue"),
        count("OrderId").alias("TotalOrders"),
        min("OrderDate").alias("FirstOrder"),
        max("OrderDate").alias("LastOrder")
    )

display(customer_summary)
```

---

## Step 5 – Write to Delta Tables

```python
# Write as new managed table
df_enhanced.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("clean_sales")

# Append to existing table
monthly_sales.write.format("delta") \
    .mode("append") \
    .saveAsTable("monthly_sales_summary")

# Write with partitioning
df_enhanced.write.format("delta") \
    .partitionBy("OrderYear", "OrderMonth") \
    .mode("overwrite") \
    .saveAsTable("partitioned_sales")
```

---

## Step 6 – Use SQL in Notebooks

```python
# Run SQL directly
spark.sql("""
    SELECT 
        OrderYear,
        SUM(OrderAmount) as TotalSales
    FROM clean_sales
    GROUP BY OrderYear
    ORDER BY OrderYear
""").show()

# Mix SQL and DataFrame
result = spark.sql("SELECT * FROM clean_sales WHERE Category = 'High'")
result_count = result.count()
print(f"High-value orders: {result_count}")
```

### SQL Magic:

```sql
%%sql
SELECT * FROM clean_sales LIMIT 10
```

---

## Step 7 – Optimize Spark Jobs

### Caching:

```python
# Cache frequently used DataFrame
df_enhanced.cache()
df_enhanced.count()  # Trigger caching

# Unpersist when done
df_enhanced.unpersist()
```

### Partitioning:

```python
# Repartition for better parallelism
df_repartitioned = df.repartition(8, "CustomerId")

# Coalesce to reduce partitions (for small outputs)
df_coalesced = df.coalesce(1)
```

### Broadcast Joins:

```python
from pyspark.sql.functions import broadcast

# Small dimension table
dim_customers = spark.table("dim_customers")

# Broadcast join for small tables
result = df_enhanced.join(
    broadcast(dim_customers),
    "CustomerId"
)
```

---

## Step 8 – Parameterize Notebooks

```python
# Define parameters cell (toggle as parameters)
input_table = "raw_sales"
output_table = "clean_sales"
process_date = "2024-01-01"
```

When called from a pipeline, parameters are passed dynamically.

---

## ✅ Lab Checklist

- [ ] Created a notebook connected to lakehouse
- [ ] Read data from tables and files
- [ ] Transformed data with PySpark
- [ ] Aggregated data for analytics
- [ ] Wrote results to Delta tables
- [ ] Used SQL within notebooks
- [ ] Applied optimization techniques
- [ ] Parameterized notebook for pipeline use
