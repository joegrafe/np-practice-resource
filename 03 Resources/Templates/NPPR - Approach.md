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
---
<!-- List taken from <publisher index URL> on <date> (<n> items). Link to the items; don't copy them.
     An approach page is an index of a publisher's own "approach to" articles, schemes or pathways.
     NPPR writes no clinical steps, bias checks or pearls of its own. -->
*One sentence naming the publisher, what its items are, who writes them, and their jurisdiction (label international or other-province sources).*

[Open <publisher>](<publisher index URL>){ .md-button .md-button--primary target="_blank" rel="noopener" }

## <Items> by System

<div class="nppr-filter" data-placeholder="Filter <items>, e.g. pain"></div>

<!-- The list lives in <Page name>.csv beside this page, one row per item; the site build writes it in here.
     Edit the sheet, not this page, to change the list. Start the sheet from "NPPR - Approach.csv" in Templates.
     Every row carries a region code from docs/regions.csv (the jurisdiction the item is written for, usually the publisher's own).
     Approaches pages are the one exception to "frontmatter plus one sheet": the intro line and More Approaches stay in the page. -->
<!-- nppr-list: <Page name>.csv counts -->

## More Approaches

- [Other approach page](Other%20Approach%20Page.md) — *what it holds*
