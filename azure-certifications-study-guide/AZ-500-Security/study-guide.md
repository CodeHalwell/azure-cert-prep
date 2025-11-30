# 📖 AZ-500 Study Guide

## Azure Security Engineer Associate

This study guide covers all skills measured in the AZ-500 exam.

---

# Domain 1: Manage Identity and Access (25-30%)

## 1.1 Microsoft Entra ID Security

### Authentication Methods

| Method | Security Level | Use Case |
|--------|---------------|----------|
| Password only | Low | Legacy (avoid) |
| MFA (SMS) | Medium | Basic protection |
| MFA (Authenticator) | High | Recommended |
| Passwordless (FIDO2) | Very High | Modern security |
| Certificate-based | Very High | Enterprise |

### Conditional Access Policies

```
┌─────────────────────────────────────────────────────────────┐
│                   Conditional Access Policy                  │
├─────────────────────────────────────────────────────────────┤
│  Assignments (WHO + WHAT):                                   │
│  ├── Users and groups                                        │
│  ├── Cloud apps or actions                                   │
│  └── Conditions:                                             │
│      ├── Sign-in risk                                        │
│      ├── Device platforms                                    │
│      ├── Locations                                           │
│      └── Client apps                                         │
├─────────────────────────────────────────────────────────────┤
│  Access Controls (THEN):                                     │
│  ├── Grant: Allow / Block / Require MFA                     │
│  └── Session: App enforced restrictions                     │
└─────────────────────────────────────────────────────────────┘
```

### Common Conditional Access Scenarios

| Scenario | Configuration |
|----------|---------------|
| Require MFA for admins | Users: Admin roles, Grant: Require MFA |
| Block legacy auth | Client apps: Other clients, Grant: Block |
| Require compliant device | Grant: Require compliant device |
| Location-based access | Conditions: Named locations, Grant: Block |

---

## 1.2 Privileged Identity Management (PIM)

### PIM Features

| Feature | Description |
|---------|-------------|
| **Just-in-time access** | Activate roles when needed |
| **Time-bound** | Automatic expiration |
| **Approval workflow** | Require approval for sensitive roles |
| **MFA on activation** | Additional verification |
| **Audit logs** | Track all activations |

### PIM Configuration

| Setting | Options |
|---------|---------|
| Maximum activation duration | 1-24 hours |
| Require justification | Yes/No |
| Require approval | Yes/No |
| Require MFA | Yes/No |
| Require ticket info | Yes/No |

---

## 1.3 Identity Protection

### Risk Levels

| Risk | Examples |
|------|----------|
| **Sign-in risk** | Anonymous IP, impossible travel, malware |
| **User risk** | Leaked credentials, unusual behavior |

### Risk-Based Policies

```
If sign-in risk = High:
    → Block access or Require MFA

If user risk = High:
    → Block access or Require password change
```

---

# Domain 2: Secure Networking (20-25%)

## 2.1 Network Security Groups

### NSG Rules

| Property | Description |
|----------|-------------|
| Priority | 100-4096 (lower = higher priority) |
| Source | IP, CIDR, service tag, ASG |
| Destination | IP, CIDR, service tag, ASG |
| Protocol | TCP, UDP, ICMP, Any |
| Action | Allow or Deny |

### Default Rules

| Rule | Priority | Description |
|------|----------|-------------|
| AllowVNetInBound | 65000 | Allow VNet traffic |
| AllowAzureLBInBound | 65001 | Allow load balancer |
| DenyAllInBound | 65500 | Deny all other inbound |

---

## 2.2 Azure Firewall

### Firewall Rule Types

| Type | Description |
|------|-------------|
| **NAT rules** | DNAT for inbound |
| **Network rules** | Layer 4 filtering |
| **Application rules** | FQDN filtering |

### Firewall Policy

```
┌─────────────────────────────────────────────────────────────┐
│                    Azure Firewall Policy                     │
├─────────────────────────────────────────────────────────────┤
│  Rule Collection Groups (Priority order):                    │
│  ├── DNAT Rule Collection (1000)                            │
│  │   └── Allow RDP from specific IP                         │
│  ├── Network Rule Collection (2000)                         │
│  │   └── Allow internal traffic                             │
│  └── Application Rule Collection (3000)                     │
│      └── Allow *.microsoft.com                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 2.3 Private Link

### Private Endpoint

```
VNet
├── Subnet A
│   └── VM (10.0.1.4)
└── Subnet B (Private Endpoints)
    └── Private Endpoint (10.0.2.5) ──► Azure Storage Account
                                         (privatelink.blob.core.windows.net)
