#!/usr/bin/env python3
"""Check every page in docs/ against FRONTMATTER.md and the list-sheet format.

Usage: python3 scripts/check_pages.py [docs_dir] [--report report.md] [--files f1 f2 ...]
                                       [--audit DIR] [--config nppr-website-config]
  --files   only report problems in these files (paths as git prints them);
            site-wide checks such as duplicate source ids still read every page.
  --report  also write the findings as a Markdown table (the PR job summary).
  --audit   also write a scorecard, one row per page with a count per rule
            (scorecard.csv and summary.md in DIR): the page-by-page compliance
            audit (plan: NPPR-FRAMEWORK.md, Roadmap item 4, 2026-11-05).
  --config  the nppr-website-config checkout, for the search rule (default: the
            folder beside this repository, or $NPPR_CONFIG_DIR).

Checks:
  frontmatter    required page fields, allowed values, dates as YYYY-MM-DD
  review-due     review-due is after last-reviewed and has not passed
  sources        docs/sources.csv, the sources registry: one row per document with a
                 unique slug id, a title, a region from docs/regions.csv, a url or a
                 pdf, a kind and dates in YYYY-MM-DD; supersedes names another id.
                 A page carries no frontmatter sources list (retired 2026-11-05).
  source         a sheet row's source names a registry id; a row that repeats the
                 registry's url, pdf or year is told to leave the cell blank, and a
                 linked row whose address is in the registry is told its id
  list-sheet     each <!-- nppr-list: --> marker names a CSV beside the page, the CSV
                 uses only the list-sheet columns, every row has a title (a note row
                 has a note), kind and level hold allowed values, links are http(s),
                 every top-level row with a link has a region from docs/regions.csv
                 (or a source whose registry row has one),
                 an only mark sits on a top-level row that has a region, a row
                 whose link is a one-region service (BCCNM, RACE, Pathways BC,
                 BC Laws, CNO, Ontario Health) is marked only, and on a
                 condition sheet each BC key source is only=yes with an
                 only=other copy under Further Resources,
                 and every CSV in docs/ is used by a page
  page-body      a page with a list sheet holds no heading or link line of its own
                 (Approaches, About and index pages excepted): the page is its
                 frontmatter plus its sheet (a warning)
  Audit rules (warnings; the compliance audit of 2026-11-05 clears them by section,
  and each moves out of WARN_ONLY once every page passes it):
  region-order   within a section (or its subheading), a top-level row ranked below the
                 row before it (provinces and territories, then CA, then US, then INTL); only=other
                 copies and the Ontario rows that follow their BC mirrors are skipped
  intro-in-page  a sheet-backed page whose intro line (or other text) is still in the
                 Markdown instead of the sheet's first row
  section-order  sheet headings out of the Page standard order for the page type, or
                 a heading a condition page doesn't have
  key-sources    Key Sources count outside 1 to 3, in the BC view and each other live
                 region's view
  superseded     a row that names (or links) a document another registry row supersedes
  duplicate      the same document (id or address) on two top-level rows of one page
  pdf-alone      a row whose only link is a PDF; once checked that no publisher page
                 exists, the sheet row's url "-" records that and the rule leaves it
  year           a guideline, algorithm or pathway row with no year, or a year in
                 brackets in its title
  rxfiles        a condition page with no rxfiles.ca row in Prescribing, and no Prescribing note
                 recording that RxFiles has nothing for the condition (check that
                 RxFiles has a resource for it)
  aafp-first     on condition and population pages, an international row before an
                 AAFP row in the same section
  jurisdiction   frontmatter jurisdiction that doesn't match the regions on the rows (a live
                 province with rows but not listed, or a listed code with no row)
  bc-wording     "in BC" (or "in Ontario") on a row not marked only=yes
  md-links       a prose md row with an external link: a document belongs in a linked row
                 with a registry id (how-to steps, contacts, prescribing notes, tables
                 and list lines stay md, as the Page standard says)
  search         a content page with no aliases (frontmatter or hooks/search_aliases.yml)
                 or no line in scripts/search-checks.txt (needs nppr-website-config)
  index-list     a page missing from its folder's In This Section list, or a listed
                 page that no longer exists
  registry-checked  a registry row with no checked date, or one older than 12 months
  team           the Team sheet (style=team, docs/About/Team.csv) has its own
                 columns, an id, name and allowed level on every row, and a photo
                 file that exists; every id in a page's reviewers is on the sheet
                 (a warning), and a published page isn't reviewed only by past
                 members (a warning)

Each finding is an error or a warning. Rules that some existing pages don't meet
yet are warnings (WARN_ONLY below); move a rule to an error once pages pass.
The home page (docs/index.md) is skipped: it has only a title.
Prints GitHub Actions annotations when run in Actions. Exits 1 only on errors.
Needs PyYAML.
"""
import argparse
import csv
import datetime
import os
import pathlib
import re
import sys

import yaml

TYPES = {"approach", "assessment", "condition", "population", "prescribing", "practice",
         "evidence-pack", "resource", "index", "about"}
STATUSES = {"draft", "review", "published"}
REGIONS_SHEET = "regions.csv"  # docs/regions.csv: code, name, country, kind, live
JURIS = ["BC", "CA", "INTL"]  # replaced by the codes in docs/regions.csv when it exists
JURIS_RANK = {}  # code -> order sources are listed in: provinces, then CA, then US, then INTL
LIVE = ["BC"]  # regions with live=yes in docs/regions.csv: the views the key-sources rule counts


def load_regions(docs):
    """Region codes from docs/regions.csv, in source-order rank."""
    global JURIS, JURIS_RANK
    path = docs / REGIONS_SHEET
    if not path.exists():
        JURIS_RANK = {j: i for i, j in enumerate(JURIS)}
        return
    global LIVE
    codes, rank, live = [], {}, []
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            code = (row.get("code") or "").strip()
            if not code:
                continue
            kind, country = (row.get("kind") or "").strip(), (row.get("country") or "").strip()
            codes.append(code)
            rank[code] = (0 if kind in ("province", "territory", "state") and country == "CA"
                          else 1 if code == "CA" else 2 if country == "US" else 3 if code == "INTL" else 2)
            if (row.get("live") or "").strip().lower() == "yes" and kind in ("province", "territory", "state"):
                live.append(code)
    JURIS, JURIS_RANK = codes, rank
    LIVE = live or ["BC"]
KINDS = {"guideline", "algorithm", "pathway", "summary", "tool", "patient"}
SYSTEMS = {
    "Cardiovascular": "cardiovascular", "Respiratory": "respiratory",
    "Endocrine and Metabolic": "endocrine-metabolic",
    "Renal and Genitourinary": "renal-genitourinary",
    "Gastrointestinal and Liver": "gastrointestinal-liver",
    "Musculoskeletal": "musculoskeletal", "Neurology": "neurology",
    "Mental Health and Substance Use": "mental-health-substance-use",
    "Infectious Disease": "infectious-disease", "Dermatology": "dermatology",
    "Hematology and Oncology": "hematology-oncology",
    "Eyes, Ears, Nose and Throat": "eyes-ears-nose-throat",
    "Sexual and Reproductive Health": "sexual-reproductive-health",
}
PAGE_REQUIRED = ["title", "type", "tags", "jurisdiction", "status", "last-reviewed",
                 "review-due", "reviewers"]
