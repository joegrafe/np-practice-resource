---
title: <% tp.file.title %>
type: population
tags: [population, <% tp.file.title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') %>]
jurisdiction: [BC, CA]
status: draft
last-reviewed: <% tp.date.now("YYYY-MM-DD") %>
review-due: <% tp.date.now("YYYY-MM-DD", 365) %>
reviewers: []
sources:
  # BC sources first, then national, then international (INTL). Field list: FRONTMATTER.md
  - id:
    title:
    publisher:
    jurisdiction: BC
    kind: guideline        # guideline | algorithm | pathway | summary | tool | patient
    version:
    url:
    pdf:                   # publisher's own PDF link only
    checked: <% tp.date.now("YYYY-MM-DD") %>
---
<!-- Every section lives in the CSV list sheet beside this page (copy NPPR - Population.csv and give it the page's name; format: List sheets in NPPR-FRAMEWORK.md).
     Link to the source guidance; don't restate its recommendations. -->
*One sentence on who this population is and what this page collects for them.*

<!-- nppr-list: <% tp.file.title %>.csv style=condition -->
