import collections
import csv
import json
import os
import random
import re
import sys
from concurrent.futures import ThreadPoolExecutor

import requests

UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
}
random.seed(42)
census = [
    r for r in csv.DictReader(open("data/ai-orgs-census.csv")) if r["tier"] in ("curated", "org")
]
names = {r["name"] for r in census}
rows = (
    [json.loads(line) for line in open("data/scan3758.jsonl")]
    if os.path.exists("data/scan3758.jsonl")
    else []
)
scanned = {r["name"] for r in rows}
res = []
fails = []


def chk(name, ok, detail=""):
    (res if ok else fails).append((name, detail))
    print(("PASS " if ok else "FAIL ") + name + " | " + detail)


chk(
    "coverage: every org-tier name has a scan row",
    names <= scanned,
    f"{len(names - scanned)} missing of {len(names)}",
)
chk("no duplicate scan rows", len(rows) == len(scanned), f"{len(rows)} rows, {len(scanned)} unique")
chk("every row has a status", all(r.get("status") for r in rows), "")
chk("every FOUND row has a hit URL", all(r["hits"] for r in rows if r["status"] == "FOUND"), "")
chk("every NONE row was reachable", all(r["reachable"] for r in rows if r["status"] == "NONE"), "")
chk(
    "no false-positive titles in FOUND",
    all(
        not re.search(r"apache|page not found|not found", h["title"], re.I)
        for r in rows
        if r["status"] == "FOUND"
        for h in r["hits"]
    ),
    "",
)


# live re-check of every FOUND row
def ok_found(r):
    for h in r["hits"]:
        try:
            x = requests.get(h["url"], headers=UA, timeout=10)
            if x.status_code == 200:
                return True
        except Exception:
            pass
    return False


found = [r for r in rows if r["status"] == "FOUND"]
if found:
    with ThreadPoolExecutor(max_workers=12) as ex:
        live = list(ex.map(ok_found, found))
    chk("every FOUND link still returns 200", all(live), f"{sum(1 for x in live if not x)} dead")
else:
    chk("every FOUND link still returns 200", True, "no FOUND rows yet")
# independent negative sample: 40 NONE rows re-probed
none = [r for r in rows if r["status"] == "NONE"]
sample = random.sample(none, min(40, len(none)))


def recheck(r):
    for p in ["/ambassador", "/ambassadors", "/campus"]:
        try:
            x = requests.get(r["site"].rstrip("/") + p, headers=UA, timeout=8)
            if x.status_code == 200:
                t = re.search(r"<title[^>]*>(.*?)</title>", x.text, re.S | re.I)
                if t and re.search(r"ambassador|campus|student", t.group(1), re.I):
                    return False
        except Exception:
            pass
    return True


if sample:
    with ThreadPoolExecutor(max_workers=10) as ex:
        agree = list(ex.map(recheck, sample))
    chk(
        "independent re-probe agrees on NONE sample",
        sum(agree) >= 0.9 * len(agree),
        f"{sum(agree)}/{len(agree)} agree",
    )
else:
    chk("independent re-probe agrees on NONE sample", True, "no NONE rows")
# category coverage
c = collections.Counter(r.get("status", "?") for r in rows)
print("\nSTATUS COUNTS:", dict(c))
print(
    "CATEGORY COVERAGE:",
    dict(
        collections.Counter(
            next((x["category"] for x in census if x["name"] == r["name"]), "?") for r in rows
        )
    ),
)
print(f"\n{len(res)} passed, {len(fails)} failed")
sys.exit(1 if fails else 0)
