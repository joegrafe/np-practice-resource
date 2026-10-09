---
title: <% tp.file.title %>
type: assessment
tags: [assessment]
jurisdiction: [BC, CA]
status: draft
last-reviewed: <% tp.date.now("YYYY-MM-DD") %>
review-due: <% tp.date.now("YYYY-MM-DD", 365) %>
reviewers: []
sources:
  # BC sources first, then national, then international (INTL). Field list: FRONTMATTER.md
  - id:
    title:
    publisher:
    jurisdiction: BC
    kind: guideline        # guideline | algorithm | pathway | summary | tool | patient
    version:
    url:
    pdf:                   # publisher's own PDF link only
    checked: <% tp.date.now("YYYY-MM-DD") %>
---
*Scope: which system or exam this covers and when it's used in primary care.*

## Focused History
- Key question
- Key question

## Exam and Special Tests

| **Test / Manoeuvre** | **Technique** | **Positive Finding** | **Sn / Sp** | **Link** |
| -------------------- | ------------- | -------------------- | ----------- | -------- |
|                      |               |                      |             |          |

## Clinical Decision Rules & Calculators
- [Rule Name (MDCalc)](URL) — *what it rules in or out*

??? danger "Red Flags"
	- Finding that needs urgent action or referral.

## Learning Resources & Videos
- [Resource Name](URL) — *what it shows*

??? example "Sample Documentation"
	Normal exam written as it would appear in a chart note.

---

??? cite "References"
	1. Author, A. (Year). *Title*. Publisher. [Link](URL)  
