# NPPR Framework

Exported 2026-10-09 from the NPPR Framework doc (https://claude.ai/code/artifact/5e9d248a-789d-4815-8f25-a3c965081661). The doc is the master copy: re-export this file whenever the doc changes. Part 1 is the framework; Part 2 is the step-by-step build prompts.

---

# Part 1: Benchmarking and Structure

## Summary

NPPR is the only open, BC-first, NP-focused index of Canadian practice sources. The sites it resembles each do one job. Some publish their own guidance (BC Guidelines, PEER, RxFiles, AMMI Canada's antibiotic guidance). Others are referral or advice services (Pathways, RACE) or member portals (NNPBC). The one national index of Canadian guidelines, CMA's CPG Infobase, was shut down in December 2023.

The recommendation is for NPPR to fill that gap for BC NPs: a curated, dated index of the current BC and Canadian sources for each topic, readable by a clinician at the bedside and by an AI tool. NPPR should link to guidance and record its version and date, not write its own clinical recommendations.

Three changes get it there:

1. **One structure and one page standard.** Eight top-level sections, a fixed list of body systems, and frontmatter that records each source's publisher, jurisdiction, version and the date it was last checked.
2. **An Evidence Pack for each condition.** A page, generated from that frontmatter, that lists the exact current guideline and algorithm PDFs an NP needs to load into Heidi Evidence's My Library or another AI tool, with a manifest showing what is current and what has been superseded.
3. **Visible currency.** A review date on every page, automated weekly link checks, and a review step on GitHub before clinical pages are published.

## Comparable Canadian sites

Each of these does one job well. None indexes current BC and Canadian sources by topic for NPs, and none is set up for loading into an AI tool. Details come from each site's own pages, checked 2026-10-09.

| Site | Who makes it | Audience and access | What it offers | Lesson for NPPR |
| --- | --- | --- | --- | --- |
| [BC Guidelines](https://www2.gov.bc.ca/gov/content/health/practitioner-professional-resources/bc-guidelines) | GPAC, a joint committee of the BC Ministry of Health and Doctors of BC | BC practitioners; free | Provincial guidelines by topic; the whole collection downloads as one 67.7 MB ZIP | The main BC source. The single ZIP makes it easy to load into an AI library. |
| [Pathways](https://divisionsbc.ca/provincial/what-we-do/practice-support/pathways) | Divisions of Family Practice; regional administrators curate the data | Family physicians in a division, their staff, and NPs; login required | Specialist wait times and expertise, patient and physician resources, Referral Tracker | Link to it from each condition page instead of duplicating it. |
| [RACE](https://healthcareexcellence.ca/en/resources/race-rapid-access-to-consultative-expertise) | Providence Health Care, Vancouver Coastal Health, Shared Care Committee | Family physicians and NPs; one phone line, Mon to Fri 8:00 to 17:00 PT | Real-time phone advice from specialists | Give each condition page an Advice and referral block. |
| [PEER resources](https://acfp.ca/research-and-tools/peer-resources/) and [Tools for Practice](https://cfpclearn.ca/tools-for-practice-library/) | PEER team (pharmacists, nurses, family physicians) with ACFP; hosted on CFPCLearn | Mainly family physicians; articles emailed free, 0.25 Mainpro+ credits each | 200+ evidence summaries; simplified guidelines for chronic pain, lipids and opioid use disorder | Link these as plain-language evidence summaries on condition pages. |
| [RxFiles](https://www.rxfiles.ca/rxfiles/modules/aboutus/AboutUs.aspx) | RxFiles Academic Detailing, University of Saskatchewan | Front-line practitioners; app needs a subscription | Drug Comparison Charts (15th edition, July 2025), app, Q&As, patient handouts | A model for a Prescribing section that links out rather than copying. |
| [Firstline: Canadian Antibiotic Treatment Guidance](https://firstline.org/canada/) | AMMI Canada, supported by PHAC | Primary care prescribers; free app and web | National antibiotic guidance, starting with respiratory infections | Cite on every infection page. |
| [Thrombosis Canada app](https://krs.libguides.com/mobile/thrombosiscanada) | Thrombosis Canada | Canadian health care providers; no ads, works offline | Clinical guides and calculators, e.g. perioperative anticoagulation | Shows the value of offline access and built-in calculators, which NPPR already has as a PWA. |
| Centre for Effective Practice | CEP, co-lead of [Evidence2Practice Ontario](https://digitalhealthcanada.com/?p=33928) | Ontario primary care | Point-of-care tools, including Ontario Health quality standards built into EMRs | Structured tools fit into clinical workflow. |
| [CMA CPG Infobase](https://lists.koumbit.net/pipermail/canmedlib-chlaabsc.koumbit.org/2023-September/001674.html) | Canadian Medical Association | All clinicians | Database of Canadian clinical practice guidelines | Shut down December 1, 2023; there is no national guideline index now. |
| [NNPBC NP Portal](https://www.nnpbc.com/np-portal/) | Nurses and Nurse Practitioners of BC | BC NPs; some resources members-only | Practice supports and a searchable content library | Link to it for NP practice and scope topics. |

## Strengths and gaps

NPPR has the strongest publishing model of the group but the thinnest coverage and the weakest signals of currency. As of 2026-10-09 the site has 35 pages and 246 unique external links. 23 pages have frontmatter, and 9 have a last-reviewed date.

**What NPPR already does better than its peers**

- Free and open, with no login. Pathways, RxFiles' app and parts of NNPBC are gated.
- BC-first and written for NPs, where most peers are written for physicians or are national.
- Every change is versioned in Git, and readers can suggest edits through GitHub.
- Installs as an offline app, like the Thrombosis Canada app.

**Gaps the comparison exposes**

- **Coverage.** There are 8 condition pages, against the much larger list of topics BC Guidelines alone covers.
- **Inconsistent pages.** Resource pages range from a single bare link (Pediatrics) to a full summary (Trans Care), and 12 pages have no frontmatter at all.
- **No visible currency.** Last-reviewed dates sit in frontmatter but are not shown on the page. The git-revision-date plugin is listed in requirements.txt but not turned on in mkdocs.yml.
- **No source metadata.** Links don't record a publisher, version or jurisdiction, so neither a reader nor an AI tool can tell a 2018 guideline from its 2025 replacement.
- **Missing layers.** There is no prescribing layer (RxFiles, Firstline, PharmaCare Special Authority), no advice and referral layer (RACE, Pathways), and no NP scope and regulation content (BCCNM standards).
- **One way in.** Conditions are reached only by body system. There is no entry by population (children, pregnancy, older adults, rural practice) or by presenting symptom.

## Recommended structure

NPPR should have eight top-level sections. Four keep their current names and four are new. Population, prescribing and practice content moves out of Resources into sections of its own, so Resources holds only general directories.

| # | Section | Holds | Moves in from today |
| --- | --- | --- | --- |
| 1 | Approaches | Clinical reasoning frameworks, documentation, using AI tools safely | A Systematic Approach, UCalgary Black Books |
| 2 | Assessments | Exams by system, decision rules, screening, lab and imaging interpretation | Assessment Resources |
| 3 | Conditions | One page per condition, grouped by body system | All 8 condition pages |
| 4 | Populations (new) | Pediatrics, pregnancy and perinatal, older adults, women's health, trans and gender-affirming care, Indigenous health and cultural safety, rural and remote | Pediatrics folder, Trans Care, Woman's Health, BC Rural Health |
| 5 | Prescribing (new) | Drug references, antimicrobials, PharmaCare and Special Authority, immunization, deprescribing, controlled drugs | Bugs & Drugs, BC Immunization Manual |
| 6 | Practice (new) | NP scope and BCCNM standards, advice and referral (RACE, Pathways), forms, associations | Associations |
| 7 | Evidence Packs (new) | One pack per condition for loading into AI tools, plus how-to guides | none |
| 8 | Resources | Guideline directories, libraries, evidence summaries, CPD | BC Guidelines, Guidelines folder, Library Guides, Peerevidence.ca, Clinical Tools |

About stays as it is, as a separate tab after Resources.

**Body systems under Conditions.** Use one fixed list so the folders, tags and Evidence Packs all line up: Cardiovascular; Respiratory; Endocrine and Metabolic; Renal and Genitourinary; Gastrointestinal and Liver; Musculoskeletal; Neurology; Mental Health and Substance Use; Infectious Disease; Dermatology; Hematology and Oncology; Eyes, Ears, Nose and Throat; Sexual and Reproductive Health. Electrolyte disorders stay under Endocrine and Metabolic.

**Second ways in.** Tags give each condition page a population and a presenting symptom, such as `pediatrics` or `chest-pain`. The Material tags plugin is already enabled, so readers can browse by those tags without duplicating any pages.

## Page standard

Every page carries the same frontmatter. Its `sources` list is the one place where each guideline's details are recorded. The build reads it to draw the page's source blocks, its Evidence Pack and the AI text files, so a source updated once is updated everywhere.

```yaml
---
title: Hypertension
type: condition            # approach | assessment | condition | population | prescribing | practice | evidence-pack | resource
system: cardiovascular     # condition pages only, from the fixed list
tags: [condition, cardiovascular, htn, adults]
jurisdiction: [BC, CA]
status: published          # draft | review | published
last-reviewed: 2026-04-16
review-due: 2027-04-16
reviewers: [joegrafe]
sources:
  - id: htn-canada-2025
    title: Hypertension Canada 2025 Primary Care Guidelines
    publisher: Hypertension Canada
    jurisdiction: CA
    kind: guideline        # guideline | algorithm | pathway | summary | tool | patient
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

The same rule applies to every page type: provincial sources first, then national, then other sources, each labelled with its publisher and year.

| Page type | Sections, in order |
| --- | --- |
| Condition | Key sources (BC, then national) · Algorithms and pathways · Assessment tools and calculators · Prescribing · Advice and referral · Patient resources · Evidence Pack link · Review notes |
| Assessment | Scope · Focused history · Exam and special tests · Decision rules · Red flags · Learning videos · Sample documentation · References |
| Approach | Purpose · Numbered steps with bias checks · Clinical pearls · References |
| Population | Key sources · Screening and preventive care · Conditions with population notes (links) · Services and referral · Patient resources |
| Prescribing | Reference · What it covers · Access (free, subscription, PharmaCare) · NP prescribing notes, linked to BCCNM standards |
| Practice | Topic · Standard or rule, linked to its source · How to do it in BC · Contacts |
| Evidence Pack | Generated from frontmatter: the source manifest table · Download links · Superseded versions · Changelog |
| Resource | Organization · Title · Link · What it covers · Access and scope |

The six templates already in the vault map onto these types. They would need `type`, `jurisdiction`, `review-due` and `sources` added, and two new templates for Population and Practice pages.

## Source map

Before writing or reviewing any page, check every site in the "All topics" row and in the row for that page's system or population. Search in the order the columns run: BC, then Canadian, then calculators, then patient resources. Use American or international sources only where no BC or Canadian source covers the question, and label them as such. For approaches and condition pages, AAFP (aafp.org) is the first international source to check, using only articles that are free to read; then USPSTF, NICE, Cochrane and TRIP. Where Alberta's Pathway Hub (primarycarealberta.ca) has a pathway for a condition, link it and leave out Specialist Link's Calgary pathway for the same condition, which repeats it. Add a site to this table whenever a new one proves useful.

| System or topic | BC | Canadian | Calculators and tools | Patient resources |
| --- | --- | --- | --- | --- |
| All topics | BC Guidelines and PharmaCare (gov.bc.ca), BCCDC (bccdc.ca), RACE (raceconnect.ca), Pathways (pathwaysbc.ca) | Canadian Task Force on Preventive Health Care (canadiantaskforce.ca), Choosing Wisely Canada, PEER and Tools for Practice (peerevidence.ca, cfpclearn.ca), Canadian Family Physician (cfp.ca) | MDCalc (mdcalc.com) | HealthLinkBC (healthlinkbc.ca) |
| Approaches (and "approach to" reviews on condition pages) | none listed yet | McGill Journal of Medicine "Approach to" articles (mjm.mcgill.ca), UCalgary Black Book (blackbook.ucalgary.ca); AAFP (aafp.org, free articles only) as the first international source | none listed yet | none listed yet |
| Cardiovascular | Cardiac Services BC (cardiacbc.ca) | Hypertension Canada, Canadian Cardiovascular Society (ccs.ca, onlinecjc.ca), Canadian Heart Failure Society (heartfailure.ca), Canadian Heart Rhythm Society (chrsonline.ca), Thrombosis Canada | MDCalc: CHA2DS2-VASc, HAS-BLED, Framingham | Heart & Stroke (heartandstroke.ca) |
| Respiratory | BC Guidelines (asthma, COPD) | Canadian Thoracic Society (cts-sct.ca), Lung Association (lung.ca); GOLD and GINA (international) | MDCalc: Wells and PERC for PE; GOLD COPD tools | Lung Association |
| Endocrine and Metabolic | BC Guidelines | Diabetes Canada (diabetes.ca), Obesity Canada, Osteoporosis Canada (osteoporosis.ca) | MDCalc: BMI; FRAX (frax.shef.ac.uk) | Diabetes Canada, Obesity Canada |
| Renal and Genitourinary | BC Renal (bcrenal.ca) | KDIGO (international), Canadian Urological Association (cua.org) | MDCalc: CKD-EPI eGFR, Kidney Failure Risk Equation | BC Renal |
| Gastrointestinal and Liver | BC Guidelines | Canadian Association of Gastroenterology (cag-acg.org) | MDCalc: FIB-4, Child-Pugh | HealthLinkBC |
| Musculoskeletal | BC Guidelines | Canadian Rheumatology Association (rheum.ca), RheumInfo, RheumGuide | MDCalc: Ottawa ankle and knee rules; OrthoBullets, Physiopedia | RheumInfo |
| Neurology | BC Guidelines | Alzheimer Society (alzheimer.ca), Heart & Stroke for stroke | MoCA (mocacognition.com); MDCalc: NIHSS, ABCD2 | Alzheimer Society |
| Mental Health and Substance Use | BCCSU (bccsu.ca), HeretoHelp (heretohelp.bc.ca) | CANMAT, CAMH, CADDRA, META:PHI (metaphi.ca), Canadian Psychiatric Association | MDCalc: PHQ-9, GAD-7 | HeretoHelp, CAMH |
| Infectious Disease | BCCDC, BC Centre for Excellence in HIV/AIDS (bccfe.ca), ImmunizeBC | AMMI Canada and Firstline (firstline.org), NACI and STI guidelines (canada.ca), Bugs & Drugs | MDCalc: Centor (McIsaac) | HealthLinkBC, ImmunizeBC, Smart Sex Resource |
| Dermatology | BC Guidelines | Canadian Dermatology Association (dermatology.ca) | DermNet NZ (images) | DermNet NZ |
| Hematology and Oncology | BC Cancer (bccancer.bc.ca) | Thrombosis Canada (thrombosiscanada.ca) | MDCalc: Wells for DVT | BC Cancer |
| Eyes, Ears, Nose and Throat | BC Guidelines | Canadian Paediatric Society for children | EyeGuru (eyeguru.org) | HealthLinkBC |
| Sexual and Reproductive Health | Perinatal Services BC, BC Women's, Smart Sex Resource | SOGC (sogc.org, jogc.com), Sex & U (sexandu.ca) | none listed yet | Sex & U, Smart Sex Resource |
| Pediatrics | BC Children's (bcchildrens.ca), Perinatal Services BC | Canadian Paediatric Society (cps.ca), Rourke Baby Record, TREKK, Pediatric Palliative Care | PedsCases | Caring for Kids (cps.ca) |
| Older adults | BC Guidelines (frailty, dementia) | Canadian Geriatrics Society, deprescribing.org, Canadian Deprescribing Network | MoCA | deprescribing.org handouts |
| Indigenous health | First Nations Health Authority (fnha.ca) | none listed yet | none listed yet | FNHA |
| Trans and gender-affirming care | Trans Care BC (transcarebc.ca) | WPATH (international) | none listed yet | Trans Care BC |
| Rural and remote | BC Rural Health Network (bcruralhealth.org), RACE, Pathways | none listed yet | none listed yet | none listed yet |
| Pain | Pain BC (painbc.ca), BC Guidelines (chronic pain) | Pain Canada, PEER simplified chronic pain guideline | none listed yet | Pain BC |
| Prescribing | PharmaCare and Special Authority (gov.bc.ca), BCCNM prescribing standards, Therapeutics Initiative (ti.ubc.ca) | RxFiles, CPS (pharmacists.ca), Bugs & Drugs, Firstline, deprescribing.org | MDCalc | none listed yet |
| NP practice and scope | BCCNM (bccnm.ca), NNPBC (nnpbc.com) | Nurse Practitioner Association of Canada (npac-aiipc.org), CNPS (cnps.ca) | none listed yet | none listed yet |

## Loading guidelines into AI tools

Heidi Evidence answers from the documents an NP uploads, so NPPR's job is to tell NPs exactly which current BC and Canadian documents to upload and to flag when one is replaced. Its own national coverage is thin: the only Canadian-specific source Heidi names is BMJ Best Practice (CA), a paid partner source.

**Evidence Pack flow (diagram in the doc, described here).** One source list feeds the page, the Evidence Pack and the AI files:

1. Source list (each page's frontmatter: publisher and version, PDF link, date checked) feeds the MkDocs build (Evidence Pack hook, llmstxt plugin).
2. The build produces three outputs: the condition page (what the clinician reads at the bedside); llms.txt and Markdown copies (clean text for any AI assistant); and the Evidence Pack (manifest, CSV, links to publisher PDFs, superseded list, changelog and RSS feed).
3. From the Evidence Pack, the NP downloads the PDFs from the publisher sites, named by publisher and version.
4. The NP adds them to Heidi My Library, one collection per topic group, with superseded files removed.
5. Heidi gives an answer with citations; the NP checks each citation against the current version.

The NP only handles the Evidence Pack. The page and the AI text files update themselves from the same source list.

**What Heidi Evidence supports today** (from Heidi's help pages):

- **My Library.** NPs upload guidelines, protocols or reference PDFs, which become sources Evidence can search. Documents are grouped into collections, and each search can be limited to chosen collections.
- **Contextual notes.** A specific guideline can be attached to a single consult.
- **Practice plan controls.** Admins can share collections across the team and set a source to "Always search", which members cannot turn off.
- **Limits.** Uploads and collections are part of the paid per-user Evidence product. On iOS, Library filtering is not available yet and Evidence takes no attachments.
- **Citations.** Key statements link to the passage they came from, and a References list shows every source used.

**What NPPR adds: an Evidence Pack for each condition.** The pack is generated from the page's `sources` frontmatter and contains:

1. A manifest table listing each document's title, publisher, jurisdiction, kind, version, date checked and direct PDF link. The same table is available as a downloadable CSV.
2. Download links that point to each publisher's own copy. NPPR does not re-host third-party PDFs for now, so every download comes from the publisher's current copy.
3. A Superseded list, so an NP knows which older file to delete from their library.
4. A short changelog with the date of each change, also published as an RSS feed so NPs can follow updates.

**Suggested My Library collections,** each one built from a group of packs: BC Guidelines core (or the full ZIP), Chronic disease, Infections and antimicrobials (with the AMMI Canada guidance), Pediatrics and perinatal, Mental health and substance use, and Prescribing.

**For other AI tools.** The [mkdocs-llmstxt](https://github.com/pawamoy/mkdocs-llmstxt) plugin publishes `/llms.txt`, a clean Markdown copy of each page, and an `llms-full.txt` of the whole site. That lets an NP paste or point any assistant at NPPR's index without scraping HTML.

**Safe use, stated on every pack:**

- **Name files with the publisher, title and version,** for example `BC-GPAC_Hypertension-AppA_<year>.pdf`, so current and superseded copies are easy to tell apart.
- **Check the citation, not just the library.** A document being in the library does not prove that a particular answer used it.
- **Use Heidi's Canadian region setting.** Northern Health's setup guide says the Canadian version must be used for data to stay in Canada.

## Governance

An index is only as trustworthy as its dates. Each rule below can be shown on the page or enforced by the build, so NPs and AI tools can see how current each source is.

| Area | Standard |
| --- | --- |
| Source order | BC (GPAC, BCCDC, PharmaCare, BCCNM), then national bodies (Canadian Task Force on Preventive Health Care, specialty societies, AMMI Canada), then Canadian evidence summaries (PEER), then international guidance only where no Canadian source exists, labelled as such |
| Review cycle | Every clinical page is reviewed within 12 months, and sooner when a listed source publishes a new version. `review-due` drives an "overdue" banner on the page |
| Publishing workflow | Clinical pages go draft, then review, then published. Each change goes through a GitHub pull request with one reviewer other than the author |
| Shown on each page | Last reviewed, review due, and git last-updated date (turn on the git-revision-date plugin already in requirements.txt) |
| Link health | A weekly GitHub Action checks every external link and opens an issue for each broken or redirected link |
| Licensing | NPPR's own text under an open licence such as CC BY 4.0. Third-party documents are linked to the publisher's own copy and not hosted on NPPR |
| Disclaimer | Keep the home page disclaimer and repeat a one-line version on every Evidence Pack: AI answers must be checked against the cited source |
| Build stability | Pin `mkdocs<2` in requirements.txt. Material's maintainers say MkDocs 2.0 removes the plugin and theme-override systems this site relies on |

## Roadmap

Build in four phases, each finished before the next starts: first the foundation, then coverage, then the AI layer, then community. No dates are set yet.

Each phase opens only when its gate is met (diagram in the doc, described here):

| Phase | Work | Gate to the next phase |
| --- | --- | --- |
| 1 Foundation | Frontmatter schema · New section folders · Review dates on pages · Link checks, pin MkDocs | 8 pages migrated |
| 2 Coverage | 20 priority conditions · Populations section · Prescribing section · Practice section | 20 pages published |
| 3 AI layer | Evidence Pack hook · Manifest CSV and RSS · llms.txt plugin · Heidi how-to guide | Packs tested in Heidi |
| 4 Community | Contributor guide · Reviewer roster · NP student projects · Yearly review sweep | — |

**Priority conditions for phase 2.** These are high-volume primary care topics with BC or national guidance. The ticked items already have a page; tick the rest as their pages are published:

- [x] Hypertension
- [x] Type 2 diabetes
- [x] Chronic kidney disease
- [x] Acute kidney injury
- [ ] Cardiovascular risk and lipids
- [ ] Heart failure
- [ ] Atrial fibrillation and anticoagulation
- [ ] Asthma
- [ ] COPD
- [ ] Depression and anxiety
- [ ] Opioid use disorder
- [ ] Chronic pain
- [ ] Urinary tract infection
- [ ] Respiratory tract infections
- [ ] Thyroid disease
- [ ] Osteoporosis
- [ ] Dementia and frailty
- [ ] Prenatal care
- [ ] Well-child care (Rourke)
- [ ] Contraception and STI care

## Sources

All pages opened 2026-10-09.

- [BC Guidelines](https://www2.gov.bc.ca/gov/content/health/practitioner-professional-resources/bc-guidelines), Government of BC
- [Pathways](https://divisionsbc.ca/provincial/what-we-do/practice-support/pathways), Divisions of Family Practice
- [RACE: Rapid Access to Consultative Expertise](https://healthcareexcellence.ca/en/resources/race-rapid-access-to-consultative-expertise), Healthcare Excellence Canada
- [PEER resources](https://acfp.ca/research-and-tools/peer-resources/), Alberta College of Family Physicians
- [Tools for Practice library](https://cfpclearn.ca/tools-for-practice-library/), CFPCLearn
- [About RxFiles](https://www.rxfiles.ca/rxfiles/modules/aboutus/AboutUs.aspx), University of Saskatchewan
- [Canadian Antibiotic Treatment Guidance](https://firstline.org/canada/), AMMI Canada on Firstline
- [Thrombosis Canada app review](https://krs.libguides.com/mobile/thrombosiscanada), AHS Knowledge Resource Service
- [Evidence2Practice Ontario session](https://digitalhealthcanada.com/?p=33928), Digital Health Canada
- [CMA Infobase sunset notice](https://lists.koumbit.net/pipermail/canmedlib-chlaabsc.koumbit.org/2023-September/001674.html), CANMEDLIB list, September 2023
- [NP Portal](https://www.nnpbc.com/np-portal/), Nurses and Nurse Practitioners of BC
- [Heidi Evidence](https://support.heidihealth.com/en/articles/13191359-heidi-evidence), Heidi Health support
- [Managing your Evidence library and source control](https://support.heidihealth.com/en/articles/15595402-managing-your-evidence-library-and-source-control), Heidi Health support
- [Heidi Evidence library: adding local guidelines](https://www.iatrox.com/blog/heidi-evidence-library-how-to-add-local-guidelines-and-check-the-sources-behind-an-answer), iatroX, 6 September 2026
- [Setting up Heidi for use in Northern Health](https://physicians.northernhealth.ca/sites/physicians/files/physician-resources/ai-ambient-scribes/documents/setting-up-heidi-nh.pdf), Northern Health
- [mkdocs-llmstxt](https://github.com/pawamoy/mkdocs-llmstxt), GitHub
- NPPR vault and nppr-website-config repositories, read 2026-10-09

---

# Part 2: Build prompts

Run the framework one step at a time, in roadmap order. Each step says where to run it, what to do, the prompt to paste, and what to check before committing. Step status is tracked in the doc, not here.

## Where to run each step

Almost every step runs in Claude Code, because it edits files, builds the site and commits. Only two steps need Claude with your computer linked: one reads the doc, the other sets up a scheduled task. No step needs a plain chat.

- **Claude Code** runs in the Code tab of the Claude desktop app, or in a terminal, opened on the nppr-website-config folder with the vault added. Use it for every step that changes files or runs git.
- **Claude, computer linked** is a chat in the Claude app with your folders attached. Use it to read or edit the doc and to create scheduled tasks.
- **You** means a step done outside Claude: reviewing in Obsidian or testing a pack in Heidi.

| Step | What it does | Run in | Model and effort |
| --- | --- | --- | --- |
| 0.1 | Save this framework into the vault | Claude, computer linked | Default |
| 0.2 | Set up Claude Code (cloud or local) | Claude Code | Opus 5.5, medium |
| 1.1 | Housekeeping in the website config | Claude Code | Opus 5.5, medium |
| 1.2 | Frontmatter schema and templates | Claude Code | Opus 5.5, medium |
| 1.3 | New sections and page moves | Claude Code | Opus 5.5, high, plan mode |
| 1.4 | Migrate the condition pages | Claude Code | Opus 5.5, high |
| 1.5 | Review dates and overdue banner | Claude Code | Opus 5.5, medium |
| 1.6 | Weekly link check | Claude Code | Opus 5.5, medium |
| 1 gate | Phase 1 check | Claude Code | Opus 5.5, medium |
| 2.1 | New condition page (repeat per condition) | Claude Code | Opus 5.5, high |
| 2.2 | Populations, Prescribing and Practice pages | Claude Code | Opus 5.5, high |
| 2.3 | Population and symptom tags | Claude Code | Opus 5.5, medium |
| 2.4 | Review and update existing pages (repeat per section) | Claude Code | Opus 5.5, high |
| 2.5 | Update section index pages (repeat after pages change) | Claude Code | Opus 5.5, medium |
| 2 gate | Phase 2 check | Claude Code | Opus 5.5, medium |
| 3.1 | Evidence Pack generator | Claude Code | Opus 5.5, high (Fable if stuck) |
| 3.2 | Manifest CSV and RSS feed | Claude Code | Opus 5.5, medium |
| 3.3 | llms.txt for other AI tools | Claude Code | Opus 5.5, medium |
| 3.4 | Heidi how-to page | Claude Code | Opus 5.5, high |
| 3 gate | Test a pack in Heidi | You | Not needed |
| 4.1 | Contributor guide and review workflow | Claude Code | Opus 5.5, medium |
| 4.2 | Reviewer roster | Claude Code | Opus 5.5, medium |
| 4.3 | Monthly review sweep | Claude, computer linked | Default |
| 4 gate | Phase 4 check | Claude Code | Opus 5.5, medium |

**Model and effort.** Use Opus 5.5 throughout. Medium is Claude Code's default effort, so you only change it for the steps marked high, where checking sources or a risky change matters. "Default" means whatever the Claude chat already uses.

- **Set effort:** type `/effort high` before a high step, and `/effort auto` afterwards to go back to the default.
- **Plan mode for step 1.3:** press Shift+Tab (in a cloud session, choose Plan from the mode menu) to switch into plan mode, so Claude plans the moves and waits for your OK. Or use `/model opusplan`, which plans with Opus and does the work with Sonnet.
- **Fable for step 3.1:** switch with `/model fable` only if Opus gets stuck. It's meant for work longer than one sitting and may use paid usage credits.
- **Skip:** Haiku, because speed is the wrong trade when checking clinical source versions; and max effort, which [Anthropic's docs](https://code.claude.com/docs/en/model-config) say is prone to overthinking. Sonnet 5.5 is fine for medium steps if you want to save usage.

**Cloud or local Claude Code.** Claude Code can run in the cloud with your two GitHub repos connected, or on your computer. The cloud is the better fit for most steps.

- **What the cloud gives you:** no Python or MkDocs install on Windows. Every step lands as a pull request you merge on GitHub, so nothing reaches the live site without your approval. It also runs from any device, with your computer off.
- **What it costs you:** no live preview in your own browser. You check screenshots instead, or a preview link if your Cloudflare Pages project builds one for each branch. Obsidian only sees the changes after you pull them.
- **Use the cloud for website and code work:** 1.1, 1.3, 1.5, 1.6, all of Phase 3, and 4.1 and 4.2. Review step 1.3 carefully as a pull request, since it moves many files.
- **Use either for content:** 1.2, 1.4 and Phase 2. Choose local to watch pages appear in Obsidian as they're written, or the cloud if you're happy reviewing a pull request.
- **The one rule:** push your Obsidian changes before you start a cloud session, and pull them back after you merge its pull request. Editing a page in Obsidian while a cloud session edits the same page causes a conflict.

## Step 0: Setup

Do this once. It gives Claude Code a copy of this plan and a live preview of the site on your computer.

**0.1 Save this framework into the vault** · Run in: Claude, computer linked

1. Open a Claude chat with your np-practice-resource folder linked.
2. Paste:

```text
Export my NPPR Framework doc (https://claude.ai/code/artifact/5e9d248a-789d-4815-8f25-a3c965081661), both tabs, to NPPR-FRAMEWORK.md at the root of my np-practice-resource vault, outside docs/. Then add a section to the vault's CLAUDE.md telling Claude to read NPPR-FRAMEWORK.md before any NPPR build step and to follow its rules: BC sources first, link to publishers' PDFs only, no clinical recommendations in our own words, and test-build before committing.
```

3. Check that NPPR-FRAMEWORK.md opens in Obsidian.
4. Re-run this prompt whenever you change the doc, so Claude Code always has the latest plan.

**0.2 Set up Claude Code (cloud or local)** · Run in: Claude Code · Opus 5.5, medium

**Option A: Claude Code in the cloud (recommended).**

1. Push both repos' uncommitted changes first: the section buttons, templates, NPPR-FRAMEWORK.md and CLAUDE.md. A cloud session only sees what is on GitHub.
2. Go to [claude.ai/code](https://claude.ai/code), or choose Cloud instead of Local in the desktop app's Code tab. The first time, connect GitHub by authorizing the Claude GitHub App, and install it on np-practice-resource and nppr-website-config.
3. Start a session with both repos selected and paste:

```text
Read NPPR-FRAMEWORK.md in np-practice-resource. Set up a test build for nppr-website-config that uses np-practice-resource's docs folder instead of the content submodule, with mkdocs below 2.0 and the social and offline plugins turned off. Build the site, screenshot the Conditions page so I can check the section buttons, and open a pull request for the setup.
```

4. Check the screenshot, then merge the pull request on GitHub.

If a session lets you pick only one repo, start it on nppr-website-config and ask Claude to update the content submodule to the latest np-practice-resource commit before building.

**Option B: Claude Code on your computer.** Use this for content steps if you'd rather watch pages appear in Obsidian as they're written.

1. Open the Code tab in the Claude desktop app, or Claude Code in a terminal, on `C:\Users\josep\Documents\GitHub\nppr-website-config`.
2. Add the vault so Claude Code can edit both repos: `/add-dir C:\Users\josep\Documents\Obsidian\np-practice-resource`
3. Paste:

```text
Read NPPR-FRAMEWORK.md in my vault. Then set up a local preview: create a Python virtual environment in nppr-website-config, install requirements.txt with mkdocs below 2.0, and create mkdocs.local.yml that inherits mkdocs.yml but uses my vault's docs folder as docs_dir and turns off the social and offline plugins. Keep it out of git if it holds my local path. Start mkdocs serve with it and give me the local address. Then show me the uncommitted changes in both repos (the section buttons work from before) and commit them once I approve.
```

4. Open the local address in your browser and check that the section buttons show on the Conditions page.

The local preview reads your vault directly. The `content` folder inside nppr-website-config is an older copy that GitHub updates on its own, so it isn't used for previews.

**After every local Claude Code step**

1. Look at the change in the local preview, or in Obsidian for vault-only changes.
2. If it looks right, paste:

```text
Commit the changes from this step with a clear message. Push nppr-website-config first, then np-practice-resource.
```

3. If something is wrong, paste:

```text
Show me exactly what changed in this step and undo the parts I name: [list them].
```

4. Set the step's Status to Done in the doc.

**After every cloud step**

1. Check the screenshots or the diff in the session.
2. If it looks right, paste:

```text
Open a pull request for this step's changes, one per repo, with a clear title and a short summary of what changed and what I should check.
```

3. Review and merge the pull request on GitHub: nppr-website-config first, then np-practice-resource.
4. Pull the changes into your vault before editing in Obsidian again.
5. Set the step's Status to Done in the doc.

## Phase 1: Foundation

All seven steps run in Claude Code, in order, before any new pages are written. Open Claude Code on nppr-website-config with the vault added (step 0.2), paste the prompt, check the result, then commit.

**1.1 Housekeeping in the website config** · Run in: Claude Code · Opus 5.5, medium

```text
In nppr-website-config: pin mkdocs below 2.0 in requirements.txt, turn on the git-revision-date-localized plugin so each page shows when it was last updated, and change overrides/partials/comments.html so pages with "hide: comments" show no Comments heading. Fix any missing asset files the build reports (logo, favicon, extra.css, extra.js). Show me the result in the local preview.
```

Check: a page shows its last-updated date, and the home page has no Comments heading.

**1.2 Frontmatter schema and templates** · Run in: Claude Code · Opus 5.5, medium

```text
Using the Page standard section of NPPR-FRAMEWORK.md, write the frontmatter schema as FRONTMATTER.md at the root of my vault (outside docs/). Update the six NPPR templates in 03 Resources/Templates to use it, and add Population and Practice templates. Keep Templater syntax.
```

Check: in Obsidian, create a test note from the new Condition template, look it over, then delete it.

**1.3 New sections and page moves** · Run in: Claude Code · Opus 5.5, high, plan mode

```text
Restructure docs/ to the eight sections in the Recommended structure section of NPPR-FRAMEWORK.md. First show me the old-to-new URL list and wait for my OK. Then create the new section folders with index pages from the Section Index template, move the pages as the table says, add the mkdocs-redirects plugin with a redirect for every moved page, update the buttons in overrides/partials/section-nav.html, and fix internal links.
```

Check: approve the URL list before anything moves, then click through every top tab in the local preview and try one old URL.

**1.4 Migrate the condition pages** · Run in: Claude Code · Opus 5.5, high

```text
Migrate the 8 condition pages to the new frontmatter. Move every guideline and algorithm link into the sources list with publisher, jurisdiction, kind and URL. Fill version and checked dates only where you confirm them by opening the source page, and list the ones you couldn't confirm. Leave the page text as it is.
```

Check: the list of unconfirmed versions. Fill them in yourself or ask Claude Code to look each one up.

**1.5 Review dates and overdue banner** · Run in: Claude Code · Opus 5.5, medium

```text
Show "Last reviewed" and "Review due" under the title of every page that has last-reviewed, and a warning banner when review-due has passed. Use a hook like hooks/section_nav.py if that is simpler than a theme override. Set one page overdue temporarily so I can see the banner, then set it back.
```

Check: the dates and the banner in the local preview.

**1.6 Weekly link check** · Run in: Claude Code · Opus 5.5, medium

```text
Add a GitHub Action to np-practice-resource that checks every external link in docs/ every week and opens or updates one GitHub issue listing broken and redirected links. Run the same check locally now and show me what it finds.
```

Check: the list of broken links. Ask Claude Code to fix the ones you agree with.

**Phase 1 gate** · Run in: Claude Code · Opus 5.5, medium

```text
Run the Phase 1 gate check from NPPR-FRAMEWORK.md: all 8 condition pages use the new frontmatter, the build has no warnings, redirects work, and dates show on pages. Report anything that fails.
```

## Phase 2: Coverage

All steps run in Claude Code. Step 2.1 repeats once per condition on the Roadmap checklist in Part 1; do one condition per session so each gets a careful source check.

**2.1 New condition page** · Run in: Claude Code · Opus 5.5, high · repeat per condition

1. Replace the bracketed parts and paste:

```text
Create a condition page for [Heart failure] under 3 Conditions/[Cardiovascular] using the NPPR Condition template and the Page standard in NPPR-FRAMEWORK.md. Check every site in the Source map rows for this page's system and the All topics row. Find the current BC Guidelines page first, then national Canadian guidance ([Canadian Cardiovascular Society]), PEER or Tools for Practice summaries, RxFiles or Firstline where prescribing applies, relevant clinical calculators, scores and decision aids (from MDCalc where it has them, for example CHA2DS2-VASc or BMI; a BC or Canadian tool where that is the standard here), and patient resources. Record each calculator in sources with kind: tool. Open every source you cite, record publisher, version and date checked in the sources frontmatter, and set status to review. List anything where you found no BC or Canadian source.
```

2. Open every link on the new page in the local preview and confirm the versions.
3. Set `status: published` yourself in Obsidian, then commit.
4. Tick the condition off in the Roadmap checklist in the doc.

**2.2 Populations, Prescribing and Practice pages** · Run in: Claude Code · Opus 5.5, high · once per section

```text
Build out the [Populations] section from the Recommended structure in NPPR-FRAMEWORK.md. Write its index page, then create one page per topic listed there using the matching template, with BC sources first. Keep pages to links and short descriptions; no clinical recommendations in our own words.
```

Check: each page's links in the local preview.

**2.3 Population and symptom tags** · Run in: Claude Code · Opus 5.5, medium

```text
Add population and presenting-symptom tags to every condition page (for example pediatrics, older-adults, chest-pain), and add a Tags page so readers can browse by them. Show me the tag list and wait for my OK before applying it.
```

Check: approve the tag list, then browse the Tags page.

**2.4 Review and update existing pages** · Run in: Claude Code, cloud or local · Opus 5.5, high · repeat per section

This brings the pages written before the framework up to the current standard and checks that their sources are still current. Start with 3 Conditions, then do the other sections one at a time.

1. Replace the bracketed section and paste:

```text
Review and update the existing pages in [3 Conditions], one page at a time, against NPPR-FRAMEWORK.md. For each page, open every link and check that it still works and points to the current version. Replace superseded guidelines and record the old version in that source's supersedes field. Check every site in the Source map rows for that page's system or population and the All topics row, and add missing sources in this order: BC first, then Canadian, then American or other international sources labelled as such. Reorder the page to the section order in the Page standard for its type, and fill any missing frontmatter. Under Assessment tools and calculators, add links to the clinical calculators, scores and decision aids relevant to the condition, from MDCalc where it has them (for example CHA2DS2-VASc for atrial fibrillation, or BMI); use a BC or Canadian tool instead where that is the standard here. Open each calculator link to confirm it is the right tool, and record it in sources with kind: tool. Set status to review and last-reviewed to today. Don't add clinical recommendations in our own words. Before changing anything, show me a table of each page with what is out of date and what you plan to change, and wait for my OK.
```

2. Approve the plan table, or tell Claude which changes to drop.
3. Check the updated pages in the preview or the pull request, opening any link whose version changed.
4. Set `status: published` yourself on each page you're happy with, then commit or merge.

Re-run this step for any section the monthly review sweep (4.3) flags.

**2.5 Update the section index pages** · Run in: Claude Code, cloud or local · Opus 5.5, medium · repeat after pages are added, moved or removed

This keeps each section's index page listing every page in that section. Run it after a batch of 2.1 to 2.4 work, and whenever pages are added, moved or removed.

1. Paste:

```text
Update every index.md in docs/ (the home page, each top-level section and each sub-folder index) so its In This Section list matches the pages actually in that folder and its sub-folders. Add missing pages with a one-line description taken from the page itself, remove links to pages that were moved or deleted, and group condition pages under their body-system headings in the same order as the fixed list in NPPR-FRAMEWORK.md. Use relative links. Don't change the section buttons, which come from overrides/partials/section-nav.html. Show me the changes for each index page and wait for my OK before saving.
```

2. Approve the changes, or tell Claude what to drop.
3. Click through each index page in the preview or the pull request to check every link opens.
4. Commit or merge.

**Phase 2 gate** · Run in: Claude Code · Opus 5.5, medium

```text
Run the Phase 2 gate check from NPPR-FRAMEWORK.md: how many condition pages are published, which roadmap conditions are missing, which pages have sources with no version or checked date, which existing pages haven't been through step 2.4, and which index pages are missing pages from their section.
```

## Phase 3: AI layer

Steps 3.1 to 3.4 run in Claude Code. The gate is yours: test a pack in your own Heidi account, then bring what you find back to Claude Code.

**3.1 Evidence Pack generator** · Run in: Claude Code · Opus 5.5, high (Fable if stuck)

```text
In nppr-website-config, write a build hook that creates an Evidence Pack page for every condition page from its sources frontmatter, as described in the Loading guidelines into AI tools section of NPPR-FRAMEWORK.md: a manifest table, direct links to each publisher's PDF (link only, no hosted copies), a Superseded list, and a changelog from git history. Put the packs under the Evidence Packs section and link each condition page to its pack. Show me the Hypertension pack in the local preview.
```

Check: every PDF link in the Hypertension pack opens the publisher's current file.

**3.2 Manifest CSV and RSS feed** · Run in: Claude Code · Opus 5.5, medium

```text
Extend the Evidence Pack hook to publish each pack's manifest as a downloadable CSV, plus one combined CSV of all packs, and an RSS feed of pack changes so NPs can follow updates.
```

Check: open one CSV in Excel and add the RSS feed to a reader.

**3.3 llms.txt for other AI tools** · Run in: Claude Code · Opus 5.5, medium

```text
Add the mkdocs-llmstxt plugin so the site publishes /llms.txt, Markdown copies of each page and llms-full.txt. Group the sections by the eight top-level sections and leave out About. Show me llms.txt from the local preview.
```

**3.4 Heidi how-to page** · Run in: Claude Code · Opus 5.5, high

```text
Write a page in the Evidence Packs section explaining how an NP loads a pack into Heidi Evidence's My Library: downloading the PDFs, naming files, the suggested collections, removing superseded files, the Canadian region setting, and checking citations. Use only what Heidi's current help pages say, and cite them.
```

**Phase 3 gate** · Run in: You, then Claude Code

1. Follow the how-to page to load the Hypertension pack into your own Heidi My Library.
2. Ask Evidence three questions the guideline answers, and check that each answer cites the current PDF.
3. Paste what didn't work into Claude Code:

```text
I tested the [Hypertension] pack in Heidi. Here is what didn't work: [notes]. Fix the pack format or the how-to page.
```

## Phase 4: Community

Steps 4.1 and 4.2 run in Claude Code. Step 4.3 runs in a Claude chat with your computer linked, because that is where scheduled tasks are created.

**4.1 Contributor guide and review workflow** · Run in: Claude Code · Opus 5.5, medium

```text
Write a CONTRIBUTING.md for np-practice-resource and an About page version of it: how to suggest a link, how to write a page from the templates, the frontmatter rules, and the source order from NPPR-FRAMEWORK.md. Add a GitHub pull request template with a reviewer checklist (sources opened, versions recorded, BC first, no original clinical recommendations), and set main to require one approving review before merging.
```

Check: open a test pull request and confirm the checklist appears.

**4.2 Reviewer roster** · Run in: Claude Code · Opus 5.5, medium

```text
Add a reviewers list to the vault (name, GitHub username, areas) and an About page showing who reviews each section. Make the build warn when a page's reviewers field names someone not on the list.
```

**4.3 Monthly review sweep** · Run in: Claude, computer linked

1. Open a Claude chat with both folders linked.
2. Paste:

```text
Set up a scheduled task that runs on the first of each month: read the frontmatter in my np-practice-resource vault, list pages whose review-due date passes in the next 60 days, open one GitHub issue per page assigned to its reviewer, and send me a summary.
```

3. Check the first summary when it arrives.

**Phase 4 gate** · Run in: Claude Code · Opus 5.5, medium

```text
Run the Phase 4 gate check from NPPR-FRAMEWORK.md: a test pull request shows the checklist and can't merge without a review, and the reviewer list matches every page's reviewers field.
```
