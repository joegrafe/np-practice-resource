# NPPR frontmatter schema

The frontmatter every page in `docs/` carries, taken from the Page standard in NPPR-FRAMEWORK.md. The templates in `03 Resources/Templates` follow it. A page carries no list of its sources (retired 2026-11-05): each document's details live once in `docs/sources.csv`, the sources registry, and the page's sheet names the document by its id in the `source` column (Sources registry in NPPR-FRAMEWORK.md).

## Example

```yaml
---
title: Hypertension
type: condition
system: cardiovascular
tags: [condition, cardiovascular, htn, adults]
jurisdiction: [BC, CA]
status: published
last-reviewed: 2026-04-16
review-due: 2027-04-16
reviewers: [joegrafe]
sources:
  - id: htn-canada-2025
    title: Hypertension Canada 2025 Primary Care Guidelines
    publisher: Hypertension Canada
    jurisdiction: CA
    kind: guideline
    version: "2025"
    url: https://hypertension.ca/guidelines/
    checked: 2026-04-16
  - id: bc-htn-algorithm
    title: "BC Guidelines: Hypertension, Appendix A algorithm"
    publisher: BC GPAC
    jurisdiction: BC
    kind: algorithm
    pdf: https://www2.gov.bc.ca/assets/gov/health/practitioner-pro/bc-guidelines/htn-appendix-a.pdf
    checked: 2026-04-16
    supersedes: null
---
```

## Page fields

| Field | Required | Values | Notes |
| --- | --- | --- | --- |
| `title` | Yes | Text | Page title as shown on the site. |
| `type` | Yes | `approach` · `assessment` · `condition` · `population` · `prescribing` · `practice` · `evidence-pack` · `resource` · `index` · `about` | `index` (section index pages) and `about` (About pages) are additions for pages the framework's list doesn't cover. |
| `system` | Condition pages only | One slug from the body-system list below | Must match the Conditions sub-folder. |
| `tags` | Yes | Lowercase, hyphenated list | First tag is the page type. Add the system, then any population and presenting-symptom tags that apply (see Tags below). |
| `jurisdiction` | Yes | List of codes from `docs/regions.csv` (`BC`, `CA`, `INTL`, `ON`, `AB` ...) | Every jurisdiction the page's sources cover, provinces first: `[BC, "ON", CA]`. Write `"ON"` in quotes, because YAML reads a bare `ON` as true. |
| `regions` | No | List of codes from `docs/regions.csv` | The regions whose sources were swept for this page, e.g. `[BC, ON]`, for the province switch. Leave out until a page has been swept for a second region. |
| `status` | Yes | `draft` · `review` · `published` | `draft` while writing, `review` when ready for a reviewer, `published` after review. |
| `last-reviewed` | Yes | `YYYY-MM-DD` | The date every source on the page was last checked. |
| `review-due` | Yes | `YYYY-MM-DD` | Usually `last-reviewed` plus one year. Sooner when a guideline update is expected. |
| `reviewers` | Yes | List of team ids | Who checked the page: each id is a row of the Team sheet, `docs/About/Team.csv` (Joe is `joegrafe`). The page shows their names under its title, linked to their cards on About > Team, and reviewers' cards list the pages that name them. Empty `[]` while in draft. A GitHub account is optional. |
| `aliases` | No | List of text | Other names a reader might search for: abbreviations, drug and brand names, plain words. Added to search only, not shown. Use this or the page's line in `hooks/search_aliases.yml` in nppr-website-config (Search in NPPR-FRAMEWORK.md). |
| `hide` | No | `[toc]`, `[navigation]`, `[suggest]`, `[report]` | `toc` and `navigation` are Material for MkDocs options; `suggest` hides the Suggest a link card and `report` hides only its GitHub issue button. |
| `section_nav` | No | `true` · `false` | Shows or hides the section buttons. |
| `logo` | No | Publisher's own image URL, or `/assets/logos/<name>` | Shown beside the title and on the section card. Link the publisher's file; host a copy in `docs/assets/logos/` only when Joe asks for one. |
| `logo-alt` | With `logo` | Text | The institution's name, used as the image's alt text. |
| `logo-bg` | No | CSS colour, quoted | Background behind a logo drawn for dark headers, e.g. `"#111"` for a white logo. |

## Tags

Population, presenting-symptom and `urgent-care` tags link to the [Browse by Tag](docs/Browse%20by%20Tag.md) page (under Home since 2026-11-03), which lists the pages under each one (step 2.3, build wave 13, approved by Joe 2026-11-02). Tag a page only when its own sources cover that population or symptom. Other tags (page type, system, keywords) stay plain words and aren't listed.

