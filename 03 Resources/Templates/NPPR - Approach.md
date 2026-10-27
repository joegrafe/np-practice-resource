---
title: <% tp.file.title %>
type: approach
tags: [approach]
jurisdiction: [CA]
status: draft
last-reviewed: <% tp.date.now("YYYY-MM-DD") %>
review-due: <% tp.date.now("YYYY-MM-DD", 365) %>
reviewers: []
description: "An index of <publisher>'s <article type>, grouped by body system."
logo: ""                   # publisher's own logo image URL (hotlinked)
logo-alt: ""
sources:
  # One entry per linked item. BC first, then national, then international (INTL). Field list: FRONTMATTER.md
  - id:
    title:
    publisher:
    jurisdiction: CA
    kind: summary          # guideline | algorithm | pathway | summary | tool | patient
    version:               # year or edition
    url:                   # publisher's web page for the item
    pdf:                   # publisher's own PDF link only
    checked: <% tp.date.now("YYYY-MM-DD") %>
---
<!-- List taken from <publisher index URL> on <date> (<n> items). Link to the items; don't copy them.
     An approach page is an index of a publisher's own "approach to" articles, schemes or pathways.
     NPPR writes no clinical steps, bias checks or pearls of its own. -->
*One sentence naming the publisher, what its items are, who writes them, and their jurisdiction (label international or other-province sources).*

[Open <publisher>](<publisher index URL>){ .md-button .md-button--primary target="_blank" rel="noopener" }

## <Items> by System

<div class="nppr-filter" data-placeholder="Filter <items>, e.g. pain"></div>

### <Body system> (<count>)

- [Item title (year)](web page) · [PDF](pdf link) — *note on what the link holds*

## More Approaches

- [Other approach page](Other%20Approach%20Page.md) — *what it holds*
