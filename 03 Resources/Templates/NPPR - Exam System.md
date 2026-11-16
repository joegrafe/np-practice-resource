---
title: <% tp.file.title %>
type: assessment
tags: [assessment, physical-exam]
jurisdiction: [BC, CA]
aliases: []
status: draft
last-reviewed: <% tp.date.now("YYYY-MM-DD") %>
review-due: <% tp.date.now("YYYY-MM-DD", 365) %>
reviewers: []
---
<!-- A body system's exam page, in docs/2 Assessments/Physical Exam by System/ beside the folder's index (plan https://claude.ai/artifact/ULf8Y8ikpxTsovq4GaywcZ, 2026-11-16).
     A system gets its own page once it has about 15 links on Physical Exam by System; move its rows here, add the page to the index sheet's Exam Pages by System list, and point inbound links at the new page.
     Exam technique only (Joe, 2026-11-01): no condition pages, no red flags or management in our own words; what the findings mean lives on each condition page.
     Sources unconfirmed because their sites block checks, and what was left out and why.
     Link to the source; don't restate its technique, findings or cut-offs. -->
<!-- The page is its frontmatter plus <% tp.file.title %>.csv beside it, one row per line; the site build writes it in here.
     Copy NPPR - Exam System.csv beside the page and rename it to the page's name. Edit the sheet, not this page.
     Columns: List sheets in NPPR-FRAMEWORK.md. The intro line is the first row (kind md, no heading).
     Sections, in order (leave out a section with no sources):
       Exam Guides and Videos (whole-system walk-throughs: Stethopedia, U of T Clinical Skills Hub, then Stanford Medicine 25, UCSD, Geeky Medics)
       The exam steps, one heading each, holding sources about that step:
         chest and heart: Inspection, Palpation, Percussion, Auscultation
         abdomen: Inspection, Auscultation, Percussion, Palpation (steps one source teaches together share a heading)
         joints: one heading per joint, since each joint source covers look, feel, move and special tests
         neurology: Mental Status, Cranial Nerves, Motor, Sensory, Reflexes, Coordination and Gait
         skin: Inspection, Skin Checks and Dermoscopy, Photos and Teledermatology
         eyes, ears, nose and throat: Inspection, Visual Acuity or Otoscopy, Fundoscopy, Special Tests
       Children (and Newborns): pediatric technique and screens
       Skin of Colour: only where signs look different in darker skin (rashes, cyanosis, jaundice, pallor)
       Related Pages: kind md rows to Clinical Decision Rules, Screening Questionnaires, POCUS and the condition pages that use the exam
     Every linked top-level row carries a region code from docs/regions.csv; Canadian sources first, then Stanford Medicine 25 as the first international source, each note starting "International source: <country>;".
     Put the year in the year column, not the title. A link to another NPPR page is a kind md row (../ for Assessments pages, ../../ for other sections). -->
<div class="nppr-filter" data-ai="off" data-placeholder="Filter, e.g. spleen"></div>

<!-- nppr-list: <% tp.file.title %>.csv style=condition -->