- **Populations:** `pediatrics`, `adolescents`, `older-adults`, `pregnancy`, `lactation`, `womens-health`, `trans-care`, `indigenous-health`, `newcomers`, `rural-remote`, `idd`. Use `pediatrics`, not `children`, and no `adults` tag: adults are the default.
- **Presenting symptoms:** the complaint headings of Presentations A to Z (`scripts/presentations.yml` in nppr-website-config), lowercase and hyphenated: for example `chest-pain`, `dyspnea`, `dysuria-and-urinary-symptoms`.
- **Setting:** `urgent-care`, for pages built for urgent or same-day presentations.

A tag only shows on Browse by Tag once it's in one of that page's `include` lists: add a new population or symptom tag there too.

## Sources registry (`docs/sources.csv`)

One row per document, shared by every page (since 2026-11-05). A page sheet row names the document in its `source` column and leaves the cells the registry fills blank; `scripts/check_pages.py` checks both.

| Column | Required | Values | Notes |
| --- | --- | --- | --- |
| `id` | Yes | Lowercase slug, unique | Publisher, topic and year, e.g. `bc-gpac-asthma`, `htn-canada-2025`. |
| `title` | Yes | Text | The document's own title. A page row may give its own title instead. |
| `publisher` | No | Text | The organization that publishes it, e.g. `BC GPAC`, `Hypertension Canada`. |
| `url` | `url` or `pdf` | Publisher's web page | |
| `pdf` | `url` or `pdf` | Publisher's own PDF link | Link only. Never upload or host a copy. |
| `year` | No | Text starting with a 4-digit year | The year shown beside the document on every page: `2023`, `2016, reaffirmed 2024`. |
| `version` | No | Text | Edition as the publisher states it (`v3.1`), when the year is not enough. |
| `region` | Yes | A code from `docs/regions.csv` (`BC` · `CA` · `INTL` · `ON` · `AB` ...) | The jurisdiction its content is written for, not the publisher's address. |
| `kind` | No | `guideline` · `algorithm` · `pathway` · `summary` · `tool` · `patient` | |
| `checked` | No | `YYYY-MM-DD` | The date the link and version were last confirmed. |
| `supersedes` | No | The `id` of the older version | Superseded versions never appear on a page. |
| `keywords` | No | Text | Extra search words. |

## Body systems

Condition pages use one of these `system` slugs, which match the Conditions sub-folders. Electrolyte disorders go under `endocrine-metabolic`.

| Folder | `system` |
| --- | --- |
| Cardiovascular | `cardiovascular` |
| Respiratory | `respiratory` |
| Endocrine and Metabolic | `endocrine-metabolic` |
| Renal and Genitourinary | `renal-genitourinary` |
| Gastrointestinal and Liver | `gastrointestinal-liver` |
| Musculoskeletal | `musculoskeletal` |
| Neurology | `neurology` |
| Mental Health and Substance Use | `mental-health-substance-use` |
| Infectious Disease | `infectious-disease` |
| Dermatology | `dermatology` |
| Hematology and Oncology | `hematology-oncology` |
| Eyes, Ears, Nose and Throat | `eyes-ears-nose-throat` |
| Sexual and Reproductive Health | `sexual-reproductive-health` |

## Rules

- Every source carries a region code from `docs/regions.csv`, in frontmatter `jurisdiction` and in the sheet's `region` column: the jurisdiction its content is written for. Order them provinces and territories first (BC first, as the default region), then `CA`, then `US`, then `INTL`, and label international guidance as such. A sheet row that is for its region alone (a referral line, drug coverage, a regulator's standard, a province's own quality standard) also carries `only=yes`, so it shows only in that region's view (List sheets in NPPR-FRAMEWORK.md).
- A page is its frontmatter plus one list sheet beside it (Page standard in NPPR-FRAMEWORK.md): every link, intro line, step and table is a sheet row. Section index pages and About pages are the exception.
- Link to each publisher's own page or PDF. Don't host or copy third-party documents.
- Don't write clinical recommendations in our own words. Link to the source guidance instead.

## Templates

| Template | `type` |
| --- | --- |
| NPPR - Approach | `approach` |
| NPPR - Approach.csv | List sheet to copy beside a new Approaches page (columns: List sheets in NPPR-FRAMEWORK.md) |
| NPPR - Condition.csv, Population.csv, Assessment.csv, Practice.csv, Prescribing.csv, Resource.csv | The `style=condition` list sheet to copy beside a new page of that type, renamed to the page's name; its first row is the intro line (`kind=md`), and every linked top-level row has a `region` (columns: List sheets in NPPR-FRAMEWORK.md) |
| NPPR - Assessment | `assessment` |
| NPPR - Condition | `condition` |
| NPPR - Population | `population` |
| NPPR - Practice | `practice` |
| NPPR - Prescribing | `prescribing` |
| NPPR - Resource | `resource` |
| NPPR - Section Index | `index` |
| NPPR - About Page | `about` |
