---
title: Drug References
type: prescribing
tags: [prescribing, drug-information, medication-safety]
jurisdiction: [BC, CA, INTL]
status: review
last-reviewed: 2026-10-27
review-due: 2027-10-27
reviewers: []
description: "Independent and Canadian drug references for checking a drug choice: monographs, comparison charts, safety alerts, shortages and dosing calculators."
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
  - id: bc-pharmacare-drug-shortages
    title: Drug shortages
    publisher: BC Ministry of Health
    jurisdiction: BC
    kind: tool
    url: https://www2.gov.bc.ca/gov/content/health/practitioner-professional-resources/pharmacare/pharmacies/drug-shortage-information
    checked: 2026-10-27
  # National
  - id: cpha-cps
    title: CPS (Compendium of Pharmaceuticals and Specialties)
    publisher: Canadian Pharmacists Association
    jurisdiction: CA
    kind: tool
    url: https://www.pharmacists.ca/products-services/compendium-of-pharmaceuticals-and-specialties/
    checked: 2026-10-27
  - id: rxfiles-drug-comparison-charts
    title: RxFiles Drug Comparison Charts
    publisher: RxFiles, University of Saskatchewan
    jurisdiction: CA
    kind: tool
    version: "15th edition"
    url: https://www.rxfiles.ca/rxfiles/uploads/documents/books/charts.html
    checked: 2026-10-27
  - id: hc-drug-product-database
    title: Drug Product Database
    publisher: Health Canada
    jurisdiction: CA
    kind: tool
    url: https://health-products.canada.ca/dpd-bdpp/index-eng.jsp
    checked: 2026-10-27
  - id: hc-medeffect
    title: MedEffect Canada
    publisher: Health Canada
    jurisdiction: CA
    kind: tool
    url: https://www.canada.ca/en/health-canada/services/drugs-health-products/medeffect-canada.html
    checked: 2026-10-27
  - id: hc-recalls-safety-alerts
    title: Recalls and safety alerts
    publisher: Government of Canada
    jurisdiction: CA
    kind: tool
    url: https://recalls-rappels.canada.ca/en
    checked: 2026-10-27
  - id: hc-drug-shortages
    title: Drug shortages in Canada
    publisher: Health Canada
    jurisdiction: CA
    kind: tool
    url: https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-shortages.html
    checked: 2026-10-27
  - id: ismp-canada
    title: Institute for Safe Medication Practices Canada
    publisher: ISMP Canada
    jurisdiction: CA
    kind: tool
    url: https://www.ismp-canada.org/
    checked: 2026-10-27
  - id: cda-amc-find-reports
    title: Find Reports
    publisher: Canada's Drug Agency (CDA-AMC)
    jurisdiction: CA
    kind: summary
    url: https://www.cda-amc.ca/find-reports
    checked: 2026-10-27
  # International
  - id: mdcalc-cockcroft-gault
    title: Creatinine Clearance (Cockcroft-Gault Equation)
    publisher: MDCalc
    jurisdiction: INTL
    kind: tool
    url: https://www.mdcalc.com/calc/43/creatinine-clearance-cockcroft-gault-equation
    checked: 2026-10-27
---
<!-- Prescribing wave 1 (plan: https://claude.ai/artifact/GJeAP8SPPZrsk4G8ihftgU, approved by Joe 2026-10-27).
     Topic ownership (NPPR-FRAMEWORK.md): Therapeutics Initiative and drug-dosing calculators live here;
     medication in pregnancy and lactation lives on Populations: Pregnancy and Perinatal; gender-affirming hormones on Trans Care.
     Access labels: subscription sources are labelled (Joe's decision 3).
     Not opened from the build container (host not reachable there): ismp-canada.org, cda-amc.ca, healthproductshortages.ca
     (URLs from search results and Health Canada's drug shortages page). CPS product page loaded; pharmacists.ca/cps returned 403. -->
*Independent and Canadian references for checking a drug choice against the AI's suggestion or your own: monographs, comparison charts, safety alerts, shortages and dosing calculators. Coverage is on [Drug Coverage](Drug%20Coverage.md).*

<div class="nppr-filter" data-ai="off" data-placeholder="Filter, e.g. monograph"></div>

## Key Sources

- [Therapeutics Initiative - Therapeutics Letter (UBC)](https://www.ti.ubc.ca/therapeutics-letter/) — *independent, bimonthly reviews of drug therapy questions, published since 1994; free*
    - [Drug Assessments](https://www.ti.ubc.ca/research-publications/drug-assessments/)
- [Canadian Pharmacists Association - CPS (Compendium of Pharmaceuticals and Specialties)](https://www.pharmacists.ca/products-services/compendium-of-pharmaceuticals-and-specialties/) — *Canadian drug monographs and therapeutic information* · *subscription*
- [RxFiles - Drug Comparison Charts, 15th edition](https://www.rxfiles.ca/rxfiles/uploads/documents/books/charts.html) — *side-by-side drug comparisons by system, from University of Saskatchewan academic detailing; some charts and the app need a subscription*

## Monographs and Product Information

- [Health Canada - Drug Product Database](https://health-products.canada.ca/dpd-bdpp/index-eng.jsp) — *every drug authorized for sale in Canada, with its product monograph and marketing status; updated nightly*
- [Canada's Drug Agency (CDA-AMC) - Find Reports](https://www.cda-amc.ca/find-reports) — *reimbursement reviews and recommendations that inform public drug plans, including PharmaCare*

## Safety and Supply

- [Health Canada - MedEffect Canada](https://www.canada.ca/en/health-canada/services/drugs-health-products/medeffect-canada.html) — *report an adverse reaction and find new drug safety information*
    - [Adverse reaction reporting](https://www.canada.ca/en/health-canada/services/drugs-health-products/medeffect-canada/adverse-reaction-reporting.html)
    - [Advisories, warnings and recalls](https://www.canada.ca/en/health-canada/services/drugs-health-products/medeffect-canada/advisories-warnings-recalls.html)
- [Government of Canada - Recalls and safety alerts](https://recalls-rappels.canada.ca/en)
- [ISMP Canada](https://www.ismp-canada.org/) — *safety bulletins, including the "Do Not Use" list of dangerous abbreviations*
- [BC PharmaCare - Drug shortages](https://www2.gov.bc.ca/gov/content/health/practitioner-professional-resources/pharmacare/pharmacies/drug-shortage-information) — *current shortages at BC community pharmacies, with covered alternatives and coverage notes*
- [Health Canada - Drug shortages in Canada](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-shortages.html) — *national shortage and discontinuation reports from manufacturers*
    - [Drug and health product shortages reporting site](https://healthproductshortages.ca/)

## Dosing Calculators

- [MDCalc - Creatinine Clearance (Cockcroft-Gault Equation)](https://www.mdcalc.com/calc/43/creatinine-clearance-cockcroft-gault-equation) — *international; for renal dose adjustment*

## Special Populations

- [Pregnancy and Perinatal](../4%20Populations/Pregnancy%20and%20Perinatal.md) — *medication in pregnancy and lactation*
- [Trans Care](../4%20Populations/Trans%20Care.md) — *gender-affirming hormone therapy*
- [Pediatrics](../4%20Populations/Pediatrics/Pediatrics.md)

## NP Prescribing Notes

- Check that a drug is within NP prescribing authority in [BCCNM - Nurse Practitioners: Prescribing Drugs](https://www.bccnm.ca/NP/PracticeStandards/Pages/Prescribing.aspx). The full set of NP prescribing rules will sit on Practice: Prescribing authority.
- For how to work through a prescribing decision, see [Rational Prescribing](Rational%20Prescribing.md).