REGISTRY_SHEET = "sources.csv"  # docs/sources.csv: the sources registry
REGISTRY_COLUMNS = {"id", "title", "publisher", "url", "pdf", "year", "version", "region", "kind",
                    "checked", "supersedes", "keywords"}
REGISTRY_REQUIRED = ["id", "title", "region"]
LIST_COLUMNS = {"heading", "subheading", "title", "url", "year", "pdf", "links", "note",
                "keywords", "sub", "kind", "level", "region", "only", "source"}
LIST_KINDS = {"", "box", "note", "md"}  # condition sheets; blank is a link line
LIST_LEVELS = {"", "0", "1", "2"}
# Sites whose pages are for one region alone (a regulator, an advice line, a province's
# own pathways, law or quality standards): a row linking one must carry an only mark.
ONE_REGION_HOSTS = {"bccnm.ca": "BC", "raceconnect.ca": "BC", "pathwaysbc.ca": "BC", "bclaws.gov.bc.ca": "BC",
                    "bclaws.ca": "BC", "cno.org": "ON", "ontariohealth.ca": "ON", "econsultontario.ca": "ON"}
KEY_SOURCES = "key sources"  # condition sheets: BC key sources are only=yes, copied only=other here:
FURTHER = "further resources"
TEAM_SHEET = "About/Team.csv"
TEAM_COLUMNS = {"id", "name", "credentials", "level", "areas", "setting", "affiliation", "bio",
                "links", "photo", "coi", "github", "since", "until", "consent"}
TEAM_LEVELS = {"editor", "reviewer", "contributor"}
TEAM_ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# Rules reported as warnings only. Every page passed frontmatter, sources and
# source-order on 2026-11-02 (build wave 12), so those are errors now, like list-sheet.
# review-due stays a warning: it goes stale with the calendar, not with an edit.
# page-body (a sheet-backed page with a heading or link line of its own) stays a
# warning until Tools: Checking AI Output moves into its sheet (switch wave).
# Audit rules (compliance audit, 2026-11-05 plan): warnings until every page passes each.
AUDIT_RULES = {"region-order", "intro-in-page", "section-order", "key-sources", "superseded",
               "duplicate", "pdf-alone", "year", "rxfiles", "aafp-first", "jurisdiction",
               "bc-wording", "md-links", "search", "index-list", "registry-checked"}
WARN_ONLY = {"review-due", "page-body", "source"} | AUDIT_RULES
# Page standard: section order on a condition page (Review notes and the Evidence Pack
# link are added by later steps); the sections other sheet-backed pages open and close with.
CONDITION_ORDER = ["key sources", "further resources", "algorithms and pathways",
                   "assessment tools and calculators", "prescribing", "advice and referral",
                   "patient resources", "evidence pack", "review notes"]
LAST_SECTION = {"prescribing": "np prescribing notes", "practice": "contacts"}  # else Patient Resources, when present
CONTENT_TYPES = {"approach", "assessment", "condition", "population", "prescribing", "practice", "resource"}
DATED_KINDS = {"guideline", "algorithm", "pathway"}
DATED_HEADINGS = {"key sources", "further resources", "algorithms and pathways"}
AAFP_HOST, RXFILES_HOST = "aafp.org", "rxfiles.ca"
REGION_WORDING = re.compile(r"\b(?:in|for|across) (?:BC|B\.C\.|British Columbia|Ontario)\b")
YEAR_IN_TITLE = re.compile(r"\((?:[A-Za-z .&-]+, )?(?:19|20)\d{2}\)")  # "(2021)" or "(BC GPAC, 2021)"; a month-dated version ("July 2026") may stay
DATED_TITLE = re.compile(r"\b(guidelines?|algorithm|pathway|standards?|recommendations?|consensus|statement)\b", re.I)
MD_KEEP_HEADING = re.compile(r"^(how to do it|contacts|np prescribing notes|where to check)")  # md rows the Page standard keeps
MD_KEEP_CELL = re.compile(r"^\s*(\d+\.|[-*]\s|\|)")  # a numbered step, a list line or a table
INTRO_LINE = re.compile(r"^\s*(?:\*|_)[^*_].*(?:\*|_)\s*$")  # *an italic intro line*
PAGE_TEXT = re.compile(r"^\s*(?:<div\b[^>]*>\s*</div>|<p\b[^>]*>.*?</p>|<!--.*|-{3,})?\s*$")  # lines that aren't page text (a --- rule included)
CHECKED_MAX_AGE = 365  # days a registry row's checked date may be old
SITE_SUBDIR = "nppr-website-config"  # the config checkout beside this repository
HOME = "index.md"  # the home page (docs/index.md) carries only a title, by design

FRONT = re.compile(r"^---\s*\n(.*?)\n---\s*(\n|$)", re.S)
MARKER = re.compile(r"<!--\s*nppr-list:\s*(.+?)\s*-->")
COMMENT = re.compile(r"<!--.*?-->", re.S)
BODY_LINE = re.compile(r"^(## |\s*(?:[-*]|\d+\.)\s+\[[^\]]*\]\()")
# Pages allowed a heading or link line of their own beside their sheet
BODY_TYPES = {"approach", "about", "index"}  # an Approaches page keeps its intro and More Approaches
OPTION = re.compile(r"^(counts|notes=\S+|style=\S+)$")
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
URL = re.compile(r"^https?://\S+$")
MD_URL = re.compile(r"\]\(([^)\s]+)\)")
TODAY = datetime.date.today()


class Findings:
    def __init__(self):
        self.items = []  # (level, rule, path, line, message)

    def add(self, rule, path, line, message, level=None):
        level = level or ("warning" if rule in WARN_ONLY else "error")
        self.items.append((level, rule, path, line, message))


def as_date(value):
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, datetime.date):
        return value
    if isinstance(value, str):
        try:
            return datetime.date.fromisoformat(value.strip())
        except ValueError:
            return None
    return None


def key_line(text, key, start=1):
    """Line number of the first 'key:' at or after line start (1-based), else start."""
    for n, line in enumerate(text.splitlines()[start - 1:], start):
        if re.match(rf"^\s*(- )?{re.escape(key)}:", line):
            return n
    return start


