"""Build the allowed-domain lists for the NPPR cloud environments.

The cloud environment's Allowed domains setting holds about 400 entries, and
a domain whose pages sit on subdomains needs two (`domain` and `*.domain`),
so one list cannot hold every site NPPR links. This script reads every link
on the site (docs/sources.csv, every list sheet, every Markdown page) and
UNOPENED-SOURCES.csv, and writes two lists under environments/:

  environment-1.txt  BC, Alberta and national Canadian sources, calculators
                     and patient resources: the list for BC and Canadian
                     condition, assessment, prescribing and practice waves.
  environment-2.txt  Ontario, international and pediatric sources, the
                     unopened-sources candidates, the research sites of the
                     2026-10-29 list that no page links yet, plus the core
                     shared with environment 1: the list for new condition
                     pages (BC + Ontario + AAFP sweep), Ontario waves,
                     international sweeps and pediatric pages.

Journal and reference sites (PubMed, BMJ, NEJM, JAMA, CMA ...) go on both.

  environment-core.txt  The default: every linked domain in order of how
                     many links the site has to it, whatever its region,
                     filled to the 400-entry cap (journal sites first,
                     unopened-source candidates after the linked sites).
                     Switch to 1 or 2 only for a wave that needs a site
                     the core lacks (domains.csv shows which).

environments/domains.csv lists every domain with its link count, regions,
hosts and environment(s), so a wave can check which list it needs.

Usage, from the vault root:  python3 scripts/environment_lists.py
"""
import csv
import glob
import re
from collections import Counter, defaultdict
from urllib.parse import urlsplit

LIMIT = 400
SHARED_TOP = 40  # most-linked environment-1 domains that environment 2 carries too
PREVIOUS = "environments/previous-list-2026-11-05.txt"  # Joe's saved 400-entry list
JOURNALS = {"ncbi.nlm.nih.gov", "bmj.com", "nejm.org", "jamanetwork.com", "sciencedirect.com", "springer.com", "cambridge.org", "lww.com", "cma.ca", "radiopaedia.org", "mcc.ca", "cochranelibrary.com", "thelancet.com", "wiley.com", "oup.com", "uptodate.com", "nice.org.uk", "cdc.gov", "who.int"}
INTL = {"INTL", "US"}
SKIP = {"nppr.ca", "claude.ai", "github.com", "githubusercontent.com", "example.com", "localhost"}
THREE_LABEL = {"bc.ca", "on.ca", "ab.ca", "gov.bc.ca", "gc.ca", "qc.ca", "nih.gov", "ac.uk", "org.uk", "co.uk", "org.au", "gov.au", "edu.au", "com.au", "nhs.uk", "gov.on.ca"}


def host(u):
    try:
        h = urlsplit((u or "").strip()).hostname or ""
    except ValueError:
        return ""
    return h.lower()


def base(h):
    parts = h.split(".")
    if ".".join(parts[-2:]) in THREE_LABEL and len(parts) >= 3:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])


def main():
    links = Counter()
    regions = defaultdict(Counter)
    hosts = defaultdict(set)

    def add(u, region, weight=1):
        h = host(u)
        if not h:
            return
        b = base(h)
        if b in SKIP:
            return
        links[b] += weight
        regions[b][region or "?"] += weight
        hosts[b].add(h)

    with open("docs/sources.csv", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            add(r["url"], r["region"])
            add(r["pdf"], r["region"])
    for p in glob.glob("docs/**/*.csv", recursive=True):
        if p.endswith("sources.csv") or p.endswith("regions.csv"):
            continue
        with open(p, encoding="utf-8-sig", newline="") as fh:
            rd = csv.DictReader(fh)
            if not rd.fieldnames or "url" not in rd.fieldnames:
                continue
            for r in rd:
                add(r.get("url"), r.get("region"))
                add(r.get("pdf"), r.get("region"))
                for u in re.findall(r"https?://[^\s)\]>\"']+", r.get("links") or ""):
                    add(u, r.get("region"))
    for p in glob.glob("docs/**/*.md", recursive=True):
        for u in re.findall(r"https?://[^\s)\]>\"']+", open(p, encoding="utf-8").read()):
            add(u, "md")
    unopened = set()
    with open("UNOPENED-SOURCES.csv", encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            if r["status"].strip().lower() == "done":
                continue
            b = base(host(r["url"]))
            if b:
                unopened.add(b)
                add(r["url"], "unopened", 0)

    previous = []
    with open(PREVIOUS, encoding="utf-8") as fh:
        for line in fh:
            d = line.strip().lstrip("*.")
            if d and d not in links and d not in SKIP and d not in previous:
                previous.append(d)
                regions[d]["previous"] += 1
                if d.count(".") >= 2 and base(d) != d:
                    hosts[base(d)].add(d)
    for d in JOURNALS:
        links.setdefault(d, 0)
        hosts[d].add("www." + d)
        if d in previous:
            previous.remove(d)

    def entries(d):
        wild = any(h != d and h != "www." + d for h in hosts[d])
        return [d] + (["*." + d] if wild else [])

    def ontario_or_intl(d):
        reg = regions[d]
        prov = sum(v for k, v in reg.items() if k in INTL or k == "ON")
        return prov and prov >= sum(v for k, v in reg.items() if k not in ("?", "md", "unopened")) / 2

    ranked = sorted(links, key=lambda d: (-links[d], d))
    env1, env2 = [], []
    for d in ranked:
        if d in JOURNALS:
            env1.append(d)
            env2.append(d)
        elif d in unopened or ontario_or_intl(d):
            env2.append(d)
        else:
            env1.append(d)
    # environment 2 also carries the shared core, then the old list's research sites
    core = [d for d in env1[:SHARED_TOP]]
    env2 = core + [d for d in env2 if d not in core] + previous
    ranked += previous

    def fit(ds, name):
        out, n = [], 0
        for d in ds:
            e = entries(d)
            if n + len(e) > LIMIT:
                print(f"{name}: dropped {d} ({links[d]} links), list full at {n}")
                continue
            out.extend(e)
            n += len(e)
        return out, n

    l1, n1 = fit(env1, "environment-1")
    l2, n2 = fit(env2, "environment-2")
    core_order = sorted(JOURNALS) + [d for d in ranked if d not in JOURNALS and d not in unopened and d not in previous] + [d for d in ranked if d in unopened] + previous
    lc, nc = fit(core_order, "environment-core")
    for name, lst in (("environment-1", l1), ("environment-2", l2), ("environment-core", lc)):
        with open(f"environments/{name}.txt", "w", encoding="utf-8") as fh:
            fh.write("\n".join(sorted(lst, key=lambda s: s.lstrip("*."))) + "\n")
    with open("environments/domains.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["domain", "environment", "links", "regions", "unopened", "hosts"])
        for d in ranked:
            env = ("core " if d in lc else "") + ("1 " if d in l1 else "") + ("2" if d in l2 else "")
            w.writerow([d, env.strip() or "-", links.get(d, 0), " ".join(f"{k}:{v}" for k, v in regions[d].most_common() if k != "unopened"), "yes" if d in unopened else "", " ".join(sorted(hosts[d]))])
    both = len(set(env1) & set(env2))
    print(f"environment-core {len(lc) and sum(1 for d in core_order if d in lc)} domains, {nc} entries")
    print(f"domains {len(ranked)}; environment-1 {len(env1)} domains, {n1} entries; environment-2 {len(env2)} domains, {n2} entries; on both {both}")


if __name__ == "__main__":
    main()
