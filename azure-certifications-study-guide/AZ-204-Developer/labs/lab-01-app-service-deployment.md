# Lab 01: Deploy an App Service Web App

## 🎯 Lab Goal

Deploy a web application to **Azure App Service** and configure:

- Deployment from local code or GitHub
- Application settings and connection strings
- Deployment slots (staging/production)

This supports the **Implement Azure App Service web apps** domain of AZ‑204.

---

## ✅ Prerequisites

- Azure subscription
- Azure CLI installed
- A simple web app (Node.js, Python, or .NET)

---

## Step 1 – Create an App Service Plan and Web App

```bash
# Create resource group
az group create --name rg-az204-appservice --location eastus

# Create App Service plan (Linux, Basic tier for lab)
az appservice plan create \
  --name plan-az204 \
  --resource-group rg-az204-appservice \
  --sku B1 \
  --is-linux

# Create web app (Python example)
az webapp create \
  --name webapp-az204-<unique> \
  --resource-group rg-az204-appservice \
  --plan plan-az204 \
  --runtime "PYTHON:3.11"
```

---

## Step 2 – Deploy Code Using ZIP Deploy

1. Create a simple Flask app locally:

```python
# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Azure App Service!"

if __name__ == "__main__":
    app.run()
```

2. Create `requirements.txt`:

```
flask
gunicorn
```

3. Zip and deploy:

```bash
zip -r app.zip . -x ".git/*"
az webapp deploy \
  --resource-group rg-az204-appservice \
  --name webapp-az204-<unique> \
  --src-path app.zip \
  --type zip
```

4. Browse to `https://webapp-az204-<unique>.azurewebsites.net` and verify.

---

## Step 3 – Configure Application Settings

```bash
az webapp config appsettings set \
  --resource-group rg-az204-appservice \
  --name webapp-az204-<unique> \
  --settings MY_SETTING="HelloFromAzure"
```

In your app, read this via `os.environ.get("MY_SETTING")`.

---

## Step 4 – Create a Deployment Slot

```bash
az webapp deployment slot create \
  --name webapp-az204-<unique> \
  --resource-group rg-az204-appservice \
  --slot staging
```

Deploy a different version to staging:

```bash
az webapp deploy \
  --resource-group rg-az204-appservice \
  --name webapp-az204-<unique> \
  --slot staging \
  --src-path app-v2.zip \
  --type zip
```

Swap slots:

```bash
az webapp deployment slot swap \
  --name webapp-az204-<unique> \
  --resource-group rg-az204-appservice \
  --slot staging \
  --target-slot production
```

---

## Cleanup

```bash
az group delete --name rg-az204-appservice --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created App Service plan and web app
- [ ] Deployed code using ZIP deploy
- [ ] Configured application settings
- [ ] Created a staging deployment slot and performed a swap
- [ ] Cleaned up resources