def check_page(path, rel, text, f, source_ids):
    if pathlib.PurePosixPath(rel).parts[1:] == (HOME,):
        return
    m = FRONT.match(text)
    if not m:
        f.add("frontmatter", rel, 1, "No frontmatter block (--- at the top of the page).")
        return
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        line = getattr(getattr(e, "problem_mark", None), "line", 0) + 2
        f.add("frontmatter", rel, line, f"Frontmatter is not valid YAML: {e.problem if hasattr(e, 'problem') else e}",
              level="error")
        return
    if not isinstance(meta, dict):
        f.add("frontmatter", rel, 1, "Frontmatter is not a set of fields.", level="error")
        return
    ln = lambda key: key_line(text, key)

    missing = [k for k in PAGE_REQUIRED if k not in meta]
    if missing:
        f.add("frontmatter", rel, 1, "Missing required field(s): " + ", ".join(missing) + ".")
    check_body(rel, text, m.end(), meta, f)
    ptype = meta.get("type")
    if ptype is not None and ptype not in TYPES:
        f.add("frontmatter", rel, ln("type"), f"type '{ptype}' is not one of: {', '.join(sorted(TYPES))}.")
    for key in PAGE_REQUIRED:
        if key in meta and meta[key] is None and key != "reviewers":
            f.add("frontmatter", rel, ln(key), f"{key} is empty.")
    if meta.get("status") is not None and meta["status"] not in STATUSES:
        f.add("frontmatter", rel, ln("status"), f"status '{meta['status']}' is not draft, review or published.")
    juris = meta.get("jurisdiction")
    if juris is not None and (not isinstance(juris, list) or any(j not in JURIS for j in juris)):
        hint = ' Write ON in quotes ("ON"): YAML reads a bare ON as true.' if isinstance(juris, list) and True in juris else ""
        f.add("frontmatter", rel, ln("jurisdiction"), "jurisdiction must be a list of codes from docs/regions.csv (BC, CA, INTL, ON ...)." + hint)
    regions = meta.get("regions")
    if regions is not None and (not isinstance(regions, list) or any(r not in JURIS for r in regions)):
        f.add("frontmatter", rel, ln("regions"), "regions must be a list of codes from docs/regions.csv.")
    region = meta.get("region")  # a page that is one region from top to bottom (province switch wrap-up, 2026-11-06)
    if region is not None:
        if region is True or not isinstance(region, str) or region not in JURIS:
            hint = ' Write "ON" in quotes: YAML reads a bare ON as true.' if region is True else ""
            f.add("frontmatter", rel, ln("region"), "region must be one code from docs/regions.csv: the page is for that region alone and leaves the menus, section lists and search in other regions' views." + hint)
        elif isinstance(juris, list) and juris != [region]:
            f.add("frontmatter", rel, ln("region"), f"A page with region {region} is for that region alone, so its jurisdiction should be [{region}] (it is {juris}).")
    tags = meta.get("tags")
    if tags is not None:
        if not isinstance(tags, list) or not tags:
            f.add("frontmatter", rel, ln("tags"), "tags must be a non-empty list.")
        else:
            bad = [t for t in tags if not isinstance(t, str) or not SLUG.match(t)]
            if bad:
                f.add("frontmatter", rel, ln("tags"), f"Tags must be lowercase and hyphenated: {', '.join(map(str, bad))}.")
            if ptype in TYPES and tags[0] != ptype and ptype not in NO_SOURCES:
                f.add("frontmatter", rel, ln("tags"), f"First tag should be the page type '{ptype}'.")
    if "reviewers" in meta and not isinstance(meta["reviewers"], list):
        f.add("frontmatter", rel, ln("reviewers"), "reviewers must be a list, [] while in draft.")
    if meta.get("status") == "published" and isinstance(meta.get("reviewers"), list) and not meta["reviewers"]:
        f.add("frontmatter", rel, ln("reviewers"), "Published page has no reviewers.")
    if ptype == "condition":
        folder = pathlib.PurePosixPath(rel).parts
        expected = next((SYSTEMS[p] for p in folder if p in SYSTEMS), None)
        if "system" not in meta:
            f.add("frontmatter", rel, 1, "Condition page has no system field.")
        elif meta["system"] not in SYSTEMS.values():
            f.add("frontmatter", rel, ln("system"), f"system '{meta['system']}' is not a body-system slug.")
        elif expected and meta["system"] != expected:
            f.add("frontmatter", rel, ln("system"), f"system '{meta['system']}' doesn't match its folder ('{expected}').")

    # Review dates
    reviewed, due = meta.get("last-reviewed"), meta.get("review-due")
    for key, value in (("last-reviewed", reviewed), ("review-due", due)):
        if value not in (None, "") and as_date(value) is None:
            f.add("frontmatter", rel, ln(key), f"{key} '{value}' is not a YYYY-MM-DD date.")
    reviewed, due = as_date(reviewed), as_date(due)
    if due and reviewed and due <= reviewed:
        f.add("review-due", rel, ln("review-due"), "review-due is not after last-reviewed.")
    if due and due < TODAY:
        f.add("review-due", rel, ln("review-due"), f"Review overdue: review-due {due} has passed.")
    if reviewed and reviewed > TODAY:
        f.add("review-due", rel, ln("last-reviewed"), f"last-reviewed {reviewed} is in the future.")

    # Sources live in docs/sources.csv and the page's sheet (since 2026-11-05)
    if "sources" in meta:
        f.add("sources", rel, ln("sources"),
              "Frontmatter sources are retired: a document's facts go in docs/sources.csv and its "
              "placement in the page's sheet (source column). Remove the list.")


def check_body(rel, text, start, meta, f):
    """A page with a list sheet is its frontmatter plus that sheet (Page standard,
    2026-11-05): a heading or a link line in the Markdown belongs in the sheet."""
    if not MARKER.search(text) or meta.get("type") in BODY_TYPES:
        return
    body = COMMENT.sub(lambda c: "\n" * c.group(0).count("\n"), text[start:])
    offset = text[:start].count("\n")
    for n, line in enumerate(body.split("\n"), offset + 1):
        if BODY_LINE.match(line):
            f.add("page-body", rel, n,
                  "A heading or link line in the page: move it into the page's list sheet (kind md for prose).")


def split_marker(spec):
    words = spec.split()
    while words and OPTION.match(words[-1]):
        words.pop()
    return " ".join(words)


def _host(url):
    m = re.match(r"^https?://([^/?#]+)", url or "")
    return m.group(1).lower().removeprefix("www.") if m else ""


def _one_region_host(url):
    host = _host(url)
    return next((code for site, code in ONE_REGION_HOSTS.items() if host == site or host.endswith("." + site)), "")


