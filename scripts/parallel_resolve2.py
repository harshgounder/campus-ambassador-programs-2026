import csv
import json
import os
import re
import sys
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

KEY = os.environ.get("MCP_PARALLEL_SEARCH_API_KEY", "")
if not KEY:
    for line in open(os.path.expanduser("~/.hermes/.env")):
        if line.startswith("MCP_PARALLEL_SEARCH_API_KEY="):
            KEY = line.split("=", 1)[1].strip()
UA = {"User-Agent": "Mozilla/5.0 Chrome/131.0 Safari/537.36"}
SKIP = (
    "aifasthub.com",
    "hf-mirror.com",
    "foundr.ai",
    "topai.tools",
    "opentools.ai",
    "skillsmp.com",
    "exploreds.xyz",
    "savrn.com",
    "kizunaai.com",
    "hermes-ai.net",
    "gitdiscover.org",
    "facebook",
    "linkedin",
    "x.com",
    "twitter",
    "youtube",
    "crunchbase",
    "pitchbook",
    "wikipedia",
    "github.com",
    "huggingface",
    "reddit",
    "medium.com",
    "glassdoor",
    "indeed",
    "ycombinator",
    "instagram",
    "tiktok",
    "discord",
    "t.me",
    "g2.com",
    "capterra",
    "producthunt",
    "stackshare",
    "similarweb",
    "sacra.com",
    "pitchgrade",
    "cbinsights",
    "tracxn",
)
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
    "data/resolve3.jsonl",
    "data/searx.jsonl",
    "data/parallel.jsonl",
]
maps = [load(f) for f in files]


def covered(n):
    for d in maps:
        x = d.get(n)
        if x and x["status"] in ("NONE", "FOUND", "RESOLVED"):
            return True
    return False


targets = [r for r in census if not covered(r["name"])]
targets.sort(key=lambda r: -int(r["downloads"] or 0))
DONE = "data/parallel2b_done.txt"
OUT = "data/parallel2b.jsonl"
done = set(open(DONE).read().split("\n")) if os.path.exists(DONE) else set()
targets = [r for r in targets if r["name"] not in done]
PATHS = ["/ambassador", "/ambassadors", "/campus", "/students"]


def search(n):
    body = {
        "objective": f"find the official website of {n}, an AI company or project",
        "search_queries": [f"{n} official website", f"{n} AI"],
        "max_results": 5,
    }
    for a in range(3):
        try:
            r = requests.post(
                "https://api.parallel.ai/v1beta/search",
                headers={"x-api-key": KEY, "Content-Type": "application/json"},
                json=body,
                timeout=30,
            )
            if r.status_code == 200:
                for x in r.json().get("results", []):
                    net = urllib.parse.urlparse(x.get("url", "")).netloc.lower().replace("www.", "")
                    if not net or any(s in net for s in SKIP):
                        continue
                    return "https://" + net
                return ""
            if r.status_code == 429:
                time.sleep(15)
                continue
            if r.status_code in (500, 502, 503):
                time.sleep(5)
                continue
            return ""
        except Exception:
            time.sleep(2)
    return ""


def check(r):
    n = r["name"]
    site = search(n)
    if not site:
        return n, "", "UNRESOLVED", []
    try:
        x = requests.get(site, headers=UA, timeout=8)
        txt = re.sub(r"<[^>]+>", " ", x.text).lower()
        key = re.sub(r"[^a-z0-9]", "", n.lower())[:5]
        if key and key not in re.sub(r"[^a-z0-9]", "", txt):
            return n, site, "UNVERIFIED", []
        hits = []
        for p in PATHS:
            try:
                y = requests.get(site.rstrip("/") + p, headers=UA, timeout=6)
                if y.status_code == 200:
                    b = re.sub(r"<[^>]+>", " ", y.text).lower()
                    if b.count("ambassador") >= 2 and re.search(r"apply|join|program", b):
                        t = re.search(r"<title[^>]*>(.*?)</title>", y.text, re.S | re.I)
                        hits.append({"url": y.url, "title": t.group(1).strip()[:100] if t else ""})
            except Exception:
                pass
        return n, site, "FOUND" if hits else "RESOLVED", hits
    except Exception:
        return n, site, "UNREACHABLE", []


print("targets", len(targets), "key", bool(KEY))
sys.stdout.flush()
out = open(OUT, "a")
log = open(DONE, "a")
c = 0
with ThreadPoolExecutor(max_workers=3) as ex:
    for f in as_completed([ex.submit(check, r) for r in targets]):
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
