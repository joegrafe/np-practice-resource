#!/usr/bin/env python3
"""Check every external link in docs/ and write a Markdown report.

Usage: python3 scripts/check_links.py [docs_dir] [report.md]

Report sections:
  Broken      - 404/410, other 4xx/5xx, DNS or connection failures
  Redirected  - the link works but lands on a different address; update it
  Check by hand - the site refused an automated request (401/403/429, cookie
                  or bot checks); the link may be fine in a browser
Uses only the Python standard library. Always exits 0; the report is the result.
"""
import concurrent.futures
import datetime
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

DOCS = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "docs")
REPORT = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "link-report.md")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36 NPPR-link-check")
TIMEOUT = 25
MAX_REDIRECTS = 10
BLOCKED_CODES = {401, 403, 405, 406, 429, 999}
# Hosts that never work for automated checks (embeds, calculators behind JS).
SKIP_HOSTS = {"open.spotify.com", "static.xx.fbcdn.net"}

TAG_RE = re.compile(r"""(?:src|href)=["'](https?://[^"']+)["']|<(https?://[^>\s]+)>""")


def markdown_targets(line):
    """URLs in [text](url) links, allowing balanced parentheses inside the URL."""
    i = 0
    while (start := line.find("](http", i)) != -1:
        j, depth = start + 2, 0
        while j < len(line):
            c = line[j]
            if c == "(":
                depth += 1
            elif c == ")":
                if depth == 0:
                    break
                depth -= 1
            elif c.isspace():
                break
            j += 1
        yield line[start + 2:j].strip("<>")
        i = j


def find_links():
    links = {}
    for path in sorted(DOCS.rglob("*.md")):
        rel = path.relative_to(DOCS).as_posix()
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            found = list(markdown_targets(line))
            found += [next(g for g in m.groups() if g) for m in TAG_RE.finditer(line)]
            for url in found:
                url = url.rstrip(".,;")
                if urllib.parse.urlsplit(url).hostname in SKIP_HOSTS:
                    continue
                links.setdefault(url, []).append(f"{rel}:{n}")
    return links


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


OPENER = urllib.request.build_opener(NoRedirect)


def fetch(url, method):
    req = urllib.request.Request(url, method=method, headers={
        "User-Agent": UA, "Accept": "text/html,application/xhtml+xml,application/pdf,*/*;q=0.8",
        "Accept-Language": "en-CA,en;q=0.9"})
    try:
        with OPENER.open(req, timeout=TIMEOUT) as r:
            return r.status, None
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Location")


def same_place(a, b):
    """Ignore http->https, a trailing slash and a dropped fragment."""
    def norm(u):
        p = urllib.parse.urlsplit(u)
        return (p.hostname or "").removeprefix("www."), p.path.rstrip("/"), p.query
    return norm(a) == norm(b)


def check(url):
    current, hops = url.split("#")[0], 0
    while True:
        try:
            code, location = fetch(current, "HEAD")
            if code in (400, 403, 404, 405, 501) or code >= 500:
                code, location = fetch(current, "GET")  # many sites reject HEAD
        except Exception as e:  # DNS, TLS, timeout, refused
            reason = getattr(e, "reason", e)
            if "Tunnel connection failed: 403" in str(reason):
                return "blocked", "blocked by this environment's network policy", None
            return "broken", f"no response ({reason})", None
        if code in (301, 302, 303, 307, 308) and location and hops < MAX_REDIRECTS:
            current, hops = urllib.parse.urljoin(current, location), hops + 1
            continue
        if code in BLOCKED_CODES:
            return "blocked", f"HTTP {code}", None
        if code >= 400:
            return "broken", f"HTTP {code}", None
        if hops and not same_place(url.split("#")[0], current):
            return "redirected", f"HTTP {code}", current
        return "ok", f"HTTP {code}", None


def main():
    links = find_links()
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        results = dict(zip(links, pool.map(check, links)))
    groups = {k: [] for k in ("broken", "redirected", "blocked", "ok")}
    for url, (status, detail, target) in results.items():
        groups[status].append((url, detail, target, links[url]))

    today = datetime.date.today().isoformat()
    out = [f"Link check run {today}: {len(links)} external links in `{DOCS}/`, "
           f"{len(groups['broken'])} broken, {len(groups['redirected'])} redirected, "
           f"{len(groups['blocked'])} to check by hand.", ""]

    def section(title, rows, note):
        out.extend([f"## {title} ({len(rows)})", "", note, ""])
        if not rows:
            out.extend(["None.", ""])
            return
        for url, detail, target, where in sorted(rows, key=lambda r: r[3][0]):
            line = f"- [ ] {url} — {detail}"
            if target:
                line += f" → {target}"
            out.append(line)
            out.append(f"  - in {', '.join(where)}")
        out.append("")

    section("Broken", groups["broken"], "These links fail. Replace or remove them.")
    section("Redirected", groups["redirected"], "These work but land on a new address. Update the link to the address after the arrow.")
    section("Check by hand", groups["blocked"], "The site refused an automated check. Open each in a browser.")
    REPORT.write_text("\n".join(out), encoding="utf-8")
    print(out[0])


if __name__ == "__main__":
    main()
