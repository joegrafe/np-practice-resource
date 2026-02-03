"Admonitions" are a must-have for clinical documentation. They allow you to pull a reader's eye toward critical information—like a "Contraindication" warning or a "Clinical Pearl"—using color-coded boxes and icons.

### Step 1: Enable Admonitions in `mkdocs.yml`

To use these, you need to add the `admonition` and `pymdownx.details` extensions to your configuration file. (The `details` extension is what allows you to make "collapsible" boxes, which are great for keeping long protocols tidy).

Update your `markdown_extensions` section like this:

YAML

```
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.emoji:
      emoji_index: !!python/name:materialx.emoji.twemoji
      emoji_generator: !!python/name:materialx.emoji.to_svg
```

---

### Step 2: How to Write Them

Once enabled, you can create a box by starting a line with three exclamation marks (`!!!`) followed by the "type" of box.

#### The Standard Warning

Use this for safety-critical info, like "Red Flags."

Markdown

```
!!! failure "Red Flags / Contraindications"
    * Acute chest pain with radiation to the jaw.
    * New-onset neurological deficits.
```

#### The Clinical Pearl

Use this for "pro-tips" from your experience.

Markdown

```
!!! quote "Clinical Pearl"
    When assessing pediatric patients, always check the capillary refill on the sternum rather than the finger for better accuracy.
```

#### The Collapsible Section (The "Spoiler" Box)

This is perfect for "Answer Keys" or "Deep Dive" sections that you don't want to clutter the main page. Note the `???` instead of `!!!`.

Markdown

```
??? info "Click to expand: Pathophysiology of BC-specific strains"
    This section contains a deep dive into the local epidemiological data...
```

---

### Step 3: Available Styles

The Material theme provides several built-in colors and icons:

|**Type**|**Color**|**Best Use Case**|
|---|---|---|
|`!!! info`|Blue|General helpful information.|
|`!!! tip`|Teal|Clinical pearls or shortcuts.|
|`!!! warning`|Orange|Cautions or important steps not to miss.|
|`!!! failure`|Red|Critical warnings, contraindications, or "don't do this".|
|`!!! example`|Purple|Case studies or specific examples.|

### Pro-Tip for BC NPs

Since you are building this for colleagues, consistency is key. I recommend deciding on a "Style Guide" (e.g., always use `!!! failure` for medication contraindications) so that when a clinician is in a hurry, they instantly know what a red box means without having to read the title.

**Would you like me to help you set up a "Table of Contents" that stays on the side of the screen as you scroll, so your colleagues never get lost in long guides?**