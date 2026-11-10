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
     Assessment Tools and Calculators: a BC or Canadian calculator first (BC Guidelines appendices, Thrombosis Canada clinical tools), then MDCalc and other sites as required. Not MDCalc's Framingham (hard coronary model): use BC Guidelines CVD Appendix B.
     Prescribing: always the RxFiles page when RxFiles has an appropriate resource (note when it needs a subscription). Special Authority criteria and forms go last, in one box.
     Advice and Referral: RACE, then the Pathways BC directory row (source pathways-bc, only=yes) with the specialty to search in its note, then other regions' lines. check_pages.py fails a condition sheet without the Pathways row.
     Every linked top-level row carries a region code from docs/regions.csv (BC, AB, ON, CA, US, INTL): the jurisdiction the content is written for, not the publisher's address.
     A row for its region alone (the BC Guideline in Key Sources, Special Authority, RACE, a CEP tool, Ontario eConsult, a quality standard) is only=yes; the BC key source gets a one-line copy at the top of Further Resources marked only=other. check_pages.py fails a condition sheet without them.
     A document's facts (title, publisher, url, pdf, year, region, checked) go in docs/sources.csv once; the row names it in the source column and leaves url, pdf and year blank.
     Review notes as footnotes go below the marker, e.g.  [^1]: *On YYYY-MM-DD references the 20XX guideline.* -->
<!-- nppr-list: <% tp.file.title %>.csv style=condition -->
