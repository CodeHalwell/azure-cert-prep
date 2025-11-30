# Lab 07: Configure Virtual Machine Scale Sets

## 🎯 Lab Goal

Deploy and manage a **Virtual Machine Scale Set (VMSS)** to:

- Automatically scale based on CPU usage
- Distribute traffic via a load balancer

This reinforces the **compute** and **availability** aspects of AZ‑104.

---

## ✅ Prerequisites

- Azure subscription or sandbox
- Rights to create VMs, scale sets, load balancers

You should be comfortable with single VM deployment (Lab 06).

---

## Step 1 – Create a Scale Set

1. In the portal, search **Virtual machine scale sets** → **+ Create**.
2. Basics:
	- Resource group: `rg-az104-vmss-lab`
	- Name: `vmss-az104-lab`
	- Region: choose a region that supports zones if possible
	- Orchestration mode: **Uniform**
	- Image: Ubuntu LTS or Windows Server
	- Size: `Standard_B2s` or similar
3. Instances:
	- Initial instance count: 2
4. Disks: keep defaults (managed OS disk)

Networking:

- Create or select a VNet and subnet
- Enable **Load balancing** with an Azure Load Balancer (new)

Scaling:

- Enable **Autoscale** with a simple rule (we’ll configure next).

Review and **Create**.

---

## Step 2 – Configure Autoscale Rules

1. Go to the scale set → **Scaling**.
2. Configure autoscale based on **CPU percentage**, for example:
	- Default instance count: 2
	- Scale out: if average CPU > 75% for 10 minutes, add 1 instance (max 5)
	- Scale in: if average CPU < 30% for 10 minutes, remove 1 instance (min 2)
3. Save the autoscale settings.

Understand that in a real environment, load generation is required to see scaling in action; conceptually, you must know how to configure.

---

## Step 3 – Review Load Balancer Configuration

From the scale set or directly from **Load balancers**:

1. Open the automatically created load balancer.
2. Review:
	- **Frontend IP configuration**
	- **Backend pool** (scale set instances)
	- **Health probe**
	- **Load balancing rule** (e.g., port 80)

Understand how the load balancer distributes incoming traffic across VM instances in the scale set.

---

## Step 4 – Connect to an Instance (Optional)

For Linux, you can enable **SSH** in the VM profile or use **Run command** in the portal.

1. In the scale set, go to **Instances**.
2. Select an instance and explore:
	- Disk
	- Network
	- Effective security rules

Optionally, **upgrade** the scale set model (e.g., change size or image) and apply it to instances to see how updates roll out.

---

## Cleanup

- Delete the scale set and related resources by deleting the resource group `rg-az104-vmss-lab`:

```bash
az group delete --name rg-az104-vmss-lab --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created a VM scale set with at least 2 instances
- [ ] Enabled load balancing via an Azure Load Balancer
- [ ] Configured basic autoscale rules based on CPU
- [ ] Reviewed frontend, backend pool, probes, and rules on the load balancer
- [ ] (Optional) Inspected or connected to individual instances
- [ ] Deleted the lab resource group when finished

