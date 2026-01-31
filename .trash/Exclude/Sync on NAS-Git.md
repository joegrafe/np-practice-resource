To shift the responsibility of the Git sync from your individual Obsidian clients to your **Synology NAS**, you change the architecture so that your devices simply save files to the NAS, and the NAS handles the "Git Work" (commit and push) in the background.

This centralizes the sync logic and removes the need for Git plugins or PAT configurations on every phone or laptop you use.

---

### 1. The Architecture Shift

Instead of each device talking to GitHub, they will all talk to a shared folder on your NAS.

- **Obsidian Client:** Saves `.md` files to a synchronized folder (via Synology Drive Client or SMB).
- **Synology NAS:** Monitors that folder for changes.
- **GitHub:** Receives updates from the NAS, which then triggers the Wiki.js update.

---

### 2. Method A: Leverage Your Existing Wiki.js Sync

Since you already have **Wiki.js** set up with **Bi-directional sync**, the easiest way is to let Wiki.js be your Git client.

1. **Map the Folder:** Mount the Synology folder where Wiki.js stores its data (e.g., `docker/wikijs/data/home`) to your computer as a network drive (SMB) or via the **Synology Drive Client**.
2. **Point Obsidian There:** Open that folder as your Obsidian Vault.
3. **The Result:** When you save a note in Obsidian, the file is written directly to the NAS. Wiki.js will eventually detect the change during its next sync interval and "Push" it to GitHub for you.

---

### 3. Method B: Synology Task Scheduler (Most Robust)

If you want more control or faster syncing than Wiki.js provides, you can use a simple script that runs on the NAS itself.

#### Step 1: Create the Sync Script

Create a file named `git_sync.sh` in your `docker/scripts` folder:

Bash

```
#!/bin/bash
# Navigate to your wiki data folder
cd /volume1/docker/wikijs/data/home

# Pull latest changes from GitHub first
/usr/bin/git pull origin main

# Add all new clinical notes
/usr/bin/git add .

# Commit with a timestamp
/usr/bin/git commit -m "NAS Auto-Sync: $(date)"

# Push to GitHub
/usr/bin/git push origin main
```

#### Step 2: Set up the Scheduled Task

1. Go to **Control Panel > Task Scheduler**.
2. Click **Create > Scheduled Task > User-defined script**.
3. **General tab**: Set the user to the one owning the folder (e.g., PUID `1034`).
4. **Schedule tab**: Set it to run every **5 or 10 minutes**.
5. **Task Settings tab**: Paste the path to your script: `bash /volume1/docker/scripts/git_sync.sh`.

---

### 4. Handling SSH Authentication

Since the NAS is running this in the background, it cannot prompt you for a password or PAT. You should use an **SSH Key**.

1. **Generate Key on NAS:** Open PuTTY, log in to your NAS, and run `ssh-keygen`.
2. **Add to GitHub:** Copy the contents of `~/.ssh/id_rsa.pub` and add it to your **GitHub Profile > Settings > SSH and GPG keys**.
3. **Update Remote:** Ensure your repository on the NAS is using the SSH URL (`git@github.com:joegrafe/np-practice-resource.git`) rather than the HTTPS URL.

---

### Comparison of NAS-Side Sync Methods

|**Feature**|**Wiki.js Sync**|**Task Scheduler Script**|
|---|---|---|
|**Complexity**|Very Low|Medium|
|**Sync Speed**|Depends on Wiki.js interval|As fast as you schedule it|
|**Reliability**|Good (UI-managed)|Excellent (Native Git)|
|**Best For...**|General clinical notes|Large batches of files/images|
