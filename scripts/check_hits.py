import json
import re
from concurrent.futures import ThreadPoolExecutor

import requests

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36"}
d = json.load(open("data/probe/probe.json"))
urls = {}
for r in d:
    for u in r["hits"]:
        if re.search(r"ambassador|campus|student", u, re.I):
            urls.setdefault(u, r["name"])
print("unique urls", len(urls))


def chk(u):
    try:
        r = requests.get(u, headers=UA, timeout=10, allow_redirects=True)
        t = re.search(r"<title[^>]*>(.*?)</title>", r.text, re.S | re.I)
        return (u, r.status_code, r.url, (t.group(1).strip()[:90] if t else ""))
    except Exception as e:
        return (u, "ERR", u, str(e)[:60])


with ThreadPoolExecutor(max_workers=24) as ex:
    out = list(ex.map(chk, list(urls)))
ok = [o for o in out if o[1] == 200]
json.dump(out, open("data/probe/hits.json", "w"), indent=1)
print("200s", len(ok))
for o in sorted(ok, key=lambda x: x[0])[:120]:
    print(o[1], o[0][:95], "|", o[3][:70])
