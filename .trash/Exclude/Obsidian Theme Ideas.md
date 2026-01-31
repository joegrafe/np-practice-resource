To make your **Master Index** look professional and clinical—transforming it from a plain list into a functional dashboard—you can use a combination of standard Markdown enhancements and **Wiki.js-specific classes**.

Since Wiki.js supports specific CSS classes directly in Markdown, you can style your directory to look like a modern web portal while keeping it perfectly compatible with your Obsidian vault.

### 1. Create a "Grid" or "Cards" Layout

Instead of a long vertical list, you can display your folders as a grid of cards. In Wiki.js, you can trigger this by adding a special class tag directly below your list.

**Add this to your Master Index note:**

Markdown

```
### 🏥 Clinical Guidelines
- [Cardiology](./Guidelines/Cardiology)
- [Pharmacology](./Guidelines/Pharmacology)
- [Pediatrics](./Guidelines/Pediatrics)
- [Geriatrics](./Guidelines/Geriatrics)
{.grid-list}

### 📂 Administrative Resources
- [Billing Codes](./Admin/Billing)
- [Lab References](./Admin/Labs)
{.links-list}
```

- **`.grid-list`**: This class turns a standard bulleted list into a multi-column grid on your Wiki.js site.
- **`.links-list`**: This styles the list with clean borders and icons, making it look like a professional directory.

---

### 2. Use Callouts for Visual Hierarchy

Callouts (also known as alerts or admonitions) are excellent for highlighting "Featured" resources or "Urgent" clinical updates. Wiki.js recognizes these and applies specific colors.

- **Blue (`is-info`)**: General resources.
- **Green (`is-success`)**: Finalized/Verified guidelines.
- **Yellow (`is-warning`)**: Drafts or notes under review.

**Example Syntax:**

> [!info] **New NP Orientation**
> 
> Welcome to the NP Practice Resource. Start with the [Onboarding Checklist](https://www.google.com/search?q=./Onboarding) to set up your access.
> 
> {.is-info}

---

### 3. Add a Professional Banner

A high-quality header image instantly makes a site feel like a "resource" rather than a "folder". You can add a clinical-themed banner at the very top of your note.

- **Obsidian Tip**: Use the **Pixel Banner** plugin to manage these locally.
- **Markdown Syntax**: `![Banner Image](https://link-to-your-image.jpg)`.
- **Wiki.js Tip**: You can also use the **Page Properties** menu in Wiki.js to set a "Header Image" that appears behind the title on every page.

---

### 4. Use "Minimal" Styling (Obsidian-side)

If you want the dashboard to look beautiful while you are working inside Obsidian, I recommend the **Minimal Theme**.

- **Cards View**: Use the helper class `cssclasses: cards` in the frontmatter of your Master Index note to turn your lists into cards _inside_ Obsidian as well.
- **Headings**: Use the **Style Settings** plugin to give your headers clinical colors (like dark blues or teals) to match a medical aesthetic.

---

### Summary Checklist for a "Nice" Index

|**Feature**|**Markdown Element**|**Wiki.js Effect**|
|---|---|---|
|**Directory**|Bullet List + `{.grid-list}`|Multi-column grid/cards.|
|**Sections**|`### Heading`|Styled headers for navigation.|
|**Highlights**|`> [!info]` + `{.is-info}`|Colored "alert" boxes for clinical info.|
|**Separation**|`---`|Horizontal rules to break up subjects.|
