@AGENTS.md

## NPPR build work

Before any NPPR build step, read NPPR-FRAMEWORK.md at the root of this vault. It holds the site structure, the page standard and the step-by-step build prompts. Follow these rules:

- BC sources first, then national Canadian sources, then others; label international guidance as such.
- For approaches and condition pages, AAFP (aafp.org) is the first international source, free articles only. Don't link Specialist Link's Calgary pathway when Alberta's Pathway Hub (primarycarealberta.ca) has a pathway for the same condition.
- Before researching any page, check every site in the Source map table in NPPR-FRAMEWORK.md: the All topics row plus the row for that page's system or population.
- Link to each publisher's own PDF only. Do not host or copy third-party documents.
- No clinical recommendations in our own words: link to the source guidance instead.
- One current version of each source per page. When a guideline is replaced, swap the link and record the old version only in that source's `supersedes` field; superseded versions never appear in the page body.
- One entry per guideline. Put its PDF, appendices and algorithm as sub-links under that entry, not as separate bullets, and don't link the same document from more than one section of a page.
- Show the year beside every guideline, algorithm and pathway in the page body.
- Always keep the BC Guidelines on a condition page, however old, and keep each one at its current version: when GPAC updates a guideline, replace the link and its year on every page that cites it.
- Remove summaries, reviews and "approach to" articles (PEER, AAFP, journal reviews) that predate the current version of the guideline they discuss, unless they cover something the guideline doesn't.
- When you add, move or remove a page, update the In This Section list on its section's index.md in the same change.
- Test-build the site and show the result before committing.
