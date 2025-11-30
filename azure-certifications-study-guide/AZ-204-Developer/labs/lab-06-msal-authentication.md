# Lab 06: Implement Authentication with MSAL and Entra ID

## 🎯 Lab Goal

Implement **user authentication** using MSAL and Microsoft Entra ID:

- Register an app in Entra ID
- Acquire tokens using MSAL
- Call a protected API

This supports the **Implement user authentication and authorization** domain of AZ‑204.

---

## ✅ Prerequisites

- Azure subscription with Entra ID access
- Python 3.9+ with `msal` package

```bash
pip install msal requests python-dotenv
```

---

## Step 1 – Register an Application in Entra ID

1. Go to **Microsoft Entra ID → App registrations → + New registration**.
2. Name: `az204-msal-app`
3. Supported account types: Single tenant (or as needed)
4. Redirect URI: `http://localhost` (Public client/native)
5. After creation, note:
   - **Application (client) ID**
   - **Directory (tenant) ID**

---

## Step 2 – Configure API Permissions

1. In the app registration, go to **API permissions**.
2. Add permission: **Microsoft Graph → User.Read** (delegated).
3. Grant admin consent if required.

---

## Step 3 – Acquire Token Using Device Code Flow

```python
import os
from dotenv import load_dotenv
import msal

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
TENANT_ID = os.getenv("TENANT_ID")
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["User.Read"]

app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY)

# Device code flow
flow = app.initiate_device_flow(scopes=SCOPES)
print(flow["message"])

result = app.acquire_token_by_device_flow(flow)

if "access_token" in result:
    print("Token acquired!")
    print(f"Access token: {result['access_token'][:50]}...")
else:
    print(f"Error: {result.get('error_description')}")
```

Add to `.env`:

```
CLIENT_ID=<your-client-id>
TENANT_ID=<your-tenant-id>
```

---

## Step 4 – Call Microsoft Graph API

```python
import requests

if "access_token" in result:
    headers = {"Authorization": f"Bearer {result['access_token']}"}
    response = requests.get(
        "https://graph.microsoft.com/v1.0/me",
        headers=headers
    )
    user = response.json()
    print(f"Hello, {user['displayName']}!")
```

---

## Step 5 – Token Caching (Conceptual)

MSAL provides built-in token caching:

```python
# Check cache first
accounts = app.get_accounts()
if accounts:
    result = app.acquire_token_silent(SCOPES, account=accounts[0])
```

This avoids re-authentication when tokens are still valid.

---

## Cleanup

- Delete the app registration from Entra ID if no longer needed.

---

## ✅ Lab Checklist

- [ ] Registered an application in Microsoft Entra ID
- [ ] Configured API permissions for Microsoft Graph
- [ ] Acquired an access token using MSAL device code flow
- [ ] Called Microsoft Graph API with the token
- [ ] Understood token caching concepts
