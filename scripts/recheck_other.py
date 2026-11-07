import csv,re,json,requests
from concurrent.futures import ThreadPoolExecutor, as_completed
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0 Safari/537.36"}
rows=[r for r in csv.DictReader(open("data/registry.csv")) if r["status"] in ("CLOSED","LEAD","UNKNOWN","WAITLIST","PAUSED","INVITE ONLY","OPENS SOON","STALE")]
OPEN=re.compile(r"applications?\s+(are\s+)?(now\s+)?open|apply now|accepting applications|applications? (are )?live|registrations? (are )?open",re.I)
CLOSED=re.compile(r"applications?\s+(are\s+)?(now\s+)?closed|no longer accepting|not accepting (new )?applications|submissions? (are )?closed",re.I)
def chk(r):
    u=r["apply_url"]
    try:
        x=requests.get(u,headers=UA,timeout=15,allow_redirects=True)
        txt=re.sub(r"<script.*?</script>|<style.*?</style>","",x.text,flags=re.S|re.I)
        txt=re.sub(r"<[^>]+>"," ",txt); txt=re.sub(r"\s+"," ",txt)
        return {"name":r["name"],"old":r["status"],"url":u,"http":x.status_code,
                "open":bool(OPEN.search(txt)),"closed":bool(CLOSED.search(txt))}
    except Exception as e:
        return {"name":r["name"],"old":r["status"],"url":u,"http":"ERR","open":False,"closed":False}
out=[]
with ThreadPoolExecutor(max_workers=10) as ex:
    for f in as_completed([ex.submit(chk,r) for r in rows]): out.append(f.result())
json.dump(out,open("data/recheck_other.json","w"),indent=1)
print("checked",len(out))
for x in out:
    if x["open"] and not x["closed"]: print("MAYBE_OPEN",x["old"],x["name"][:45],x["url"][:60])
    elif x["closed"]: print("STILL_CLOSED",x["name"][:45])
