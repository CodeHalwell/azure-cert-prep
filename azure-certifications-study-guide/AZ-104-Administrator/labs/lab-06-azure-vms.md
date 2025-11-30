# Lab 06: Deploy and Configure Azure Virtual Machines

## 🎯 Lab Goal

Practice core **Azure VM** skills:

- Deploy a VM with correct sizing and networking
- Configure availability (availability set or zone, as supported)
- Connect and perform basic management tasks

This supports the **Deploy and manage Azure compute resources** domain of AZ‑104.

---

## ✅ Prerequisites

- Azure subscription or sandbox
- Rights to create VMs, NICs, public IPs, and NSGs

Recommended:

- SSH client (for Linux) or RDP client (for Windows)

---

## Step 1 – Create a Compute Resource Group and Network

1. Create a resource group `rg-az104-vm-lab` in your preferred region.
2. Create a virtual network `vnet-az104-vm` with:
	- Address space, e.g. `10.10.0.0/16`
	- Subnet `subnet-vm` with `10.10.1.0/24`

You can do this via the **Virtual networks** blade or the **VM creation wizard** (it can create these automatically).

---

## Step 2 – Deploy a Linux or Windows VM

From **Virtual machines → + Create → Azure virtual machine**:

1. Basics:
	- Resource group: `rg-az104-vm-lab`
	- VM name: `vm-az104-lab`
	- Region: same as VNet
	- Availability options: choose **Availability zone** or **Availability set** (create new) if available in region
	- Image: Ubuntu LTS or Windows Server (per your preference)
	- Size: `Standard_B2s` or similar small size
2. Administrator account:
	- For Linux: SSH public key recommended
	- For Windows: strong username/password
3. Inbound port rules:
	- Allow **SSH (22)** for Linux or **RDP (3389)** for Windows, but only for lab/testing.
4. Networking:
	- VNet: `vnet-az104-vm`
	- Subnet: `subnet-vm`
	- Public IP: create new (for lab)

Review and **Create**.

---

## Step 3 – Connect to the VM

After deployment:

1. From the VM overview, copy the **public IP address**.
2. Connect:
	- Linux: `ssh <username>@<public-ip>`
	- Windows: Use RDP client and the public IP
3. Verify you can sign in and run a simple command:
	- Linux: `uname -a`, `df -h`
	- Windows: Check Server Manager, disks, etc.

This demonstrates connectivity and basic VM management.

---

## Step 4 – Review VM Configuration

In the portal, for `vm-az104-lab`, review:

- **Size** and vCPU/RAM
- **Disks** (OS disk type, size, managed disk)
- **Networking** (NIC, NSG rules, public IP)
- **Availability** configuration (zone/availability set)

Make sure you understand how these components connect.

---

## Step 5 – Optional: Use Azure CLI to Query VM Info

```bash
az vm show \
  --name vm-az104-lab \
  --resource-group rg-az104-vm-lab \
  --show-details \
  --output table
```

Observe:

- Power state
- Public and private IP
- OS type and version

You can also **stop/deallocate** the VM via CLI to reduce costs:

```bash
az vm deallocate -g rg-az104-vm-lab -n vm-az104-lab
```

---

## Cleanup

- Stop/deallocate or delete the VM when not in use.
- Optionally delete the entire `rg-az104-vm-lab` resource group when you’re done:

```bash
az group delete --name rg-az104-vm-lab --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created a resource group and virtual network for VMs
- [ ] Deployed a Windows or Linux VM with appropriate size and availability configuration
- [ ] Connected to the VM via SSH or RDP
- [ ] Reviewed disks, networking, and availability configuration in the portal
- [ ] (Optional) Queried VM details and managed power state with Azure CLI
- [ ] Cleaned up VM and resource group when finished

