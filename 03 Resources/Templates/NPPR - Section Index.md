---
title: <% tp.file.folder(false).replace(/^\d+\s+/, '') %>
type: index
tags: [index]
jurisdiction: [BC, CA]
status: draft
last-reviewed: <% tp.date.now("YYYY-MM-DD") %>
review-due: <% tp.date.now("YYYY-MM-DD", 365) %>
reviewers: []
---
<!-- Section buttons are added automatically by the website build on top-level section pages.
     Edit them in nppr-website-config/overrides/partials/section-nav.html.
     For a sub-folder index, add `section_nav: true` above to show them here too.
     Blocks, in this order (The page standard in NPPR-FRAMEWORK.md): intro line, section search box (tabs with five or more
     pages), In This Section, Also See. The build turns the In This Section list into cards: each page's `card-icon`
     (frontmatter, a Material icon name), its title, then the note here or the page's `description`. -->

*One sentence on what this section contains.*

<div class="nppr-filter nppr-filter--pages" data-section="Section Name" data-placeholder="Search all section pages, e.g. a term"></div>

## In This Section
- [Page Name](Page%20Name.md) — *one line on what the page holds, when the page has no description*
    - [Sub-page Name](Folder/Sub-page%20Name.md)

## Also See
- [Page in Another Tab](../Other%20Section/Page.md): why a reader here may want it.
