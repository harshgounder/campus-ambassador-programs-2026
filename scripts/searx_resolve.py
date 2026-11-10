import csv
import json
import os
import re
import sys
import time
import urllib.parse

import requests

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/131.0 Safari/537.36"}
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
)
census = [
    r for r in csv.DictReader(open("data/ai-orgs-census.csv")) if r["tier"] in ("curated", "org")
]


def load(f):
    if not os.path.exists(f):
        return {}
    return {json.loads(line)["name"]: json.loads(line) for line in open(f)}


scan = load("data/scan3758.jsonl")
r1 = load("data/resolve.jsonl")
r2 = load("data/resolve2.jsonl")
r3 = load("data/resolve3.jsonl")


def covered(n):
    for d in (scan, r1, r2, r3):
        x = d.get(n)
        if x and x["status"] in ("NONE", "FOUND", "RESOLVED"):
            return True
    return False


targets = [r for r in census if not covered(r["name"])]
targets.sort(key=lambda r: -int(r["downloads"] or 0))
DONE = "data/searx_done.txt"
OUT = "data/searx.jsonl"
done = set(open(DONE).read().split("\n")) if os.path.exists(DONE) else set()
targets = [r for r in targets if r["name"] not in done]
PATHS = ["/ambassador", "/ambassadors", "/campus", "/students"]


def search(q):
    try:
        u = "http://127.0.0.1:8888/search?format=json&q=" + urllib.parse.quote(q)
        r = requests.get(u, headers=UA, timeout=20)
        d = r.json()
        for x in d.get("results", []):
            net = urllib.parse.urlparse(x.get("url", "")).netloc.lower().replace("www.", "")
            if not net or any(s in net for s in SKIP):
                continue
            return "https://" + net
    except Exception:
        pass
    return ""


def check(r):
    n = r["name"]
    site = search(n + " AI official website")
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


print("targets", len(targets))
sys.stdout.flush()
out = open(OUT, "a")
log = open(DONE, "a")
c = 0
for r in targets:
    c += 1
    try:
        n, s, st, h = check(r)
    except Exception:
        continue
    out.write(json.dumps({"name": n, "site": s, "status": st, "hits": h}) + "\n")
    out.flush()
    log.write(n + "\n")
    log.flush()
    if c % 50 == 0:
        print("done", c, "last", st)
        sys.stdout.flush()
    time.sleep(0.2)
print("FINISHED", c)
