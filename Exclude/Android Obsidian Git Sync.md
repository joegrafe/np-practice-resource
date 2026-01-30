To sync your Obsidian folder to GitHub on an Android device, you cannot use the standard "Obsidian Git" plugin directly because mobile devices lack a built-in Git installation. Instead, you must use a third-party app to act as the "bridge" between your phone's file system and GitHub.

The most reliable method for Android users is using **Termux** or a specialized app like **GitJournal** or **Working Copy** (if available), but **Termux** provides the most professional, high-control setup similar to your desktop environment.

---
### 1. Install and Set Up Termux

Termux provides a Linux-like terminal on your Android device where you can run actual Git commands.

1. **Download Termux**: It is recommended to download it from **F-Droid** rather than the Play Store for the most up-to-date version.
2. **Grant Storage Access**: Open Termux and type the following command to allow it to see your phone's folders:
    
    `termux-setup-storage`
    
3. **Install Git**: Type this command to install the Git engine:
    
    `pkg install git`
    

### 2. Clone Your Clinical Repository

You need to pull your `np-practice-resource` repo onto your phone.

1. **Navigate to your Documents folder**:
    
    `cd ~/storage/documents`
    
2. **Clone the Repo**: Use your GitHub username and the same **Personal Access Token (PAT)** you used for your desktop setup:
    
    `git clone https://github.com/joegrafe/np-practice-resource.git`
    
3. **Open in Obsidian**: Open the Obsidian app on Android, select **"Open folder as vault,"** and navigate to the folder you just created in your Documents.


---

### 3. Automating the Sync

Since the "Obsidian Git" plugin won't run its own Git commands on Android, you have two choices for syncing:

#### Option A: Manual Sync via Termux (Most Reliable)

Whenever you finish a clinical note on your phone, open Termux and run:
- `git add .`
- `git commit -m "Mobile update"`
- `git push`

#### Option B: Use the "Obsidian Git" Plugin (Native UI)

You can still install the **Obsidian Git** plugin on your Android app. While it cannot execute Git itself, you can configure it to use **"Isomorphic-Git"** (a JavaScript-based Git engine) which is built into the plugin for mobile support.

1. **Enable the Plugin**: In Obsidian mobile, go to **Settings > Community Plugins > Obsidian Git**.
2. **Authentication**: Enter your **Username** and **PAT** in the plugin settings.
3. **Backup Interval**: Set the "Vault backup interval" to **10 minutes** to match your desktop.

---

### 4. Critical Formatting Reminder

To ensure your mobile edits don't break the links on your Wiki.js site, verify these settings on your Android device:

- **Relative Paths**: Ensure **New link format** is set to **Relative path to file**.
- **Markdown Links**: Ensure **Use [[Wikilinks]]** is toggled **OFF**.
- **Custom Base Path**: Ensure this field is **completely blank** in the mobile plugin settings.

**Would you like me to show you how to create a "Shortcut" on your Android home screen that runs the Git sync command with a single tap?**

To make syncing on Android as seamless as it is on your desktop, you can create a one-tap shortcut using **Termux:Widget**. This allows you to "Push" your clinical updates to GitHub without ever typing a command on your phone's keyboard.

### 1. Install the Required Tools

You need a small add-on for Termux to enable home screen shortcuts.

- **Download Termux:Widget**: Get it from **F-Droid** (ensure it is from the same source as your main Termux app to avoid signature conflicts).
- **Grant Permissions**: Ensure Termux:Widget has permission to "Display over other apps" in your Android settings.

---

### 2. Create the Sync Script

You need to create a small file that contains the Git commands.

1. **Open Termux** and create the shortcut directory:
    
    `mkdir -p ~/.shortcuts`
    
2. **Create the script file**:
    
    `nano ~/.shortcuts/sync_wiki.sh`
    
3. **Paste these exact lines** (replace the path with your actual vault folder):
    
    Bash
    
    ```
    #!/bin/bash
    cd ~/storage/documents/np-practice-resource
    git add .
    git commit -m "Mobile Update $(date)"
    git push
    echo "Sync Complete!"
    sleep 2
    ```
    
4. **Save and Exit**: Press `Ctrl + O`, then `Enter`, then `Ctrl + X`.
    
5. **Make it executable**:
    
    `chmod +x ~/.shortcuts/sync_wiki.sh`
    

---

### 3. Add the Widget to Your Home Screen

1. Go to your **Android Home Screen**.
2. Long-press an empty space and select **Widgets**.
3. Find **Termux:Widget** and drag the "Termux Shortcut" to your screen.
4. A list will pop up; select `sync_wiki.sh`.

---

### 4. Final Mobile Checklist

To ensure your Android device doesn't introduce "broken links" into your Nurse Practitioner resource:

- **Relative Paths**: In Obsidian Mobile, verify `Settings > Files & Links > New link format` is set to **Relative path to file**.
- **Markdown Links**: Ensure **Use [[Wikilinks]]** is **OFF**.
- **Conflict Prevention**: Always tap your new "Sync" widget **before** you start editing and **after** you finish to keep the phone and Synology NAS in perfect harmony.
