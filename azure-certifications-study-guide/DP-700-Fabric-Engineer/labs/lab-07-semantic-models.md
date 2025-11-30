# Lab 07: Build and Manage Semantic Models

## 🎯 Lab Goal

Create **semantic models** for reporting:

- Build model from lakehouse tables
- Define relationships and measures
- Configure row-level security

This supports the **Implement analytics and reporting** domain of DP‑700.

---

## ✅ Prerequisites

- Fabric lakehouse with tables
- Power BI Desktop (optional)

---

## Step 1 – Create a Semantic Model

### From Lakehouse:

1. Open your lakehouse.
2. Click **New semantic model**.
3. Select tables to include:
   - `fact_sales`
   - `dim_customers`
   - `dim_products`
   - `dim_date`
4. Name: `Sales Analytics Model`
5. Click **Create**.

### The Default Model:

A default semantic model is created automatically with your lakehouse.

---

## Step 2 – Open Model in Web Editor

1. Click on the semantic model in workspace.
2. Click **Open data model**.
3. Explore the model view.

---

## Step 3 – Define Relationships

1. In the model view, drag and drop to create relationships:
   - `fact_sales[CustomerKey]` → `dim_customers[CustomerKey]`
   - `fact_sales[ProductKey]` → `dim_products[ProductKey]`
   - `fact_sales[DateKey]` → `dim_date[DateKey]`

2. Configure relationship properties:
   - **Cardinality**: Many-to-one
   - **Cross-filter direction**: Single
   - **Active**: Yes

### Via Properties:

1. Click on a relationship line.
2. Edit cardinality and filter direction.

---

## Step 4 – Create Measures with DAX

1. Select a table (e.g., `fact_sales`).
2. Click **New measure**.
3. Enter DAX formulas:

```dax
Total Sales = SUM(fact_sales[SalesAmount])
```

```dax
Total Orders = COUNTROWS(fact_sales)
```

```dax
Average Order Value = DIVIDE([Total Sales], [Total Orders])
```

```dax
YTD Sales = 
TOTALYTD(
    [Total Sales],
    dim_date[Date]
)
```

```dax
Sales vs Prior Year = 
VAR CurrentSales = [Total Sales]
VAR PriorYearSales = CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(dim_date[Date])
)
RETURN
DIVIDE(CurrentSales - PriorYearSales, PriorYearSales)
```

---

## Step 5 – Create Calculated Columns

```dax
Profit Margin = 
DIVIDE(
    fact_sales[SalesAmount] - fact_sales[Cost],
    fact_sales[SalesAmount]
)
```

```dax
Customer Segment = 
SWITCH(
    TRUE(),
    dim_customers[LifetimeValue] > 10000, "Platinum",
    dim_customers[LifetimeValue] > 5000, "Gold",
    dim_customers[LifetimeValue] > 1000, "Silver",
    "Bronze"
)
```

---

## Step 6 – Configure Row-Level Security (RLS)

1. In the model, click **Manage roles**.
2. Create a new role:
   - **Name**: `Regional Sales`
3. Add table filter:
   - Table: `dim_customers`
   - Filter: `[Region] = USERPRINCIPALNAME()`

```dax
// More complex filter
[SalesRegion] = 
LOOKUPVALUE(
    SecurityTable[Region],
    SecurityTable[UserEmail],
    USERPRINCIPALNAME()
)
```

4. Click **Save**.

### Test RLS:

1. Click **View as role**.
2. Select the role to test.
3. Verify data filtering.

---

## Step 7 – Configure Permissions

1. Go to semantic model settings.
2. Under **Permissions**:
   - **Build**: Allow building reports
   - **Write**: Allow editing model
   - **Share**: Allow sharing

### Assign RLS Roles:

1. Go to **Security**.
2. Assign users/groups to roles.

---

## Step 8 – Create a Report

1. From the semantic model, click **Create report**.
2. Add visuals:
   - Card: Total Sales
   - Line chart: Sales over Time
   - Bar chart: Sales by Product
   - Table: Customer Details
3. Add slicers:
   - Date range
   - Product category
   - Region
4. Save the report.

---

## Step 9 – Refresh and Sync

The semantic model syncs with lakehouse data:

1. **Default model**: Auto-syncs with lakehouse changes.
2. **Custom model**: Refresh manually or schedule.

### Schedule Refresh:

1. Go to model settings.
2. Configure refresh schedule.
3. Set frequency and time.

---

## ✅ Lab Checklist

- [ ] Created semantic model from lakehouse tables
- [ ] Defined relationships between fact and dimension tables
- [ ] Created DAX measures for analytics
- [ ] Added calculated columns
- [ ] Configured row-level security
- [ ] Set up model permissions
- [ ] Created a report from the model
- [ ] Configured refresh schedule
