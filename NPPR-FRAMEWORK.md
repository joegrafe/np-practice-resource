# NPPR Framework

Exported 2026-10-09 from the NPPR Framework doc (https://claude.ai/code/artifact/5e9d248a-789d-4815-8f25-a3c965081661). The doc is the master copy: re-export this file whenever the doc changes. Part 1 is the framework; Part 2 is the step-by-step build prompts. The "Section page lists" part of Part 1 comes from the NPPR.ca master plan (https://claude.ai/artifact/8pVpBPZ5hLjistCczBVaow), agreed by Joe on 2026-10-26.

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
| [Thrombosis Canada app](https://krs.libguides.com/mobile/thrombosiscanada) | Thrombosis Canada | Canadian health care providers; no ads, works offline | Clinical guides and calculators, e.g. perioperative anticoagulation | Shows the value of offline access and built-in calculators, which NPPR plans: it installs as an app today, and offline use comes with a service worker in stage C. |
| Centre for Effective Practice | CEP, co-lead of [Evidence2Practice Ontario](https://digitalhealthcanada.com/?p=33928) | Ontario primary care | Point-of-care tools, including Ontario Health quality standards built into EMRs | Structured tools fit into clinical workflow. |
| [CMA CPG Infobase](https://lists.koumbit.net/pipermail/canmedlib-chlaabsc.koumbit.org/2023-September/001674.html) | Canadian Medical Association | All clinicians | Database of Canadian clinical practice guidelines | Shut down December 1, 2023; there is no national guideline index now. |
| [NNPBC NP Portal](https://www.nnpbc.com/np-portal/) | Nurses and Nurse Practitioners of BC | BC NPs; some resources members-only | Practice supports and a searchable content library | Link to it for NP practice and scope topics. |

## Strengths and gaps

NPPR has the strongest publishing model of the group but the thinnest coverage and the weakest signals of currency. As of 2026-10-09 the site has 35 pages and 246 unique external links. 23 pages have frontmatter, and 9 have a last-reviewed date.

**What NPPR already does better than its peers**

- Free and open, with no login. Pathways, RxFiles' app and parts of NNPBC are gated.
- BC-first and written for NPs, where most peers are written for physicians or are national.
- Every change is versioned in Git, and readers can suggest edits through GitHub.
- Installs as an app; offline use, like the Thrombosis Canada app, needs a service worker (planned for stage C).

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
| 1 | Approaches | Indexes of published "approach to" articles, diagnostic schemes and primary care pathways, by body system; NPPR writes no approaches of its own (documentation lives in Practice, safe use of AI tools in Tools: AI Tools) | A Systematic Approach, UCalgary Black Books |
| 2 | Assessments | Exams by system, point-of-care ultrasound (POCUS), decision rules, screening, lab and imaging interpretation | Assessment Resources; POCUS (from Tools, 2026-10-27) |
| 3 | Conditions | One page per condition, grouped by body system | All 8 condition pages |
| 4 | Populations (new) | Pediatrics, pregnancy and perinatal, older adults, women's health, trans and gender-affirming care, Indigenous health and cultural safety, rural and remote | Pediatrics folder, Trans Care, Woman's Health, BC Rural Health |
| 5 | Prescribing (new) | Drug references, antimicrobials, PharmaCare and Special Authority, immunization, deprescribing, controlled drugs | Bugs & Drugs, BC Immunization Manual |
| 6 | Practice (new) | NP scope and BCCNM standards, advice and referral (RACE, Pathways), forms | Associations (removed 2026-10-29, Joe) |
| 7 | Tools (new) | Sub-sections: Evidence Packs (one pack per condition for loading into AI tools, plus how-to guides), Templates (peer-written charting templates and AI templates, such as scribe note templates and prompts, contributed through the nppr-templates repository), AI Tools. POCUS moved to Assessments on 2026-10-27 | none |
| 8 | Resources | Guideline directories, libraries, evidence summaries, CPD | BC Guidelines, Guidelines folder, Library Guides, Peerevidence.ca, Clinical Tools |

About stays as it is, as a separate tab after Resources.

**Body systems under Conditions.** Use one fixed list so the folders, tags and Evidence Packs all line up: Cardiovascular; Respiratory; Endocrine and Metabolic; Renal and Genitourinary; Gastrointestinal and Liver; Musculoskeletal; Neurology; Mental Health and Substance Use; Infectious Disease; Dermatology; Hematology and Oncology; Eyes, Ears, Nose and Throat; Sexual and Reproductive Health. Electrolyte disorders stay under Endocrine and Metabolic. Infections go under Infectious Disease (respiratory tract infections, cellulitis, herpes zoster) except ear and eye infections, which go under Eyes, Ears, Nose and Throat. Urgent care conditions go under their body system and carry the `urgent-care` tag. Chronic pain goes under Musculoskeletal.

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
| Condition | Key sources (1 to 3, see below) · Further resources · Algorithms and pathways · Assessment tools and calculators · Prescribing · Advice and referral · Patient resources · Evidence Pack link (added by step 3.1 once the pack exists; no placeholder heading before then) · Review notes |
| Assessment | Scope · Focused history · Exam and special tests · Decision rules · Red flags · Learning videos · Sample documentation · References |
| Approach | Publisher logo title bar · One-line intro naming the publisher and jurisdiction · Link to the publisher's index · Items by body system, each with its year, under a filter box · More Approaches |
| Population | Key sources · Screening and preventive care · Conditions with population notes (links) · Services and referral · Patient resources |
| Prescribing | Reference · What it covers · Access (free, subscription, PharmaCare) · NP prescribing notes, linked to BCCNM standards |
| Practice | Topic · Standard or rule, linked to its source · How to do it in BC · Contacts |
| Evidence Pack | Generated from frontmatter: the source manifest table · Download links · Superseded versions · Changelog |
| Resource | Organization · Title · Link · What it covers · Access and scope |

**Key sources on condition pages.** Key sources holds only the 1 to 3 most relevant, high-yield, primary care sources for broad diagnosis and management, in this order: the BC Guideline (or another BC source where there is no BC Guideline); then a more recent or broader national guideline; then one high-yield "approach to" or "management of" review (for example AAFP, Canadian Family Physician or McGill). Every other source the page cites goes under Further resources, in the usual order: BC, then Canadian, then international, labelled as such. Agreed by Joe on 2026-10-27.

The six templates already in the vault map onto these types. They would need `type`, `jurisdiction`, `review-due` and `sources` added, and two new templates for Population and Practice pages.

## Source map

Before writing or reviewing any page, check every site in the "All topics" row and in the row for that page's system or population. Search in the order the columns run: BC, then Canadian, then calculators, then patient resources. Use American or international sources only where no BC or Canadian source covers the question, and label them as such. For approaches and condition pages, AAFP (aafp.org) is the first international source to check, using only articles that are free to read; then USPSTF, NICE, Cochrane and TRIP. Where Alberta's Pathway Hub (primarycarealberta.ca) has a pathway for a condition, link it and leave out Specialist Link's Calgary pathway for the same condition, which repeats it. Add a site to this table whenever a new one proves useful.

| System or topic | BC | Canadian | Calculators and tools | Patient resources |
| --- | --- | --- | --- | --- |
| All topics | BC Guidelines and PharmaCare (gov.bc.ca), BCCDC (bccdc.ca), RACE (raceconnect.ca), Pathways (pathwaysbc.ca), BC Medical Journal (bcmj.org) | Canadian Task Force on Preventive Health Care (canadiantaskforce.ca), Choosing Wisely Canada, PEER and Tools for Practice (peerevidence.ca, cfpclearn.ca), Canadian Family Physician (cfp.ca), CMAJ guidelines and "Five things to know about" (cmaj.ca) | MDCalc (mdcalc.com) | HealthLinkBC (healthlinkbc.ca) |
| Approaches (and "approach to" reviews on condition pages) | Pathways BC Enhanced Care Pathways (pathwaysbc.ca/ci/<id>, open without login), Child Health BC clinician resources (childhealthbc.ca, pediatric emergency and urgent care; Emergency Care BC is retiring) | McGill Journal of Medicine "Approach to" articles (mjm.mcgill.ca), UCalgary Black Book (blackbook.ucalgary.ca), PedsCases Notes (pedscases.com), Alberta's Pathway Hub (primarycarealberta.ca), Canadian Family Physician "Approach to" and "Management of" clinical reviews (cfp.ca), Centre for Effective Practice clinical tools (cep.health, Ontario), TREKK (trekk.ca, pediatric emergency), CMAJ "Five things to know about" (cmaj.ca), MCC Examination Objectives (mcc.ca, complaint headings for Presentations A to Z); AAFP (aafp.org, free "approach to", "evaluation" and "management of" articles only) as the first international source, then NICE Clinical Knowledge Summaries (cks.nice.org.uk) and Royal Children's Hospital Melbourne guidelines (rch.org.au) | none listed yet | none listed yet |
| Assessments | BC Guidelines (lab, imaging and screening guidelines), BCCDC Public Health Laboratory eLab Handbook, BC Lifetime Prevention Schedule (gov.bc.ca), BC Cancer screening programs | Canadian Task Force, Canadian Association of Radiologists referral guidelines (car.ca), Ottawa and other Canadian decision rules (derivation papers, e.g. Canadian Syncope Risk Score), CPS Greig Health Record, CFPC Preventive Care Checklist; Stanford 25, Geeky Medics, TheNNT (international) | MDCalc, LITFL ECG Library (litfl.com), Radiopaedia (radiopaedia.org), C-SSRS, STOP-Bang | HealthLinkBC |
| Cardiovascular | Cardiac Services BC (cardiacbc.ca) | Hypertension Canada, Canadian Cardiovascular Society (ccs.ca, onlinecjc.ca), Canadian Heart Failure Society (heartfailure.ca), Canadian Heart Rhythm Society (chrsonline.ca), Thrombosis Canada | MDCalc: CHA2DS2-VASc, HAS-BLED, Framingham | Heart & Stroke (heartandstroke.ca) |
| Respiratory | BC Guidelines (asthma, COPD) | Canadian Thoracic Society (cts-sct.ca), Lung Association (lung.ca); GOLD and GINA (international) | MDCalc: Wells and PERC for PE; GOLD COPD tools | Lung Association |
| Endocrine and Metabolic | BC Guidelines | Diabetes Canada (diabetes.ca), Obesity Canada, Osteoporosis Canada (osteoporosis.ca) | MDCalc: BMI; FRAX (frax.shef.ac.uk) | Diabetes Canada, Obesity Canada |
| Renal and Genitourinary | BC Renal (bcrenal.ca) | KDIGO (international), Canadian Urological Association (cua.org) | MDCalc: CKD-EPI eGFR, Kidney Failure Risk Equation | BC Renal |
| Gastrointestinal and Liver | BC Guidelines | Canadian Association of Gastroenterology (cag-acg.org) | MDCalc: FIB-4, Child-Pugh | HealthLinkBC |
| Musculoskeletal | BC Guidelines | Canadian Rheumatology Association (rheum.ca), RheumInfo, RheumGuide | MDCalc: Ottawa ankle and knee rules; OrthoBullets, Physiopedia | RheumInfo |
| Neurology | BC Guidelines | Alzheimer Society (alzheimer.ca), Heart & Stroke for stroke, Canadian Headache Society (headachesociety.ca) | MoCA (mocacognition.com); MDCalc: NIHSS, ABCD2 | Alzheimer Society |
| Mental Health and Substance Use | BCCSU (bccsu.ca), HeretoHelp (heretohelp.bc.ca), BC Eating Disorders Toolkit (gov.bc.ca) | CANMAT, CAMH, CADDRA, META:PHI (metaphi.ca), Canadian Psychiatric Association | MDCalc: PHQ-9, GAD-7 | HeretoHelp, CAMH |
| Infectious Disease | BCCDC, BC Centre for Excellence in HIV/AIDS (bccfe.ca), BC Immunization Manual (BCCDC) | AMMI Canada, Firstline Canadian Antibiotic Treatment Guidance (firstline.org/canada, AMMI Canada and PHAC), NACI and STI guidelines (canada.ca), Bugs & Drugs | MDCalc: Centor (McIsaac) | HealthLinkBC (incl. Immunizations, formerly ImmunizeBC), Smart Sex Resource |
| Dermatology | BC Guidelines | Canadian Dermatology Association (dermatology.ca) | DermNet (dermnetnz.org): check every topic, image, treatment and drug page for the condition | DermNet NZ |
| Hematology and Oncology | BC Cancer (bccancer.bc.ca) | Thrombosis Canada (thrombosiscanada.ca) | MDCalc: Wells for DVT | BC Cancer |
| Eyes, Ears, Nose and Throat | BC Guidelines | Canadian Paediatric Society for children | EyeGuru (eyeguru.org) | HealthLinkBC |
| Sexual and Reproductive Health | Perinatal Services BC, BC Women's, Smart Sex Resource | SOGC (sogc.org, jogc.com), Sex & U (sexandu.ca) | none listed yet | Sex & U, Smart Sex Resource |
| Pediatrics | BC Children's (bcchildrens.ca), Child Health BC (childhealthbc.ca), Perinatal Services BC | Canadian Paediatric Society (cps.ca), Rourke Baby Record, TREKK, Pediatric Palliative Care | PedsCases | Caring for Kids (cps.ca) |
| Older adults | BC Guidelines (frailty, dementia) | Canadian Geriatrics Society, deprescribing.org, Canadian Deprescribing Network | MoCA | deprescribing.org handouts |
| Indigenous health | First Nations Health Authority (fnha.ca) | none listed yet | none listed yet | FNHA |
| Trans and gender-affirming care | Trans Care BC (transcarebc.ca) | WPATH (international) | none listed yet | Trans Care BC |
| Rural and remote | BC Rural Health Network (bcruralhealth.org), RACE, Pathways, RCCbc Real-Time Virtual Support (rccbc.ca/rtvs: RUDi, CHARLiE, MaBAL) | Canadian Journal of Rural Medicine (cjrm.srpc.ca) | none listed yet | none listed yet |
| Pain | Pain BC (painbc.ca), BC Guidelines (chronic pain) | Pain Canada, PEER simplified chronic pain guideline | none listed yet | Pain BC |
| Prescribing | PharmaCare and Special Authority (gov.bc.ca), BCCNM prescribing standards, Therapeutics Initiative (ti.ubc.ca), Provincial Academic Detailing (gov.bc.ca), BCCSU, BCCDC (Immunization Manual, PACE antimicrobial stewardship), FNHA | RxFiles, CPS (pharmacists.ca), Health Canada (Drug Product Database, MedEffect, drug shortages), ISMP Canada, CDA-AMC, Bugs & Drugs, Firstline (Canadian Antibiotic Treatment Guidance), Canadian Immunization Guide and NACI (canada.ca), Choosing Wisely Canada, deprescribing.org, Canadian Deprescribing Network; WHO Guide to Good Prescribing (international) | MDCalc (Cockcroft-Gault, PEN-FAST) | PharmaCare information sheets, Ottawa Patient Decision Aids, HealthLinkBC Immunizations (formerly ImmunizeBC), Antibiotic Wise |
| NP practice and scope | BCCNM (bccnm.ca), NNPBC (nnpbc.com), Ministry of Health (PRIME, PharmaNet, MSP), RoadSafetyBC, WorkSafeBC, OIPC BC (oipc.bc.ca), BCCSU and Pain BC ECHO communities of practice | Nurse Practitioner Association of Canada (npac-aiipc.org), CNPS (cnps.ca), NP Circle (npcircle.ca) | none listed yet | none listed yet |

## Loading guidelines into AI tools

Heidi Evidence answers from the documents an NP uploads, so NPPR's job is to tell NPs exactly which current BC and Canadian documents to upload and to flag when one is replaced. Its own national coverage is thin: the only Canadian-specific source Heidi names is BMJ Best Practice (CA), a paid partner source.

**Evidence Pack flow (diagram in the doc, described here).** One source list feeds the page, the Evidence Pack and the AI files:

1. Source list (each page's frontmatter: publisher and version, PDF link, date checked) feeds the site build (Evidence Pack and llms.txt build scripts).
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

**For other AI tools.** A post-build script (modelled on the [mkdocs-llmstxt](https://github.com/pawamoy/mkdocs-llmstxt) plugin) publishes `/llms.txt`, a clean Markdown copy of each page, and an `llms-full.txt` of the whole site. That lets an NP paste or point any assistant at NPPR's index without scraping HTML.

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
| 3 AI layer | Evidence Pack build script · Manifest CSV and RSS · llms.txt build script · Heidi how-to guide | Packs tested in Heidi |
| 4 Community | Contributor guide · Reviewer roster · NP student projects · Yearly review sweep | — |

**Priority conditions for phase 2.** These are high-volume primary care topics with BC or national guidance. The ticked items already have a page; tick the rest as their pages are published:

- [x] Hypertension
- [x] Type 2 diabetes
- [ ] Chronic kidney disease (Renal and Genitourinary)
- [ ] Acute kidney injury (Renal and Genitourinary)
- [x] Cardiovascular risk and lipids
- [x] Heart failure
- [x] Atrial fibrillation and anticoagulation
- [x] Asthma
- [x] COPD
- [ ] Depression and anxiety (Mental Health and Substance Use)
- [ ] Opioid use disorder (Mental Health and Substance Use)
- [ ] Chronic pain (Musculoskeletal)
- [x] Urinary tract infection
- [ ] Respiratory tract infections (Infectious Disease)
- [x] Thyroid disease
- [ ] Osteoporosis (Endocrine and Metabolic)
- [ ] Dementia and frailty (Neurology)
- [ ] Prenatal care (build as a section of Populations > Pregnancy and Perinatal, not a condition page)
- [ ] Well-child care (Rourke) (build as a section of Populations > Pediatrics, not a condition page)
- [x] Contraception and STI care

**Build order.** From the [Conditions section plan](https://claude.ai/artifact/5UM4RnW9PTP8De8FtSLmQm), agreed by Joe on 2026-10-27. Build in waves, taking the first unticked item each time: wave 1 is the unticked priority conditions above in this order (depression and anxiety, respiratory tract infections, opioid use disorder, osteoporosis, chronic pain, dementia and frailty, chronic kidney disease, acute kidney injury), then the wave 1 conditions below; waves 2 and 3 follow top to bottom. The folder for each page is in brackets. Urgent care conditions also carry the `urgent-care` tag, and their decision rules go on Assessments > Clinical decision rules.

**Next conditions.** Added after the phase 2 list, as Joe asks for them, in build order:

- [x] Psoriasis
- Wave 1 (rebuild): these pages, and the CKD and AKI pages above, were older pages removed on 2026-10-29 to be rebuilt to the current standard. The research notes are in the [wave 0 plan](https://claude.ai/artifact/NEYRhd487FAhC9ZS6kGUcV). When a page is rebuilt at its old path, remove its redirect from `mkdocs.yml` in nppr-website-config.
    - [ ] Low back pain (Musculoskeletal)
    - [ ] Calcium disorders (Endocrine and Metabolic, Electrolyte Imbalances)
    - [ ] Potassium disorders (Endocrine and Metabolic, Electrolyte Imbalances)
    - [ ] Sodium disorders (Endocrine and Metabolic, Electrolyte Imbalances)
- Wave 1 (urgent care):
    - [ ] Chest pain (Cardiovascular)
    - [ ] Sprains and minor fractures (Musculoskeletal)
- Wave 2:
    - [ ] Alcohol use disorder (Mental Health and Substance Use)
    - [ ] Tobacco use disorder (Mental Health and Substance Use)
    - [ ] Lacerations and minor wounds (Dermatology; urgent care)
    - [ ] Venous thromboembolism (Hematology and Oncology)
    - [x] Obesity (Endocrine and Metabolic)
    - [ ] Anemia and iron (iron deficiency, B12 and folate, high ferritin) (Hematology and Oncology)
    - [ ] Burns (Dermatology; urgent care)
    - [ ] GERD and H. pylori (Gastrointestinal and Liver)
    - [ ] Migraine and headache (Neurology)
    - [ ] Osteoarthritis (Musculoskeletal)
    - [ ] Insomnia (Mental Health and Substance Use)
- Wave 3:
    - [ ] Irritable bowel syndrome (Gastrointestinal and Liver)
    - [ ] Abnormal liver tests and MASLD (Gastrointestinal and Liver)
    - [ ] Stroke and TIA (Neurology)
    - [ ] Menopause (Sexual and Reproductive Health)
    - [ ] Obstructive sleep apnea (Respiratory)
    - [ ] Cellulitis and skin infections (Infectious Disease; sweep DermNet too)
    - [ ] Herpes zoster (Infectious Disease)
    - [ ] Acute otitis media and otitis externa (Eyes, Ears, Nose and Throat)
    - [ ] Red eye (Eyes, Ears, Nose and Throat)
    - [ ] Palliative care (build as a Populations page, listed in the Conditions index, not a condition page)
    - [ ] Gout (Musculoskeletal)
    - [ ] Atopic dermatitis and acne (Dermatology; sweep DermNet too)
    - [ ] Suspected cancer in primary care (breast, lung, prostate, endometrial and ovarian BC Guidelines) (Hematology and Oncology)
    - [ ] Eating disorders (Mental Health and Substance Use)
- Later:
    - [ ] Allergic rhinitis and anaphylaxis (Eyes, Ears, Nose and Throat; urgent care)
    - [ ] Post COVID-19 condition (Infectious Disease)

## Section page lists

Agreed by Joe on 2026-10-26 from the [NPPR.ca master plan](https://claude.ai/artifact/8pVpBPZ5hLjistCczBVaow). Read this before planning or building a page in any tab. The detailed section plans are [Practice](https://claude.ai/artifact/Fsisf7tmgnWJ9xwcKp2bHc), [Prescribing](https://claude.ai/artifact/GJeAP8SPPZrsk4G8ihftgU) and [Assessments](https://claude.ai/artifact/1XYYoWApRRZt5SydEACouE); their own open decisions still need Joe's answers before those pages are built.

**Purpose.** NPPR.ca gives primary care and urgent care NPs point-of-care access to high-yield BC and Canadian sources for each step of an appointment, so they can double-check AI diagnostic tools as the human in the loop. Pages lead with the one or two sources an NP would open mid-visit; completeness comes after.

| Step of the visit | Tab | What the NP checks against the AI's output |
| --- | --- | --- |
| Presenting complaint and differential | 1 Approaches | Has the differential missed something an "approach to" source lists? |
| History, exam and tests | 2 Assessments | Is the decision rule, score or test the right one, applied as published? Is the bedside scan (POCUS) within my training and scope? |
| Diagnosis and management | 3 Conditions | Does the plan match the current BC or Canadian guideline and its year? |
| Who the patient is | 4 Populations | Does anything change for this patient group? |
| Treatment | 5 Prescribing | Is the drug appropriate, covered, and checked against an independent reference? |
| Referral, forms, documentation | 6 Practice | Is it within NP scope, and what must be reported, filed or referred? |
| Using AI tools | 7 Tools | Is the AI tool used safely and working from the current documents? |
| Background reading | 8 Resources | Where to look when the topic isn't on NPPR yet |

**Pages by tab.** *(new)* marks a page not built yet; the number is its build wave within the tab.

- **1 Approaches** ([plan](https://claude.ai/artifact/4ryGRHfoVhvEURcuPSk1E9), decisions settled 2026-10-27): AAFP, McGill, UCalgary Black Books, PedsCases, Alberta Primary Care Pathways (built); Pathways BC Enhanced Care Pathways, all 53 in Pathways category 1 (built 2026-10-29 from Joe's Pathways index); Centre for Effective Practice clinical tools, all clinical tools with an Ontario label (built 2026-10-29: 36 of 41 tools, linked to each tool's CEP page because the tools open behind a reCAPTCHA); Canadian Family Physician "Approach to", "Management of" and "Diagnosis and management" articles, clinical topics, 2010 onward (built 2026-10-29: 114 articles; the last two added at Joe's request); AAFP "Management of" and "Diagnosis and Management" feature reviews added to the AAFP page (2026-10-29, 89 free articles, incl. obesity 2016 with its members-only 2024 update; 182 in all); Presentations A to Z, generated at build time from the other Approaches pages' lists (built 2026-10-29 by scripts/presentations.py in nppr-website-config, complaints in scripts/presentations.yml); TREKK pediatric emergency topics *(new, 3)*; CMAJ "Five things to know about" articles, clinical topics with year *(new, 3; added 2026-10-27 from the resource gap audit)*. Presentations A to Z should use the MCC Examination Objectives for its complaint headings; mcc.ca is blocked in cloud sessions, so the first version uses its own list of 68 complaints until mcc.ca can be reached. Condition pages link their matching Approaches items as the daily routine touches them.
- **2 Assessments:** Lab and imaging *(new, 1, published 2026-10-27)*; Preventive care and cancer screening *(new, 2)*; Physical exam by system *(new, 3)*; Clinical decision rules *(new, 4)*; Screening questionnaires and scales *(new, 5)* (order changed by Joe 2026-10-29); POCUS: Scope and training, Protocols and references *(new, 6, built in stage E; moved from Tools 2026-10-27, placeholder at assessments/pocus)*; retire Assessment Resources once its rows have moved. Added 2026-10-27 from the [resource gap audit](https://claude.ai/artifact/XoVNcRWTM1yEeBH6mz7MWr): Lab and imaging gets the BCCDC eLab Handbook, an ECG heading (LITFL ECG Library) and Radiopaedia; Clinical decision rules adds the Canadian Syncope Risk Score, Ottawa SAH Rule, Canadian TIA Score and TheNNT; Screening adds C-SSRS, STOP-Bang and HEADSSS; Preventive care leads with the BC Lifetime Prevention Schedule, then the Task Force, CPS Greig Health Record and CFPC Preventive Care Checklist; Physical exam adds Geeky Medics.
- **3 Conditions:** the Roadmap checklists above are the to-do list, in the build order given there. The older CKD, AKI, low back pain, calcium, potassium and sodium disorders pages were removed on 2026-10-29 and are rebuilt in wave 1 instead of updated in place. Infection pages link Firstline's Canadian Antibiotic Treatment Guidance (UTI first), and urgent care pages link RCCbc RTVS beside RACE.
- **4 Populations** ([plan](https://claude.ai/artifact/Smz8FYnzW34EFU3K96MKTV), decisions settled 2026-10-27; one PR per wave)**:** Pediatrics (fold in the Canadian Paediatric Society and Rourke stubs; add well-child care and an adolescents section, 1; pediatric acute care pages for croup and bronchiolitis, fever and gastroenteritis from Child Health BC, TREKK and CPS, wave set in the Populations plan); Pregnancy and Perinatal (add prenatal care and medication in pregnancy and lactation, 1); Older adults *(new, 2)*; Women's Health (rebuild, 2); Trans Care (rebuild, with gender-affirming hormone sources, 2); Rural and remote (rebuild BC Rural Health, 3); Indigenous Health (review, 3); Newcomers and refugees *(new, 3)*; Adults with intellectual and developmental disabilities *(new, 3)*.
- **5 Prescribing:** Rational prescribing, Drug coverage (PharmaCare and Special Authority), Drug references *(new, 1)*; Antimicrobials, Immunization *(new, 2; replace the Bugs & Drugs and BC Immunization Manual pages)*; Opioids, controlled drugs and substance use prescribing, Deprescribing *(new, 3)*.
- **6 Practice** ([plan](https://claude.ai/artifact/Fsisf7tmgnWJ9xwcKp2bHc), decisions settled 2026-10-27; one PR per wave, wave 1 waits for Joe's go-ahead)**:** Scope of practice and standards, Prescribing authority *(new, 1)*; Registration and licensure, Practice models and compensation, Documentation privacy and records, Starting NP practice in BC, Community of practice (NP Circle, NNPBC NP-PIP Community of Practice, BC ECHO series) *(new, 2)*; Consultation referral and advice, Forms and duty to report *(new, 3)*. Associations page removed for now (Joe, 2026-10-29); don't rebuild it unless Joe asks. Members-only sources are linked with an access label.
- **7 Tools** ([plan](https://claude.ai/artifact/2XqfqicaaAKEQUksHFCVtX), decisions settled 2026-10-27)**:** AI tools and what is loaded into them (POCUS moved to Assessments, 2026-10-27). AI Tools: Checking AI output, Safe use and accountability, AI scribes consent and privacy, AI tools NPs use (only tools approved by a BC health authority or funded by Infoway, with data residency and no rankings) *(new, 1, with step 3.3 llms.txt)*; Templates (peer-written charting templates and AI templates, a community project in the nppr-templates repository; a template is listed only when it is structure only, cites its sources, names its author and has one NP reviewer's approval); Evidence Packs (phase 3, steps 3.1, 3.2 and 3.4, 2).
- **8 Resources** ([plan](https://claude.ai/artifact/ACLq44znFt6SHSx3t176aX), decisions settled 2026-10-27)**:** a landing page with a "not on NPPR yet" search order (BC Guidelines, Canadian Task Force, specialty-society library, PEER and Tools for Practice, TRIP) and Guideline directories (with specialty-society guideline libraries; NICE and USPSTF labelled; Guideline Central and the Alberta Medical Association page dropped) and Evidence summaries and journals *(1, stage B)*; Libraries and databases (with UpToDate, DynaMed and BMJ Best Practice, labelled subscription with free routes) and CPD and learning *(new, 2, stage D)*. Flatten `8 Resources/Guidelines/` with redirects. Clinical Tools moves to Assessments: Clinical decision rules.
- **About:** has About NPPR, Contact, Disclaimer, Licence and Privacy, Install as an App and Submit a Link (since 2026-10-27). Still to add: a Contributor guide and Reviewer roster (steps 4.1 and 4.2) and a "How NPPR is kept current" page.

**Topic ownership.** A topic has one home page that holds its links; other tabs link to that page. A diagnosis goes in Conditions, a tool or test in Assessments, a drug or its coverage in Prescribing, a rule or form in Practice, a patient group in Populations, and an AI tool and what is loaded into it in Tools. Point-of-care ultrasound is an assessment, so it lives in Assessments. Specific cases:

| Topic | Home | Linked from |
| --- | --- | --- |
| BCCNM prescribing rules, controlled drugs, PharmaNet, PRIME | Practice: Prescribing authority | Every Prescribing page |
| PharmaCare, Special Authority, Limited Coverage programs | Prescribing: Drug coverage | Practice Forms; Indigenous Health (Plan W) |
| Drug-specific coverage criteria | The condition page's Prescribing section | — |
| Clinical OUD and AUD treatment | Conditions pages | Prescribing: Opioids and substance use |
| Antibiotic choice for an infection | The condition page | Prescribing: Antimicrobials (general references) |
| Deprescribing; immunization | Prescribing | Older adults; Pediatrics, Pregnancy, Preventive care |
| Drug-dosing calculators (CrCl, MME, PEN-FAST) | Prescribing | Assessments: Lab and imaging |
| Risk scores and calculators (eGFR, FIB-4, CHA2DS2-VASc) | Assessments, with "Used on:" links | Condition pages keep their own tools box |
| Preventive care and cancer screening; developmental screening | Assessments | Population pages, instead of their own screening lists |
| Prenatal care; well-child care | Populations pages | Conditions index |
| Pediatric versions of conditions (asthma, UTI, croup, bronchiolitis) | Populations: Pediatrics | Conditions index, under their system, marked (pediatric) |
| Menopause; frailty and dementia | Conditions | Women's Health; Older adults |
| Gender-affirming hormone therapy | Populations: Trans Care | Prescribing |
| Medication in pregnancy and lactation | Populations: Pregnancy and Perinatal | Prescribing |
| Driver fitness, WorkSafeBC and other reporting forms (no lab or imaging requisitions: sites supply their own, Joe 2026-10-27) | Practice: Forms | Assessments |
| RACE, Pathways, advice lines | Practice: Consultation, referral and advice | Condition pages' Advice and referral; Rural and remote |
| Documentation standards | Practice: Documentation | Tools: Templates |
| Safe use of AI tools, privacy, data residency | Tools: AI Tools | Practice: Documentation |
| Point-of-care ultrasound (scope, training, protocols) | Assessments: POCUS | Assessments: Physical exam by system; Tools index (one line) |
| Pathways BC Enhanced Care Pathways, Alberta Pathway Hub, Centre for Effective Practice tools | Approaches | Resources: Guideline directories (one line) |
| Specialty-society guideline libraries | Resources: Guideline directories | none (Practice: Associations removed 2026-10-29) |
| Therapeutics Initiative and Therapeutics Letter | Prescribing: Drug references | Resources: Evidence summaries (one line) |
| PEER, Tools for Practice, Choosing Wisely Canada | Resources: Evidence summaries | Condition pages cite single articles |
| "Approach to" articles | Approaches | Condition pages |

**Access labels.** Link members-only and subscription sources with a label so an NP knows before clicking: *members only* (NNPBC NP Portal, CNPS member pages), *login* (the Pathways BC directory; its Enhanced Care Pathway documents at pathwaysbc.ca/ci/<id> open without one and need no label), *subscription* (RxFiles app, CPS, Lexicomp, UpToDate, BMJ Best Practice; note when a health authority library gives free access). Label sources written for physicians *physician-focused* (for example Doctors of BC scribe resources, CAEP POCUS statements).

**Site platform** (decided 2026-10-27, Joe approved the [platform audit](https://claude.ai/artifact/EHYwiCpiTExS75Rubcfmog)). nppr.ca stays a static site on MkDocs Material, hosted on Cloudflare, with every change a draft PR; it does not move to WordPress.

- Write new generated features (Evidence Packs, Presentations A to Z, the calculators index, llms.txt) as stand-alone build scripts that read the frontmatter before or after the build, not as MkDocs hooks or plugins, so they carry over to Zensical unchanged.
- Don't build new features on Material's search box.
- Re-check Zensical at its 1.0 release, or by February 2027 at the latest; Astro Starlight is the fallback if it stalls.
- A way to contribute without GitHub (a Tally form that Claude turns into a PR, or a git-based web editor such as Sveltia CMS) waits for Phase 4.
- Platform PRs by stage, in nppr-website-config: **B** a preview link for each content PR, draft-status and access badges, a build warning for incomplete source entries, llms.txt (step 3.3); **C** calculators index and "Used on:" links (one script, after Clinical decision rules), a service worker for offline use; **D** Presentations A to Z with Approaches wave 2, branch rule and PR template (4.1), reviewer roster check (4.2), monthly review-due issues as a scheduled GitHub Action; **E** Evidence Packs (3.1, 3.2).

**Build order across tabs.** No more than two section PRs open at once, on top of the daily routine's limit of two condition pages awaiting review. Conditions continue through the routine throughout.

1. Stage A: settle each section plan's open decisions; add a Prescribing template to the templates. *(Prescribing template added 2026-10-27.)*
2. Stage B: Practice wave 1 · Prescribing wave 1 · Assessments wave 1 · Populations wave 1 · Resources wave 1 · Tools wave 1 (AI Tools and step 3.3 llms.txt). Then run step 2.4 on Populations and Resources.
3. Stage C: Prescribing wave 2 · Practice wave 2 · Assessments waves 2 and 3 · Populations wave 2 · Approaches wave 1.
4. Stage D: Prescribing wave 3 · Practice wave 3 · Assessments waves 4 and 5 · Populations wave 3 · Resources wave 2 · Approaches waves 2 and 3 · About pages. This completes the phase 2 gate.
5. Stage E: Assessments POCUS (wave 6), then Tools wave 2: phase 3 (Evidence Packs, steps 3.1, 3.2 and 3.4).

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
In nppr-website-config, write a stand-alone build script (run before the site build, not an MkDocs hook; see Site platform) that creates an Evidence Pack page for every condition page from its sources frontmatter, as described in the Loading guidelines into AI tools section of NPPR-FRAMEWORK.md: a manifest table, direct links to each publisher's PDF (link only, no hosted copies), a Superseded list, and a changelog from git history. Put the packs under the Evidence Packs section and link each condition page to its pack. Show me the Hypertension pack in the local preview.
```

Check: every PDF link in the Hypertension pack opens the publisher's current file.

**3.2 Manifest CSV and RSS feed** · Run in: Claude Code · Opus 5.5, medium

```text
Extend the Evidence Pack build script to publish each pack's manifest as a downloadable CSV, plus one combined CSV of all packs, and an RSS feed of pack changes so NPs can follow updates.
```

Check: open one CSV in Excel and add the RSS feed to a reader.

**3.3 llms.txt for other AI tools** · Run in: Claude Code · Opus 5.5, medium

Runs early, with Tools wave 1 in stage B (decided 2026-10-27), since it needs no Evidence Packs.

```text
Write a post-build script in nppr-website-config (not an MkDocs plugin or hook; see Site platform) so the site publishes /llms.txt, Markdown copies of each page and llms-full.txt. Group the sections by the eight top-level sections and leave out About. Show me llms.txt from the local preview.
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
