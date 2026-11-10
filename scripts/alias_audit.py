import collections
import csv
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0 Safari/537.36"}
rows = [r for r in csv.DictReader(open("data/domain-audit.csv")) if r["verdict"] == "ALIAS"]
AGG = re.compile(
    r"directory|mirror|top ai|topai|aggregator|list of|alternatives|similar tools|open tools|models list|hub",
    re.I,
)


def check(r):
    n = r["name"]
    s = r["site"]
    try:
        x = requests.get(s, headers=UA, timeout=10)
        if x.status_code != 200:
            return n, s, "UNREACHABLE", ""
        txt = re.sub(r"<[^>]+>", " ", x.text).lower()
        title = re.search(r"<title[^>]*>(.*?)</title>", x.text, re.S | re.I)
        title = title.group(1).strip() if title else ""
        toks = [t for t in re.split(r"[^a-z0-9]+", n.lower()) if len(t) >= 4]
        hits = [t for t in toks if t in txt]
        if not hits:
            return n, s, "FAIL_NO_NAME", title[:80]
        if AGG.search(title):
            return n, s, "SUSPECT_AGGREGATOR", title[:80]
        return n, s, "OK", title[:80]
    except Exception:
        return n, s, "UNREACHABLE", ""


out = []
with ThreadPoolExecutor(max_workers=14) as ex:
    for f in as_completed([ex.submit(check, r) for r in rows]):
        out.append(f.result())
print(collections.Counter(x[2] for x in out))
with open("data/alias-audit.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "site", "verdict", "title"])
    for r in sorted(out, key=lambda x: x[2]):
        w.writerow(r)
for r in out:
    if r[2] in ("FAIL_NO_NAME", "SUSPECT_AGGREGATOR"):
        print(r[2], r[0], "->", r[1], "|", r[3])
