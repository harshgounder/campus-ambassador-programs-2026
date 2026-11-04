import csv,os,re,json,collections
files=["data/ai-curated.csv","data/ai-hf.csv","data/ai-gh.csv"]
rows={}
def norm(n):
    k=n.lower().strip()
    k=re.sub(r"\s+"," ",k)
    for suf in [" ai","-ai","_ai"," labs"," inc"," hq"," research"," technologies"]:
        if k.endswith(suf) and len(k)>len(suf)+2: k=k[:-len(suf)]
    return k
for fp in files:
    if not os.path.exists(fp): continue
    for r in csv.DictReader(open(fp)):
        k=norm(r["name"])
        if not k: continue
        if k not in rows:
            rows[k]={"name":r["name"],"handle":r["handle"],"sources":set(),"kinds":set(),"cats":set(),"url":r.get("url",""),"metric":0,"curated":False}
        v=rows[k]
        v["sources"].add(r["source"]); v["kinds"].add(r["kind"])
        for c in (r.get("cats","")+";"+r.get("category","")).split(";"):
            if c.strip(): v["cats"].add(c.strip())
        if r["source"]=="curated": v["curated"]=True; v["name"]=r["name"]
        try: v["metric"]=max(v["metric"],int(float(r.get("metric") or 0)))
        except: pass
        if r.get("url") and not v["url"]: v["url"]=r["url"]
out=[]
for v in rows.values():
    v["sources"]=";".join(sorted(v["sources"])); v["kinds"]=";".join(sorted(v["kinds"])); v["cats"]=";".join(sorted(v["cats"]))
    out.append(v)
out.sort(key=lambda x:(not x["curated"], -x["metric"], x["name"].lower()))
with open("data/ai-universe.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["name","handle","sources","kinds","cats","url","metric","curated"])
    w.writeheader()
    for v in out: w.writerow({k:v[k] for k in w.fieldnames})
print("TOTAL",len(out))
print("curated",sum(1 for x in out if x["curated"]))
print("from hf",sum(1 for x in out if "huggingface" in x["sources"]))
print("from gh",sum(1 for x in out if "github" in x["sources"]))
c=collections.Counter()
for x in out:
    for t in x["cats"].split(";"):
        if t: c[t]+=1
print("top cats",c.most_common(15))
# notable
notable=[x for x in out if x["curated"] or x["metric"]>=5_000_000 or len(x["cats"].split(";"))>=3]
print("notable",len(notable))
with open("data/ai-notable.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["name","handle","sources","kinds","cats","url","metric","curated"])
    w.writeheader(); w.writerows(notable)
