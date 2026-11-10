import csv
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

import requests

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0 Safari/537.36"}
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
    "data/retry.jsonl",
]
maps = [load(f) for f in files]
best = {}
rank = {
    "FOUND": 0,
    "NONE": 1,
    "RESOLVED": 2,
    "UNVERIFIED": 3,
    "UNREACHABLE": 4,
    "UNRESOLVED": 5,
    "NO_SITE": 6,
}
for d in maps:
    for n, r in d.items():
        if n not in {c["name"] for c in census}:
            continue
        if n not in best or rank.get(r["status"], 9) < rank.get(best[n]["status"], 9):
            best[n] = r
targets = [r for r in best.values() if r["status"] == "UNVERIFIED" and r.get("site")]
PATHS = ["/ambassador", "/ambassadors", "/campus", "/students"]


def check(r):
    n = r["name"]
    s = r["site"]
    dom = urlparse(s).netloc.replace("www.", "").lower()
    key = re.sub(r"[^a-z0-9]", "", n.lower())
    if not (
        key[:6] in re.sub(r"[^a-z0-9]", "", dom)
        or re.sub(r"[^a-z0-9]", "", dom).split(".")[0][:6] in key
    ):
        return n, s, "UNVERIFIED", []
    hits = []
    for p in PATHS:
        try:
            y = requests.get(s.rstrip("/") + p, headers=UA, timeout=7)
            if y.status_code == 200:
                b = re.sub(r"<[^>]+>", " ", y.text).lower()
                if b.count("ambassador") >= 2 and re.search(r"apply|join|program", b):
                    t = re.search(r"<title[^>]*>(.*?)</title>", y.text, re.S | re.I)
                    hits.append({"url": y.url, "title": t.group(1).strip()[:100] if t else ""})
        except Exception:
            pass
    return n, s, "FOUND" if hits else "RESOLVED", hits


print("targets", len(targets))
sys.stdout.flush()
out = open("data/unverified_fix.jsonl", "w")
c = 0
with ThreadPoolExecutor(max_workers=14) as ex:
    for f in as_completed([ex.submit(check, r) for r in targets]):
        c += 1
        try:
            n, s, st, h = f.result()
        except Exception:
            continue
        out.write(json.dumps({"name": n, "site": s, "status": st, "hits": h}) + "\n")
        out.flush()
        if c % 200 == 0:
            print("done", c)
            sys.stdout.flush()
out.close()
print("FINISHED", c)
