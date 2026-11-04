import csv,json,re,subprocess,sys,time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin,urlparse
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) Chrome/131.0 Safari/537.36"}
try: TOK=subprocess.run(["gh","auth","token"],capture_output=True,text=True,timeout=10).stdout.strip()
except Exception: TOK=""
GH={"Authorization":"Bearer "+TOK,"Accept":"application/vnd.github+json"} if TOK else {}
SKIP=("huggingface.co","github.com","x.com","twitter.com","linkedin.com","discord.gg","discord.com","youtube.com","t.me","medium.com","reddit.com")
PROBE=["/ambassador","/ambassadors","/ambassador-program","/campus","/campus-ambassador","/students","/student-ambassador","/community/ambassadors","/community"]
def ext_links(html):
    out=[]
    for m in re.finditer(r'href="(https?://[^"]+)"',html):
        u=m.group(1)
        d=urlparse(u).netloc.lower().replace("www.","")
        if any(s in d for s in SKIP): continue
        if d: out.append("https://"+d)
    return list(dict.fromkeys(out))
def hf_site(name):
    try:
        r=requests.get("https://huggingface.co/"+name,headers=UA,timeout=12)
        ls=ext_links(r.text)
        return ls[0] if ls else ""
    except Exception: return ""
def gh_site(login):
    if not GH: return ""
    try:
        r=requests.get("https://api.github.com/users/"+login,headers=GH,timeout=12)
        b=r.json().get("blog") or ""
        if b and not b.startswith("http"): b="https://"+b
        return b
    except Exception: return ""
def probe(dom):
    hits=[]
    base=dom.rstrip("/")
    for p in PROBE:
        try:
            r=requests.get(base+p,headers=UA,timeout=8,allow_redirects=True)
            if r.status_code==200:
                t=re.search(r"<title[^>]*>(.*?)</title>",r.text,re.S|re.I)
                title=(t.group(1).strip()[:120] if t else "")
                if re.search(r"ambassador|campus|student|community",title+r.url,re.I):
                    hits.append({"url":r.url,"title":title})
        except Exception: pass
    return hits
rows=list(csv.DictReader(open("data/ai-notable.csv")))
print("notable",len(rows)); sys.stdout.flush()
out=open("data/scan_hits.jsonl","w")
def work(r):
    name=r["handle"]; sites=[]
    if "huggingface" in r["sources"]: sites.append(hf_site(name))
    if "github" in r["sources"]: sites.append(gh_site(name))
    sites=[s for s in dict.fromkeys(sites) if s]
    res={"name":r["name"],"sources":r["sources"],"cats":r["cats"],"sites":sites,"hits":[]}
    for s in sites[:2]:
        if "huggingface.co" in s or "github.com" in s: continue
        h=probe(s)
        if h: res["hits"].extend(h)
    return res
n=0
with ThreadPoolExecutor(max_workers=16) as ex:
    futs={ex.submit(work,r):r for r in rows}
    for f in as_completed(futs):
        n+=1
        try: res=f.result()
        except Exception as e: continue
        if res["hits"]:
            out.write(json.dumps(res)+"\n"); out.flush()
        if n%100==0: print("done",n); sys.stdout.flush()
out.close()
print("FINISHED",n)
