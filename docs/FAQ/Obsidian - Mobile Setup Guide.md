**Goal:** Link the Obsidian app on your computer to our shared clinical database to co-create the "NP Practice Resource."

---
### Phase 1: Accounts & Keys (The "Badge" Setup)

_Before entering the secure system, you need a digital key. We use GitHub to store our data securely._

1. **Create a GitHub Account:** If you don't have one, sign up at [www.github.com](https://www.github.com/).
2. **Accept the Invite:** Check your email for an invitation to the `np-practice-resource` repository and click **Accept**.
3. **Generate Your "Access Token" (PAT):**
    - _Note: You cannot use your regular GitHub password for Obsidian. You must use this special token._
    1. Log in to GitHub and click your profile photo (top right) $\rightarrow$ **Settings**.
    2. Scroll to the very bottom left sidebar $\rightarrow$ **Developer Settings**.
    3. Select **Personal access tokens** $\rightarrow$ **Tokens (classic)**.
    4. Click **Generate new token (classic)**.
    5. **Note:** Type "Obsidian Key".
    6. **Expiration:** Set to "No expiration" (easiest) or "90 days" (more secure).
    7. **Select scopes:** ☑️ Check the box next to **`repo`** (Full control of private repositories).
    8. Click **Generate token**.
        

!!! failure "🔴 COPY THIS CODE NOW"
	You will never see this code again. Copy it and paste it into a temporary sticky note or password manager immediately.

---
### Phase 2: Desktop Setup (The Engine)

_This sets up the software on your computer._

#### 1. Install Obsidian

- Download and install Obsidian from [www.obsidian.md](https://obsidian.md/).
- Open Obsidian.

#### 2. Create a "Setup" Vault

_We need a temporary vault just to install the software tools. We will switch to the real one in Phase 3._

- Click **Create new vault**.
- Name it "Setup" (or anything you like).
- Save it to your Desktop/Documents.

#### 3. Install the Git Plugin

- In Obsidian, click **Settings** (Gear Icon ⚙️) $\rightarrow$ **Community Plugins**.
- Turn **Restricted Mode** $\rightarrow$ **OFF**.
- Click **Browse**, search for **"Git"** (by Vinzent03), and click **Install**.
- Once installed, click **Enable**.

---

### Phase 3: Connect to Database (The Clone)

_Now we download the shared clinical content._

1. In Obsidian, open the **Command Palette** (Press `Ctrl + P` on Windows / `Cmd + P` on Mac).
2. Type "Clone" and select: **`Git: Clone an existing remote repo`**.
3. **Repo URL:** Paste this exactly:
    
    `https://github.com/joegrafe/np-practice-resource.git`
    
1. **Authentication:**
    - **Username:** Your GitHub username.
    - **Password:** Paste the **Access Token (PAT)** you copied in Phase 1.
    - _(If asked for a directory name, type: `NP-Practice-Resource`)_
2. **Wait:** The download may take a moment.
3. **The Switch:** Obsidian will ask: _"Repo cloned. Would you like to open the new vault?"_
    - Click **YES** (or "Open Vault").
    - _You are now inside the shared database._

!!! failure "CRITICAL RULE: The 'docs' Folder"
	Never rename or move the folder named **`docs`**. The website requires this specific folder to function.

---

### Phase 4: Configure Automation

_We must configure the new vault to sync automatically and format links correctly for the website._

#### 1. Git Automation Settings

- Go to **Settings** (Gear Icon ⚙️) $\rightarrow$ **Git** (at the bottom under Community Plugins).
- **Vault backup interval (minutes):** Set to `10`.
- **Auto backup after file change:** Toggle **ON**.
- **Auto pull interval (minutes):** Set to `10`.
- **Pull updates on startup:** Toggle **ON**.
    - _This ensures you see your colleagues' updates every time you open the app._
- **Author:** Enter your Name and Email where requested.

#### 2. Obsidian Link Settings

- Go to **Settings** $\rightarrow$ **Files and Links**.
- **Default location for new attachments:** Select "In folder specified below".
    - **Attachment folder path:** Type `docs/assets`.
- **New link format:** Select "Relative path to file".
- **Use Wikilinks:** Toggle **OFF**.
    - _This is required for the website to read your links._

#### 3. Cleanup

- Go to **Settings** $\rightarrow$ **Core Plugins**.
- Turn **OFF** "Daily Notes" (We don't use them for this project).
- **Restart Obsidian** to lock in all changes.

!!! success "Setup Complete"
	- You are ready to contribute! Any changes you make in the `docs` folder will sync to the team every 10 minutes.