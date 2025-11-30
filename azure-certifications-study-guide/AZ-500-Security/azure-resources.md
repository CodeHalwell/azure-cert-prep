# 🔧 AZ-500 Azure Resources Reference

Deep-dive reference for security-focused Azure services in AZ-500: capabilities, built-ins, limits, and where customization is required.

---

## 📋 Table of Contents

1. Identity & Access Security
   - Microsoft Entra ID (Security Features)
   - Conditional Access & Identity Protection
   - Privileged Identity Management (PIM)
2. Network Security
   - Network Security Groups (NSG) & ASG
   - Azure Firewall
   - Web Application Firewall (App Gateway / Front Door)
   - DDoS Protection
3. Compute & Data Protection
   - Disk & Storage Encryption
   - Azure Key Vault
   - Just-In-Time VM Access
   - SQL & Data Security
4. Threat Protection & SIEM
   - Microsoft Defender for Cloud
   - Defender for Servers, Storage, SQL, Key Vault, Containers
   - Microsoft Sentinel
5. Governance & Compliance
   - Azure Policy
   - Security Center Recommendations & Secure Score

---

# 1. Identity & Access Security

## 1.1 Microsoft Entra ID Security

### Built-in Security Features

| Feature | License | Description |
|---------|---------|-------------|
| Security defaults | Free | Baseline MFA & protections |
| Conditional Access | P1+ | Dynamic access controls |
| Identity Protection | P2 | Risk-based policies |
| PIM | P2 | Just-in-time privileged access |
| Access Reviews | P2 | Regular entitlement reviews |

### What You Can Do

- Enforce MFA, passwordless, and strong authentication
- Implement **Zero Trust** controls (verify explicitly, least privilege)
- Detect risky sign-ins and risky users via Identity Protection

### Requires Customization

- Conditional Access policy design (by group, app, risk, location, device)
- Risk-based policies (block vs require password reset/MFA)
- Role design using custom roles and PIM eligibility rules

---

## 1.2 Conditional Access

### Capabilities

- Assign conditions by **user/group, app, risk, location, device state, client apps**
- Enforce controls like **MFA, compliant device, hybrid joined, terms of use**

### Built-in Templates

- Baseline templates for common scenarios (protect admins, protect all users, etc.)

### Requires Customization

- Exclusions for break-glass accounts
- Per-application or per-group policies for fine-grain control

---

## 1.3 Privileged Identity Management (PIM)

### Built-in

- Just-in-time activation for roles
- Approval workflows
- Activation MFA & justification
- Access reviews and alerts

### Design Considerations

- Which roles should be **eligible** vs **permanent**
- Activation durations, approvers, and incident response

---

# 2. Network Security

## 2.1 NSG & Application Security Groups

- As in AZ-104, but AZ-500 expects **secure-by-default rule sets**
- Use **ASGs** to group VMs by workload instead of raw IPs

### Best Practices

- Deny by default, explicit allow rules
- Use service tags for Microsoft services instead of IP lists

---

## 2.2 Azure Firewall

### Built-in Capabilities

| Capability | Description |
|------------|-------------|
| L3/L4 filtering | Network rules |
| L7 FQDN filtering | Application rules |
| DNAT/SNAT | NAT rules |
| Threat intelligence | Known malicious IPs/domains |
| TLS inspection (Premium) | Deep packet inspection |

### Requires Customization

- Rule collection groups (by environment or app)
- Logging to Log Analytics and building analytics queries
- Central firewall-in-hub design and routing

---

## 2.3 Web Application Firewall (WAF)

### Deployment Options

| Option | Platform |
|--------|----------|
| WAF on Application Gateway | Regional |
| WAF on Azure Front Door | Global |

### Built-in

- Core rule sets (OWASP)
- Bot protection features
- Managed rule sets with automatic updates

### Requires Customization

- Custom rules (Geo-blocking, IP allow/block lists)
- Exclusions for legitimate traffic that triggers false positives

---

## 2.4 DDoS Protection

### Basic vs Standard

- **Basic:** Always on, free, platform-level
- **Standard:** Per-VNet, telemetry, cost protection, advanced mitigation

### When to Use Standard

- Internet-facing critical workloads with strict uptime and SLA requirements

---

# 3. Compute & Data Protection

## 3.1 Disk & Storage Encryption

### Disk Encryption

- **Built-in:** SSE with Microsoft-managed keys (default)
- **Customization:** Customer-managed keys via Key Vault, double encryption

### Storage Encryption

- All data encrypted at rest with SSE
- Optional CMK for stricter compliance

---

## 3.2 Azure Key Vault

Security-focused view (see also AZ-305):

- Store **secrets**, **keys**, **certificates** with fine-grained RBAC
- Support for **HSM-backed keys** (Premium tier)

### Built-in

- Soft delete, purge protection (should be enabled)
- Logging to Azure Monitor for all operations

### Requires Customization

- Separation of duties: separate vaults/permissions for app vs ops
- Network isolation via private endpoints
- Key rotation and lifecycle policies

---

## 3.3 Just-In-Time VM Access

### What It Does

- Locks down RDP/SSH ports by default, allows **time-limited access**

### Built-in

- Defender for Cloud integration
- Configurable port, duration, and requester

### Requires Customization

- Approval workflows
- Policy definitions to enforce JIT on all VMs

---

## 3.4 SQL & Data Security

### SQL Database Security Features

| Feature | Description |
|---------|-------------|
| TDE | Encrypts data at rest |
| Always Encrypted | Client-side encryption for sensitive columns |
| Dynamic Data Masking | Masks data in query results |
| Row-Level Security | Filters rows based on user context |
| Auditing & Threat Detection | Logs and alerts |

### Requires Customization

- Classification and labeling of sensitive columns
- Auditing destinations and retention

---

# 4. Threat Protection & SIEM

## 4.1 Microsoft Defender for Cloud

### Scope

- CSPM (Cloud Security Posture Management)
- Defender plans for servers, storage, containers, SQL, Key Vault, etc.

### Built-in

- Secure score
- Recommendations
- Regulatory compliance dashboards

### Requires Customization

- Tailoring recommendations to your risk appetite
- Enabling specific Defender plans based on workload
- Auto-provisioning of agents (Log Analytics, Defender agents)

---

## 4.2 Defender Plans

| Plan | Protects |
|------|----------|
| Defender for Servers | Azure/Hybrid servers |
| Defender for Storage | Blob and file storage |
| Defender for SQL | Azure SQL, SQL on VMs |
| Defender for Containers | AKS, registries |
| Defender for Key Vault | Vault operations |

Each plan has **built-in detections** but often needs:
- Tuning for alert noise
- Integration with SIEM (Sentinel)

---

## 4.3 Microsoft Sentinel

### What You Can Do

- Cloud-native SIEM and SOAR
- Ingest and correlate logs from Azure, Microsoft 365, on-prem, other clouds

### Built-in

- Data connectors (Defender, Entra ID, Office 365, AWS, etc.)
- Analytics rule templates
- Workbooks and dashboards
- Playbook templates (Logic Apps)

### Requires Customization

- Custom analytics rules and hunting queries (KQL)
- Incident triage and automation playbooks
- Data retention and cost management strategy

---

# 5. Governance & Compliance

## 5.1 Azure Policy for Security

- Enforce **required security configurations** (e.g., require encryption, restrict locations)
- Use **initiative definitions** like built-in security baselines

## 5.2 Secure Score & Recommendations

- Central view of security posture
- Helps prioritize remediation based on risk impact

---

*Last updated: November 2025*