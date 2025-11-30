# Lab 04: Perform Exploratory Data Analysis (EDA)

## 🎯 Lab Goal

Perform **exploratory data analysis** in Azure ML:

- Use notebooks in Azure ML Studio
- Analyze datasets with pandas and visualizations
- Profile data for ML readiness

This supports the **Explore data** domain of DP‑100.

---

## ✅ Prerequisites

- Azure ML workspace with compute instance
- Sample dataset (e.g., Titanic)

---

## Step 1 – Create a Notebook in Azure ML Studio

1. Go to **Azure ML Studio → Notebooks**.
2. Click **+ Create new file**.
3. Name: `eda-titanic.ipynb`
4. Select your compute instance.

---

## Step 2 – Load Data from Data Asset

```python
# Connect to workspace
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient.from_config(DefaultAzureCredential())

# Get data asset
data_asset = ml_client.data.get(name="titanic-data", version="1")
print(f"Data path: {data_asset.path}")

# Load with pandas
import pandas as pd
df = pd.read_csv(data_asset.path)
print(df.head())
```

---

## Step 3 – Basic Data Exploration

```python
# Dataset shape
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Data types
print(df.dtypes)

# Basic statistics
print(df.describe())

# Missing values
print(df.isnull().sum())

# Target distribution
print(df['Survived'].value_counts())
```

---

## Step 4 – Data Visualization

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")

# Survival by class
plt.figure(figsize=(10, 4))
sns.countplot(data=df, x='Pclass', hue='Survived')
plt.title('Survival by Passenger Class')
plt.show()

# Age distribution
plt.figure(figsize=(10, 4))
sns.histplot(data=df, x='Age', hue='Survived', kde=True)
plt.title('Age Distribution by Survival')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
numeric_cols = df.select_dtypes(include=['number'])
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Feature Correlations')
plt.show()
```

---

## Step 5 – Handle Missing Values

```python
# Check missing percentages
missing_pct = (df.isnull().sum() / len(df)) * 100
print(missing_pct.sort_values(ascending=False))

# Fill Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill Embarked with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop columns with too many missing values
df.drop(columns=['Cabin'], inplace=True)

# Verify
print(df.isnull().sum())
```

---

## Step 6 – Feature Engineering

```python
# Create new features
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

# Extract title from name
df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)

# Bin ages
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 18, 35, 60, 100], 
                         labels=['Child', 'Teen', 'Adult', 'Middle', 'Senior'])

print(df[['Name', 'Title', 'Age', 'AgeGroup', 'FamilySize', 'IsAlone']].head())
```

---

## Step 7 – Generate Data Profile Report

```python
# Using ydata-profiling (formerly pandas-profiling)
!pip install ydata-profiling

from ydata_profiling import ProfileReport

profile = ProfileReport(df, title="Titanic EDA Report", explorative=True)

# Save to HTML
profile.to_file("titanic_eda_report.html")

# Display in notebook
profile.to_notebook_iframe()
```

---

## Step 8 – Save Processed Data

```python
# Save cleaned data
df.to_csv("titanic_cleaned.csv", index=False)

# Upload as new data asset
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

cleaned_data = Data(
    name="titanic-cleaned",
    description="Cleaned and feature-engineered Titanic data",
    path="./titanic_cleaned.csv",
    type=AssetTypes.URI_FILE
)

ml_client.data.create_or_update(cleaned_data)
```

---

## ✅ Lab Checklist

- [ ] Created notebook in Azure ML Studio
- [ ] Loaded data from data asset
- [ ] Explored data types, statistics, and missing values
- [ ] Created visualizations (distributions, correlations)
- [ ] Handled missing values appropriately
- [ ] Performed feature engineering
- [ ] Generated automated data profile report
- [ ] Saved processed data as new data asset
