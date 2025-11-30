# Lab 07: Publish an Agent to Microsoft Teams

## 🎯 Lab Goal

**Publish your agent** to Microsoft Teams:

- Configure Teams channel
- Publish and deploy the agent
- Manage agent availability

This supports the **Deploy agents** domain of MS‑102.

---

## ✅ Prerequisites

- Completed agent from Labs 05-06
- Teams admin access (for organization-wide deployment)

---

## Step 1 – Prepare Agent for Publishing

1. Open your agent in Copilot Studio.
2. Review:
   - All topics are complete
   - Knowledge sources are configured
   - Actions are tested
3. Click **Publish** to save the current version.

---

## Step 2 – Configure Teams Channel

1. Go to **Channels** in the left navigation.
2. Click **Microsoft Teams**.
3. Configure:
   - **Turn on Teams**: Enable the toggle

---

## Step 3 – Customize Teams Experience

### Bot Details:

1. Configure:
   - **App name**: IT Help Desk
   - **Short description**: Get IT help quickly
   - **Long description**: Detailed description of capabilities
   - **Developer name**: Contoso IT
   - **Website**: Company intranet URL
   - **Privacy policy**: Link to privacy policy
   - **Terms of use**: Link to terms

### App Icon:

1. Upload icons:
   - **Color icon**: 192x192 px (full color)
   - **Outline icon**: 32x32 px (single color)

---

## Step 4 – Configure Availability

### Options:

| Option | Scope |
|--------|-------|
| Show in Teams store | Users discover in app catalog |
| Direct link | Share link directly |
| Pre-install for users | Admin deploys to users |

### For Immediate Access:

1. Click **Open bot in Teams** to test.
2. Copy the **Direct link** to share with users.

---

## Step 5 – Submit to Teams Admin

### For Organization-Wide Deployment:

1. Click **Submit for admin approval**.
2. This sends the app to Teams admin center.

### In Teams Admin Center:

1. Go to **Teams admin center → Teams apps → Manage apps**.
2. Find the pending agent.
3. Review and **Approve** the app.

---

## Step 6 – Configure App Policies

### Permission Policy:

1. Go to **Teams admin center → Permission policies**.
2. Create or edit a policy.
3. Under **Custom apps**, allow your agent.
4. Assign policy to users/groups.

### Setup Policy (Pre-Install):

1. Go to **Setup policies**.
2. Create or edit a policy.
3. Click **+ Add apps**.
4. Search for and add your agent.
5. Configure:
   - **Pinned**: Add to sidebar
   - **Installed**: Install for users
6. Assign to users/groups.

---

## Step 7 – Test in Teams

### As a User:

1. Open Microsoft Teams.
2. Go to **Apps** and search for "IT Help Desk".
3. Click **Add**.
4. Start a conversation:

```
User: Hello
Agent: Welcome! I'm the IT Help Desk assistant. How can I help?

User: I need to reset my password
Agent: [Follows password reset topic flow]
```

### Verify Features:

- [ ] Agent responds correctly
- [ ] Topics trigger properly
- [ ] Actions execute successfully
- [ ] Knowledge sources are used

---

## Step 8 – Enable in Group Chats (Optional)

1. In Teams channel settings, enable:
   - **Personal chat**: One-on-one with agent
   - **Group chat**: @mention agent in groups
   - **Teams channel**: @mention in channels

### Configure Scope:

```
@IT Help Desk how do I connect to VPN?
```

---

## Step 9 – Communicate Rollout

### User Communication:

```markdown
## New: IT Help Desk Agent in Teams!

We've launched an AI-powered IT Help Desk assistant in Microsoft Teams.

**How to access:**
1. Open Microsoft Teams
2. Go to Apps → Search "IT Help Desk"
3. Click Add

**What it can help with:**
- Password resets
- VPN troubleshooting
- Microsoft 365 questions
- Creating support tickets

**Tips:**
- Be specific with your questions
- Use conversation starters for quick help
- The agent learns from your feedback

Questions? Contact IT Support.
```

---

## Step 10 – Monitor Post-Launch

1. Go to Copilot Studio **Analytics**.
2. Monitor:
   - Session volume
   - Resolution rate
   - Escalation rate
   - User satisfaction

---

## ✅ Lab Checklist

- [ ] Prepared and published agent
- [ ] Configured Teams channel
- [ ] Customized Teams app details and icons
- [ ] Configured availability settings
- [ ] Submitted for admin approval (if required)
- [ ] Configured Teams app policies
- [ ] Tested agent in Teams
- [ ] Enabled group chat support
- [ ] Communicated rollout to users
