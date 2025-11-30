# Lab 03: Implement Azure Policy

## 🎯 Lab Goal

Use **Azure Policy** to enforce and audit configuration across resources:

- Assign built-in policies to a resource group
- Review compliance results
- Understand deny vs. audit effects

This supports the **identity and governance** domain for AZ‑104.

---

## ✅ Prerequisites

- Azure subscription or sandbox
- Ability to assign policies at resource group scope
- A lab resource group (you can re‑use `rg-az104-rbac-lab` or create `rg-az104-policy-lab`)

---

## Step 1 – Create / Reuse a Lab Resource Group

1. In the portal, create `rg-az104-policy-lab` (or reuse an existing lab RG).
2. Ensure it is empty or only contains lab resources.

Optional CLI:

```bash
az group create --name rg-az104-policy-lab --location westeurope
```

---

## Step 2 – Assign a Built-In Policy

1. Open the resource group → **Policies** or **Azure Policy** blade.
2. Click **Assign policy**.
3. Choose a policy definition such as:
	- `Allowed locations` (restrict where resources can be created)
	- or `Audit VMs that do not use managed disks` (if available)
4. Set:
	- **Scope**: `rg-az104-policy-lab`
	- **Assignment name**: something descriptive, e.g. `rg-az104-allowed-locations`.
5. For `Allowed locations`, choose 1–2 allowed regions (e.g., `westeurope`).
6. Review and **Create** the assignment.

---

## Step 3 – Test the Policy (Deny Effect)

If you used **Allowed locations** with a **Deny** effect:

1. Inside `rg-az104-policy-lab`, attempt to create a resource (e.g., a storage account) in a **disallowed region**.
2. Observe the error message – it should reference policy.
3. Try again in an **allowed** region and confirm creation succeeds.

Understand:

- How policy evaluates requests **before** resources are created
- The difference between policy **definition** (rule) and **assignment** (scope + parameters)

---

## Step 4 – Review Compliance

1. Go to **Azure Policy** (global) → **Compliance**.
2. Filter by the scope of `rg-az104-policy-lab` or look for your assignment.
3. Review:
	- Overall compliance percentage
	- Number of compliant vs non‑compliant resources
4. Drill into non‑compliant resources (if any) and read the details.

If no resources exist yet, create a simple resource that **violates** or **satisfies** the policy and re‑evaluate.

---

## Step 5 – Try an Audit Policy (Optional)

1. Create or identify a resource that might violate a configuration (e.g., a storage account without secure transfer, depending on available built-in policies in your environment).
2. Assign an **Audit** policy to `rg-az104-policy-lab` that checks a configuration.
3. Wait for evaluation (can take several minutes) and revisit the **Compliance** tab.
4. Note the difference:
	- **Deny**: blocks non-compliant deployments
	- **Audit**: allows but flags resources

---

## Cleanup

- Delete or disable policy assignments you created for the lab.
- Optionally delete the `rg-az104-policy-lab` resource group:

```bash
az group delete --name rg-az104-policy-lab --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created or reused a resource group for policy testing
- [ ] Assigned at least one built-in policy at resource group scope
- [ ] Observed how a **Deny** policy prevents non-compliant deployment
- [ ] Reviewed compliance results in the Azure Policy blade
- [ ] (Optional) Assigned an **Audit** policy and saw how it flags resources
- [ ] Cleaned up policy assignments and (optionally) the lab resource group

