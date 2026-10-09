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
<!-- Link to the source guidance; don't restate its recommendations. -->
*One sentence on who this population is and what this page collects for them.*

## Key Sources

??? info "[BC Source Name (Publisher, Year)](URL)"
	- [Section](URL)  

??? info "[National Source Name (Publisher, Year)](URL)"
	- [Section](URL)  

## Screening and Preventive Care

- [Screening guideline or schedule (Publisher, Year)](URL)

## Conditions with Population Notes

- [Condition Page](../3%20Conditions/System/Condition.md) — *which part applies to this population*

## Services and Referral

- [Service Name](URL) — *who it serves and how to refer*

## Patient Resources

- [Resource Name (Publisher)](URL)
