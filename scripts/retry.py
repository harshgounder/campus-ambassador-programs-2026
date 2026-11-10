import csv
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Upgrade-Insecure-Requests": "1",
}
census = [
    r for r in csv.DictReader(open("data/ai-orgs-census.csv")) if r["tier"] in ("curated", "org")
]


def load(f):
    if not os.path.exists(f):
        return {}
    return {json.loads(line)["name"]: json.loads(line) for line in open(f)}


files = [
    "data/scan3758.jsonl",
    "data/resolve.jsonl",
    "data/resolve2.jsonl",
    "data/searx.jsonl",
    "data/parallel.jsonl",
]
maps = [load(f) for f in files]
sites = {}
for d in maps:
    for n, r in d.items():
        if r.get("site"):
            sites.setdefault(n, r["site"])
names = [n for n in sites if n in {c["name"] for c in census}]
DONE = "data/retry_done.txt"
OUT = "data/retry.jsonl"
done = set(open(DONE).read().split("\n")) if os.path.exists(DONE) else set()
names = [n for n in names if n not in done]
PATHS = ["/ambassador", "/ambassadors", "/campus", "/students"]


def check(n):
    s = sites[n]
    try:
        x = requests.get(s, headers=UA, timeout=15, allow_redirects=True)
        if x.status_code != 200:
            return n, s, "UNREACHABLE", []
        txt = re.sub(r"<[^>]+>", " ", x.text).lower()
        key = re.sub(r"[^a-z0-9]", "", n.lower())[:5]
        if key and key not in re.sub(r"[^a-z0-9]", "", txt):
            return n, s, "UNVERIFIED", []
        hits = []
        for p in PATHS:
            try:
                y = requests.get(s.rstrip("/") + p, headers=UA, timeout=8)
                if y.status_code == 200:
                    b = re.sub(r"<[^>]+>", " ", y.text).lower()
                    if b.count("ambassador") >= 2 and re.search(r"apply|join|program", b):
                        t = re.search(r"<title[^>]*>(.*?)</title>", y.text, re.S | re.I)
                        hits.append({"url": y.url, "title": t.group(1).strip()[:100] if t else ""})
            except Exception:
                pass
        return n, s, "FOUND" if hits else "RESOLVED", hits
    except Exception:
        return n, s, "UNREACHABLE", []


print("targets", len(names))
sys.stdout.flush()
out = open(OUT, "a")
log = open(DONE, "a")
c = 0
with ThreadPoolExecutor(max_workers=12) as ex:
    for f in as_completed([ex.submit(check, n) for n in names]):
        c += 1
        try:
            n, s, st, h = f.result()
        except Exception:
            continue
        out.write(json.dumps({"name": n, "site": s, "status": st, "hits": h}) + "\n")
        out.flush()
        log.write(n + "\n")
        log.flush()
        if c % 100 == 0:
            print("done", c, "last", st)
            sys.stdout.flush()
print("FINISHED", c)
