import csv,json,re,requests
from concurrent.futures import ThreadPoolExecutor
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) Chrome/131.0 Safari/537.36"}
rows=list(csv.DictReader(open("data/registry.csv")))
def chk(r):
    u=r["apply_url"]
    try:
        x=requests.get(u,headers=UA,timeout=12,allow_redirects=True)
        t=re.search(r"<title[^>]*>(.*?)</title>",x.text,re.S|re.I)
        return {"name":r["name"],"url":u,"http":x.status_code,"final":x.url,"title":(t.group(1).strip()[:90] if t else "")}
    except Exception as e:
        return {"name":r["name"],"url":u,"http":"ERR","final":"","title":str(e)[:80]}
with ThreadPoolExecutor(max_workers=16) as ex:
    out=list(ex.map(chk,rows))
json.dump(out,open("data/recheck.json","w"),indent=1)
bad=[o for o in out if o["http"] not in (200,)]
print("total",len(out),"non200",len(bad))
for o in bad: print(o["http"],o["name"][:40],o["url"][:80],o["title"][:50])
