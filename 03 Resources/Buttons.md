Because your site architecture uses Markdown files that compile into HTML, you have two primary ways to add buttons depending on how your MkDocs configuration is set up.

### **Method 1: The Material for MkDocs Native Way (Recommended)**

If you are using the popular **Material for MkDocs** theme, it has beautiful, built-in button styles that you can apply directly to standard Markdown links.

To use this, you just need to add a small curly-brace class `{ .md-button }` right after your link.

**The Syntax:**

Markdown

```
[Download Guidelines](https://www.bcguidelines.ca){ .md-button }

[Primary Action Button](https://example.com){ .md-button .md-button--primary }
```

**Prerequisite Check:**

For this syntax to work, you must have the `attr_list` extension enabled in your `nppr-website-config` repository's `mkdocs.yml` file. Check to ensure it looks like this:

YAML

```
markdown_extensions:
  - attr_list
```

### **Method 2: Pure HTML (Works Everywhere Instantly)**

If you haven't enabled the `attr_list` extension yet or want a custom design that doesn't rely on your theme's default colors, you can paste raw HTML directly into your Markdown file. Using an anchor tag (`<a>`) styled as a button is best practice for web links.

**The Syntax:**

HTML

```
<a href="https://www.bcguidelines.ca" style="display: inline-block; padding: 10px 20px; background-color: #005A9C; color: white; text-decoration: none; border-radius: 6px; font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  Open BC Guidelines
</a>
```

### **Clinical UX Recommendations for Buttons**

When adding buttons to a fast-paced clinical resource like `nppr.ca`, keep these design principles in mind:

- **Use Primary vs. Secondary Styles:** If you have two buttons next to each other (e.g., "View Interactive Flowchart" and "Download PDF Checklist"), make the most important action solid colored (Primary) and the less critical action outlined or lighter colored (Secondary).
    
- **External Link Icons:** If a button takes the clinician _off_ of `nppr.ca` (like directing them to a government billing page), it is incredibly helpful to add an external link icon or explicitly state `(External Link)` so they know they are leaving your tool.
    
- **Target Blank:** For external tools, you may want the button to open in a new tab so they don't lose their place on your diagnostic page. In HTML, you do this by adding `target="_blank"` to the tag:
    

HTML

```
<a href="https://example.com" target="_blank" style="...">Open in New Tab</a>
```

To arrange buttons in a clean, horizontal row that looks great on desktop but automatically drops down into a stack on mobile screens, you want to use a layout container called **Flexbox**.

Here are the two ways to implement this, depending on whether you prefer the native Markdown theme styles or raw HTML.

### **Method 1: Universal HTML Flexbox (Safest & Most Customizable)**

This approach gives you total control over the spacing and guarantees the layout won’t break on mobile. It wraps standard HTML buttons inside a flex container.

Paste this into your Markdown file:

HTML

```
<div style="display: flex; gap: 12px; flex-wrap: wrap; margin-vertical: 15px;">
  
  <a href="https://example.com/1" style="display: inline-block; padding: 10px 20px; background-color: #005A9C; color: white; text-decoration: none; border-radius: 6px; font-weight: bold;">
    Primary Action
  </a>

  <a href="https://example.com/2" style="display: inline-block; padding: 10px 20px; background-color: #f4f4f5; color: #18181b; text-decoration: none; border-radius: 6px; font-weight: bold; border: 1px solid #e4e4e7;">
    Secondary Action
  </a>

  <a href="https://example.com/3" style="display: inline-block; padding: 10px 20px; background-color: #f4f4f5; color: #18181b; text-decoration: none; border-radius: 6px; font-weight: bold; border: 1px solid #e4e4e7;">
    Third Tool
  </a>

</div>
```

### **Method 2: Combining HTML Layout with Material Markdown Buttons**

If you are using the `{ .md-button }` extension from your theme and want to keep using it, you can wrap your Markdown links inside a special HTML `div`.

> **Important:** To make Markdown syntax work inside a raw HTML tag, you _must_ add `markdown="1"` to the opening `<div>` tag.

HTML

```
<div style="display: flex; gap: 12px; flex-wrap: wrap;" markdown="1">

[First Guideline](https://example.com/1){ .md-button .md-button--primary }
[Second Guideline](https://example.com/2){ .md-button }
[Third Guideline](https://example.com/3){ .md-button }

</div>
```

### **Why this specific code works for Clinical UX**

- **`gap: 12px;`** This handles the perfect horizontal space between the buttons so they don't mash together on a desktop screen.
    
- **`flex-wrap: wrap;`** This is the secret sauce for mobile. If an NP pulls up `nppr.ca` on an iPhone, a rigid row of three buttons would overflow off the screen. This attribute forces the second and third buttons to neatly drop down to a new row if space runs out, making them easy to tap with a thumb.