# Lab 03: Create Datastores and Data Assets

## 🎯 Lab Goal

Manage **data in Azure ML** using datastores and data assets:

- Register datastores
- Create URI file and folder data assets
- Create MLTable data assets

This supports the **Manage data** domain of DP‑100.

---

## ✅ Prerequisites

- Azure ML workspace
- Azure Storage account with sample data

---

## Step 1 – Understand Data Concepts

| Concept | Description |
|---------|------------|
| Datastore | Connection to storage (Blob, ADLS, etc.) |
| Data Asset | Reference to specific data (versioned) |
| URI File | Single file reference |
| URI Folder | Folder reference |
| MLTable | Tabular data with schema |

---

## Step 2 – Register a Datastore

### Default Datastores:

```python
# List existing datastores
for ds in ml_client.datastores.list():
    print(f"{ds.name}: {ds.type}")

# workspaceblobstore is created automatically
```

### Register Custom Blob Datastore:

```python
from azure.ai.ml.entities import AzureBlobDatastore
from azure.ai.ml.entities import AccountKeyConfiguration

blob_datastore = AzureBlobDatastore(
    name="blob_training_data",
    account_name="<storage-account>",
    container_name="training-data",
    credentials=AccountKeyConfiguration(
        account_key="<account-key>"
    )
)

ml_client.datastores.create_or_update(blob_datastore)
```

### Using Managed Identity (Recommended):

```python
blob_datastore = AzureBlobDatastore(
    name="blob_training_data",
    account_name="<storage-account>",
    container_name="training-data"
    # No credentials = use workspace identity
)
```

---

## Step 3 – Create URI File Data Asset

```python
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

csv_data = Data(
    name="titanic-data",
    description="Titanic passenger data",
    path="azureml://datastores/workspaceblobstore/paths/data/titanic.csv",
    type=AssetTypes.URI_FILE
)

ml_client.data.create_or_update(csv_data)
print(f"Created data asset: {csv_data.name}")
```

### From Local File:

```python
local_data = Data(
    name="local-titanic",
    description="Uploaded from local",
    path="./data/titanic.csv",  # Local path
    type=AssetTypes.URI_FILE
)

ml_client.data.create_or_update(local_data)
# File is uploaded to default datastore
```

---

## Step 4 – Create URI Folder Data Asset

```python
folder_data = Data(
    name="images-training",
    description="Training images folder",
    path="azureml://datastores/workspaceblobstore/paths/images/train/",
    type=AssetTypes.URI_FOLDER
)

ml_client.data.create_or_update(folder_data)
```

---

## Step 5 – Create MLTable Data Asset

First, create an `MLTable` file in your data folder:

```yaml
# MLTable file
paths:
  - file: ./titanic.csv

transformations:
  - read_delimited:
      delimiter: ','
      header: all_files_same_headers
      encoding: utf8
```

Then register:

```python
mltable_data = Data(
    name="titanic-mltable",
    description="Titanic data as MLTable",
    path="./data/titanic-mltable/",  # Folder containing MLTable file
    type=AssetTypes.MLTABLE
)

ml_client.data.create_or_update(mltable_data)
```

### Load MLTable in Training Script:

```python
import mltable

# Load the MLTable
table = mltable.load("./input_data/")

# Convert to pandas
df = table.to_pandas_dataframe()
print(df.head())
```

---

## Step 6 – Version and Retrieve Data Assets

```python
# List versions of a data asset
for data in ml_client.data.list(name="titanic-data"):
    print(f"Version: {data.version}")

# Get specific version
data_v1 = ml_client.data.get(name="titanic-data", version="1")
print(f"Path: {data_v1.path}")

# Get latest version
data_latest = ml_client.data.get(name="titanic-data", label="latest")
```

---

## Step 7 – Use Data in Training Jobs

```python
from azure.ai.ml import command, Input

job = command(
    code="./src",
    command="python train.py --data ${{inputs.training_data}}",
    inputs={
        "training_data": Input(
            type="uri_file",
            path="azureml:titanic-data@latest"
        )
    },
    environment="AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest",
    compute="cpu-cluster"
)
```

---

## ✅ Lab Checklist

- [ ] Listed default datastores
- [ ] Registered a custom blob datastore
- [ ] Created URI file data asset
- [ ] Created URI folder data asset
- [ ] Created MLTable data asset
- [ ] Versioned and retrieved data assets
- [ ] Referenced data assets in job inputs
