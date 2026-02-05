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
	- Note: "Obsidian Key".
	- Expiration: Set to "No expiration" or "90 days" (your preference).
	- Select scopes: Check the box next to repo (this gives full control of private repositories).
	- Click Generate token.

!!! failure "🔴 COPY THIS CODE NOW." 
	- You will never see it again. 
	- Paste it into a temporary sticky note.
### Phase 2: Desktop Setup (Office Computer)
*This sets up your primary workstation.*

1. Install & Connect
	- Download and install Obsidian from www.obsidian.md.
	- Open Obsidian. 
	- Create a new vault. 
	- Go to Settings (Gear Icon) > Community Plugins.
	- Turn Restricted Mode -> OFF.
	- Click Browse, search for "Git", and click Install then Enable.
 
2. Download the Clinical Database ("Clone")
	1. In Obsidian, open the Command Palette (>_ icon on the left side OR Press Ctrl + P on Windows OR Cmd + P on Mac).
	2. Type "Clone" and select: "Git: Clone an existing remote repo."
	3. Repo URL: Paste this exactly: https://github.com/joegrafe/np-practice-resource.git
	4. Directory for Clone
	5. Authentication:
		- Username: Your GitHub username.
		- Password: Paste the Access Token (PAT) you copied in Phase 1.
	6. Location: Type "NP Practice Resource"
	7. Depth of Clone: Hit enter

!!! info ""The NP Practice Resource" folder is the github repository."
	- Everything INSIDE the folder will now sync with the repository. 
	- Everything OUTSIDE will stay on your computer.
	- Everything in the "docs" folder will appear on the website.

!!! failure "Never Rename the "docs" folder." 
	- That is required by the website.
 
3. Configure Automation
	Now that you are inside the correct vault:
	 * Go to Settings > Community Plugins > Git (Gear Icon).
		 * Pull updates on startup: Toggle ON. This ensures you see your colleagues' updates immediately.
		 * Auto Pull Interval: Set to 10 minutes
	 * Go to Settings (Gear Icon) > Files and Links
		 * Default location for new attachments = In folder specified below
		 * Attachment fold path = docs/assets
		 * New link format = path from current file
		 * Use Wikilinks = OFF

### Phase 3: Mobile Setup (Point of Care)
*This sets up your phone/tablet.*
1. Install & Prep
	- Download the Obsidian app.
	- Select "Create Vault" named "NP Practice Resource"
		- *This whole vault will sync with the github repository*
	- Select "Device Storage"
	- Tap the Settings (Gear Icon) in the sidebar.
	- Go to Community Plugins > Turn Restricted Mode OFF.
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
