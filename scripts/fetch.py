import csv, os, re, json, sys
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"}
KW=re.compile(r"(application[s]?\s+(?:are|is|now)?\s*(?:open|closed|live)|applications?\s+close|apply now|rolling|deadline|not accepting|no longer|closed for|coming soon|waitlist|interest form)",re.I)
LINK=re.compile(r"(ambassador|student|campus)",re.I)

def slug(u):
    s=re.sub(r"^https?://","",u); s=re.sub(r"[^A-Za-z0-9]+","-",s).strip("-")
    return s[:120]

def one(row):
    url=row["url"]; out={"name":row["name"],"url":url}
    try:
        r=requests.get(url,headers=UA,timeout=20,allow_redirects=True)
        out["http"]=r.status_code; out["final_url"]=r.url
        html=r.text
        out["bytes"]=len(html)
        # strip tags roughly
        text=re.sub(r"<script.*?</script>|<style.*?</style>","",html,flags=re.S|re.I)
        text=re.sub(r"<[^>]+>"," ",text); text=re.sub(r"\s+"," ",text)
        out["title"]=(re.search(r"<title[^>]*>(.*?)</title>",html,re.S|re.I).group(1).strip()[:160] if re.search(r"<title[^>]*>(.*?)</title>",html,re.S|re.I) else "")
        hits=sorted(set(m.group(0).lower() for m in KW.finditer(text)))
        out["kw"]="; ".join(hits[:12])
        # candidate links
        links=[]
        for m in re.finditer(r'href=["\']([^"\']+)["\']',html,re.I):
            h=m.group(1)
            if LINK.search(h) and not h.startswith(("mailto:","javascript:")):
                links.append(urljoin(r.url,h))
        out["links"]="; ".join(sorted(set(links))[:12])
        out["snip"]=text[:1400]
        with open(f"data/http/{slug(url)}.txt","w") as f:
            f.write(f"URL {url}\nFINAL {r.url}\nHTTP {r.status_code}\n\n{text[:20000]}")
    except Exception as e:
        out["http"]="ERR"; out["err"]=str(e)[:120]
    return out

rows=list(csv.DictReader(open("data/universe.csv")))
os.makedirs("data/http",exist_ok=True)
res=[]
with ThreadPoolExecutor(max_workers=10) as ex:
    futs={ex.submit(one,r):r for r in rows}
    for f in as_completed(futs):
        res.append(f.result())
res.sort(key=lambda x:x["name"])
with open("data/sweep.json","w") as f: json.dump(res,f,indent=1)
with open("data/sweep.tsv","w") as f:
    f.write("name\thttp\tfinal_url\tkw\tsnip\n")
    for r in res:
        f.write(f'{r["name"]}\t{r.get("http")}\t{r.get("final_url","")}\t{r.get("kw","")}\t{r.get("snip","")[:300]}\n')
print("done",len(res))
