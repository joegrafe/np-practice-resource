---
title: <% tp.file.title %>
type: assessment
tags: [assessment]
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
<!-- Which exam, test or tool family this page indexes across conditions, and what lives elsewhere (condition pages keep their own tools; drug calculators are on Prescribing).
     Sources unconfirmed because their sites block checks, and what was left out and why.
     Link to the source; don't restate its technique, criteria or cut-offs. -->
<!-- The page is its frontmatter plus <% tp.file.title %>.csv beside it, one row per line; the site build writes it in here.
     Copy NPPR - Assessment.csv beside the page and rename it to the page's name. Edit the sheet, not this page.
     Columns: List sheets in NPPR-FRAMEWORK.md. The intro line is the first row (kind md, no heading).
     Sections: Key Sources (1 to 3), then sections by system or topic in the order of the page's plan, with the subheading column for "###" headings.
     Every linked top-level row carries a region code from docs/regions.csv (BC, CA, US, INTL ...); a US rule or a UK score is INTL until that region is live.
     Put the year in the year column, not the title. A link to another NPPR page is a kind md row. -->
<div class="nppr-filter" data-ai="off" data-placeholder="Filter, e.g. ankle"></div>

<!-- nppr-list: <% tp.file.title %>.csv style=condition -->
