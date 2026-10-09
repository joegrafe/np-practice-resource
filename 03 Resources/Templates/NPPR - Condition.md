---
title: <% tp.file.title %>
type: condition
system: <% tp.file.folder(false).replace(/^\d+\s+/, '').toLowerCase().replace(/\band\b/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') %>
tags: [condition, <% tp.file.folder(false).replace(/^\d+\s+/, '').toLowerCase().replace(/\band\b/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') %>]
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
<!-- system comes from the folder name; check it against the list in FRONTMATTER.md.
     Add population and symptom tags (e.g. pediatrics, chest-pain).
     status: draft → review → published. Update last-reviewed and each source's checked date when links are re-checked.
     Link to the source guidance; don't restate its recommendations. -->

## Key Sources

??? info "[BC Guidelines - Condition Name (Year)](URL)"
	- [Key Recommendations](URL)  
	- [Summary PDF](URL)  

??? info "[National Guideline Name (Year)](URL)"
	*Only chapters relevant to primary care are listed here*  
	- [Chapter](URL)  

<!-- BC first, then national, then international (label it). One block per source in the sources list above. -->

## Algorithms and Pathways

- [Algorithm Name (Publisher, Year)](PDF URL)

<!-- BC first, then Alberta pathway hub. -->
## Assessment Tools and Calculators

- [Tool Name](URL) — *what it's for*

<!-- include relevant calculators from mdcalc.com first -->

## Prescribing

- [Drug reference or PharmaCare / Special Authority page](URL)

## Advice and Referral

- [RACE / Pathways / service](URL)

## Patient Resources

- [Resource Name (Publisher)](URL)

## Evidence Pack

*Pending: generated from the sources list in a later build step.*

---

<!-- Optional extras such as a Spotify embed go above this line. -->
<!-- Review notes as footnotes, e.g.  [^1]: *On YYYY-MM-DD references the 20XX guideline.* -->
