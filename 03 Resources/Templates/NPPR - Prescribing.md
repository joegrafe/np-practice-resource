---
title: <% tp.file.title %>
type: prescribing
tags: [prescribing]
jurisdiction: [BC, CA]
status: draft
last-reviewed: <% tp.date.now("YYYY-MM-DD") %>
review-due: <% tp.date.now("YYYY-MM-DD", 365) %>
reviewers: []
description: ""
sources:
  # Codes from docs/regions.csv: provinces and territories first (BC first), then CA, then US, then INTL. Field list: FRONTMATTER.md
  - id:
    title:
    publisher:
    jurisdiction: BC
    kind: tool             # guideline | algorithm | pathway | summary | tool | patient
    version:
    url:
    pdf:                   # publisher's own PDF link only
    checked: <% tp.date.now("YYYY-MM-DD") %>
---
<!-- Link to each reference; don't give dosing or recommendations in our own words.
     Label access after the note: *subscription*, *login* or *members only*. Free sources need no label.
     NP prescribing rules (BCCNM limits, controlled drugs, PharmaNet, PRIME) live on Practice: Prescribing Authority; link there with a kind md row.
     Sources unconfirmed because their sites block checks, and what was left out and why. -->
<!-- The page is its frontmatter plus <% tp.file.title %>.csv beside it, one row per line; the site build writes it in here.
     Copy NPPR - Prescribing.csv beside the page and rename it to the page's name. Edit the sheet, not this page.
     Columns: List sheets in NPPR-FRAMEWORK.md. The intro line is the first row (kind md, no heading).
     Sections: Key Sources (1 to 3; RxFiles whenever it has a fitting resource, with a note when it needs a subscription), topic sections, NP Prescribing Notes last.
     Every linked top-level row carries a region code from docs/regions.csv: drug coverage and Special Authority rows are their province's code (BC for PharmaCare), Health Canada is CA, a US or UK reference is INTL. -->
<div class="nppr-filter" data-ai="off" data-placeholder="Filter, e.g. monograph"></div>

<!-- nppr-list: <% tp.file.title %>.csv style=condition -->