def check_sheet(path, rel, f, registry=None, by_address=None, condition=False):
    registry, by_address = registry or {}, by_address or {}
    keys, copies = [], []  # condition sheets: BC key sources and the only=other rows under Further Resources
    try:
        with open(path, encoding="utf-8-sig", newline="") as fh:
            reader = csv.reader(fh)
            header = next(reader, [])
            rows = list(enumerate(reader, 2))
    except (UnicodeDecodeError, csv.Error) as e:
        f.add("list-sheet", rel, 1, f"Can't read the sheet: {e}", level="error")
        return
    cols = [h.strip().lower() for h in header]
    unknown = [c for c in cols if c and c not in LIST_COLUMNS]
    if unknown:
        f.add("list-sheet", rel, 1, f"Unknown column(s): {', '.join(unknown)} (format: List sheets in NPPR-FRAMEWORK.md).")
    if "title" not in cols:
        f.add("list-sheet", rel, 1, "No title column.", level="error")
        return
    first = True
    for n, row in rows:
        cells = {c: (row[i].strip() if i < len(row) else "") for i, c in enumerate(cols)}
        if not any(cells.values()):
            continue
        if len(row) > len(cols) and any(x.strip() for x in row[len(cols):]):
            f.add("list-sheet", rel, n, "Row has more cells than the header (an unquoted comma?).")
        kind = cells.get("kind", "").lower()
        if kind not in LIST_KINDS:
            f.add("list-sheet", rel, n, f"kind '{cells['kind']}' is not blank, box, note or md.")
        if cells.get("level", "") not in LIST_LEVELS:
            f.add("list-sheet", rel, n, f"level '{cells['level']}' is not blank, 0, 1 or 2.")
        source = cells.get("source", "")
        doc = registry.get(source)
        if kind == "note":
            if not cells.get("note"):
                f.add("list-sheet", rel, n, "Note row has nothing in its note column.")
        elif not cells.get("title") and not registry.get(cells.get("source", ""), {}).get("title"):
            f.add("list-sheet", rel, n, "Row has no title.")
        for k in ("url", "pdf"):
            if cells.get(k) == "-" and not doc:
                f.add("list-sheet", rel, n, f"{k} is '-' (keep blank) but the row names no source.")
            elif cells.get(k) and cells[k] != "-" and not URL.match(cells[k]):
                f.add("list-sheet", rel, n, f"{k} is not an http(s) address: {cells[k][:60]}")
        for u in MD_URL.findall(cells.get("links", "")):
            if not URL.match(u):
                f.add("list-sheet", rel, n, f"links cell has a link that isn't http(s): {u[:60]}")
        if cells.get("year") and cells["year"] != "-" and not re.match(r"^\d{4}(\D.*)?$", cells["year"]):  # "-": no year, on purpose
            f.add("list-sheet", rel, n, f"year should start with a 4-digit year: {cells['year']}")
        is_sub = cells.get("sub", "").lower() in {"yes", "y", "1", "true", "x"}
        if is_sub and first:
            f.add("list-sheet", rel, n, "First row is marked sub, but there's no row above it.")
        first = False
        if source and not doc:
            f.add("list-sheet", rel, n, f"source '{source}' is not an id in docs/{REGISTRY_SHEET}.")
        elif doc:
            same = [k for k in ("url", "pdf", "year") if cells.get(k) and cells[k].rstrip("/") == doc.get(k, "").rstrip("/")]
            if same:
                f.add("source", rel, n, f"Row repeats the registry's {', '.join(same)} for {source}: leave the cell blank, the registry fills it.")
        else:
            address = (cells.get("pdf") or cells.get("url") or "").rstrip("/")
            hit = by_address.get(address)
            if hit and cells.get("url", "").rstrip("/") == registry[hit].get("url", "").rstrip("/"):
                f.add("source", rel, n, f"This document is in the registry as '{hit}': put the id in the source column and blank its url, pdf and year.")
        region = cells.get("region", "") or (doc or {}).get("region", "")
        if region and region not in JURIS:
            f.add("list-sheet", rel, n, f"region '{region}' is not a code from docs/regions.csv.")
        elif not region and "region" in cols and (cells.get("url") or cells.get("pdf")) \
                and cells.get("level", "") in ("", "0") and not is_sub:
            f.add("list-sheet", rel, n, "Linked top-level row has no region (BC, CA, INTL, ON ...).")
        only = cells.get("only", "").lower()
        if only and only not in {"yes", "y", "1", "true", "x", "other"}:
            f.add("list-sheet", rel, n, f"only should be yes, other or blank, not '{cells['only']}'.")
        elif only:
            if not region:
                f.add("list-sheet", rel, n, "A row marked only needs a region: it shows for that region alone (or, with other, for every region but its own).")
            elif cells.get("level", "") not in ("", "0") or is_sub:
                f.add("list-sheet", rel, n, "Mark only on the top-level row: its sub-rows hide with it.")
        top = cells.get("level", "") in ("", "0") and not is_sub
        link = next((x for x in (cells.get("url"), cells.get("pdf"), (doc or {}).get("url"), (doc or {}).get("pdf")) if x and x != "-"), "")
        code = _one_region_host(link) if top and link else ""
        if code and not only:
            f.add("list-sheet", rel, n, f"{_host(link)} is a {code}-only service: mark the row only=yes (or only=other for a copy) with region {code}.")
        if condition and top and link and kind != "note":
            ident = {source, link.rstrip("/"), (doc or {}).get("url", "").rstrip("/"), (doc or {}).get("pdf", "").rstrip("/")} - {""}
            if cells.get("heading", "").lower() == KEY_SOURCES and region == "BC":
                keys.append((n, ident, only))
            elif cells.get("heading", "").lower() == FURTHER and only == "other":
                copies.append(ident)
    for n, ident, only in keys:
        if only != "yes":
            f.add("list-sheet", rel, n, "A BC key source on a condition page is only=yes, with a one-line copy at the top of Further Resources marked only=other (Regions in NPPR-FRAMEWORK.md).")
        elif not any(ident & c for c in copies):
            f.add("list-sheet", rel, n, "This BC key source has no only=other copy under Further Resources: add one line there (same source id) so other regions' views still list it.")


# ---- Audit rules (compliance audit, 2026-11-05 plan) ------------------------------

def read_sheet(path):
    """(columns, [(line, cells)]) of a list sheet, or (None, []) when it can't be read."""
    try:
        with open(path, encoding="utf-8-sig", newline="") as fh:
            reader = csv.reader(fh)
            header = next(reader, [])
            cols = [h.strip().lower() for h in header]
            rows = []
            for n, row in enumerate(reader, 2):
                cells = {c: (row[i].strip() if i < len(row) else "") for i, c in enumerate(cols)}
                if any(cells.values()):
                    rows.append((n, cells))
            return cols, rows
    except (UnicodeDecodeError, csv.Error, OSError):
        return None, []


def _is_sub(cells):
    return cells.get("sub", "").lower() in {"yes", "y", "1", "true", "x"}


def _is_top(cells):
    return cells.get("level", "") in ("", "0") and not _is_sub(cells)


def _row_link(cells, doc):
    return next((x for x in (cells.get("url"), cells.get("pdf"), doc.get("url"), doc.get("pdf")) if x and x != "-"), "")


def _shown(only, region, view):
    """Whether a row shows when `view` is the picked region (the only column's rule)."""
    if only in ("", None):
        return True
    return region == view if only != "other" else region != view


