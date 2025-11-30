# Lab 05: Ingest Data with Dataflows Gen2

## 🎯 Lab Goal

Use **Dataflows Gen2** for no-code data ingestion:

- Connect to various data sources
- Transform data with Power Query
- Load data to lakehouse

This supports the **Ingest and transform data** domain of DP‑700.

---

## ✅ Prerequisites

- Fabric workspace with lakehouse
- Access to data sources (SQL, files, APIs)

---

## Step 1 – Create a Dataflow Gen2

1. In your workspace, click **+ New → Dataflow Gen2**.
2. Name: `ingest_customer_data`
3. The Power Query editor opens.

---

## Step 2 – Connect to Data Source

### SQL Database:

1. Click **Get data → Azure SQL Database**.
2. Enter:
   - Server: `server.database.windows.net`
   - Database: `SalesDB`
3. Choose authentication method.
4. Select tables to import.

### Excel/CSV:

1. Click **Get data → Text/CSV** or **Excel**.
2. Upload file or provide URL.
3. Configure parsing options.

### Web API:

1. Click **Get data → Web**.
2. Enter API URL.
3. Configure headers and authentication.

---

## Step 3 – Transform with Power Query

### Common Transformations:

| Transformation | Steps |
|----------------|-------|
| Remove columns | Right-click column → Remove |
| Rename columns | Double-click header |
| Change type | Right-click → Change type |
| Filter rows | Click filter icon on column |
| Sort | Click column header |

### Advanced Transformations:

1. **Add Column → Custom Column**:

```m
// M formula for custom column
if [Amount] > 1000 then "High" else "Low"
```

2. **Merge Queries** (Join):
   - Select first table
   - Click **Merge queries**
   - Select second table and join columns
   - Choose join type (Left, Inner, etc.)

3. **Append Queries** (Union):
   - Click **Append queries**
   - Select tables to combine

---

## Step 4 – Group and Aggregate

1. Click **Transform → Group By**.
2. Configure:
   - **Group by columns**: CustomerID
   - **New column**: TotalPurchases
   - **Operation**: Sum
   - **Column**: Amount

---

## Step 5 – Configure Data Destination

1. Click on the query in the Queries pane.
2. Click **+ (Add data destination)**.
3. Select **Lakehouse**.
4. Configure:
   - **Lakehouse**: Select your lakehouse
   - **Table name**: `customers`
   - **Update method**: Replace (or Append)

### Column Mapping:

- Map source columns to destination columns
- Handle type mismatches

---

## Step 6 – Handle Incremental Refresh

1. Create a parameter for date range:
   - **Manage parameters → New parameter**
   - Name: `RangeStart`, `RangeEnd`
   - Type: Date/Time

2. Filter data using parameter:

```m
Table.SelectRows(Source, each [OrderDate] >= RangeStart and [OrderDate] < RangeEnd)
```

3. Configure incremental refresh in destination settings.

---

## Step 7 – Run the Dataflow

1. Click **Publish** to save the dataflow.
2. Click **Refresh now** to run immediately.
3. Monitor progress in the dataflow view.

### View Refresh History:

1. Go to workspace.
2. Click **...** on dataflow → **Refresh history**.
3. View status, duration, and errors.

---

## Step 8 – Schedule Refresh

1. Click **...** on dataflow → **Settings**.
2. Under **Scheduled refresh**:
   - Enable scheduled refresh
   - Set frequency (daily, hourly)
   - Set time zone and times
3. Click **Apply**.

---

## Step 9 – Error Handling

### In Power Query:

```m
// Replace errors with null
Table.ReplaceErrorValues(Source, {{"Amount", null}})

// Remove error rows
Table.RemoveRowsWithErrors(Source)
```

### Monitor Failures:

1. Check refresh history for errors.
2. Review detailed error messages.
3. Fix transformations and republish.

---

## ✅ Lab Checklist

- [ ] Created a Dataflow Gen2
- [ ] Connected to various data sources
- [ ] Applied Power Query transformations
- [ ] Grouped and aggregated data
- [ ] Configured lakehouse as destination
- [ ] Set up incremental refresh
- [ ] Published and ran the dataflow
- [ ] Scheduled automatic refresh
