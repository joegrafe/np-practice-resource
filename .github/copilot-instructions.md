# Copilot review instructions for NPPR.ca content

This repo is the content of NPPR.ca, a point-of-care practice resource for BC and Canadian nurse practitioners. Pages live in `docs/` as Markdown with YAML frontmatter. The site is built by joegrafe/nppr-website-config (MkDocs). The full rules are in `NPPR-FRAMEWORK.md`, `FRONTMATTER.md` and `CLAUDE.md`; this file is the review checklist.

When reviewing a pull request, check the rules below and comment only where the change breaks one. Name the rule. Don't suggest clinical wording: the site links to guidance instead of restating it. Don't comment on items the PR checks workflow already reports (frontmatter fields, review dates, the sources registry, list-sheet format, new broken links) unless the workflow can't see them.

## Sources

- Order sources BC first, then national Canadian, then others, in every section of the sheet: that is the region rank, provinces and territories, then `CA`, then `US`, then `INTL`. Every frontmatter `jurisdiction` value, every registry row's `region` and every sheet row's `region` is a code from `docs/regions.csv`, the jurisdiction the content is written for (Alberta's Pathway Hub is `AB`, the UCalgary Black Book is `CA`, a US guideline is `INTL` until a US region is live). International guidance is labelled as such.
- For approaches and condition pages, AAFP (aafp.org, free articles only) is the first international source. Don't link Specialist Link's Calgary pathway when Alberta's Pathway Hub (primarycarealberta.ca) has one for the same condition.
- Link to each publisher's own page or PDF. Flag any third-party document added to the repo, or a link to a copy hosted somewhere other than the publisher.
- No clinical recommendations in our own words. Flag added text that gives doses, thresholds or management steps without linking the source that says it.
- One current version of each source per page. A superseded version appears only in the new source's `supersedes` field, never in the page body.
- One entry per guideline. Its PDF, appendices and algorithm are sub-links under that entry, not separate bullets, and the same document isn't linked from more than one section of a page.
- Show the year beside every guideline, algorithm and pathway in the page body.

## Condition pages

- Entry format: `- [Title (year)](publisher web page) · [PDF](pdf link) — *note*`. The PDF alone only when no publisher page links to it. In frontmatter the web page is `url` and the PDF is `pdf`.
- `## Key Sources` holds 1 to 3 entries: the BC Guideline first, then a more recent or broader national guideline, then one high-yield "approach to" or "management of" review. Everything else goes under `## Further Resources`, straight after Key Sources.
- Keep the BC Guidelines on the page, however old, at their current version.
- Remove summaries and reviews (PEER, journal reviews) older than the current version of the guideline they discuss, unless they cover something the guideline doesn't.
- Sections in order: Key Sources · Further Resources · Algorithms and pathways · Assessment tools and calculators · Prescribing · Advice and referral · Patient resources · Review notes. No Evidence Pack placeholder heading and no comment embeds.
- `system` matches the Conditions sub-folder.

## List sheets (Approaches, condition and other content pages)

- Approaches, condition, Assessments, Prescribing, Practice, Populations, Resources and AI Tools pages keep their link lists in the CSV beside the page (same name, `.csv`), written in by the `<!-- nppr-list: ... -->` marker at build time. Items are added, changed or removed in the CSV, never in the page. Flag list items added to the page body.
- Sheet columns: `heading, subheading, title, url, year, pdf, links, note, keywords, sub, region, only, source`, plus `kind` (blank, `box`, `note`, `md`) and `level` (blank, 0, 1, 2) on condition sheets. The year goes in `year`, not in `title`. Rows stay in the page's order. Flag a linked top-level row with no `region`, or a region code that isn't in `docs/regions.csv`.
- A new page is its frontmatter plus one sheet (Page standard, since 2026-11-05): its intro line is the sheet's first row (`kind=md`). Flag an intro line, heading or link written into the Markdown of a new page. Approaches pages keep their intro and More Approaches list in the page; pages built before 2026-11-05 keep their intro line until the switch wave.
- A document's facts live once in `docs/sources.csv` (the sources registry: id, title, publisher, url, pdf, year, version, region, kind, checked, supersedes, keywords). A sheet row names its document in `source` and leaves `url`, `pdf` and `year` blank (`-` keeps a cell blank on purpose). Flag a page that adds a frontmatter `sources` list, a row that repeats a registry document's url, PDF or year, a document added to two sheets instead of the registry, or a guideline update made on a page instead of in the registry row.
- The Approaches section is a complete list of each source's "approach to" articles, whatever their age. When a newer guideline covers the same topic, the approach stays and the guideline is added beside it (in `links`) with its year.

## Search

Search is the site's key feature and NPPR's own (assets/search.json, built by nppr-website-config). Flag:

- A new or renamed page with no search aliases (frontmatter `aliases` or a line in nppr-website-config's `hooks/search_aliases.yml`).
- Frontmatter `type`, `system`, `jurisdiction` or `tags` that don't match the page, or a sheet row's `region` that doesn't match its source: the search's filters and region badges come from them.
- A sheet row with its year or PDF in the title instead of the `year` and `pdf` columns.
- A new section, sheet column or list style with no matching change to `scripts/search_data.py` and `site_assets/nppr-search.js`.
- Text repeated on every page without `data-search-exclude`.

## Structure

- Adding, moving or removing a page updates the In This Section list on its section's `index.md` in the same PR.
- Frontmatter follows `FRONTMATTER.md`: `status` is `draft`, `review` or `published`; `reviewers` is `[]` while draft; `review-due` is usually `last-reviewed` plus one year.
- Changes go through a draft PR with a screenshot preview; Joe approves before a page is published or merged.
