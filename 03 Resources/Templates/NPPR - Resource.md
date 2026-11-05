---
title: <% tp.file.title %>
type: resource
tags: [resource]
jurisdiction: [BC, CA]
status: draft
last-reviewed: <% tp.date.now("YYYY-MM-DD") %>
review-due: <% tp.date.now("YYYY-MM-DD", 365) %>
reviewers: []
---
<!-- What this resource page collects (a kind of source: libraries, guideline directories, journals) and which Resources pages hold neighbouring kinds.
     Sources unconfirmed because their sites block checks, and what was left out and why. -->
<!-- The page is its frontmatter plus <% tp.file.title %>.csv beside it, one row per line; the site build writes it in here.
     Copy NPPR - Resource.csv beside the page and rename it to the page's name. Edit the sheet, not this page.
     Columns: List sheets in NPPR-FRAMEWORK.md. The intro line is the first row (kind md, no heading).
     Sections by jurisdiction: BC, then Canadian, then specialty-society libraries, then International (each international row's note starts "International source:").
     Every linked top-level row carries a region code from docs/regions.csv. A directory row has no year unless the directory itself is dated.
     Access goes in the note after what the source holds: free sources need no label; say *subscription*, *login* or *institutional login* otherwise.
     A topic owned by another tab (pathways in Approaches, Therapeutics Letter in Prescribing) is one kind md row pointing there. -->
<div class="nppr-filter" data-ai="off" data-placeholder="Filter, e.g. library"></div>

<!-- nppr-list: <% tp.file.title %>.csv style=condition -->
