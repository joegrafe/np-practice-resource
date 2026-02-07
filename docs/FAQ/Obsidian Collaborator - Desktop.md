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
