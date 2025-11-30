# Lab 09: Configure Azure Load Balancing Solutions

## 🎯 Lab Goal

Work with **Azure load balancing** options to:

- Configure a basic Azure Load Balancer
- Understand backend pools, probes, and rules

This supports the **virtual networking** and **compute** domains of AZ‑104.

---

## ✅ Prerequisites

- Azure subscription or sandbox
- Ability to deploy small VMs and networking resources

Ideally, complete Lab 06 (VMs) and Lab 08 (VNets/NSGs) first.

---

## Step 1 – Prepare Two Backend VMs

1. In a lab resource group (e.g., `rg-az104-lb-lab`), deploy two small VMs:
	- `vm-app1`
	- `vm-app2`
2. Place them in the same subnet and VNet.
3. Ensure they have an NSG that allows required inbound traffic **from the load balancer** (typically port 80).

On each VM, you can optionally configure a simple web server (e.g., `nginx` or IIS) with different index pages to distinguish traffic.

---

## Step 2 – Create a Public Load Balancer

1. In the portal, go to **Load balancers → + Create**.
2. Configure:
	- Name: `lb-az104-lab`
	- Type: **Public**
	- SKU: Basic or Standard (Standard recommended for production; know differences conceptually)
	- Frontend IP: create new public IP
3. Create the load balancer in `rg-az104-lb-lab` and the same region/VNet as your VMs.

---

## Step 3 – Configure Backend Pool and Health Probe

1. In `lb-az104-lab`, go to **Backend pools → + Add**:
	- Name: `bepool-vms`
	- Add both `vm-app1` and `vm-app2` NICs.
2. In **Health probes → + Add**:
	- Name: `hp-http`
	- Protocol: HTTP
	- Port: 80
	- Path: `/` (or a simple health path)

The health probe determines which instances are considered healthy.

---

## Step 4 – Create a Load Balancing Rule

1. In **Load balancing rules → + Add**:
	- Name: `lbr-http`
	- Frontend IP: the public frontend
	- Backend pool: `bepool-vms`
	- Protocol: TCP
	- Port: 80
	- Backend port: 80
	- Health probe: `hp-http`
	- Session persistence: None (for this lab)
2. Save the rule.

---

## Step 5 – Test Load Balancing

1. From your browser or `curl`, access the **public IP** of the load balancer:
	- `http://<lb-public-ip>/`
2. Refresh several times.

If you customized responses on each VM (e.g., different messages on the default web page), you should see requests being distributed between `vm-app1` and `vm-app2`.

Understand:

- How the load balancer uses probes and rules to route traffic
- Difference between backend pool membership and health

---

## Cleanup

- Delete the load balancer and public IP.
- Delete backend VMs and the resource group `rg-az104-lb-lab`:

```bash
az group delete --name rg-az104-lb-lab --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Deployed at least two VMs to act as backend targets
- [ ] Created a public Azure Load Balancer with frontend IP
- [ ] Configured a backend pool and HTTP health probe
- [ ] Created a load balancing rule for HTTP traffic
- [ ] Verified that traffic is distributed across backend VMs
- [ ] Cleaned up load balancer and VM resources

