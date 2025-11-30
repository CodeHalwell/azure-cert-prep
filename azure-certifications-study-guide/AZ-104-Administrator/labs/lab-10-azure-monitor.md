# Lab 10: Configure Azure Monitor and Alerts

## 🎯 Lab Goal

Use **Azure Monitor** to:

- Enable and explore metrics and logs
- Create alerts based on resource health or usage

This supports the **Monitor and maintain Azure resources** domain of AZ‑104.

---

## ✅ Prerequisites

- Azure subscription or sandbox
- At least one existing resource to monitor (e.g., storage account, VM, or scale set from previous labs)

---

## Step 1 – Explore Metrics for a Resource

1. Pick a resource such as a VM or storage account.
2. In the resource blade, go to **Metrics**.
3. Select a metric (examples):
	- VM: `Percentage CPU`
	- Storage: `Total egress`, `Transactions`
4. Adjust **Time range** and **Aggregation**.
5. Add a second metric or filter by dimension if available.

Understand how metrics are used for alerting and capacity planning.

---

## Step 2 – Configure Activity Log Alerts

1. In the portal search, open **Activity log**.
2. Filter for your subscription and recent operations (e.g., `Create`, `Delete`).
3. Click **+ New alert rule** from an example event.
4. Configure:
	- Scope: subscription or resource group
	- Condition: Activity log signal (e.g., `Administrative` / `Delete Resource`)
	- Action group: create a simple one (email, if allowed)
	- Alert rule name: `az104-activity-delete-alert`
5. Create the rule.

Now, when a matching event occurs, an alert will fire.

---

## Step 3 – Create a Metric Alert (e.g., CPU)

1. Go to **Monitor → Alerts → + Create → Alert rule**.
2. Scope: select a VM or VM scale set.
3. Condition:
	- Signal: `Percentage CPU`
	- Condition: `Greater than` 70%
	- Aggregation: Average over last 5 or 10 minutes
4. Action:
	- Reuse or create an **action group** (email, SMS, etc.)
5. Give the alert a name such as `az104-cpu-high` and create it.

Understand that in a small lab, you may not generate enough load to trigger the alert, but configuration is what matters for AZ‑104.

---

## Step 4 – (Optional) Enable Diagnostic Settings for Logs

1. For a resource like a storage account or key resource group, open **Diagnostic settings**.
2. Add a diagnostic setting that sends logs and/or metrics to:
	- A Log Analytics workspace (preferred)
	- Or a storage account/event hub
3. Choose relevant log categories (e.g., `Read`, `Write`, `Delete`).

This step introduces you to the idea of centralizing logs for query with **Log Analytics**.

---

## Cleanup

- Disable or delete test alert rules when done.
- Remove diagnostic settings if they were only for lab purposes.

---

## ✅ Lab Checklist

- [ ] Explored metrics for at least one Azure resource
- [ ] Configured an Activity log alert rule
- [ ] Configured a metric-based alert (e.g., CPU)
- [ ] (Optional) Enabled diagnostic settings to send logs to a central destination
- [ ] Cleaned up alert rules and diagnostic settings as appropriate

