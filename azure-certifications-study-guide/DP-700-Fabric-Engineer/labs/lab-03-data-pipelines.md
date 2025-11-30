# Lab 03: Build Data Pipelines in Fabric

## 🎯 Lab Goal

Create **data pipelines** for orchestrating data movement:

- Build a pipeline with Copy activity
- Add data transformation steps
- Schedule and monitor pipelines

This supports the **Implement and manage data pipelines** domain of DP‑700.

---

## ✅ Prerequisites

- Fabric workspace with lakehouse
- Source data (e.g., Azure SQL, files)

---

## Step 1 – Create a Pipeline

1. In your workspace, switch to **Data Factory** experience.
2. Click **+ New → Data pipeline**.
3. Name: `ingest_sales_data`
4. Click **Create**.

---

## Step 2 – Add Copy Activity

1. In the pipeline canvas, click **Add activity → Copy data**.
2. Configure **Source**:
   - **Data store type**: Azure SQL Database (or other)
   - **Connection**: Create new or select existing
   - **Table**: Select source table
3. Configure **Destination**:
   - **Data store type**: Lakehouse
   - **Lakehouse**: Select your lakehouse
   - **Root folder**: Tables (for Delta) or Files (for raw)
   - **Table name**: `raw_sales`

---

## Step 3 – Configure Copy Settings

### Source Settings:

```sql
-- Use a query instead of table
SELECT * FROM Sales 
WHERE OrderDate >= @pipeline().parameters.StartDate
```

### Sink Settings:

| Setting | Value |
|---------|-------|
| Table action | Append (or Overwrite) |
| Enable partition | Yes |
| Partition column | OrderDate |

---

## Step 4 – Add Notebook Activity for Transformation

1. Add **Notebook** activity after Copy.
2. Connect Copy → Notebook (on success).
3. Configure:
   - **Notebook**: Select transformation notebook
   - **Parameters**: Pass dynamic values

```json
{
  "input_table": "raw_sales",
  "output_table": "clean_sales"
}
```

---

## Step 5 – Add Control Flow Activities

### ForEach Loop:

1. Add **ForEach** activity.
2. Configure items: `@createArray('2023', '2024')`
3. Add nested activities to process each year.

### If Condition:

```
@greater(activity('CopyData').output.rowsCopied, 0)
```

### Set Variable:

1. Add **Set variable** activity.
2. Configure:
   - Variable name: `ProcessedRows`
   - Value: `@activity('CopyData').output.rowsCopied`

---

## Step 6 – Add Parameters

1. Click **Parameters** tab.
2. Add parameters:

| Name | Type | Default |
|------|------|--------|
| StartDate | String | 2024-01-01 |
| Environment | String | dev |

3. Use in activities: `@pipeline().parameters.StartDate`

---

## Step 7 – Run and Monitor Pipeline

### Manual Run:

1. Click **Run** → **Run now**.
2. Provide parameter values.
3. Monitor in **Output** tab.

### View Run History:

1. Go to **Monitor** hub.
2. Select **Pipeline runs**.
3. View:
   - Status (Succeeded, Failed, Running)
   - Duration
   - Activity details

---

## Step 8 – Schedule the Pipeline

1. Click **Schedule** in the pipeline.
2. Configure:
   - **Recurrence**: Daily
   - **Time**: 02:00 UTC
   - **Start date**: Today
3. Click **Apply**.

### Or Use Trigger:

1. Add **Schedule trigger**.
2. Configure:
   - Frequency: Hourly, Daily, etc.
   - Parameters: Dynamic values

---

## Step 9 – Error Handling

### Retry Policy:

1. Click on an activity.
2. Go to **Settings → Retry**.
3. Configure:
   - Retry count: 3
   - Retry interval: 30 seconds

### Failure Path:

1. Connect activity → error handling activity (on failure).
2. Add **Web** activity to send alert:

```json
{
  "message": "Pipeline failed",
  "activity": "@activity('CopyData').error.message"
}
```

---

## ✅ Lab Checklist

- [ ] Created a data pipeline
- [ ] Added Copy activity to ingest data
- [ ] Configured source and destination settings
- [ ] Added Notebook activity for transformation
- [ ] Implemented control flow (ForEach, If)
- [ ] Added pipeline parameters
- [ ] Ran and monitored the pipeline
- [ ] Scheduled the pipeline for automation
