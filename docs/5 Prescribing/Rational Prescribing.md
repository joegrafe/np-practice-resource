---
title: Rational Prescribing
type: prescribing
tags: [prescribing, rational-prescribing]
jurisdiction: [BC, CA, INTL]
status: published
last-reviewed: 2026-10-27
review-due: 2027-10-27
reviewers: [joegrafe]
description: "Published frameworks for working through a prescribing decision, and where to check each step in BC."
sources:
  # BC
  - id: ti-therapeutics-letter
    title: Therapeutics Letter
    publisher: Therapeutics Initiative, University of British Columbia
    jurisdiction: BC
    kind: summary
    url: https://www.ti.ubc.ca/therapeutics-letter/
    checked: 2026-10-27
  - id: ti-drug-assessments
    title: Drug Assessments
    publisher: Therapeutics Initiative, University of British Columbia
    jurisdiction: BC
    kind: summary
    url: https://www.ti.ubc.ca/research-publications/drug-assessments/
    checked: 2026-10-27
  - id: bc-pad-service
    title: B.C. Provincial Academic Detailing (PAD) service
    publisher: BC Ministry of Health
    jurisdiction: BC
    kind: tool
    url: https://www2.gov.bc.ca/gov/content/health/practitioner-professional-resources/pad-service
    checked: 2026-10-27
  - id: ti-prescribing-portraits
    title: Prescribing Portraits
    publisher: Therapeutics Initiative, University of British Columbia
    jurisdiction: BC
    kind: tool
    url: https://www.ti.ubc.ca/portrait/
    checked: 2026-10-27
  - id: bccnm-np-prescribing-standard
    title: "Nurse Practitioners: Prescribing Drugs (practice standard)"
    publisher: BC College of Nurses and Midwives
    jurisdiction: BC
    kind: guideline
    url: https://www.bccnm.ca/NP/PracticeStandards/Pages/Prescribing.aspx
    checked: 2026-10-27
  # National
  - id: rxfiles-academic-detailing
    title: RxFiles Academic Detailing
    publisher: RxFiles, University of Saskatchewan
    jurisdiction: CA
    kind: tool
    url: https://www.rxfiles.ca/rxfiles/modules/aboutus/AboutUs.aspx
    checked: 2026-10-27
  - id: cwc-medications
    title: Medications
    publisher: Choosing Wisely Canada
    jurisdiction: CA
    kind: tool
    url: https://choosingwiselycanada.org/medications/
    checked: 2026-10-27
  - id: ohri-patient-decision-aids
    title: Patient Decision Aids, A to Z inventory
    publisher: Ottawa Hospital Research Institute
    jurisdiction: CA
    kind: patient
    url: https://decisionaid.ohri.ca/AZsearch.php
    checked: 2026-10-27
  # International
  - id: who-guide-good-prescribing-1994
    title: "Guide to Good Prescribing: A Practical Manual"
    publisher: World Health Organization
    jurisdiction: INTL
    kind: guideline
    version: "1994"
    url: https://iris.who.int/handle/10665/59001
    checked: 2026-10-27
  - id: schiff-conservative-prescribing-2011
    title: Principles of Conservative Prescribing
    publisher: Archives of Internal Medicine (Schiff GD et al.)
    jurisdiction: INTL
    kind: summary
    version: "2011"
    url: https://pubmed.ncbi.nlm.nih.gov/21670331/
    checked: 2026-10-27
  - id: thinkcascades-2022
    title: "ThinkCascades: A Tool for Identifying Clinically Important Prescribing Cascades Affecting Older People"
    publisher: Drugs & Aging (McCarthy LM et al.)
    jurisdiction: INTL
    kind: tool
    version: "2022"
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9477172/
    checked: 2026-10-27