def audit_sheet(path, rel, f, meta, registry, by_address, superseded):
    """The audit rules that read one sheet: region-order, section-order, key-sources,
    superseded, duplicate, pdf-alone, year, rxfiles, aafp-first, jurisdiction, bc-wording,
    md-links. `superseded` maps a superseded id or address to the id that replaced it."""
    cols, rows = read_sheet(path)
    if cols is None or "title" not in cols:
        return
    ptype = (meta or {}).get("type")
    condition = ptype == "condition" or (ptype == "population" and any(
        (c.get("heading") or "").lower() in ("algorithms and pathways", "advice and referral") for _, c in rows))
    headings, seen_docs, used_regions = [], {}, set()
    last_rank, last_row, section, top_only, rx_in_prescribing = None, None, None, "", False
    intl_seen = {}  # section -> line of the first international row
    key_counts = {view: 0 for view in ["BC"] + [v for v in LIVE if v != "BC"]}
    for n, cells in rows:
        heading = (cells.get("heading") or "").strip()
        hl = heading.lower()
        if heading and (not headings or headings[-1][1] != hl):
            headings.append((n, hl, heading))
        group = (hl, (cells.get("subheading") or "").strip().lower())
        if group != section:  # a subheading starts its own list on the page
            section, last_rank, last_row = group, None, None
        kind = cells.get("kind", "").lower()
        source = cells.get("source", "")
        doc = registry.get(source, {})
        link = _row_link(cells, doc)
        region = cells.get("region", "") or doc.get("region", "")
        only = cells.get("only", "").lower()
        top = _is_top(cells)
        if top:
            top_only = only
        title = cells.get("title") or doc.get("title", "")
        note = cells.get("note", "")

        # bc-wording: a row worded for one region that isn't marked only=yes
        if REGION_WORDING.search((title + " " if top else "") + note) and top_only not in {"yes", "y", "1", "true", "x"} and kind != "md":  # a sub-row's title is the document's own
            f.add("bc-wording", rel, n, "Worded for one region (\"in BC\", \"in Ontario\"): mark the row only=yes with its region, or reword it so it reads anywhere.")
        # md-links: prose rows with an external link
        if only != "other" and region:
            used_regions.add(region)
        if kind == "md":
            if MD_KEEP_HEADING.match(hl) or MD_KEEP_CELL.match(cells.get("title", "")):
                continue  # how-to steps, contacts, prescribing notes, tables and list lines stay md (Page standard)
            ext = [u for u in MD_URL.findall(cells.get("title", "")) if URL.match(u) and "nppr.ca" not in u]
            if ext:
                hit = next((by_address.get(u.rstrip("/")) for u in ext if by_address.get(u.rstrip("/"))), "")
                f.add("md-links", rel, n, ("This md row links a registry document (" + hit + "): make it a linked row with that source id."
                                           if hit else "This md row has an external link: a document belongs in a linked row with a registry id; a contact line or an NPPR page can stay md."))
            continue
        if hl == "prescribing" and "rxfiles" in note.lower():
            rx_in_prescribing = True  # a note that records what RxFiles has (or that it has nothing)
        if kind == "note" or not link:
            continue

        # superseded: an old version named or linked
        old = source if source in superseded else next((a for a in (link.rstrip("/"),) if a in superseded), "")
        if old:
            f.add("superseded", rel, n, f"'{old}' is superseded by '{superseded[old]}': point the row at the current version (its registry row keeps the old one in supersedes).")
        if not top:
            continue

        # region-order, aafp-first
        if only != "other" and region in JURIS_RANK:
            rank = JURIS_RANK[region]
            if last_rank is not None and rank < last_rank and not (rank == 0 and region != "BC"):
                f.add("region-order", rel, n, f"{region} row sits below a {last_row} row in {heading or 'this section'}: order is provinces and territories (BC first), then CA, then US, then INTL.")
            last_rank, last_row = rank, region
        if (ptype in ("condition", "population")) and only != "other" and JURIS_RANK.get(region) == 3:
            host = _host(link)
            if host == AAFP_HOST or host.endswith("." + AAFP_HOST):
                if hl in intl_seen:
                    f.add("aafp-first", rel, n, f"AAFP is the first international source on a condition page: move this row above the international row at line {intl_seen[hl]}.")
            else:
                intl_seen.setdefault(hl, n)
        # duplicate
        ident = source or next((x for x in (cells.get("pdf"), doc.get("pdf"), cells.get("url"), doc.get("url")) if x and x != "-"), link).rstrip("/")
        if only != "other":
            if ident in seen_docs:
                f.add("duplicate", rel, n, f"Same document as line {seen_docs[ident]}: link a document from one section only (its PDF, appendices and algorithm as sub-rows under it).")
            else:
                seen_docs[ident] = n
        # pdf-alone
        web = next((x for x in (cells.get("url"), doc.get("url")) if x and x != "-"), "")
        if cells.get("url") != "-" and (not web or web.lower().endswith(".pdf")):  # url "-": checked, no publisher page
            f.add("pdf-alone", rel, n, "Only a PDF is linked: link the publisher's web page for the document with its PDF on the same line, unless no page links to it.")
        # year
        year = cells.get("year") or doc.get("year", "")
        dated = ((ptype in ("condition", "population") and hl in DATED_HEADINGS)
                 or doc.get("kind") == "algorithm" or DATED_TITLE.search(title)) and ptype != "resource"
        if YEAR_IN_TITLE.search(cells.get("title", "")):
            f.add("year", rel, n, "Year typed in the title: put it in the year column (the registry's, for a row with a source), the build shows it.")
        elif dated and not year and cells.get("year") != "-":  # "-": no year, on purpose (a living index)
            f.add("year", rel, n, "No year: show the year beside every guideline, algorithm and pathway (the registry's year column, or the sheet's for a row with no source).")
        # key-sources (per live view), rxfiles
        if hl == KEY_SOURCES:
            for view in key_counts:
                if _shown(only, region, view):
                    key_counts[view] += 1
        if hl == "prescribing" and (RXFILES_HOST in _host(link)):
            rx_in_prescribing = True

    # section-order
    if ptype == "condition":
        pos = -1
        for n, hl, heading in headings:
            if hl not in CONDITION_ORDER:
                f.add("section-order", rel, n, f"'{heading}' is not a condition page section (Page standard: {', '.join(h.title() for h in CONDITION_ORDER[:7])}).")
                continue
            i = CONDITION_ORDER.index(hl)
            if i < pos:
                f.add("section-order", rel, n, f"'{heading}' is out of order: the Page standard lists the sections as {', '.join(h.title() for h in CONDITION_ORDER[:7])}.")
            pos = max(pos, i)
    elif ptype in CONTENT_TYPES and ptype != "approach" and headings:
        names = [hl for _, hl, _ in headings]
        if KEY_SOURCES in names and names[0] != KEY_SOURCES:
            f.add("section-order", rel, headings[names.index(KEY_SOURCES)][0], "Key Sources comes first on the page (Page standard).")
        last = LAST_SECTION.get(ptype, "patient resources")
        if last in names and names[-1] != last:
            f.add("section-order", rel, headings[names.index(last)][0], f"'{headings[names.index(last)][2]}' is the page's last section (Page standard).")
    # key-sources
    if any(hl == KEY_SOURCES for _, hl, _ in headings) and ptype in CONTENT_TYPES:
        for view, count in key_counts.items():
            if not 1 <= count <= 3:
                line = next(n for n, hl, _ in headings if hl == KEY_SOURCES)
                f.add("key-sources", rel, line, f"Key Sources lists {count} sources in the {view} view: it holds 1 to 3 (the rest go under Further Resources).")
    # rxfiles
    if ptype == "condition" and not rx_in_prescribing:
        line = next((n for n, hl, _ in headings if hl == "prescribing"), 1)
        f.add("rxfiles", rel, line, "No RxFiles row in Prescribing: check rxfiles.ca for a resource on this condition and link it (with a note when it needs a subscription).")
    # jurisdiction
    juris = (meta or {}).get("jurisdiction")
    if isinstance(juris, list) and used_regions and ptype in CONTENT_TYPES:
        juris = {str(j) for j in juris}
        rows_only = sorted((used_regions & set(LIVE)) - juris)
        front_only = sorted(juris - used_regions)
        if rows_only or front_only:
            parts = []
            if rows_only:
                parts.append("rows have " + ", ".join(rows_only) + " sources the frontmatter doesn't list")
            if front_only:
                parts.append("frontmatter lists " + ", ".join(front_only) + " with no row")
            f.add("jurisdiction", rel, 1, "jurisdiction doesn't match the page's rows: " + "; ".join(parts) + ".")


