import collections
import csv
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0 Safari/537.36"}
rows = [r for r in csv.DictReader(open("data/registry.csv")) if r["status"] == "OPEN"]
CLOSED = re.compile(
    r"applications?\s+(are\s+)?(now\s+)?closed|no longer accepting|application closed|closed for (this|the) (cycle|cohort|season)|not accepting (new )?applications|submissions? (are )?closed|intake closed",
    re.I,
)
DEAD = re.compile(r"page not found|404 not found|this page could not be found", re.I)
DATE = re.compile(
    r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+\d{1,2},?\s*20\d\d|\d{1,2}\s+(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+20\d\d",
    re.I,
)


def chk(r):
    u = r["apply_url"]
    try:
        x = requests.get(u, headers=UA, timeout=15, allow_redirects=True)
        txt = re.sub(r"<script.*?</script>|<style.*?</style>", "", x.text, flags=re.S | re.I)
        txt = re.sub(r"<[^>]+>", " ", txt)
        txt = re.sub(r"\s+", " ", txt)
        closed = CLOSED.search(txt)
        dead = DEAD.search(txt) or x.status_code in (404, 410)
        dates = list(dict.fromkeys(DATE.findall(txt)))[:3]
        return {
            "name": r["name"],
            "url": u,
            "http": x.status_code,
            "final": x.url,
            "flag": "CLOSED" if closed else ("DEAD" if dead else "OK"),
            "closed_text": (closed.group(0)[:80] if closed else ""),
            "dates": dates,
            "title": (
                re.search(r"<title[^>]*>(.*?)</title>", x.text, re.S | re.I).group(1).strip()[:80]
                if re.search(r"<title[^>]*>(.*?)</title>", x.text, re.S | re.I)
                else ""
            ),
        }
    except Exception as e:
        return {
            "name": r["name"],
            "url": u,
            "http": "ERR",
            "final": "",
            "flag": "UNREACHABLE",
            "closed_text": str(e)[:60],
            "dates": [],
            "title": "",
        }


out = []
with ThreadPoolExecutor(max_workers=12) as ex:
    for f in as_completed([ex.submit(chk, r) for r in rows]):
        out.append(f.result())
json.dump(out, open("data/recheck_open.json", "w"), indent=1)
print("checked", len(out), collections.Counter(x["flag"] for x in out))
for x in out:
    if x["flag"] != "OK":
        print(x["flag"], x["name"][:40], "|", x["closed_text"][:60], "|", x["url"][:60])
print("\n-- dates found --")
for x in out:
    if x["dates"]:
        print(x["name"][:38], "|", x["dates"], "|", x["url"][:55])
