The best way to add more editors to your system while maintaining the security of your clinical resource is to use **Wiki.js's built-in User Management** and **Groups**. This allows you to invite colleagues as editors without giving them access to your Synology NAS or GitHub account.

### 1. The Recommended Workflow: Native Wiki.js Editors

Instead of having every editor use Obsidian and Git, it is much simpler to have them edit directly through the **Wiki.js web interface**.

1. **Create a Group:** In **Administration > Groups**, create a group called "Editors".
2. **Define Permissions:** Grant this group permissions to **Create Pages**, **Edit Pages**, and **Upload Assets**.
3. **Invite Users:** In **Administration > Users**, you can manually create accounts for your colleagues or enable **Email Invitations**.
4. **Sync Back to Obsidian:** Because you have **Bi-directional sync** enabled in your Git settings, any edits your colleagues make on the website will automatically be pushed to GitHub and then "Pulled" into your local Obsidian vault.

---

### 2. The "Power User" Workflow: Shared GitHub Access

If you have a co-editor who also uses Obsidian and wants the same offline capabilities you have, you can add them via GitHub.

- **Add Collaborator:** In your GitHub repository settings, add their GitHub username as a **Collaborator**.
- **Personal Access Token (PAT):** They will need to generate their own PAT to use in their Obsidian Git plugin.
- **Conflict Resolution:** Since multiple people are now pushing to the same repo, ensure everyone uses the **"Pull before Push"** habit in Obsidian to avoid "Merge Conflicts".

---

### 3. Comparison of Editor Types

|**Editor Type**|**Access Point**|**Setup Complexity**|**Best For...**|
|---|---|---|---|
|**Wiki Web Editor**|`nppracticeresource...synology.me`|Low|Most colleagues/NPs.|
|**Obsidian/Git Editor**|Local Obsidian App|High|Co-founders or technical leads.|
|**Synology Admin**|DSM Container Manager|Very High|**Only you** (System owner).|

---
### 4. Critical Security Tip: Clinical Data

Since this system holds clinical resources, do not use the **"Public Registration"** feature in Wiki.js.

- **Action:** Go to **Administration > Authentication** and ensure **Self-Registration** is **Disabled**.
- **Alternative:** Use **Local Authentication** so you have 100% control over exactly who has an "Editor" account on your Synology-hosted site.

### Summary Recommendation

Keep yourself as the only **Git/Obsidian** master editor. For everyone else, create **Wiki.js User Accounts**. This keeps your Synology NAS secure while allowing the clinical database to grow through the web interface.

**Would you like me to show you how to set up the "Page Locking" feature in Wiki.js so two editors don't accidentally overwrite each other's work?**