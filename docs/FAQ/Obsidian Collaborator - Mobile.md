This is meant to be a comprehensive, non-technical guide designed for our Nurse Practitioner team. This document takes you through the steps of getting synced 
on both desktop and mobile.

## NP Practice Resource: Contributor Setup Guide

Goal: Link your Obsidian app to our shared clinical database so we can co-create an "NP Practice Resource".

Time Required: ~15–20 minutes.

### Phase 1: Accounts & Keys (The "Badge" Setup)
- Before you can enter the secure system, you need a digital key. We use GitHub to store our data securely.
- Create a GitHub Account: If you don't have one, sign up at www.github.com
- Accept the Invite: Check your email for an invitation to the np-practice-resource repository and click Accept.
- Generate Your "Access Token" (PAT):
	- *Note: You cannot use your regular GitHub password for Obsidian. You must use this special token.*
	- Log in to GitHub and go to Settings (click your profile photo in the top right).
	- Scroll down to Developer Settings (left sidebar, very bottom).
	- Select Personal access tokens > Tokens (classic).
	- Click Generate new token (classic).
		- Add Note: "Obsidian Key".
		- Expiration: Set to "No expiration" or "90 days" (your preference).
		- Select scopes: Check the box next to repo (this gives full control of private repositories).
		- Click Generate token.

!!! failure "🔴 COPY THIS CODE NOW." 
	- You will never see it again. 
	- Paste it into a temporary sticky note.

### Phase 2: Mobile Setup (Point of Care)
*This sets up your phone/tablet.*
1. Install & Prep
	- Download the Obsidian app.
	- Select "Create Vault" named "NP Practice Resource"
		- *This whole vault will sync with the github repository*
	- Select "Device Storage"
	- Tap the Settings (Gear Icon) -> Go to Community Plugins -> Turn Restricted Mode OFF.
	- Browse for "Git", Install, and Enable.
 
2. Connect to the Team
	 * Swipe down from the top to open the Command Palette.
	 * Type "Clone" and tap "Git: Clone and existing remote repo".
	 * Repo URL: https://github.com/joegrafe/np-practice-resource.git
		 * Username: Your GitHub username.
		 * Password: Paste your Access Token (PAT).
	 * Directory: Select Vault Root.
	 * Depth: Hit Enter for all
 
3. Final Mobile Checks
	 * Go to Settings > Community Plugins > Git (Gear Icon).
		 * Pull updates on startup: Toggle ON. *This ensures you see your colleagues' updates immediately.*
		 * Auto Pull Interval: Set to 10 minutes.
		 * Fill in Commit Author information.
	 * Go to Settings (Gear Icon) > Files and Links
		 * Default location for new attachments = In folder specified below
		 * Attachment fold path = docs/assets
		 * New link format = path from current file
		 * Use Wikilinks = OFF
	 * Go to Settings (Gear Icon) > Core Plugins
		 * Turn off Daily Notes.
	 * Close and restart the app.

### Phase 4: Your Workflow
How to co-create without breaking the system. 
- Start: Open Obsidian. Look at the status bar (bottom right on desktop) or swipe down (mobile). Wait for "Git: Pulled" notification. Now you have the latest repository. 
- During Day: 
	- Create a new note for a guideline or resource. 
	- Write freely. 
	- The system will Auto-Backup every 10 minutes. 

Troubleshooting:
 * "Authentication Failed": Your Token (PAT) may have expired. Generate a new one in GitHub and re-enter it in the plugin settings.
 * "Git not ready": Check that the Custom base path setting is empty.
