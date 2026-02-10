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
 
Update: The Git Plugin for Obsidian is experimental and does not appear user-friendly enough for our purposes. 

I'm currently testing the android app [GitSync](https://play.google.com/store/apps/details?id=com.viscouspot.gitsync ) to sync the folder your Obsidian vault is built on with the Github repository. It is free for one repository and has a cleaner learning curve than navigating Git in Obsidian. 
