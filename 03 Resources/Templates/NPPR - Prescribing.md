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
  # BC sources first, then national, then international (INTL). Field list: FRONTMATTER.md
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
     NP prescribing rules (BCCNM limits, controlled drugs, PharmaNet, PRIME) live on Practice: Prescribing authority; link there. -->
*One or two sentences on what this page helps an NP check when prescribing.*

<div class="nppr-filter" data-ai="off" data-placeholder="Filter, e.g. monograph"></div>

## Key Sources

- [Publisher - Reference (year)](URL) — *what it covers* · *subscription*
    - [Sub-link, e.g. PDF or form](URL)

## Topic Heading

- [Publisher - Reference (year)](URL) — *what it covers*

## NP Prescribing Notes

- How the BCCNM standards apply, linked to [BCCNM - Nurse Practitioners: Prescribing Drugs](https://www.bccnm.ca/NP/PracticeStandards/Pages/Prescribing.aspx) or Practice: Prescribing authority.