```

### DNS Configuration

| Service | Private DNS Zone |
|---------|-----------------|
| Blob Storage | privatelink.blob.core.windows.net |
| SQL Database | privatelink.database.windows.net |
| Key Vault | privatelink.vaultcore.azure.net |
| Cosmos DB | privatelink.documents.azure.com |

---

# Domain 3: Secure Compute, Storage, Databases (20-25%)

## 3.1 VM Security

### Azure Disk Encryption

| Feature | Description |
|---------|-------------|
| **BitLocker** | Windows encryption |
| **DM-Crypt** | Linux encryption |
| **Key Vault** | Stores encryption keys |
| **Recovery** | Key escrow for recovery |

### Just-In-Time VM Access

| Feature | Description |
|---------|-------------|
| **Purpose** | Reduce attack surface |
| **Ports** | RDP, SSH, custom |
| **Duration** | Time-limited access |
| **Approval** | Optional workflow |

---

## 3.2 Storage Security

### Storage Account Security

| Feature | Description |
|---------|-------------|
| **Encryption at rest** | SSE with Microsoft or customer keys |
| **Encryption in transit** | HTTPS required |
| **Firewall** | IP and VNet rules |
| **Private endpoints** | Private connectivity |
| **SAS tokens** | Time-limited access |

### Shared Access Signatures

| SAS Type | Scope |
|----------|-------|
| Account SAS | Account-level access |
| Service SAS | Single service access |
| User delegation SAS | Entra ID-based (recommended) |

---

## 3.3 Azure Key Vault

### Key Vault Features

| Feature | Description |
|---------|-------------|
| **Secrets** | Passwords, connection strings |
| **Keys** | Cryptographic keys |
| **Certificates** | SSL/TLS certificates |
| **HSM-backed** | Hardware security modules |

### Access Policies vs RBAC

| Approach | Description |
|----------|-------------|
| Access policies | Vault-level permissions |
| RBAC | Resource-level, recommended |

---

## 3.4 SQL Security

### SQL Security Features

| Feature | Description |
|---------|-------------|
| **TDE** | Transparent Data Encryption |
| **Always Encrypted** | Column-level encryption |
| **Dynamic Data Masking** | Mask sensitive data |
| **Row-Level Security** | Filter rows by user |
| **Auditing** | Track database access |
| **Threat Detection** | Anomaly detection |

---

# Domain 4: Manage Security Operations (25-30%)

## 4.1 Microsoft Defender for Cloud

### Secure Score

| Category | Examples |
|----------|----------|
| Identity | MFA, PIM |
| Network | NSGs, firewall |
| Compute | Updates, encryption |
| Data | Storage security |
| Applications | App security |

### Defender Plans

| Plan | Protection |
|------|------------|
| Defender for Servers | VM protection |
| Defender for Containers | AKS security |
| Defender for Storage | Threat detection |
| Defender for SQL | Database protection |
| Defender for Key Vault | Vault monitoring |

---

## 4.2 Microsoft Sentinel

### Sentinel Components

```
┌─────────────────────────────────────────────────────────────┐
│                    Microsoft Sentinel                        │
├─────────────────────────────────────────────────────────────┤
│  Data Connectors ──► Log Analytics ──► Analytics Rules      │
│       │                    │                   │             │
│  (Azure AD, M365,     (Storage)         (Detection)         │
│   Defender, etc.)                             │              │
│                                               ▼              │
│                                          Incidents          │
│                                               │              │
│                                               ▼              │
│                                          Playbooks          │
│                                     (Logic Apps automation)  │
└─────────────────────────────────────────────────────────────┘
```

### Analytics Rules

| Rule Type | Description |
|-----------|-------------|
| Scheduled | Query runs on schedule |
| NRT | Near real-time detection |
| Fusion | ML-based correlation |
| Anomaly | Behavioral detection |

---

## ✅ Study Checklist

### Identity & Access
- [ ] Configure Conditional Access
- [ ] Implement PIM
- [ ] Set up Identity Protection
- [ ] Manage app registrations

### Networking
- [ ] Configure NSGs and ASGs
- [ ] Deploy Azure Firewall
- [ ] Implement Private Link
- [ ] Configure WAF

### Compute, Storage, Databases
- [ ] Enable disk encryption
- [ ] Configure JIT VM access
- [ ] Secure storage accounts
- [ ] Implement Key Vault
- [ ] Configure SQL security

### Security Operations
- [ ] Use Defender for Cloud
- [ ] Configure Sentinel
- [ ] Create analytics rules
- [ ] Set up playbooks

---

*Last updated: November 2025*