def audit_page(rel, text, start, meta, f, search_checks, alias_pages, address):
    """intro-in-page and search, for a sheet-backed content page."""
    ptype = (meta or {}).get("type")
    if ptype not in CONTENT_TYPES or not MARKER.search(text):
        return
    if ptype not in BODY_TYPES:
        body = COMMENT.sub(lambda c: "\n" * c.group(0).count("\n"), text[start:])
        offset = text[:start].count("\n")
        for n, line in enumerate(body.split("\n"), offset + 1):
            if MARKER.search(line) or PAGE_TEXT.match(line) or BODY_LINE.match(line):
                continue
            what = "Intro line" if INTRO_LINE.match(line) else "Page text"
            f.add("intro-in-page", rel, n, f"{what} still in the Markdown: a page is its frontmatter plus one sheet, so it goes in the sheet (the intro as the first row, kind md, no heading).")
            break
    if search_checks is None or address is None:
        return
    if isinstance((meta or {}).get("search"), dict) and meta["search"].get("exclude"):
        return
    has_aliases = bool((meta or {}).get("aliases")) or address in alias_pages
    if not has_aliases:
        f.add("search", rel, key_line(text, "title"), f"No search aliases: add `aliases:` to the frontmatter or a line for {address} in hooks/search_aliases.yml (abbreviations, drug and brand names, plain words).")
    if address not in search_checks:
        f.add("search", rel, key_line(text, "title"), f"No line in scripts/search-checks.txt leads to {address}: add its name, abbreviation and a plain other name.")


def page_address(docs, path, meta):
    """The page's short address as hooks/short_urls.py builds it (section/slug), or None for an index."""
    parts = path.relative_to(docs).parts
    if len(parts) < 2 or path.name == HOME:
        return None
    strip = lambda name: re.sub(r"^\d+\s+", "", name)
    slugify = lambda t: re.sub(r"[^a-z0-9]+", "-", t.replace("&", " and ").replace("'", "").lower()).strip("-")
    section = slugify(strip(parts[0]))
    slug = (meta or {}).get("slug")
    if slug:
        slug = slugify(str(slug))
    else:
        name = path.stem
        abbr = re.search(r"\(([A-Za-z0-9]{2,8})\)\s*$", name)
        slug = abbr.group(1).lower() if abbr else slugify(strip(name))
    return f"{section}/{slug}/"


