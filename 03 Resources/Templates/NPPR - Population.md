---
title: <% tp.file.title %>
type: population
tags: [population, <% tp.file.title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') %>]
jurisdiction: [BC, CA]
status: draft
last-reviewed: <% tp.date.now("YYYY-MM-DD") %>
review-due: <% tp.date.now("YYYY-MM-DD", 365) %>
reviewers: []
---
<!-- The page is its frontmatter plus the CSV list sheet beside it (copy NPPR - Population.csv and give it the page's name; format: List sheets in NPPR-FRAMEWORK.md).
     The intro line is the sheet's first row (kind md, no heading); every linked top-level row carries a region code from docs/regions.csv.
     Link to the source guidance; don't restate its recommendations. -->

<!-- nppr-list: <% tp.file.title %>.csv style=condition -->
