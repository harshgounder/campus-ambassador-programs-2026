import csv,json,re,os,sys,time
import requests
from urllib.parse import urlparse
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36"}
SKIP=("facebook","linkedin","x.com","twitter","youtube","crunchbase","pitchbook","wikipedia","github.com","huggingface","reddit","medium.com","glassdoor","indeed","ycombinator","instagram","tiktok","discord","t.me")
census=[r for r in csv.DictReader(open("data/ai-orgs-census.csv")) if r["tier"] in ("curated","org")]
scan={json.loads(l)["name"]:json.loads(l) for l in open("data/scan3758.jsonl")}
res1={json.loads(l)["name"]:json.loads(l) for l in open("data/resolve.jsonl")}
res2={json.loads(l)["name"]:json.loads(l) for l in open("data/resolve2.jsonl")}
def covered(n):
    s=scan.get(n); q=res1.get(n); p=res2.get(n)
    return (s and s["status"] in ("NONE","FOUND")) or (q and q["status"] in ("RESOLVED","FOUND")) or (p and p["status"] in ("RESOLVED","FOUND"))
targets=[r for r in census if not covered(r["name"])]
targets.sort(key=lambda r:-int(r["downloads"] or 0))
DONE="data/resolve3_done.txt"; OUT="data/resolve3.jsonl"
done=set(open(DONE).read().split("\n")) if os.path.exists(DONE) else set()
targets=[r for r in targets if r["name"] not in done][:600]
PATHS=["/ambassador","/ambassadors","/campus","/students"]
def ddg(q):
    for attempt in range(2):
        try:
            r=requests.post("https://html.duckduckgo.com/html/",data={"q":q},headers=UA,timeout=15)
            if r.status_code==200:
                links=re.findall(r'class="result__a" href="([^"]+)"',r.text)
                for l in links:
                    d=urlparse(l).netloc.lower().replace("www.","")
                    if any(s in d for s in SKIP): continue
                    return "https://"+d
            time.sleep(2)
        except Exception: time.sleep(2)
    return ""
def check(r):
    n=r["name"]; site=ddg(n+" AI official site")
    if not site: return n,"","UNRESOLVED",[]
    try:
        x=requests.get(site,headers=UA,timeout=8)
        txt=re.sub(r"<[^>]+>"," ",x.text).lower()
        key=re.sub(r"[^a-z0-9]","",n.lower())[:6]
        if key and key not in re.sub(r"[^a-z0-9]","",txt): return n,site,"UNVERIFIED",[]
        hits=[]
        for p in PATHS:
            try:
                y=requests.get(site.rstrip("/")+p,headers=UA,timeout=6)
                if y.status_code==200:
                    b=re.sub(r"<[^>]+>"," ",y.text).lower()
                    if b.count("ambassador")>=2 and re.search(r"apply|join|program",b):
                        t=re.search(r"<title[^>]*>(.*?)</title>",y.text,re.S|re.I)
                        hits.append({"url":y.url,"title":t.group(1).strip()[:100] if t else ""})
            except Exception: pass
        return n,site,"FOUND" if hits else "RESOLVED",hits
    except Exception: return n,site,"UNREACHABLE",[]
print("targets",len(targets)); sys.stdout.flush()
out=open(OUT,"a"); log=open(DONE,"a"); c=0
for r in targets:
    c+=1
    try: n,s,st,h=check(r)
    except Exception: continue
    out.write(json.dumps({"name":n,"site":s,"status":st,"hits":h})+"\n"); out.flush()
    log.write(n+"\n"); log.flush()
    if c%25==0: print("done",c,"found",st); sys.stdout.flush()
    time.sleep(0.8)
print("FINISHED",c)
