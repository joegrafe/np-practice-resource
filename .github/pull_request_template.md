<!-- Keep the three summary lines and tick what was done. The full list, with the rule behind each box, is "Before every pull request" in NPPR-FRAMEWORK.md. -->

**Before:**

**After:**

**How:**

## Checks

- [ ] Page checks: `python3 scripts/check_pages.py docs`, 0 errors
- [ ] Test build and search check (nppr-website-config `scripts/test-build.sh`, `node scripts/search-check.js`), result shown below
- [ ] New links opened; any site that blocks automated checks named here, and every promising source that would not open added to `UNOPENED-SOURCES.csv`
- [ ] Every source opened on the publisher's page, year matches, `docs/sources.csv` row with `checked` date, sheet row points at it in `source`; a replaced guideline changed in its registry row
- [ ] Region order kept, every linked row has `region`, one-region rows `only=yes`, BC key sources copied `only=other`, `"ON"` quoted
- [ ] Page is frontmatter plus one sheet; sections in order; Key Sources 1 to 3; RxFiles in Prescribing; no clinical advice in our own words
- [ ] Search: aliases, `scripts/search-checks.txt` lines, synonyms; frontmatter `type`, `system`, `jurisdiction`, `tags` accurate; search code changed if what it reads changed
- [ ] In This Section list and redirects updated for any page added, moved or removed
- [ ] New pages `status: draft`, `reviewers: []`, review dates set; review issue opened for a new condition page
- [ ] Screenshot or preview attached; paired PR in the other repository named, content first then config

## Build result

<!-- Paste the search-check line and the page-check counts. -->
