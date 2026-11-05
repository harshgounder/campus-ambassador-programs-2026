import json,re,os,sys,csv
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) Chrome/131.0 Safari/537.36"}
census=[r for r in csv.DictReader(open("data/ai-orgs-census.csv")) if r["tier"] in ("curated","org")]
scan={json.loads(l)["name"]:json.loads(l) for l in open("data/scan3758.jsonl")}
res={json.loads(l)["name"]:json.loads(l) for l in open("data/resolve.jsonl")}
def covered(n):
    s=scan.get(n); q=res.get(n)
    return (s and s["status"] in ("NONE","FOUND")) or (q and q["status"] in ("RESOLVED","FOUND"))
targets=[r["name"] for r in census if not covered(r["name"])]
DONE="data/resolve2_done.txt"; OUT="data/resolve2.jsonl"
done=set(open(DONE).read().split("\n")) if os.path.exists(DONE) else set()
targets=[n for n in targets if n not in done]
PATHS=["/ambassador","/ambassadors","/campus","/students"]
def variants(n):
    s=re.sub(r"[^a-z0-9]","",n.lower())
    out={s}
    for suf in ["ai","labs","hq","inc","research"]:
        if s.endswith(suf) and len(s)>len(suf)+3: out.add(s[:-len(suf)])
        out.add(s+suf)
    return [v for v in out if len(v)>=3][:4]
def check(n):
    for v in variants(n):
        for tld in [".com",".ai",".io",".co"]:
            url="https://"+v+tld
            try:
                x=requests.get(url,headers=UA,timeout=6,allow_redirects=True)
                if x.status_code!=200: continue
                txt=re.sub(r"<[^>]+>"," ",x.text).lower()
                if v[:5] not in txt: continue
                if not re.search(r"\b(ai|ml|model|llm|agent|data)\b",txt): continue
                hits=[]
                for p in PATHS:
                    try:
                        y=requests.get(url.rstrip("/")+p,headers=UA,timeout=5)
                        if y.status_code==200:
                            b=re.sub(r"<[^>]+>"," ",y.text).lower()
                            if b.count("ambassador")>=2 and re.search(r"apply|join|program",b):
                                t=re.search(r"<title[^>]*>(.*?)</title>",y.text,re.S|re.I)
                                hits.append({"url":y.url,"title":t.group(1).strip()[:100] if t else ""})
                    except Exception: pass
                return n,url,"FOUND" if hits else "RESOLVED",hits
            except Exception: continue
    return n,"","UNRESOLVED",[]
print("targets",len(targets)); sys.stdout.flush()
out=open(OUT,"a"); log=open(DONE,"a"); c=0
with ThreadPoolExecutor(max_workers=20) as ex:
    for f in as_completed([ex.submit(check,n) for n in targets]):
        c+=1
        try: n,u,st,h=f.result()
        except Exception: continue
        out.write(json.dumps({"name":n,"site":u,"status":st,"hits":h})+"\n"); out.flush()
        log.write(n+"\n"); log.flush()
        if c%100==0: print("done",c); sys.stdout.flush()
print("FINISHED",c)
