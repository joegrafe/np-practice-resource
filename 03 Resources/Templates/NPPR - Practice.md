---
title: <% tp.file.title %>
type: practice
tags: [practice]
jurisdiction: [BC, CA]
status: draft
last-reviewed: <% tp.date.now("YYYY-MM-DD") %>
review-due: <% tp.date.now("YYYY-MM-DD", 365) %>
reviewers: []
sources:
  # Codes from docs/regions.csv: provinces and territories first (BC first), then CA, then US, then INTL. Field list: FRONTMATTER.md
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
<!-- Which practice topic this page covers for NPs and what lives on other Practice pages.
     Link each standard or rule to its source (the regulator, ministry or program).
     Sources unconfirmed because their sites block checks, and what was left out and why. -->
<!-- The page is its frontmatter plus <% tp.file.title %>.csv beside it, one row per line; the site build writes it in here.
     Copy NPPR - Practice.csv beside the page and rename it to the page's name. Edit the sheet, not this page.
     Columns: List sheets in NPPR-FRAMEWORK.md. The intro line is the first row (kind md, no heading).
     Sections: Key Sources (1 to 3), one section per standard or rule, "How to Do It in <Region>" (numbered steps in one kind md row, each step linked to its form or system), Contacts (kind md rows).
     Every linked top-level row carries a region code from docs/regions.csv: a regulator's standard is its province's code (BC for BCCNM), a federal rule is CA.
     A second region's rules go on the same sheet with their own code, in a section named for that region, so the province switch can sort them. -->
<div class="nppr-filter" data-ai="off" data-placeholder="Filter, e.g. renewal"></div>

<!-- nppr-list: <% tp.file.title %>.csv style=condition -->
