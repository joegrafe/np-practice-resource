#!/usr/bin/env python3
"""Check every page in docs/ against FRONTMATTER.md and the list-sheet format.

Usage: python3 scripts/check_pages.py [docs_dir] [--report report.md] [--files f1 f2 ...]
  --files   only report problems in these files (paths as git prints them);
            site-wide checks such as duplicate source ids still read every page.
  --report  also write the findings as a Markdown table (the PR job summary).

Checks:
  frontmatter    required page fields, allowed values, dates as YYYY-MM-DD
  review-due     review-due is after last-reviewed and has not passed
  sources        required source fields; a url or a pdf; an id names one source only
                 (the same id on several pages must point to the same address)
  source-order   sources listed BC, then CA, then INTL
  list-sheet     each <!-- nppr-list: --> marker names a CSV beside the page, the CSV
                 uses only the list-sheet columns, every row has a title and http(s)
                 links, and every CSV in docs/ is used by a page

Each finding is an error or a warning. Rules that some existing pages don't meet
yet are warnings (WARN_ONLY below); move a rule to an error once pages pass.
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
JURIS = ["BC", "CA", "INTL"]
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
SOURCE_REQUIRED = ["id", "title", "publisher", "jurisdiction", "kind", "checked"]
NO_SOURCES = {"index", "about"}
LIST_COLUMNS = {"heading", "subheading", "title", "url", "year", "pdf", "links", "note",
                "keywords", "sub"}
# Rules reported as warnings only, because some published pages don't meet them yet.
# list-sheet passes on every page today, so it's an error.
WARN_ONLY = {"frontmatter", "review-due", "sources", "source-order"}

FRONT = re.compile(r"^---\s*\n(.*?)\n---\s*(\n|$)", re.S)
MARKER = re.compile(r"<!--\s*nppr-list:\s*(.+?)\s*-->")
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
        f.add("frontmatter", rel, ln("jurisdiction"), "jurisdiction must be a list of BC, CA, INTL.")
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

    # Sources
    sources = meta.get("sources")
    if sources is None:
        if ptype not in NO_SOURCES and path.name != "index.md":
            f.add("sources", rel, 1, "No sources list (required except on index and about pages).")
        return
    if not isinstance(sources, list):
        f.add("sources", rel, ln("sources"), "sources must be a list.")
        return
    line, order, last = ln("sources"), [], -1
    for i, src in enumerate(sources):
        if not isinstance(src, dict):
            f.add("sources", rel, line, f"Source {i + 1} is not a set of fields.")
            continue
        sid = src.get("id", f"#{i + 1}")
        line = key_line(text, "id", line + 1) if "id" in src else line
        miss = [k for k in SOURCE_REQUIRED if k not in src]
        if miss:
            f.add("sources", rel, line, f"Source {sid}: missing {', '.join(miss)}.")
        if not src.get("url") and not src.get("pdf"):
            f.add("sources", rel, line, f"Source {sid}: needs a url or a pdf.")
        for k in ("url", "pdf"):
            if src.get(k) and not URL.match(str(src[k])):
                f.add("sources", rel, line, f"Source {sid}: {k} is not an http(s) address.")
        if "kind" in src and src["kind"] not in KINDS:
            f.add("sources", rel, line, f"Source {sid}: kind '{src['kind']}' is not one of {', '.join(sorted(KINDS))}.")
        if src.get("checked") is not None and as_date(src["checked"]) is None:
            f.add("sources", rel, line, f"Source {sid}: checked '{src['checked']}' is not a YYYY-MM-DD date.")
        elif "checked" in src and src["checked"] is None:
            f.add("sources", rel, line, f"Source {sid}: checked is empty.")
        if "id" in src:
            if not SLUG.match(str(src["id"])):
                f.add("sources", rel, line, f"Source id '{src['id']}' should be a lowercase slug.")
            ident = (src.get("url") or "").rstrip("/") or (src.get("pdf") or "")
            source_ids.setdefault(str(src["id"]), []).append((rel, line, ident))
        j = src.get("jurisdiction")
        if j is not None and j not in JURIS:
            f.add("sources", rel, line, f"Source {sid}: jurisdiction '{j}' is not BC, CA or INTL.")
        elif j in JURIS:
            rank = JURIS.index(j)
            if rank < last:
                f.add("source-order", rel, line,
                      f"Source {sid} ({j}) is listed after a {JURIS[last]} source; list BC, then CA, then INTL.")
            last = max(last, rank)
            order.append(j)
    if isinstance(juris, list) and order:
        extra = sorted(set(order) - set(juris), key=JURIS.index)
        if extra:
            f.add("frontmatter", rel, ln("jurisdiction"),
                  f"jurisdiction leaves out {', '.join(extra)}, which its sources cover.")


def split_marker(spec):
    words = spec.split()
    while words and OPTION.match(words[-1]):
        words.pop()
    return " ".join(words)


def check_sheet(path, rel, f):
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
        if not cells.get("title"):
            f.add("list-sheet", rel, n, "Row has no title.")
        for k in ("url", "pdf"):
            if cells.get(k) and not URL.match(cells[k]):
                f.add("list-sheet", rel, n, f"{k} is not an http(s) address: {cells[k][:60]}")
        for u in MD_URL.findall(cells.get("links", "")):
            if not URL.match(u):
                f.add("list-sheet", rel, n, f"links cell has a link that isn't http(s): {u[:60]}")
        if cells.get("year") and not re.match(r"^\d{4}(\D.*)?$", cells["year"]):
            f.add("list-sheet", rel, n, f"year should start with a 4-digit year: {cells['year']}")
        if cells.get("sub", "").lower() in {"yes", "y", "1", "true", "x"} and first:
            f.add("list-sheet", rel, n, "First row is marked sub, but there's no row above it.")
        first = False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docs", nargs="?", default="docs")
    ap.add_argument("--report")
    ap.add_argument("--files", nargs="*")
    args = ap.parse_args()
    docs = pathlib.Path(args.docs)
    f, source_ids, used = Findings(), {}, set()

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
    for sid, where in source_ids.items():
        same_page = len({p for p, _, _ in where}) < len(where)
        if same_page or len({i for _, _, i in where}) > 1:
            places = ", ".join(f"{p}:{n}" for p, n, _ in where[:3])
            if len(where) > 3:
                places += f" and {len(where) - 3} more"
            why = "twice on one page" if same_page else "for different links"
            for p, n, _ in where:
                f.add("sources", p, n, f"Source id '{sid}' is used {why}: {places}.")
    for path in sorted(docs.rglob("*.csv")):
        rel = path.as_posix()
        check_sheet(path, rel, f)
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
