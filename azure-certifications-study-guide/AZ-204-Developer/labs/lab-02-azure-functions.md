# Lab 02: Implement Azure Functions

## 🎯 Lab Goal

Create and deploy **Azure Functions** with:

- HTTP trigger
- Timer trigger
- Bindings (input/output)

This supports the **Implement Azure Functions** domain of AZ‑204.

---

## ✅ Prerequisites

- Azure subscription
- Azure Functions Core Tools installed
- Python 3.9+ or Node.js

---

## Step 1 – Create a Function App in Azure

```bash
az group create --name rg-az204-functions --location eastus

az storage account create \
  --name staz204func<unique> \
  --resource-group rg-az204-functions \
  --sku Standard_LRS

az functionapp create \
  --name funcapp-az204-<unique> \
  --resource-group rg-az204-functions \
  --storage-account staz204func<unique> \
  --consumption-plan-location eastus \
  --runtime python \
  --runtime-version 3.11 \
  --functions-version 4 \
  --os-type Linux
```

---

## Step 2 – Create an HTTP Trigger Function Locally

```bash
func init az204-functions --python
cd az204-functions
func new --name HttpTrigger --template "HTTP trigger" --authlevel anonymous
```

Edit `HttpTrigger/__init__.py`:

```python
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name", "World")
    return func.HttpResponse(f"Hello, {name}!")
```

Test locally:

```bash
func start
# Visit http://localhost:7071/api/HttpTrigger?name=Azure
```

---

## Step 3 – Deploy to Azure

```bash
func azure functionapp publish funcapp-az204-<unique>
```

Test via the Azure URL.

---

## Step 4 – Add a Timer Trigger

```bash
func new --name TimerTrigger --template "Timer trigger"
```

Edit `TimerTrigger/function.json` to run every 5 minutes:

```json
{
  "bindings": [
    {
      "name": "mytimer",
      "type": "timerTrigger",
      "direction": "in",
      "schedule": "0 */5 * * * *"
    }
  ]
}
```

In `__init__.py`:

```python
import logging
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    logging.info("Timer trigger executed!")
```

Redeploy and observe logs in the portal.

---

## Cleanup

```bash
az group delete --name rg-az204-functions --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created a Function App in Azure
- [ ] Developed and tested an HTTP trigger locally
- [ ] Deployed functions to Azure
- [ ] Added a timer trigger function
- [ ] Cleaned up resources
