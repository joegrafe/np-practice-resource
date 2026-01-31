# 🏥 Onboarding: Power User Setup

Welcome to the **NP Practice Resource** team. As a Power User, you will be using Obsidian to contribute clinical guidelines, pathophysiology notes, and research directly to our shared knowledge base. Follow these steps to sync your local environment with our Synology-hosted website.

---
### 1. GitHub Access & Security

Before opening Obsidian, you must establish your connection to our central "source of truth."

- **Accept Invitation**: Check your email for a GitHub invitation to the `np-practice-resource` repository and accept it.
- **Generate your Access Token (PAT)**:
    
    1. Log in to GitHub and go to **Settings > Developer Settings > Personal Access Tokens > Tokens (classic)**.
    2. Click **Generate new token**.
    3. **Scope**: Check the box for **`repo`** (Full control of private repositories).
    4. **Copy the Token**: Save this in a secure place; you will use this instead of a password for Obsidian.

---

### 2. Local Vault Setup

You need a local copy of the clinical files on your computer.

1. **Clone the Repository**: Use **GitHub Desktop** to "Clone" the `np-practice-resource` repository to a dedicated folder on your hard drive.
2. **Open in Obsidian**: Launch Obsidian, click **Open folder as vault**, and select the folder you just cloned.

---

### 3. Sync Plugin Configuration

We use the **Obsidian Git** plugin to bridge your computer to our Synology NAS and Wiki.js site.

1. **Install**: Go to **Settings > Community Plugins > Browse** and install **Obsidian Git**.
2. **Authentication**: When prompted, enter your GitHub **Username** and the **PAT** you generated in Step 1.
3. **Critical Setting**: In the Git plugin settings, ensure **Custom base path** is **COMPLETELY BLANK**. Entering a path here will break the sync.

---

### 4. Formatting Standards (Clinical Integrity)

To ensure your notes display correctly on our public website (`nppracticeresource.jgrafe.synology.me`), your link settings must match the following:

- **Standard Markdown Links**: Go to **Settings > Files & Links** and toggle **OFF** "Use [[Wikilinks]]".
- **Relative Paths**: Set **New link format** to **Relative path to file**.
- **The Result**: Your links should look like `[Clinical Guideline](./Path/To/Guideline)`.

---

### 5. Your Daily Workflow

The system is designed to be "set it and forget it," but follow these habits to avoid clinical data conflicts:

- **Startup**: Obsidian will automatically "Pull" the latest updates from other editors when you open the app.
- **Auto-Save**: The Git plugin is set to "Push" your changes to the server every **10 minutes**.
- **Manual Sync**: If you want to push an urgent update immediately, press `Ctrl + P` and run `Obsidian Git: Commit & Push all changes`.

---

**Questions?** Reach out to the System Administrator (Joe) if you see a "Git is not ready" status or "Permission Denied" error.