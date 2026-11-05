import json,re,os,sys
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) Chrome/131.0 Safari/537.36"}
rows=[json.loads(l) for l in open("data/scan3758.jsonl")]
targets=[r for r in rows if r["status"]=="NO_SITE"]
DONE="data/resolve_done.txt"; OUT="data/resolve.jsonl"
done=set(open(DONE).read().split("\n")) if os.path.exists(DONE) else set()
targets=[r for r in targets if r["name"] not in done]
PATHS=["/ambassador","/ambassadors","/campus","/students"]
def slug(n): return re.sub(r"[^a-z0-9]","",n.lower())
def check(r):
    n=r["name"]; s=slug(n)
    if len(s)<3: return r["name"],"", "SKIP", []
    for tld in [".com",".ai",".io",".dev",".co",".app"]:
        url="https://"+s+tld
        try:
            x=requests.get(url,headers=UA,timeout=8,allow_redirects=True)
            if x.status_code!=200: continue
            txt=re.sub(r"<[^>]+>"," ",x.text); txt=re.sub(r"\s+"," ",txt).lower()
            if s[:5] not in txt and s not in txt: continue
            if not re.search(r"\b(ai|ml|model|llm|agent)\b",txt): continue
            hits=[]
            for p in PATHS:
                try:
                    y=requests.get(url.rstrip("/")+p,headers=UA,timeout=6)
                    if y.status_code==200:
                        t=re.search(r"<title[^>]*>(.*?)</title>",y.text,re.S|re.I)
                        title=t.group(1).strip()[:100] if t else ""
                        body=re.sub(r"<[^>]+>"," ",y.text).lower()
                        if body.count("ambassador")>=2 and re.search(r"apply|join|program",body):
                            hits.append({"url":y.url,"title":title})
                except Exception: pass
            return n,url,"FOUND" if hits else "RESOLVED",hits
        except Exception: continue
    return n,"","UNRESOLVED",[]
print("targets",len(targets)); sys.stdout.flush()
out=open(OUT,"a"); log=open(DONE,"a"); c=0
with ThreadPoolExecutor(max_workers=20) as ex:
    for f in as_completed([ex.submit(check,r) for r in targets]):
        c+=1
        try: n,u,st,h=f.result()
        except Exception: continue
        out.write(json.dumps({"name":n,"site":u,"status":st,"hits":h})+"\n"); out.flush()
        log.write(n+"\n"); log.flush()
        if c%100==0: print("done",c); sys.stdout.flush()
print("FINISHED",c)
