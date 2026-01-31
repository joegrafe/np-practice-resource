Setting up a "Power User" on Obsidian requires a one-time configuration to ensure their local vault stays perfectly synchronized with your Synology NAS and Wiki.js site. This process allows them to work offline while contributing to the clinical knowledge base.

---

### Step 1: GitHub Repository Access

Before your colleague opens Obsidian, they must have the authority to interact with your data.

1. **Add Collaborator:** Log in to your GitHub account, navigate to the `np-practice-resource` repository, and add their GitHub username under **Settings > Collaborators**.
2. **Generate a PAT:** Have the user log into their own GitHub account and go to **Settings > Developer Settings > Personal Access Tokens (Tokens classic)**.
3. **Permissions:** They must generate a new token with the **`repo`** scope checked. They should copy this token immediately; they will need it for Step 4.

### Step 2: Local Vault Setup

The user needs a local copy of the Markdown files to work on.

1. **Clone the Repo:** Have the user install **GitHub Desktop** or use the command line to "Clone" your repository to a folder on their computer.
2. **Open as Vault:** Open Obsidian, select **Open folder as vault**, and choose the folder they just cloned.

### Step 3: Install the Git Plugin

This plugin is the "bridge" that sends clinical notes from their computer to your NAS.

1. Go to **Settings > Community Plugins** and click **Browse**.
2. Search for **Obsidian Git** and click **Install**, then **Enable**.
3. **Critical Configuration:** Under the plugin settings, ensure **Custom base path** is left **completely blank**.

### Step 4: Authentication & Syncing

Now, connect their local Obsidian app to your GitHub repository.

1. **Enter Credentials:** When prompted by the plugin (or in the Git settings), have them enter their **GitHub Username** and the **PAT** they generated in Step 1.
2. **Sync Settings:** Set the **Vault backup interval** to 5 or 10 minutes. This ensures their clinical edits are "Pushed" to the cloud automatically throughout the day.
3. **Pull Settings:** Enable **Pull updates on startup** so they always see the latest clinical guidelines added by you or other editors before they start writing.

### Step 5: Formatting Alignment

To ensure their links don't break when they appear on the Wiki.js site, they must match your formatting.

1. Go to **Settings > Files & Links**.
2. **Toggle OFF** "Use [[Wikilinks]]".
3. Set **New link format** to **Relative path to file**.

---

### Summary Checklist for Power Users

|**Action**|**Requirement**|
|---|---|
|**GitHub**|Accepted Invite & Generated PAT.|
|**Obsidian Plugin**|Git Plugin Installed & Base Path Empty.|
|**Authentication**|Used PAT (not password) for login.|
|**Links**|Standard Markdown links with Relative Paths.|
