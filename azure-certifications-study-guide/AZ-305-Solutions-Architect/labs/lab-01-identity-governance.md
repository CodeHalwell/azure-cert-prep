# Lab 01: Design Identity and Governance Architecture

## 🎯 Lab Goal

Design a comprehensive **identity and governance architecture** for an enterprise:

- Evaluate Entra ID tenant structure
- Design RBAC and Azure Policy strategy
- Plan management group hierarchy

This supports the **Design identity, governance, and monitoring solutions** domain of AZ‑305.

---

## ✅ Prerequisites

- Azure subscription with Owner access
- Access to Microsoft Entra admin center

---

## Scenario

Contoso Ltd. is migrating to Azure and needs:
- Centralized identity management for 5,000 users
- Separate environments for Dev, Test, and Production
- Consistent security policies across all subscriptions
- Compliance with SOC 2 and GDPR requirements

---

## Step 1 – Evaluate Tenant Design

### Decision Points:

| Option | When to Use |
|--------|-------------|
| Single tenant | Most organizations; simplifies management |
| Multiple tenants | M&A scenarios, regulatory isolation |

### Recommendation for Contoso:

**Single tenant** with separate subscriptions per environment.

---

## Step 2 – Design Management Group Hierarchy

```
Root Management Group
├── Contoso-Platform
│   ├── Connectivity (hub networking)
│   └── Identity (domain controllers, Entra Connect)
└── Contoso-Workloads
    ├── Development
    │   └── dev-subscription
    ├── Test
    │   └── test-subscription
    └── Production
        └── prod-subscription
```

### Create structure:

```bash
az account management-group create --name Contoso-Root
az account management-group create --name Contoso-Platform --parent Contoso-Root
az account management-group create --name Contoso-Workloads --parent Contoso-Root
az account management-group create --name Development --parent Contoso-Workloads
az account management-group create --name Production --parent Contoso-Workloads
```

---

## Step 3 – Design RBAC Strategy

### Role Assignment Model:

| Scope | Role | Principal |
|-------|------|----------|
| Contoso-Root | Security Reader | Security Team |
| Contoso-Platform | Contributor | Platform Team |
| Development | Contributor | Dev Team |
| Production | Reader | Dev Team |
| Production | Contributor | Ops Team |

### Best Practices:

- Use **groups** for role assignments, not individuals
- Apply **least privilege** principle
- Use **custom roles** only when built-in roles are insufficient
- Enable **PIM** for privileged roles

```bash
# Example: Assign role to group at management group level
az role assignment create \
  --assignee-object-id <group-id> \
  --role "Reader" \
  --scope "/providers/Microsoft.Management/managementGroups/Contoso-Root"
```

---

## Step 4 – Design Azure Policy Strategy

### Recommended Policies:

| Policy | Scope | Effect |
|--------|-------|--------|
| Allowed locations | Contoso-Root | Deny |
| Require tags on resources | Contoso-Workloads | Deny |
| Allowed VM SKUs | Production | Deny |
| Audit VMs without managed disks | Contoso-Root | Audit |
| Deploy diagnostic settings | Contoso-Root | DeployIfNotExists |

### Create initiative:

```bash
az policy set-definition create \
  --name contoso-governance \
  --definitions '[{"policyDefinitionId":"/providers/Microsoft.Authorization/policyDefinitions/<policy-id>"}]'
```

---

## Step 5 – Design Document Template

Create an architecture decision document:

```markdown
# Identity & Governance Architecture – Contoso Ltd.

## 1. Tenant Design
- Single Entra ID tenant
- Entra Connect for hybrid identity

## 2. Management Group Structure
- [Diagram from Step 2]

## 3. RBAC Model
- [Table from Step 3]

## 4. Policy Assignments
- [Table from Step 4]

## 5. Compliance Requirements
- SOC 2: Audit logging, access reviews
- GDPR: Data residency policies, encryption
```

---

## ✅ Lab Checklist

- [ ] Evaluated single vs. multi-tenant design
- [ ] Designed management group hierarchy
- [ ] Created RBAC strategy using groups and least privilege
- [ ] Defined Azure Policy assignments for governance
- [ ] Documented architecture decisions
