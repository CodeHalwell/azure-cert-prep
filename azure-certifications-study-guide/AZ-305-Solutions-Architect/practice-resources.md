# 🧪 AZ-305 Practice Resources

## Official Microsoft Practice Assessment

The best way to prepare for the exam is with the official practice assessment.

### 📋 Microsoft Practice Assessment

| Resource | Details |
|----------|---------|
| **Link** | [AZ-305 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/practice/assessment?assessment-type=practice&assessmentId=15) |
| **Format** | Multiple choice, case studies |
| **Cost** | Free |
| **Questions** | 50+ questions |
| **Features** | Explanations, linked documentation |

**Benefits:**
- Experience actual exam format
- Learn from detailed explanations
- Identify knowledge gaps
- Practice case study analysis

---

## 🎓 Exam Sandbox

Practice the exam interface before test day.

| Resource | Link |
|----------|------|
| Exam Sandbox | [Take Demo Exam](https://aka.ms/examdemo) |

**What to practice:**
- Case study navigation
- Question types
- Time management
- Review and marking features

---

## ☁️ Hands-On Practice

### Azure Free Account

| Feature | Details |
|---------|---------|
| **Link** | [Create Free Account](https://azure.microsoft.com/free/) |
| **Credit** | $200 for 30 days |
| **Free Services** | 55+ always free services |
| **Duration** | 12 months for popular services |

### Microsoft Learn Sandbox

| Feature | Details |
|---------|---------|
| **Activation** | Included in Learn modules |
| **Cost** | Free |
| **Duration** | 4 hours per session |
| **Requires** | Microsoft account |

---

## 📚 Case Study Practice

The AZ-305 exam includes case studies. Practice analyzing scenarios.

### Case Study Format

| Component | Description |
|-----------|-------------|
| **Overview** | Business background and requirements |
| **Current Environment** | Existing infrastructure |
| **Requirements** | Technical and business needs |
| **Questions** | Design decisions based on case |

### Sample Case Study Topics

| Topic | Focus Areas |
|-------|-------------|
| E-commerce Platform | Scalability, global distribution, DR |
| Healthcare System | Compliance, security, hybrid identity |
| Manufacturing IoT | Event processing, real-time analytics |
| Financial Services | High availability, security, compliance |
| Media Streaming | CDN, global distribution, caching |

---

## 📊 Knowledge Check Questions

### Domain 1: Identity, Governance, and Monitoring

1. **When would you use a centralized vs. distributed Log Analytics workspace?**
2. **How do you design Conditional Access for Zero Trust?**
3. **What is the difference between Azure Policy and RBAC?**
4. **When should you use Privileged Identity Management?**
5. **How do you design a management group hierarchy?**

### Domain 2: Data Storage

1. **When would you choose Cosmos DB over Azure SQL?**
2. **How do you select the right Cosmos DB consistency level?**
3. **When should you use GRS vs. GZRS replication?**
4. **How do you design a data lake architecture?**
5. **When would you use Data Factory vs. Synapse pipelines?**

### Domain 3: Business Continuity

1. **How do you calculate composite SLAs?**
2. **When would you use Azure Site Recovery vs. geo-replication?**
3. **How do you design for different RTO/RPO requirements?**
4. **What is the difference between availability sets and zones?**
5. **When would you use Traffic Manager vs. Front Door?**

### Domain 4: Infrastructure

1. **When would you choose AKS vs. Container Apps?**
2. **How do you design a hub-spoke network architecture?**
3. **When should you use ExpressRoute vs. VPN Gateway?**
4. **How do you select the right App Service plan?**
5. **When would you use Azure Functions vs. Logic Apps?**

---

## 🏗️ Architecture Design Exercises

### Exercise 1: E-commerce Platform

**Requirements:**
- Global customer base
- High availability (99.99%)
- Auto-scaling during sales events
- Secure payment processing

**Design considerations:**
- Multi-region deployment
- Azure Front Door for global load balancing
- Cosmos DB for product catalog
- Azure Cache for Redis
- Azure Key Vault for secrets

### Exercise 2: Enterprise Data Platform

**Requirements:**
- Centralized data lake
- Real-time and batch processing
- Data governance and lineage
- Self-service analytics

**Design considerations:**
- Azure Data Lake Storage Gen2
- Azure Synapse Analytics
- Microsoft Purview
- Power BI

### Exercise 3: Hybrid Identity

**Requirements:**
- Sync with on-premises AD
- MFA for all users
- Conditional Access
- B2B for partners

**Design considerations:**
- Azure AD Connect
- Conditional Access policies
- Privileged Identity Management
- Azure AD B2B

---

## 📋 Design Checklists

### Identity Design Checklist

- [ ] Define identity source (cloud-only, hybrid)
- [ ] Plan authentication methods
- [ ] Design Conditional Access policies
- [ ] Plan privileged access management
- [ ] Design guest access strategy

### Storage Design Checklist

- [ ] Select storage types for each workload
- [ ] Choose redundancy options
- [ ] Plan access tiers and lifecycle
- [ ] Design security and access control
- [ ] Plan data protection and backup

### Network Design Checklist

- [ ] Design IP addressing scheme
- [ ] Plan VNet topology (hub-spoke)
- [ ] Design connectivity (VPN, ExpressRoute)
- [ ] Plan DNS and name resolution
- [ ] Design network security (NSG, firewall)

### Compute Design Checklist

- [ ] Select compute services for each workload
- [ ] Plan sizing and scaling
- [ ] Design high availability
- [ ] Plan deployment strategy
- [ ] Design monitoring and diagnostics

---

## 🎯 Study Tips

### Before the Exam

| Tip | Details |
|-----|---------|
| **Complete all learning paths** | Focus on architecture concepts |
| **Practice case studies** | Analyze requirements carefully |
| **Use Azure free account** | Build sample architectures |
| **Review reference architectures** | Azure Architecture Center |
| **Understand trade-offs** | Cost, performance, availability |

### Exam Day Tips

| Tip | Details |
|-----|---------|
| **Read case studies carefully** | Take notes on key requirements |
| **Consider all constraints** | Budget, compliance, existing infra |
| **Think about trade-offs** | There's rarely a perfect answer |
| **Manage time wisely** | Case studies take longer |
| **Review marked questions** | Use all available time |

---

## 📖 Additional Resources

### Architecture Center

| Resource | Link |
|----------|------|
| Reference Architectures | [Link](https://learn.microsoft.com/en-us/azure/architecture/browse/) |
| Design Patterns | [Link](https://learn.microsoft.com/en-us/azure/architecture/patterns/) |
| Best Practices | [Link](https://learn.microsoft.com/en-us/azure/architecture/best-practices/) |
| Cloud Design Patterns | [Link](https://learn.microsoft.com/en-us/azure/architecture/patterns/) |

### Frameworks

| Resource | Link |
|----------|------|
| Well-Architected Framework | [Link](https://learn.microsoft.com/en-us/azure/well-architected/) |
| Cloud Adoption Framework | [Link](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/) |
| Azure Security Benchmark | [Link](https://learn.microsoft.com/en-us/security/benchmark/azure/) |

### Community Resources

| Resource | Description |
|----------|-------------|
| Microsoft Q&A | Official community forum |
| Stack Overflow | Azure-tagged questions |
| Reddit r/Azure | Community discussions |
| Azure GitHub | Sample architectures |

---

## ⏰ Recommended Study Timeline

### 10-Week Plan

| Week | Focus | Practice |
|------|-------|----------|
| 1 | Prerequisites review | Setup Azure account |
| 2-3 | Identity & Governance | Design exercises |
| 4-5 | Data Storage | Architecture labs |
| 6 | Business Continuity | DR design exercises |
| 7-8 | Infrastructure | Network/compute labs |
| 9 | Case Studies | Practice assessments |
| 10 | Final Review | Full practice exams |

---

*Last updated: November 2025*
