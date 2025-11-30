# Lab 08: Configure Virtual Networks and Network Security Groups

## 🎯 Lab Goal

Configure core **virtual networking** components:

- Virtual networks and subnets
- Network security groups (NSGs)
- Basic connectivity tests

This supports the **Configure and manage virtual networking** domain of AZ‑104.

---

## ✅ Prerequisites

- Azure subscription or sandbox
- Ability to create VNets, subnets, NSGs, and small VMs

---

## Step 1 – Create a Virtual Network with Multiple Subnets

1. In the portal, go to **Virtual networks → + Create**.
2. Configure:
	- Name: `vnet-az104-lab`
	- Resource group: `rg-az104-network-lab`
	- Address space: `10.20.0.0/16`
3. Under **IP addresses**, create subnets:
	- `subnet-front` with `10.20.1.0/24`
	- `subnet-back` with `10.20.2.0/24`
4. Create the VNet.

---

## Step 2 – Deploy Two Test VMs (Optional but Valuable)

You can deploy small VMs to test connectivity (reuse patterns from Lab 06):

1. VM1:
	- Name: `vm-front`
	- Subnet: `subnet-front`
2. VM2:
	- Name: `vm-back`
	- Subnet: `subnet-back`

Assign NSGs as needed (next step).

---

## Step 3 – Create and Associate Network Security Groups

1. Go to **Network security groups → + Create**.
2. Create `nsg-front` in `rg-az104-network-lab`.
3. After creation, under **Settings → Inbound security rules**, ensure there is a rule allowing SSH/RDP from your IP (if you intend to connect) and default rules.
4. Associate `nsg-front` with `subnet-front` (or directly with `vm-front` NIC).

Repeat as needed to create `nsg-back` and associate with `subnet-back` or `vm-back`.

---

## Step 4 – Lock Down Back-End Traffic

In `nsg-back`:

1. Add an inbound rule to **deny** traffic from the internet on common ports (e.g., 80, 443, 22/3389), keeping only needed internal traffic.
2. Allow traffic from `subnet-front` to `subnet-back` on a specific port if desired.

Understand how NSG rules are evaluated (priority, allow/deny, first match wins).

---

## Step 5 – Verify Effective Security Rules

1. For `vm-back` NIC or subnet, open **Effective security rules** in the portal.
2. Review how rules from NSGs and default system rules combine.
3. Confirm that unwanted inbound internet traffic is blocked.

Optionally, if you deployed VMs and can connect, test connectivity:

- From `vm-front` to `vm-back` on allowed ports
- From your machine to `vm-back` and confirm blocked access as configured

---

## Cleanup

- Delete test VMs
- Delete the resource group `rg-az104-network-lab`:

```bash
az group delete --name rg-az104-network-lab --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created a VNet with multiple subnets
- [ ] (Optional) Deployed test VMs into different subnets
- [ ] Created and associated NSGs to subnets or NICs
- [ ] Configured NSG rules to control inbound traffic
- [ ] Reviewed effective security rules to understand final behavior
- [ ] Cleaned up networking resources and lab VMs

