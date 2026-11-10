import collections
import csv
import json
import os
import re
from urllib.parse import urlparse

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
# enforce corrections
corr = {}
if os.path.exists("data/domain_corrections.csv"):
    for r in csv.DictReader(open("data/domain_corrections.csv")):
        corr[r["name"]] = r["verdict"]
for n in corr:
    if n in best:
        best[n]["status"] = "UNVERIFIED"


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def verified(n, v):
    d = norm(urlparse(v["site"]).netloc)
    k = norm(n)
    return bool(k[:6] and k[:6] in d) or bool(d.split(".")[0][:6] and d.split(".")[0][:6] in k)


cov = {n: v for n, v in best.items() if v["status"] in ("FOUND", "NONE", "RESOLVED")}
sub = [
    n for n in cov if census[n]["tier"] == "curated" or int(census[n]["downloads"] or 0) >= 100000
]
subv = [n for n in sub if verified(n, cov[n])]
out = {
    "census": len(census),
    "covered": len(cov),
    "covered_pct": round(len(cov) / len(census) * 100, 1),
    "substantive": len(sub),
    "substantive_verified": len(subv),
    "status": dict(collections.Counter(v["status"] for v in best.values())),
    "corrections": len(corr),
}
json.dump(out, open("data/coverage.json", "w"), indent=1)
print(json.dumps(out, indent=1))
