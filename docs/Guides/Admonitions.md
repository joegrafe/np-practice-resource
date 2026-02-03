"Admonitions" are a must-have for clinical documentation. They allow you to pull a reader's eye toward critical information—like a "Contraindication" warning or a "Clinical Pearl"—using color-coded boxes and icons.
#### The Standard Warning

Use this for safety-critical info, like "Red Flags."

Markdown

```
!!! failure "Red Flags / Contraindications"
    * Acute chest pain with radiation to the jaw.
    * New-onset neurological deficits.
```

!!! failure "Red Flags / Contraindications"
    * Acute chest pain with radiation to the jaw.
    * New-onset neurological deficits.
#### The Clinical Pearl

Use this for "pro-tips" from your experience.

Markdown

```
!!! quote "Clinical Pearl"
    When assessing pediatric patients, always check the capillary refill on the sternum rather than the finger for better accuracy.
```

!!! quote "Clinical Pearl"
    When assessing pediatric patients, always check the capillary refill on the sternum rather than the finger for better accuracy.
#### The Collapsible Section (The "Spoiler" Box)

This is perfect for "Answer Keys" or "Deep Dive" sections that you don't want to clutter the main page. Note the `???` instead of `!!!`.

Markdown

```
??? info "Click to expand: Pathophysiology of BC-specific strains"
    This section contains a deep dive into the local epidemiological data...
```

??? info "Click to expand: Pathophysiology of BC-specific strains"
    This section contains a deep dive into the local epidemiological data...

---

### Available Styles

The Material theme provides several built-in colors and icons:

|**Type**|**Color**|**Best Use Case**|
|---|---|---|
|`!!! info`|Blue|General helpful information.|
|`!!! tip`|Teal|Clinical pearls or shortcuts.|
|`!!! warning`|Orange|Cautions or important steps not to miss.|
|`!!! failure`|Red|Critical warnings, contraindications, or "don't do this".|
|`!!! example`|Purple|Case studies or specific examples.|
