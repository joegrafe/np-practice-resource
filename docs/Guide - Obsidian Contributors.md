---
title: Guide - Obsidian Contributors
---
This is meant to be a comprehensive, non-technical guide designed for our Nurse Practitioner team. This document takes you through the steps of getting synced 
on both desktop and mobile.

## NP Practice Resource: Contributor Setup Guide

Goal: Link your Obsidian app to our shared clinical database so we can co-create an "NP Practice Resource".

Time Required: ~15–20 minutes.

### Phase 1: Accounts & Keys (The "Badge" Setup)
- Before you can enter the secure system, you need a digital key. We use GitHub to store our data securely.
- Create a GitHub Account: If you don't have one, sign up at github.com.
- Accept the Invite: Check your email for an invitation to the np-practice-resource repository and click Accept.
- Generate Your "Access Token" (PAT):
- Note: You cannot use your regular GitHub password for Obsidian. You must use this special token.
- Log in to GitHub and go to Settings (click your profile photo in the top right).
- Scroll down to Developer Settings (left sidebar, very bottom).
- Select Personal access tokens > Tokens (classic).
- Click Generate new token (classic).
- Note: "Obsidian Key".
- Expiration: Set to "No expiration" or "90 days" (your preference).
- Select scopes: Check the box next to repo (this gives full control of private repositories).
- Click Generate token.
- 🔴 COPY THIS CODE NOW. You will never see it again. Paste it into a temporary sticky note.

### Phase 2: Desktop Setup (Office Computer)
This sets up your primary workstation.
1. Install & Connect
	 * Download and install Obsidian from obsidian.md.
	 * Open Obsidian. In the "Start" window, do NOT click "Create new vault."
	 * We need to install the connector first. Create a "Dummy" vault (folder) just to get to the settings, or if you already use Obsidian, open your existing vault.
	 * Go to Settings (Gear Icon) > Community Plugins.
	 * Turn Restricted Mode -> OFF.
	 * Click Browse, search for "Obsidian Git", and click Install then Enable.
 
2. Download the Clinical Database ("Clone")
	 * In Obsidian, open the Command Palette (Press Ctrl + P on Windows or Cmd + P on Mac).
	 * Type "Clone" and select: Obsidian Git: Clone an existing remote repo.
	 * Repo URL: Paste this exactly:
	   https://github.com/joegrafe/np-practice-resource.git
	 * Authentication:
	   * Username: Your GitHub username.
	   * Password: Paste the Access Token (PAT) you copied in Phase 1.
	 * Location: Choose an empty folder on your computer where you want these files to live (e.g., Documents/NP-Resource).
	 * Obsidian will ask to "Open this vault?" Click Yes.
 
3. Configure Automation
	Now that you are inside the correct vault:
	 * Go to Settings > Community Plugins > Obsidian Git (Gear Icon).
	 * Vault backup interval: Set to 10 (minutes). This auto-saves your work to the team server.
	 * Pull updates on startup: Toggle ON. This ensures you see your colleagues' updates immediately.

### Phase 3: Mobile Setup (Point of Care)
This sets up your phone/tablet.
1. Install & Prep
	 * Download the Obsidian app.
	 * Select "Open folder as vault" (create a new empty folder named NP-Resource).
	 * Tap the Settings (Gear Icon) in the sidebar.
	 * Go to Community Plugins > Turn Restricted Mode OFF.
	 * Browse for "Obsidian Git", Install, and Enable.

2. Configure the "Engine" (Critical Step)
	Mobile phones don't have the same "engine" as computers, so we have to turn on a special one.
	 * Tap the Gear Icon next to the installed Obsidian Git plugin.
	 * Set Auto Pull
	 * Restart the app (close it completely and reopen) for this to take effect.
 
3. Connect to the Team
	 * Open the app again.
	 * Swipe down from the top to open the Command Palette.
	 * Type "Clone" and tap Obsidian Git: Clone.
	 * Repo URL: https://github.com/joegrafe/np-practice-resource.git
	 * Username: Your GitHub username.
	 * Password: Paste your Access Token (PAT).
	 * Directory: Select the empty folder you created.
 
4. Final Mobile Check
	Go back to the Git Plugin Settings:
	 * Custom base path: Ensure this field is COMPLETELY BLANK/EMPTY.
	 * Vault backup interval: Set to 10.

### Phase 4: Formatting Rules (The "Clinical Standard")
- To ensure our website works correctly, everyone must use the same link settings.
- On BOTH Desktop and Mobile:
- Go to Settings > Files & Links.
- Use [[Wikilinks]]: Toggle OFF.
- Why? The web server requires standard links.
- New link format: Select Relative path to file.

### Phase 5: Your Workflow
How to co-create without breaking the system.
 - Start: Open Obsidian. Look at the status bar (bottom right on desktop) or swipe down (mobile). Wait for "Git: Pulled" notification. Now you have the latest repository.
 - During Day:
   - Create a new note for a guideline or observation.
   - Write freely.
   - The system will Auto-Backup every 10 minutes.
 - Urgent Update: If you just added a critical protocol and need it on the website now:
   - Desktop: Press Ctrl + P -> Type "Push" -> Select Obsidian Git: Create Backup.
   - Mobile: Open Command Palette -> Type "Push" -> Select Obsidian Git: Create Backup.

Troubleshooting:
 * "Authentication Failed": Your Token (PAT) may have expired. Generate a new one in GitHub and re-enter it in the plugin settings.
 * "Git not ready": Check that the Custom base path setting is empty.