---
<!-- Prescribing wave 1 (plan: https://claude.ai/artifact/GJeAP8SPPZrsk4G8ihftgU, approved by Joe 2026-10-27).
     Joe's decision 6: link published frameworks and map each step to where it is checked; no NPPR-written algorithm.
     The step names in the table are navigation labels in the order of the WHO six-step model, not the WHO's wording.
     Not opened from the build container (host not reachable there): decisionaid.ohri.ca (URL from search results).
     The WHO guide's PDF download would not load; the IRIS record page links it.
     NP prescribing rules belong on Practice: Prescribing authority; link that page here once it is built. -->
*NPPR links published prescribing frameworks rather than writing its own algorithm. The table maps each step of a prescribing decision to the BC or Canadian source that checks it and the NPPR page that holds it.*

## Key Sources

- [Therapeutics Initiative - Therapeutics Letter (UBC)](https://www.ti.ubc.ca/therapeutics-letter/) — *independent, bimonthly reviews of drug therapy questions, published since 1994; free*
    - [Drug Assessments](https://www.ti.ubc.ca/research-publications/drug-assessments/)
- [WHO - Guide to Good Prescribing: A Practical Manual (1994)](https://iris.who.int/handle/10665/59001) — *international; the six-step model of rational prescribing, written for teaching; the record page links the PDF*
- [Schiff GD et al. - Principles of Conservative Prescribing (2011)](https://pubmed.ncbi.nlm.nih.gov/21670331/) — *international; Arch Intern Med 2011;171(16):1433-40; full text may need a subscription*

## Where to Check Each Step

The steps follow the order of the WHO model, with a check of NP prescribing authority added.

| Step | Where to check | On NPPR |
| --- | --- | --- |
| 1. Define the problem | The BC Guideline or national guideline for the condition | [Approaches](../1%20Approaches/index.md) · [Conditions](../3%20Conditions/index.md) |
| 2. Set the treatment goal | The same guideline's targets and outcomes | The condition page's Key Sources |
| 3. Choose the drug | Therapeutics Initiative, RxFiles, CPS, Health Canada product monographs | [Drug References](Drug%20References.md) |
| 4. Check NP prescribing authority | [BCCNM - Nurse Practitioners: Prescribing Drugs](https://www.bccnm.ca/NP/PracticeStandards/Pages/Prescribing.aspx) | Practice: Prescribing authority *(coming)* |
| 5. Check coverage and start | PharmaCare Formulary Search, Special Authority | [Drug Coverage](Drug%20Coverage.md) |
| 6. Inform the patient | Decision aids and patient handouts below | The condition page's Patient Resources |
| 7. Monitor, report and stop | MedEffect adverse reaction reporting, prescribing cascades, deprescribing algorithms | [Drug References](Drug%20References.md#safety-and-supply) · Deprescribing *(coming)* |

## Further Resources

### Independent Drug Education in BC
- [BC Ministry of Health - Provincial Academic Detailing (PAD) service](https://www2.gov.bc.ca/gov/content/health/practitioner-professional-resources/pad-service) — *accredited sessions with a PAD pharmacist on selected drug therapy topics; book through your local academic detailer or PAD@gov.bc.ca*
- [Therapeutics Initiative - Prescribing Portraits](https://www.ti.ubc.ca/portrait/) — *a snapshot of your own recent prescribing on a topic, compared with other BC clinicians; open to NPs with an active practice; online registration required*
- [RxFiles Academic Detailing (Saskatchewan)](https://www.rxfiles.ca/rxfiles/modules/aboutus/AboutUs.aspx) — *drug comparison charts and academic detailing; the app needs a subscription*

### Prescribing Less and Prescribing Safely
- [Choosing Wisely Canada - Medications](https://choosingwiselycanada.org/medications/) — *campaigns, prescriber tools and quality improvement toolkits on medication use, including antibiotics, opioids, sedatives and PPIs*
- [ThinkCascades (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9477172/) — *international, Canadian-led; nine clinically important prescribing cascades in older people; Drugs Aging 2022;39(10):829-40*

### Shared Decision-Making
- [Ottawa Hospital Research Institute - Patient Decision Aids, A to Z inventory](https://decisionaid.ohri.ca/AZsearch.php) — *decision aids by topic, screened against international standards*

## NP Prescribing Notes

- [BCCNM - Nurse Practitioners: Prescribing Drugs](https://www.bccnm.ca/NP/PracticeStandards/Pages/Prescribing.aspx) — *the standard, limits and conditions for NP prescribing in BC; the full set of prescribing rules will sit on Practice: Prescribing authority*
