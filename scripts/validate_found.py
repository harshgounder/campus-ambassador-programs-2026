import json,re,requests,sys
from concurrent.futures import ThreadPoolExecutor
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) Chrome/131.0 Safari/537.36"}
rows=[json.loads(l) for l in open("data/scan3758.jsonl")]
def valid(h):
    try:
        r=requests.get(h["url"],headers=UA,timeout=10)
        if r.status_code!=200: return None
        txt=re.sub(r"<script.*?</script>|<style.*?</style>","",r.text,flags=re.S|re.I)
        txt=re.sub(r"<[^>]+>"," ",txt); txt=re.sub(r"\s+"," ",txt)
        low=txt.lower()
        n=low.count("ambassador")
        if n<2: return None
        if not re.search(r"\b(apply|join|program|become)\b",low): return None
        if re.search(r"page not found|404|access denied",low[:400]): return None
        return {"url":h["url"],"title":h["title"],"evidence":n}
    except Exception: return None
def work(row):
    if row["status"]!="FOUND": return row
    good=[]
    for h in row["hits"]:
        v=valid(h)
        if v: good.append(v)
    row["hits"]=good
    if not good: row["status"]="NONE"
    return row
with ThreadPoolExecutor(max_workers=10) as ex:
    out=list(ex.map(work,rows))
with open("data/scan3758.jsonl","w") as f:
    for r in out: f.write(json.dumps(r)+"\n")
import collections
print(collections.Counter(r["status"] for r in out))
print("VALID FOUND:",sum(1 for r in out if r["status"]=="FOUND"))
for r in out:
    if r["status"]=="FOUND": print(" ",r["name"],r["hits"][0]["url"][:70],r["hits"][0]["evidence"])
