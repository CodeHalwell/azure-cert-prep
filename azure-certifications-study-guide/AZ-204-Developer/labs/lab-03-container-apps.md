# Lab 03: Deploy and Scale Azure Container Apps

## 🎯 Lab Goal

Deploy a containerized application to **Azure Container Apps** and:

- Configure ingress and scaling
- Use revisions for updates

This supports the **Implement containerized solutions** domain of AZ‑204.

---

## ✅ Prerequisites

- Azure subscription
- Docker installed (for building images)
- Azure CLI with `containerapp` extension

```bash
az extension add --name containerapp --upgrade
```

---

## Step 1 – Create Container Apps Environment

```bash
az group create --name rg-az204-aca --location eastus

az containerapp env create \
  --name env-az204 \
  --resource-group rg-az204-aca \
  --location eastus
```

---

## Step 2 – Deploy a Container App

```bash
az containerapp create \
  --name myapp \
  --resource-group rg-az204-aca \
  --environment env-az204 \
  --image mcr.microsoft.com/azuredocs/containerapps-helloworld:latest \
  --target-port 80 \
  --ingress external \
  --min-replicas 1 \
  --max-replicas 5
```

Get the URL:

```bash
az containerapp show \
  --name myapp \
  --resource-group rg-az204-aca \
  --query properties.configuration.ingress.fqdn -o tsv
```

---

## Step 3 – Configure Scaling Rules

```bash
az containerapp update \
  --name myapp \
  --resource-group rg-az204-aca \
  --scale-rule-name http-rule \
  --scale-rule-type http \
  --scale-rule-http-concurrency 10
```

This scales based on concurrent HTTP requests.

---

## Step 4 – Deploy a New Revision

```bash
az containerapp update \
  --name myapp \
  --resource-group rg-az204-aca \
  --set-env-vars "VERSION=v2"
```

View revisions:

```bash
az containerapp revision list \
  --name myapp \
  --resource-group rg-az204-aca \
  --output table
```

---

## Cleanup

```bash
az group delete --name rg-az204-aca --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created a Container Apps environment
- [ ] Deployed a container app with external ingress
- [ ] Configured HTTP-based scaling rules
- [ ] Deployed a new revision via update
- [ ] Cleaned up resources
