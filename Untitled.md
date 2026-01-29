Setting up this ecosystem requires a "Source of Truth" to act as the bridge between your phone and your server. **Git** (using GitHub or GitLab) is the industry-standard way to do this. It allows your Obsidian notes to travel from your phone to the cloud, and then down to your Synology NAS.

Here is your step-by-step blueprint.

---

## Step 1: Create the "Source of Truth" (GitHub)

Before touching your NAS or phone, you need a place for the files to live.

1. Create a **Private Repository** on GitHub (e.g., `np-clinical-resource`).

2. Generate a **Personal Access Token (PAT)** in your GitHub settings (under Developer Settings). You’ll need this to give your phone and NAS permission to "talk" to the repo.
    
    - _Note: Ensure you check the "repo" scope when creating the token._
        

---

## Step 2: Obsidian on Your Phone (The Input)

You need your mobile vault to automatically send changes to GitHub.

1. **Install Obsidian** and create/open your vault.
    
2. **Install the "Obsidian Git" Plugin** from the Community Plugins gallery.
    
3. **Configure the Plugin:**
    
    - Enter your GitHub Username and the **PAT** you created in Step 1.
        
    - Set the **Backup Interval** (e.g., every 5 or 10 minutes) so your notes sync automatically without you having to press anything.
        
    - Set "Pull updates on startup" to **On** so you always have the latest clinical pearls when you open the app.
        

---

## Step 3: Install Wiki.js on Synology (The Display)

Since you've used Docker before, we will use **Container Manager** (the new name for the Docker app in DSM 7.2).

1. **Create Folders:** In File Station, go to `docker/` and create a `wikijs` folder with three subfolders: `config`, `data`, and `db`.
    
2. **Deploy via Project (Docker Compose):** Open Container Manager -> Project -> Create.
    
3. **Paste the Compose Code:** Use a standard Wiki.js + PostgreSQL image.
    
    - _Tip: Use the `requarks/wiki:latest` image._
        
4. **Run the Wizard:** Once the container is running, go to `http://[NAS-IP]:3000` to set up your admin account.
    

---

## Step 4: Link Wiki.js to your Obsidian Files

This is the "magic" step where the Wiki starts reading your Markdown files.

1. In the Wiki.js Admin Area, go to **Storage**.
    
2. Select **Git** as the storage target.
    
3. **Configure the Connection:**
    
    - **Repository URL:** Link to your GitHub repo.
        
    - **Authentication:** Use the same GitHub Username and PAT.
        
    - **Sync Mode:** Set this to **Bi-directional**.
        
    - **Schedule:** Set it to sync every 5 minutes.
        
4. **The Result:** Wiki.js will pull your `.md` files from GitHub and instantly render them as beautiful wiki pages.
    

---

## Step 5: Host the Wiki on Your Website

To make the wiki accessible as `resource.yourwebsite.com`, you need to point your domain to your NAS.

1. **DNS Settings:** Go to your domain registrar (e.g., Namecheap, Cloudflare) and create a **CNAME record** for `resource` pointing to your Synology DDNS address (e.g., `yourname.synology.me`).
    
2. **Synology Reverse Proxy:**
    
    - Go to **Control Panel > Login Portal > Advanced > Reverse Proxy**.
        
    - **Source:** Protocol `HTTPS`, Hostname `resource.yourwebsite.com`, Port `443`.
        
    - **Destination:** Protocol `HTTP`, Hostname `localhost`, Port `3000` (or whatever port you assigned to Wiki.js).
        
3. **SSL Certificate:** Go to **Control Panel > Security > Certificate** and get a free Let's Encrypt certificate for your new subdomain so the site is secure (`HTTPS`).
    

---

### How it looks in practice:

- **On Shift:** You see a new clinical guideline. You open Obsidian on your phone, type it out, and close the app.
    
- **Behind the Scenes:** The Obsidian Git plugin pushes the note to GitHub. Five minutes later, Wiki.js pulls that file from GitHub.
    
- **For the Team:** Your colleagues visit `resource.yourwebsite.com` and see the updated guideline instantly, formatted perfectly.
    

**Would you like the specific Docker Compose code for Step 3 to paste directly into your Synology Container Manager?**