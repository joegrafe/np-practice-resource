# Copilot review instructions for NPPR.ca content

This repo is the content of NPPR.ca, a point-of-care practice resource for BC and Canadian nurse practitioners. Pages live in `docs/` as Markdown with YAML frontmatter. The site is built by joegrafe/nppr-website-config (MkDocs). The full rules are in `NPPR-FRAMEWORK.md`, `FRONTMATTER.md` and `CLAUDE.md`; this file is the review checklist.

When reviewing a pull request, check the rules below and comment only where the change breaks one. Name the rule. Don't suggest clinical wording: the site links to guidance instead of restating it. Don't comment on items the PR checks workflow already reports (frontmatter fields, review dates, source order in frontmatter, list-sheet format, new broken links) unless the workflow can't see them.

## Sources

- Order sources BC first, then national Canadian, then others, in the frontmatter `sources` list and in every section of the page body. International guidance is labelled as such (`jurisdiction: INTL`).
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
- Sheet columns: `heading, subheading, title, url, year, pdf, links, note, keywords, sub`, plus `kind` (blank, `box`, `note`, `md`) and `level` (blank, 0, 1, 2) on condition sheets. The year goes in `year`, not in `title`. Rows stay in the page's order.
- When a condition sheet row changes, its source entry in the page's frontmatter `sources` changes in the same PR.
- The Approaches section is a complete list of each source's "approach to" articles, whatever their age. When a newer guideline covers the same topic, the approach stays and the guideline is added beside it (in `links`) with its year.

## Search

Search is the site's key feature and NPPR's own (assets/search.json, built by nppr-website-config). Flag:

- A new or renamed page with no search aliases (frontmatter `aliases` or a line in nppr-website-config's `hooks/search_aliases.yml`).
- Frontmatter `type`, `system`, `jurisdiction` or `tags` that don't match the page: the search's filters and region badges come from them.
- A sheet row with its year or PDF in the title instead of the `year` and `pdf` columns.
- A new section, sheet column or list style with no matching change to `scripts/search_data.py` and `site_assets/nppr-search.js`.
- Text repeated on every page without `data-search-exclude`.

## Structure

- Adding, moving or removing a page updates the In This Section list on its section's `index.md` in the same PR.
- Frontmatter follows `FRONTMATTER.md`: `status` is `draft`, `review` or `published`; `reviewers` is `[]` while draft; `review-due` is usually `last-reviewed` plus one year.
- Changes go through a draft PR with a screenshot preview; Joe approves before a page is published or merged.
