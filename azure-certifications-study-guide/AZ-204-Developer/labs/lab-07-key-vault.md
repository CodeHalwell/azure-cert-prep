# Lab 07: Secure Secrets with Azure Key Vault

## 🎯 Lab Goal

Use **Azure Key Vault** to:

- Store and retrieve secrets
- Access secrets from code using managed identity or SDK

This supports the **Implement secure Azure solutions** domain of AZ‑204.

---

## ✅ Prerequisites

- Azure subscription
- Python 3.9+ with `azure-keyvault-secrets` and `azure-identity`

```bash
pip install azure-keyvault-secrets azure-identity python-dotenv
```

---

## Step 1 – Create a Key Vault

```bash
az group create --name rg-az204-kv --location eastus

az keyvault create \
  --name kv-az204-<unique> \
  --resource-group rg-az204-kv \
  --location eastus
```

---

## Step 2 – Add Secrets via CLI

```bash
az keyvault secret set \
  --vault-name kv-az204-<unique> \
  --name "DatabasePassword" \
  --value "SuperSecretPassword123!"

az keyvault secret set \
  --vault-name kv-az204-<unique> \
  --name "ApiKey" \
  --value "my-api-key-12345"
```

---

## Step 3 – Access Secrets Using Python SDK

```python
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

load_dotenv()

vault_url = os.getenv("KEY_VAULT_URL")  # https://kv-az204-<unique>.vault.azure.net/
credential = DefaultAzureCredential()
client = SecretClient(vault_url=vault_url, credential=credential)

# Retrieve secret
secret = client.get_secret("DatabasePassword")
print(f"Secret value: {secret.value}")
```

Add to `.env`:

```
KEY_VAULT_URL=https://kv-az204-<unique>.vault.azure.net/
```

> `DefaultAzureCredential` works with Azure CLI login, managed identity, or environment variables.

---

## Step 4 – List and Update Secrets

```python
# List all secrets
for secret_props in client.list_properties_of_secrets():
    print(f"Secret: {secret_props.name}")

# Update a secret
client.set_secret("ApiKey", "new-api-key-67890")
print("Secret updated!")
```

---

## Step 5 – Use Key Vault References in App Service (Conceptual)

In App Service, you can reference Key Vault secrets directly:

```
@Microsoft.KeyVault(SecretUri=https://kv-az204-<unique>.vault.azure.net/secrets/DatabasePassword/)
```

This requires the App Service to have access to the Key Vault via managed identity.

---

## Cleanup

```bash
az group delete --name rg-az204-kv --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created an Azure Key Vault
- [ ] Added secrets via CLI
- [ ] Retrieved secrets using Python SDK and DefaultAzureCredential
- [ ] Listed and updated secrets programmatically
- [ ] Understood Key Vault references for App Service
- [ ] Cleaned up resources