def load_search_files(config):
    """(pages named in search-checks.txt, pages keyed in search_aliases.yml), or (None, None)."""
    if not config:
        return None, None
    checks, aliases = config / "scripts" / "search-checks.txt", config / "hooks" / "search_aliases.yml"
    if not checks.exists():
        return None, None
    pages = set()
    for line in checks.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "|" not in line:
            continue
        pages.add(line.split("|", 1)[1].strip().strip("/") + "/")
    alias_pages = set()
    if aliases.exists():
        for line in aliases.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\s*([^#\s:][^:]*):", line)
            if m:
                alias_pages.add(m.group(1).strip().strip("/") + "/")
    return pages, alias_pages


def audit_indexes(docs, f):
    """index-list: every page is in its folder's In This Section list, and every listed page exists."""
    import urllib.parse
    for index in sorted(docs.rglob(HOME)):
        folder = index.parent
        if folder == docs:
            continue
        text = index.read_text(encoding="utf-8")
        rel = index.as_posix()
        if re.search(r"^section_cards:\s*true\s*$", text, re.M):
            continue  # the build writes this section's cards from its pages (hooks/section_pages.py)
        listed = set()
        for n, line in enumerate(text.splitlines(), 1):
            for target in MD_URL.findall(line):
                if not target.endswith(".md") or URL.match(target):
                    continue
                target_path = (folder / urllib.parse.unquote(target)).resolve()
                if not target_path.exists():
                    f.add("index-list", rel, n, f"Listed page not found: {target}")
                listed.add(target_path)
        for page in sorted(folder.glob("*.md")):
            if page.name == HOME:
                continue
            if page.resolve() not in listed:
                f.add("index-list", page.as_posix(), 1, f"Not in the In This Section list of {rel}: add it there (step 2.5).")
        for sub in sorted(p for p in folder.iterdir() if p.is_dir() and (p / HOME).exists()):
            if (sub / HOME).resolve() not in listed:
                f.add("index-list", (sub / HOME).as_posix(), 1, f"This sub-section is not in the In This Section list of {rel}.")


def audit_registry(registry, rel, f):
    """registry-checked, and the map of superseded ids and addresses to their replacements."""
    superseded = {}
    for sid, cells in registry.items():
        old = cells.get("supersedes")
        if old and old in registry:
            superseded[old] = sid
            for k in ("url", "pdf"):
                if registry[old].get(k):
                    superseded[registry[old][k].rstrip("/")] = sid
        checked = as_date(cells.get("checked"))
        line = cells.get("_line", 1)
        if not cells.get("checked"):
            f.add("registry-checked", rel, line, f"{sid}: no checked date. Open the publisher's page, confirm the version and year, and record the date.")
        elif checked and (TODAY - checked).days > CHECKED_MAX_AGE:
            f.add("registry-checked", rel, line, f"{sid}: last checked {checked}, more than 12 months ago. Open the publisher's page again.")
    return superseded


def write_scorecard(out_dir, items, pages, sheet_page):
    """scorecard.csv (one row per page, a count per rule) and summary.md in out_dir."""
    out_dir = pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    rules = sorted({i[1] for i in items} | AUDIT_RULES)
    counts = {rel: {r: 0 for r in rules} for rel in pages}
    other = {}
    for level, rule, rel, line, msg in items:
        page = sheet_page.get(rel, rel)
        if page in counts:
            counts[page][rule] += 1
        else:
            other.setdefault(page, {r: 0 for r in rules})[rule] += 1
    with open(out_dir / "scorecard.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["page", "type", "status", "last-reviewed", "total"] + rules)
        for rel, meta in pages.items():
            row = counts[rel]
            w.writerow([rel, meta.get("type", ""), meta.get("status", ""), str(meta.get("last-reviewed", "")),
                        sum(row.values())] + [row[r] for r in rules])
        for rel, row in sorted(other.items()):
            w.writerow([rel, "", "", "", sum(row.values())] + [row[r] for r in rules])
    by_rule = {r: 0 for r in rules}
    pages_hit = {r: 0 for r in rules}
    for rel, row in list(counts.items()) + list(other.items()):
        for r, n in row.items():
            by_rule[r] += n
            pages_hit[r] += 1 if n else 0
    clean = sum(1 for row in counts.values() if not sum(row.values()))
    lines = [f"# Page audit scorecard, {TODAY}", "",
             f"{len(pages)} pages checked; {clean} pass every rule. Findings by rule (count, pages):", "",
             "| Rule | Findings | Pages |", "| --- | --- | --- |"]
    lines += [f"| {r} | {by_rule[r]} | {pages_hit[r]} |" for r in rules if by_rule[r]]
    lines += ["", "Pages with the most findings:", ""]
    worst = sorted(counts.items(), key=lambda kv: -sum(kv[1].values()))[:25]
    lines += [f"- {rel}: {sum(row.values())} ({', '.join(f'{r} {n}' for r, n in row.items() if n)})" for rel, row in worst if sum(row.values())]
    (out_dir / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_dir / "scorecard.csv"


def check_registry(path, rel, f):
    """docs/sources.csv: one row per document. Returns ({id: row}, {address: id})."""
    registry, by_address = {}, {}
    try:
        with open(path, encoding="utf-8-sig", newline="") as fh:
            reader = csv.reader(fh)
            header = next(reader, [])
            rows = list(enumerate(reader, 2))
    except (UnicodeDecodeError, csv.Error) as e:
        f.add("sources", rel, 1, f"Can't read the registry: {e}")
        return registry, by_address
    cols = [h.strip().lower() for h in header]
    unknown = [c for c in cols if c and c not in REGISTRY_COLUMNS]
    if unknown:
        f.add("sources", rel, 1, f"Unknown column(s): {', '.join(unknown)} (format: Sources registry in NPPR-FRAMEWORK.md).")
    missing = [c for c in REGISTRY_REQUIRED + ["url", "pdf"] if c not in cols]
    if missing:
        f.add("sources", rel, 1, f"Missing column(s): {', '.join(missing)}.")
        return registry, by_address
    for n, row in rows:
        cells = {c: (row[i].strip() if i < len(row) else "") for i, c in enumerate(cols)}
        if not any(cells.values()):
            continue
        sid = cells["id"]
        if not SLUG.match(sid):
            f.add("sources", rel, n, f"id '{sid}' should be a lowercase slug (publisher-topic-year).")
        if sid in registry:
            f.add("sources", rel, n, f"id '{sid}' is used twice.")
        miss = [k for k in REGISTRY_REQUIRED if not cells.get(k)]
        if miss:
            f.add("sources", rel, n, f"{sid or 'Row'}: missing {', '.join(miss)}.")
        if not cells.get("url") and not cells.get("pdf"):
            f.add("sources", rel, n, f"{sid}: needs a url or a pdf.")
        for k in ("url", "pdf"):
            if cells.get(k) and not URL.match(cells[k]):
                f.add("sources", rel, n, f"{sid}: {k} is not an http(s) address.")
        if cells.get("region") and cells["region"] not in JURIS:
            f.add("sources", rel, n, f"{sid}: region '{cells['region']}' is not a code from docs/regions.csv.")
        if cells.get("kind") and cells["kind"] not in KINDS:
            f.add("sources", rel, n, f"{sid}: kind '{cells['kind']}' is not one of {', '.join(sorted(KINDS))}.")
        if cells.get("checked") and as_date(cells["checked"]) is None:
            f.add("sources", rel, n, f"{sid}: checked '{cells['checked']}' is not a YYYY-MM-DD date.")
        if cells.get("year") and cells["year"] != "-" and not re.match(r"^\d{4}(\D.*)?$", cells["year"]):  # "-": no year, on purpose
            f.add("sources", rel, n, f"{sid}: year should start with a 4-digit year: {cells['year']}")
        cells["_line"] = n
        registry[sid] = cells
        address = (cells.get("pdf") or cells.get("url") or "").rstrip("/")
        if address:
            if address in by_address:
                f.add("sources", rel, n, f"{sid} has the same address as {by_address[address]}: one row per document.")
            by_address.setdefault(address, sid)
    for sid, cells in registry.items():
        if cells.get("supersedes") and cells["supersedes"] not in registry:
            f.add("sources", rel, 1, f"{sid}: supersedes '{cells['supersedes']}', which is not a registry id.")
    return registry, by_address


def check_team(path, rel, docs, f):
    """The Team sheet: its columns and rows. Returns {id: row}."""
    team = {}
    try:
        with open(path, encoding="utf-8-sig", newline="") as fh:
            reader = csv.reader(fh)
            header = next(reader, [])
            rows = list(enumerate(reader, 2))
    except (UnicodeDecodeError, csv.Error) as e:
        f.add("team", rel, 1, f"Can't read the Team sheet: {e}", level="error")
        return team
    cols = [h.strip().lower() for h in header]
    unknown = [c for c in cols if c and c not in TEAM_COLUMNS]
    if unknown:
        f.add("team", rel, 1, f"Unknown column(s): {', '.join(unknown)} (format: Team sheet in NPPR-FRAMEWORK.md).",
              level="error")
    for need in ("id", "name", "level"):
        if need not in cols:
            f.add("team", rel, 1, f"No {need} column.", level="error")
            return team
    for n, row in rows:
        cells = {c: (row[i].strip() if i < len(row) else "") for i, c in enumerate(cols)}
        if not any(cells.values()):
            continue
        rid = cells["id"]
        if not TEAM_ID.match(rid):
            f.add("team", rel, n, f"id '{rid}' should be lowercase letters, numbers and hyphens.", level="error")
        elif rid in team:
            f.add("team", rel, n, f"id '{rid}' is used twice.", level="error")
        if not cells["name"]:
            f.add("team", rel, n, "Row has no name.", level="error")
        if cells["level"].lower() not in TEAM_LEVELS:
            f.add("team", rel, n, f"level '{cells['level']}' is not Editor, Reviewer or Contributor.", level="error")
        if cells.get("photo") and not (docs / "assets" / "team" / cells["photo"]).exists():
            f.add("team", rel, n, f"Photo not found: docs/assets/team/{cells['photo']}", level="error")
        if not cells.get("consent"):
            f.add("team", rel, n, "No consent date: list someone only after their written consent.", level="error")
        elif as_date(cells["consent"]) is None:
            f.add("team", rel, n, f"consent '{cells['consent']}' is not a YYYY-MM-DD date.", level="error")
        for u in MD_URL.findall(cells.get("links", "")):
            if not URL.match(u):
                f.add("team", rel, n, f"links cell has a link that isn't http(s): {u[:60]}", level="error")
        team[rid] = cells
    return team


def check_reviewers(docs, team, f):
    """Every reviewers id is on the Team sheet; published pages have a current reviewer."""
    for path in sorted(docs.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        m = FRONT.match(text)
        try:
            meta = yaml.safe_load(m.group(1)) if m else None
        except yaml.YAMLError:
            continue
        if not isinstance(meta, dict) or not isinstance(meta.get("reviewers"), list):
            continue
        rel, ids = path.as_posix(), [str(r) for r in meta["reviewers"]]
        line = key_line(text, "reviewers")
        missing = [r for r in ids if r not in team]
        if missing:
            f.add("team", rel, line, f"reviewers names {', '.join(missing)}, not on the Team sheet ({TEAM_SHEET}).",
                  level="warning")
        known = [r for r in ids if r in team]
        if meta.get("status") == "published" and known and all(team[r].get("until") for r in known):
            f.add("team", rel, line, "Every reviewer of this published page has left the team; it needs a current reviewer.",
                  level="warning")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docs", nargs="?", default="docs")
    ap.add_argument("--report")
    ap.add_argument("--files", nargs="*")
    ap.add_argument("--audit", metavar="DIR", help="write scorecard.csv and summary.md to DIR")
    ap.add_argument("--config", help="the nppr-website-config checkout (search rule)")
    args = ap.parse_args()
    docs = pathlib.Path(args.docs)
    load_regions(docs)
    f, source_ids, used, condition_sheets = Findings(), {}, set(), set()
    registry_sheet = docs / REGISTRY_SHEET
    registry, by_address = (check_registry(registry_sheet, registry_sheet.as_posix(), f)
                            if registry_sheet.exists() else ({}, {}))
    superseded = audit_registry(registry, registry_sheet.as_posix(), f) if registry else {}
    config = pathlib.Path(args.config or os.environ.get("NPPR_CONFIG_DIR") or docs.resolve().parent.parent / SITE_SUBDIR)
    search_checks, alias_pages = load_search_files(config if config.is_dir() else None)
    if search_checks is None:
        print(f"note: search rule skipped, nppr-website-config not found at {config} (--config or NPPR_CONFIG_DIR)")
    pages, sheet_page, sheet_meta = {}, {}, {}  # page rel -> meta; sheet rel -> page rel; sheet path -> meta

    for path in sorted(docs.rglob("*.md")):
        rel = path.as_posix()
        text = path.read_text(encoding="utf-8")
        check_page(path, rel, text, f, source_ids)
        m = FRONT.match(text)
        try:
            meta = yaml.safe_load(m.group(1)) if m else None
        except yaml.YAMLError:
            meta = None
        meta = meta if isinstance(meta, dict) else {}
        pages[rel] = meta
        if m:
            audit_page(rel, text, m.end(), meta, f, search_checks, alias_pages, page_address(docs, path, meta))
        for m in MARKER.finditer(text):
            name = split_marker(m.group(1))
            sheet = path.parent / name
            line = text[:m.start()].count("\n") + 1
            if not sheet.exists():
                f.add("list-sheet", rel, line, f"List sheet not found beside the page: {name}", level="error")
            else:
                used.add(sheet.resolve())
                sheet_page[sheet.as_posix()] = rel
                sheet_meta[sheet.resolve()] = meta
                if re.search(r"^type:\s*condition\s*$", text, re.M):
                    condition_sheets.add(sheet.resolve())
    audit_indexes(docs, f)
    team_sheet = docs / TEAM_SHEET
    team = check_team(team_sheet, team_sheet.as_posix(), docs, f) if team_sheet.exists() else {}
    if team:
        check_reviewers(docs, team, f)
    regions_sheet = docs / REGIONS_SHEET
    for path in sorted(docs.rglob("*.csv")):
        rel = path.as_posix()
        if path.resolve() in (regions_sheet.resolve(), registry_sheet.resolve()):
            continue  # the region list and the sources registry, not page sheets
        if path.resolve() != team_sheet.resolve():
            check_sheet(path, rel, f, registry, by_address, condition=path.resolve() in condition_sheets)
            if path.resolve() in sheet_meta:
                audit_sheet(path, rel, f, sheet_meta[path.resolve()], registry, by_address, superseded)
        if path.resolve() not in used:
            f.add("list-sheet", rel, 1, "No page has an nppr-list marker for this sheet.")

    items = f.items
    if args.files is not None:
        wanted = {pathlib.PurePosixPath(p).as_posix() for p in args.files}
        items = [i for i in items if i[2] in wanted]
    items.sort(key=lambda i: (i[0] != "error", i[2], i[3]))

    in_actions = os.environ.get("GITHUB_ACTIONS") == "true"
    for level, rule, rel, line, msg in items:
        if in_actions:
            print(f"::{level} file={rel},line={line},title={rule}::{msg}")
        else:
            print(f"{level.upper():7} {rule:12} {rel}:{line}  {msg}")
    errors = sum(1 for i in items if i[0] == "error")
    warnings = len(items) - errors
    scope = f"{len(args.files)} changed file(s)" if args.files is not None else f"every page in {docs}/"
    summary = f"Page checks on {scope}: {errors} error(s), {warnings} warning(s)."
    print(summary)
    if args.audit:
        print("Scorecard written to", write_scorecard(args.audit, f.items, pages, sheet_page))

    if args.report:
        out = [f"### {summary}", ""]
        if items:
            by_rule = {}
            for i in items:
                by_rule[i[1]] = by_rule.get(i[1], 0) + 1
            out += ["By rule: " + ", ".join(f"{r} {n}" for r, n in sorted(by_rule.items())), "",
                    "| Level | Rule | Where | Problem |", "| --- | --- | --- | --- |"]
            for level, rule, rel, line, msg in items[:300]:
                out.append(f"| {level} | {rule} | `{rel}:{line}` | {msg.replace('|', '/')} |")
            if len(items) > 300:
                out.append(f"\n…and {len(items) - 300} more.")
        else:
            out.append("No problems found.")
        pathlib.Path(args.report).write_text("\n".join(out) + "\n", encoding="utf-8")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
