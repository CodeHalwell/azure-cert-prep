# Lab 01: Set Up a Microsoft Fabric Workspace

## 🎯 Lab Goal

Create and configure a **Microsoft Fabric workspace**:

- Create a workspace with Fabric capacity
- Configure workspace settings
- Understand Fabric experiences

This supports the **Implement and manage analytics solutions** domain of DP‑700.

---

## ✅ Prerequisites

- Microsoft 365 account with Fabric access
- Fabric capacity (trial or paid)

---

## Step 1 – Access Microsoft Fabric

1. Go to [app.fabric.microsoft.com](https://app.fabric.microsoft.com).
2. Sign in with your organizational account.
3. If prompted, start a Fabric trial.

---

## Step 2 – Understand Fabric Experiences

| Experience | Purpose |
|-----------|--------|
| Data Engineering | Lakehouse, Spark notebooks, pipelines |
| Data Warehouse | T-SQL analytics |
| Data Science | ML models, experiments |
| Real-Time Analytics | Streaming data (KQL) |
| Data Factory | Data pipelines, dataflows |
| Power BI | Reports, dashboards |

Switch experiences using the icon in the bottom-left corner.

---

## Step 3 – Create a Workspace

1. Click **Workspaces** in the left navigation.
2. Click **+ New workspace**.
3. Configure:
   - **Name**: `dp700-lab-workspace`
   - **Description**: "Fabric labs for DP-700"
4. Expand **Advanced**:
   - **License mode**: Select Fabric capacity or Trial
   - **Default storage format**: Delta (Parquet)
5. Click **Apply**.

---

## Step 4 – Configure Workspace Settings

1. Open the workspace.
2. Click **Settings** (gear icon) → **Workspace settings**.
3. Configure:

### General:
- **Workspace name and description**
- **Workspace image** (optional)

### License:
- Verify capacity assignment

### OneLake:
- **Allow Azure Data Lake Storage shortcuts**: On
- **Allow S3 shortcuts**: On (if needed)

### Spark:
- Configure default Spark settings for notebooks

---

## Step 5 – Manage Workspace Access

1. Go to **Manage access** in workspace settings.
2. Add members with roles:

| Role | Permissions |
|------|------------|
| Admin | Full control, manage access |
| Member | Create, edit, delete items |
| Contributor | Create, edit items (no delete) |
| Viewer | View only |

3. Click **Add people or groups** and assign roles.

---

## Step 6 – Enable Git Integration (Optional)

1. Go to **Workspace settings → Git integration**.
2. Connect to:
   - Azure DevOps
   - GitHub
3. Configure:
   - Repository
   - Branch
   - Folder path
4. Sync workspace items to Git for version control.

---

## Step 7 – Explore Workspace Items

A Fabric workspace can contain:

| Item Type | Experience |
|-----------|------------|
| Lakehouse | Data Engineering |
| Warehouse | Data Warehouse |
| Notebook | Data Engineering / Data Science |
| Pipeline | Data Factory |
| Dataflow Gen2 | Data Factory |
| Semantic Model | Power BI |
| Report | Power BI |
| KQL Database | Real-Time Analytics |

---

## Step 8 – View Lineage

1. In the workspace, click **Lineage view**.
2. See data flow between items:
   - Dataflows → Lakehouse → Semantic Model → Report

---

## ✅ Lab Checklist

- [ ] Accessed Microsoft Fabric portal
- [ ] Understood the different Fabric experiences
- [ ] Created a workspace with Fabric capacity
- [ ] Configured workspace settings
- [ ] Managed workspace access and roles
- [ ] Explored Git integration options
- [ ] Viewed workspace lineage
