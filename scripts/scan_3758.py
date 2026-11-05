import csv,json,re,subprocess,sys,os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) Chrome/131.0 Safari/537.36"}
try: TOK=subprocess.run(["gh","auth","token"],capture_output=True,text=True,timeout=10).stdout.strip()
except Exception: TOK=""
GH={"Authorization":"Bearer "+TOK,"Accept":"application/vnd.github+json"} if TOK else {}
SKIP=("huggingface.co","hf.co","github.com","x.com","twitter.com","linkedin.com","discord","youtube.com","t.me","medium.com","reddit.com","apply.workable.com","google.com","forms.gle")
PATHS=["/ambassador","/ambassadors","/ambassador-program","/campus","/campus-ambassador","/students","/student-ambassador"]
DONE="data/scan3758_done.txt"
OUT="data/scan3758.jsonl"
done=set(open(DONE).read().split("\n")) if os.path.exists(DONE) else set()
def ext(html):
    out=[]
    for m in re.finditer(r'href="(https?://[^"]+)"',html):
        d=urlparse(m.group(1)).netloc.lower().replace("www.","")
        if any(s in d for s in SKIP): continue
        out.append("https://"+d)
    return list(dict.fromkeys(out))
def resolve(name,sources):
    if "huggingface" in sources:
        try:
            r=requests.get("https://huggingface.co/"+name,headers=UA,timeout=10)
            l=ext(r.text)
            if l: return l[0],"hf"
        except Exception: pass
    if "github" in sources and GH:
        try:
            r=requests.get("https://api.github.com/users/"+name,headers=GH,timeout=10)
            b=r.json().get("blog") or ""
            if b: return (b if b.startswith("http") else "https://"+b),"gh"
        except Exception: pass
    return "","none"
def probe(site):
    hits=[]; reachable=False
    for p in PATHS:
        try:
            r=requests.get(site.rstrip("/")+p,headers=UA,timeout=7,allow_redirects=True)
            if r.status_code==200:
                reachable=True
                t=re.search(r"<title[^>]*>(.*?)</title>",r.text,re.S|re.I)
                title=t.group(1).strip()[:120] if t else ""
                low=(title+r.url).lower()
                if re.search(r"ambassador|campus|student",low) and "not found" not in low and "apache" not in low and "page not found" not in low:
                    hits.append({"url":r.url,"title":title})
        except Exception: pass
    return reachable,hits
def work(r):
    name=r["name"]
    site,how=resolve(name,r["sources"])
    if not site:
        return {"name":name,"site":"","how":how,"reachable":False,"hits":[],"status":"NO_SITE"}
    reach,hits=probe(site)
    return {"name":name,"site":site,"how":how,"reachable":reach,"hits":hits,"status":"FOUND" if hits else ("NONE" if reach else "UNREACHABLE")}
rows=[r for r in csv.DictReader(open("data/ai-orgs-census.csv")) if r["tier"] in ("curated","org") and r["name"] not in done]
print("todo",len(rows)); sys.stdout.flush()
out=open(OUT,"a"); log=open(DONE,"a"); n=0
with ThreadPoolExecutor(max_workers=18) as ex:
    futs=[ex.submit(work,r) for r in rows]
    for f in as_completed(futs):
        n+=1
        try: res=f.result()
        except Exception: continue
        out.write(json.dumps(res)+"\n"); out.flush()
        log.write(res["name"]+"\n"); log.flush()
        if n%100==0: print("done",n,"found",sum(1 for _ in [0])); sys.stdout.flush()
print("FINISHED",n)
