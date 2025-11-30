# Lab 09: Protect and Publish APIs with Azure API Management

## 🎯 Lab Goal

Use **Azure API Management** to:

- Import and publish an API
- Apply policies (rate limiting, transformation)
- Secure with subscription keys

This supports the **Implement API Management** domain of AZ‑204.

---

## ✅ Prerequisites

- Azure subscription
- A backend API (can use a public API like https://httpbin.org)

---

## Step 1 – Create an API Management Instance

```bash
az group create --name rg-az204-apim --location eastus

az apim create \
  --name apim-az204-<unique> \
  --resource-group rg-az204-apim \
  --publisher-email admin@contoso.com \
  --publisher-name Contoso \
  --sku-name Consumption
```

> Consumption tier deploys quickly; Developer/Standard take 30+ minutes.

---

## Step 2 – Import an API

1. In the portal, go to your APIM instance → **APIs**.
2. Click **+ Add API → HTTP**.
3. Configure:
   - Display name: `HTTPBin API`
   - Web service URL: `https://httpbin.org`
   - API URL suffix: `httpbin`
4. Add operations manually or import from OpenAPI.

Add an operation:
- Name: `Get IP`
- URL: GET `/ip`

---

## Step 3 – Test the API

1. Go to the **Test** tab for your API.
2. Select the `Get IP` operation.
3. Click **Send** and verify the response.

---

## Step 4 – Apply Policies

Add a rate limiting policy:

1. Go to **Design → Inbound processing → + Add policy**.
2. Choose **rate-limit** and configure:

```xml
<rate-limit calls="5" renewal-period="60" />
```

Add a response header:

```xml
<outbound>
    <set-header name="X-Custom-Header" exists-action="override">
        <value>AZ204Lab</value>
    </set-header>
</outbound>
```

---

## Step 5 – Secure with Subscription Keys

1. Go to **Subscriptions → + Add subscription**.
2. Create a subscription for the HTTPBin API.
3. Copy the subscription key.
4. Test the API with the header:

```bash
curl -H "Ocp-Apim-Subscription-Key: <your-key>" \
  https://apim-az204-<unique>.azure-api.net/httpbin/ip
```

---

## Cleanup

```bash
az group delete --name rg-az204-apim --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created an API Management instance
- [ ] Imported or created an API with operations
- [ ] Tested the API in the portal
- [ ] Applied rate limiting and header transformation policies
- [ ] Secured the API with subscription keys
- [ ] Cleaned up resources
