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

<!-- The page's sections live in <% tp.file.title %>.csv beside this page, one row per line; the site build writes them in here.
     Copy NPPR - Condition.csv beside the page and rename it to the page's name. Edit the sheet, not this page, to change a link.
     Columns: List sheets in NPPR-FRAMEWORK.md. Put each year in the year column, not the title.
     Key Sources: 1 to 3 only. BC Guideline first, then a more recent or broader national guideline, then one high-yield "approach to" or "management of" review.
     Further Resources: every other source, BC first, then national, then international (label it). One box or line per guideline, its PDF, algorithm and chapters on level 1 rows under it.
     Algorithms and Pathways: BC first, then Alberta's Pathway Hub.
     Assessment Tools and Calculators: MDCalc first, then other sites as required.
     Prescribing: Special Authority criteria and forms go last, in one box.
     Keep frontmatter sources in step with the sheet: one entry per guideline, algorithm, pathway and tool it links.
     Review notes as footnotes go below the marker, e.g.  [^1]: *On YYYY-MM-DD references the 20XX guideline.* -->
<!-- nppr-list: <% tp.file.title %>.csv style=condition -->
