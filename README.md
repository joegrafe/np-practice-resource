# NP Practice Resource

NPPR.ca is a free, open index of current BC and Canadian clinical guidance for primary care and urgent care nurse practitioners.

It is organized around the steps of an appointment so an NP can find the right high-yield source quickly and confidently during patient care.

## Why it exists

NPs increasingly use AI tools that suggest diagnoses and plans. Someone still has to check those suggestions, and that someone is the NP, as the human in the loop.

NPPR.ca gives the NP fast access to the authoritative source for each step of care so they can verify or overrule what the AI says.

There is no other open, BC-first index like this. The national guideline index (CMA CPG Infobase) closed in 2023, and most similar sites are written for physicians, cover one topic, or require a login.

## How it works

Each tab matches a step of the visit:

- Approaches — presenting complaint and differential
- Assessments — history, exam and tests
- Conditions — diagnosis and management
- Populations — who the patient is
- Prescribing — treatment and coverage
- Practice — scope, referral, and forms
- Tools — loading current guidelines into AI tools
- Resources — background reading and supporting sources

## Core principles

- Link, don’t rewrite. NPPR points to the publisher’s own guideline and does not write clinical recommendations of its own.
- BC first, then national Canadian sources, then international sources, clearly labelled as such.
- Dated and current. Every guideline shows its year, and superseded versions are removed from the page.
- Open and free. No login required. The site installs as a phone app, and every change is tracked publicly on GitHub.

## Current status

The site currently includes condition pages and population pages, with a master plan outlining additional pages to build across every tab.

Next priorities include:
- NP scope and prescribing authority
- drug coverage
- lab and imaging guidance
- Evidence Packs for loading current guideline sets into AI tools like Heidi Evidence

## How you can help

There are several ways to contribute:

- Suggest a link from any page, or through the site’s submissions workflow
- Review a page in your area of practice
- Build pages using the shared page templates and source rules
- Help with site infrastructure, search, layout, or the Evidence Pack builder
- Contribute documentation, templates, or community resources

This project is maintained across:
- `np-practice-resource` — content, templates, governance, source standards
- `nppr-website-config` — site build and layout
- `nppr-templates` — reusable templates and community content

## Repository structure

- `docs/` — published site content
- `00 Inbox/` — unprocessed links and rough resources
- `01 Projects/` — active work
- `02 Areas/` — feature and workflow areas
- `03 Resources/` — templates and reference material
- `04 Archive/` — historical and superseded content
- `.github/` — GitHub automation and workflows
- `scripts/` — helper scripts
- `NPPR-FRAMEWORK.md` — master project framework and roadmap
- `FRONTMATTER.md` — metadata and page structure standards
- `CLAUDE.md` — project workflow and AI-assisted operational notes
- `LICENSE` — project license

## Get involved

To contribute or collaborate, contact Joe Grafe or start a conversation in the NPPR GitHub discussions.

## License

See [LICENSE](LICENSE).
