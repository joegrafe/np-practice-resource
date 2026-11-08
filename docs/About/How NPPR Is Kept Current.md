---
title: How NPPR Is Kept Current
slug: kept-current
description: "How NPPR.ca chooses its sources, keeps one current version of each, reviews every page, checks its links and uses AI tools, and how to report a problem."
type: about
tags: [about]
aliases: [kept current, editorial policy, editorial process, review cycle, how pages are reviewed, how sources are chosen, update policy, link check, ai drafting, ai assisted, methods, quality]
jurisdiction: [BC, CA]
status: draft
last-reviewed: 2026-11-08
review-due: 2027-11-08
reviewers: []
---
<!-- Build wave 17 (2026-11-08), About plan PR 2 (https://claude.ai/artifact/QiZKA6F7GShkVt2VLXRVPA, section 5; Joe approved all six decisions 2026-10-26, including decision 3: say that pages are drafted with AI help).
     Joe is a nurse practitioner student: the page names the editor's role from the Team page and never says pages are approved "by an NP".
     Every claim here describes something the site or its repositories do now (review_dates hook, Weekly link check workflow, PR checks, sources registry, UNOPENED-SOURCES.csv, missed-search log). Change it when they change. -->
*How NPPR chooses its sources, keeps them current and checks its own work, so you know how far to trust a link.*

## How sources are chosen

- **Your province first.** Each page lists your province's sources first, then national Canadian sources, then international guidance, labelled as such. British Columbia is the default; pick your province in the header.
- **The publisher's own copy.** Every entry links to the publisher's web page for the document, with its PDF beside it. NPPR doesn't host or copy anyone else's documents.
- **No advice of our own.** NPPR doesn't write clinical recommendations. It points to the guideline, tool or review that does.
- **Point-of-care first.** Pages favour sources a nurse practitioner can use during a visit: a provincial guideline, a national guideline, then one high-yield review.

## One current version of each source

- **A year beside every guideline.** Every guideline, algorithm and pathway shows the year of its current version.
- **Recorded once.** Each document is one row in NPPR's sources register, with its address, PDF, year and the date it was last checked. Every page that cites it reads that row, so when a guideline is updated, one change updates every page.
- **Old versions come off.** When a guideline is replaced, the new version takes its place on every page. The old one is noted in the register, never on the page.

## Reviews and dates

- **Every page is dated.** Under each page title you'll see when it was last reviewed, when its next review is due and who reviewed it. The foot of the page shows when it last changed.
- **A yearly review.** Each page is reviewed within 12 months, or sooner when one of its sources publishes a new version. AI Tools pages are reviewed every 6 months, because the tools change fast.
- **Overdue pages say so.** Once a page passes its review date, a *Review overdue* banner appears at the top until it has been checked again.
- **Drafts are marked.** A new page starts as a draft and is published only after review. The [Team](Team.md) page lists the editor and reviewers.

## How changes are made

- **In public.** Every change is a pull request in NPPR's public [GitHub repository](https://github.com/joegrafe/np-practice-resource), so anyone can see what changed, when and why.
- **Checked before it goes live.** Automatic checks run on every change: the page format, the sources register, a test build of the site, and a search check that the main terms still find the right page. A change that fails a check isn't published.
- **Approved by the editor.** Nothing goes live until the editor has looked at a preview of the changed pages and approved it.

## Link checks

- **Every week.** An automated check opens every link on the site each Monday and lists broken and redirected links for fixing.
- **Blocked sites aren't dropped.** Some publishers block automated checks. Those sources are opened by hand, and any that can't be opened are kept on a list to check, not left out.

## How AI tools are used

NPPR is built to help nurse practitioners check what AI tools tell them, and it uses AI tools to help build its pages.

- **What AI does.** An AI assistant helps search publishers' sites for sources, drafts page rows and runs the checks above.
- **What it doesn't do.** AI is never the source of a page's content. Every link points to a document that was opened on the publisher's own site, with the year shown there.
- **Who decides.** The editor reviews every change before it goes live, and you can see each change on GitHub.

## Found a problem?

- **Wrong or broken link, or a newer version:** use *Submit issue on GitHub* at the bottom of any page, or the [Contact](Contact.md) form if you don't have a GitHub account.
- **A source NPPR should have:** [Submit a link](Submissions.md). No account needed.
- **A search that found nothing:** the words are logged without anything about you, so the missing topic can be added. See [Disclaimer, Licence and Privacy](Disclaimer%2C%20Licence%20and%20Privacy.md#privacy).
