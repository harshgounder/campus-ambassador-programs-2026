import collections
import csv
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

import requests

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0 Safari/537.36"}
census = {
    r["name"]: r
    for r in csv.DictReader(open("data/ai-orgs-census.csv"))
    if r["tier"] in ("curated", "org")
}
files = [
    "data/scan3758.jsonl",
    "data/resolve.jsonl",
    "data/resolve2.jsonl",
    "data/searx.jsonl",
    "data/parallel.jsonl",
    "data/retry.jsonl",
    "data/unverified_fix.jsonl",
]
rank = {
    "FOUND": 0,
    "NONE": 1,
    "RESOLVED": 2,
    "UNVERIFIED": 3,
    "UNREACHABLE": 4,
    "UNRESOLVED": 5,
    "NO_SITE": 6,
}
best = {}
for f in files:
    if not os.path.exists(f):
        continue
    for line in open(f):
        r = json.loads(line)
        n = r["name"]
        if n not in census:
            continue
        if n not in best or rank.get(r["status"], 9) < rank.get(best[n]["status"], 9):
            best[n] = {"status": r["status"], "site": r.get("site", "")}
cov = {n: v for n, v in best.items() if v["status"] in ("FOUND", "NONE", "RESOLVED")}


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def strong(n, site):
    d = norm(urlparse(site).netloc)
    k = norm(n)
    return bool(k[:6] and k[:6] in d) or bool(d.split(".")[0][:6] and d.split(".")[0][:6] in k)


mism = [(n, v) for n, v in cov.items() if not strong(n, v["site"])]
print("covered", len(cov), "strong match", len(cov) - len(mism), "mismatch", len(mism))
sys.stdout.flush()


def check(item):
    n, v = item
    site = v["site"]
    try:
        x = requests.get(site, headers=UA, timeout=10)
        txt = re.sub(r"<[^>]+>", " ", x.text).lower()
        toks = [t for t in re.split(r"[^a-z0-9]+", n.lower()) if len(t) >= 4]
        hits = [t for t in toks if t in txt]
        if not toks:
            hits = ["(short name)"]
        return n, site, v["status"], ("ALIAS" if hits else "WRONG"), ";".join(hits[:4])
    except Exception:
        return n, site, v["status"], "UNKNOWN", ""


out = []
with ThreadPoolExecutor(max_workers=14) as ex:
    for f in as_completed([ex.submit(check, m) for m in mism]):
        out.append(f.result())
print(collections.Counter(x[3] for x in out))
with open("data/domain-audit.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "site", "status", "verdict", "tokens_found"])
    for r in sorted(out, key=lambda x: x[3]):
        w.writerow(r)
print("WRONG sample:")
for r in [x for x in out if x[3] == "WRONG"][:40]:
    print(" ", r[0], "->", r[1])
