# Cloud environment allowed-domain lists

The cloud environment that builds NPPR holds about 400 entries in its Allowed domains setting, and a site whose pages sit on subdomains needs two (`site.ca` and `*.site.ca`), so one list cannot carry every site NPPR links. Joe keeps three environments: Core is the default, and a wave switches to Environment 1 or 2 only when it needs a site Core lacks.

| List | Use it for | Entries (2026-11-09) |
|---|---|---|
| `environment-core.txt` | **Core, the default.** The journal sites, the `UNOPENED-SOURCES.csv` rows whose action is `allowlist` or `allowlist: core`, then every domain the site links, whatever its region, in order of how many links point at it, then the other unopened-source candidates, filled to the 400-entry cap. Sites with one link and zero-link candidates fall off first. | 400 |
| `environment-1.txt` | **Environment 1: BC, Alberta and Canada.** BC and national condition, assessment, prescribing, practice and population waves; link checks and page audits of existing pages; site and config work. Core's top sites, then every other Canadian source the site links, calculators and patient resources. | 356 |
| `environment-2.txt` | **Environment 2: Ontario, international and pediatric.** New condition pages from wave 17 on (BC Guideline + Ontario + AAFP sweep), Ontario waves (ON-4 and later), AAFP, DermNet, NICE and other international sweeps, pediatric pages, re-checks of `UNOPENED-SOURCES.csv` rows. Core's top sites, then every other Ontario, international and pediatric source, the unopened-source candidates and the research sites of the 2026-10-29 list that no page links yet. | 370 |

`domains.csv` lists every domain with its environment(s) (`core`, `1`, `2`), link count, regions and hosts: look a site up there before a wave to see which environment it needs. Both lists have room (about 44 and 30 entries on 2026-11-09) for the sites a wave adds.

**Top sites on every list (Joe, 2026-11-09):** Environments 1 and 2 both start with Core's top sites: the journal sites, the allowlist requests and the 150 most-linked sites (every site with 3 or more links; `SHARED_TOP` in the script). A wave on either list keeps the sites most pages link.

## Rules

- Core is on unless a thread says otherwise. Before a wave or thread, the coordinator or the thread names the environment from the table above when it is not Core, and Joe switches to it. As the site grows past what Core holds, Core keeps the most-linked sites and the lists 1 and 2 carry the rest. A thread that finds a site missing from the active environment adds a row to `UNOPENED-SOURCES.csv` with action `allowlist: environment N` and does not switch mid-build.
- Entry format: bare domain, plus `*.domain` when the site serves pages from subdomains. No `www.` lines, no subdomains under a wildcard, no paths.
- Regenerate after a wave that adds sources: `python3 scripts/environment_lists.py` from the vault root reads every list sheet, `docs/sources.csv`, every page and `UNOPENED-SOURCES.csv`, and rewrites the three files. Commit them with the wave, and say in the PR when a list changed so Joe can paste the new list into the environment's settings.
- `previous-list-2026-11-05.txt` is Joe's saved 2026-10-29 list, kept so sites from it that no page links yet stay on environment 2.
