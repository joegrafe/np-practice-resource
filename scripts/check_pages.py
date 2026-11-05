#!/usr/bin/env python3
"""Check every page in docs/ against FRONTMATTER.md and the list-sheet format.

Usage: python3 scripts/check_pages.py [docs_dir] [--report report.md] [--files f1 f2 ...]
  --files   only report problems in these files (paths as git prints them);
            site-wide checks such as duplicate source ids still read every page.
  --report  also write the findings as a Markdown table (the PR job summary).

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
                 an only mark sits on a top-level row that has a region,
                 and every CSV in docs/ is used by a page
  page-body      a page with a list sheet holds no heading or link line of its own
                 (Approaches, About and index pages excepted): the page is its
                 frontmatter plus its sheet (a warning)
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


def load_regions(docs):
    """Region codes from docs/regions.csv, in source-order rank."""
    global JURIS, JURIS_RANK
    path = docs / REGIONS_SHEET
    if not path.exists():
        JURIS_RANK = {j: i for i, j in enumerate(JURIS)}
        return
    codes, rank = [], {}
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            code = (row.get("code") or "").strip()
            if not code:
                continue
            kind, country = (row.get("kind") or "").strip(), (row.get("country") or "").strip()
            codes.append(code)
            rank[code] = (0 if kind in ("province", "territory", "state") and country == "CA"
                          else 1 if code == "CA" else 2 if country == "US" else 3 if code == "INTL" else 2)
    JURIS, JURIS_RANK = codes, rank
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
WARN_ONLY = {"review-due", "page-body", "source"}
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


def check_sheet(path, rel, f, registry=None, by_address=None):
    registry, by_address = registry or {}, by_address or {}
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
        if cells.get("year") and not re.match(r"^\d{4}(\D.*)?$", cells["year"]):
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
        if cells.get("year") and not re.match(r"^\d{4}(\D.*)?$", cells["year"]):
            f.add("sources", rel, n, f"{sid}: year should start with a 4-digit year: {cells['year']}")
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
    args = ap.parse_args()
    docs = pathlib.Path(args.docs)
    load_regions(docs)
    f, source_ids, used = Findings(), {}, set()
    registry_sheet = docs / REGISTRY_SHEET
    registry, by_address = (check_registry(registry_sheet, registry_sheet.as_posix(), f)
                            if registry_sheet.exists() else ({}, {}))

    for path in sorted(docs.rglob("*.md")):
        rel = path.as_posix()
        text = path.read_text(encoding="utf-8")
        check_page(path, rel, text, f, source_ids)
        for m in MARKER.finditer(text):
            name = split_marker(m.group(1))
            sheet = path.parent / name
            line = text[:m.start()].count("\n") + 1
            if not sheet.exists():
                f.add("list-sheet", rel, line, f"List sheet not found beside the page: {name}", level="error")
            else:
                used.add(sheet.resolve())
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
            check_sheet(path, rel, f, registry, by_address)
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
