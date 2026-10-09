# NPPR frontmatter schema

The frontmatter every page in `docs/` carries, taken from the Page standard in NPPR-FRAMEWORK.md. The templates in `03 Resources/Templates` follow it. The `sources` list is the one place each guideline's details are recorded: later build steps read it to draw source blocks, Evidence Packs and the AI text files, so update a source here, not in the page body.

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
| `tags` | Yes | Lowercase, hyphenated list | First tag is the page type. Add the system, a population (`pediatrics`, `older-adults`) and a presenting symptom (`chest-pain`) where they apply. |
| `jurisdiction` | Yes | List of `BC`, `CA`, `INTL` | Every jurisdiction the page's sources cover. |
| `status` | Yes | `draft` · `review` · `published` | `draft` while writing, `review` when ready for a reviewer, `published` after review. |
| `last-reviewed` | Yes | `YYYY-MM-DD` | The date every source on the page was last checked. |
| `review-due` | Yes | `YYYY-MM-DD` | Usually `last-reviewed` plus one year. Sooner when a guideline update is expected. |
| `reviewers` | Yes | List of GitHub usernames | Who checked the page. Empty `[]` while in draft. |
| `sources` | Yes, except `index` and `about` | List of source entries (below) | List BC sources first, then national, then international. |
| `hide` | No | `[comments]`, `[toc]`, `[navigation]` | Material for MkDocs option. Section index and About pages hide comments. |
| `section_nav` | No | `true` · `false` | Shows or hides the section buttons. |

## Source fields

| Field | Required | Values | Notes |
| --- | --- | --- | --- |
| `id` | Yes | Lowercase slug, unique across the site | Publisher, topic and year, e.g. `htn-canada-2025`. Evidence Packs and the manifest key on it. |
| `title` | Yes | Text | The source's own title. Quote it if it contains a colon. |
| `publisher` | Yes | Text | The organization that publishes it, e.g. `BC GPAC`, `Hypertension Canada`. |
| `jurisdiction` | Yes | `BC` · `CA` · `INTL` | Label international guidance as `INTL`. |
| `kind` | Yes | `guideline` · `algorithm` · `pathway` · `summary` · `tool` · `patient` | |
| `version` | When the publisher gives one | Text, quoted | Year or edition as the publisher states it, e.g. `"2025"`, `"v3.1"`. |
| `url` | `url` or `pdf` | Publisher's web page | |
| `pdf` | `url` or `pdf` | Publisher's own PDF link | Link only. Never upload or host a copy. |
| `checked` | Yes | `YYYY-MM-DD` | The date the link and version were last confirmed. |
| `supersedes` | No | The `id` of an older source, or `null` | Keeps superseded versions visible in the Evidence Pack. |

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

- BC sources first, then national Canadian sources, then others. Label international guidance as such.
- Link to each publisher's own page or PDF. Don't host or copy third-party documents.
- Don't write clinical recommendations in our own words. Link to the source guidance instead.

## Templates

| Template | `type` |
| --- | --- |
| NPPR - Approach | `approach` |
| NPPR - Assessment | `assessment` |
| NPPR - Condition | `condition` |
| NPPR - Population | `population` |
| NPPR - Practice | `practice` |
| NPPR - Resource | `resource` (change to `prescribing` for pages in the Prescribing section) |
| NPPR - Section Index | `index` |
| NPPR - About Page | `about` |
