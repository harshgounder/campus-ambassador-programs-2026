import csv,collections,re,os
PRI=[("text-generation","text-gen"),("image-text-to-text","multimodal"),("any-to-any","multimodal"),
("video-text-to-text","multimodal"),("visual-question-answering","multimodal"),("document-question-answering","multimodal"),
("text-to-image","image"),("image-to-image","image"),("text-to-video","video"),("image-to-video","video"),
("text-to-3d","3d"),("image-to-3d","3d"),("automatic-speech-recognition","audio"),("text-to-speech","audio"),
("text-to-audio","audio"),("audio-to-audio","audio"),("voice-activity-detection","audio"),
("feature-extraction","embeddings"),("sentence-similarity","embeddings"),("image-feature-extraction","embeddings"),
("reranking","rerank"),("object-detection","vision"),("image-segmentation","vision"),("depth-estimation","vision"),
("keypoint-detection","vision"),("zero-shot-object-detection","vision"),("mask-generation","vision"),
("image-classification","classification"),("video-classification","classification"),("audio-classification","classification"),
("translation","nlp"),("summarization","nlp"),("question-answering","nlp"),("fill-mask","nlp"),
("robotics","robotics"),("reinforcement-learning","rl"),("image-text-retrieval","retrieval")]
rows={}
def add(name,source,tags,dl,stars,tier):
    k=re.sub(r"[^a-z0-9]","",name.lower())
    if not k: return
    if k not in rows: rows[k]={"name":name,"sources":set(),"tags":set(),"downloads":0,"stars":0,"tier":"individual","category":"other"}
    v=rows[k]; v["sources"].add(source)
    for t in tags.split(";"):
        if t: v["tags"].add(t)
    v["downloads"]=max(v["downloads"],dl); v["stars"]=max(v["stars"],stars)
    order={"curated":0,"org":1,"small":2,"individual":3}
    if order[tier]<order[v["tier"]]: v["tier"]=tier
if os.path.exists("data/census-hf.csv"):
    for r in csv.DictReader(open("data/census-hf.csv")):
        dl=int(r["downloads"] or 0)
        tier="org" if dl>=100000 else ("small" if dl>=5000 else "individual")
        add(r["name"],"huggingface",r["tags"],dl,0,tier)
for fp in ["data/ai-gh.csv","data/census-gh.csv"]:
    if os.path.exists(fp):
        for r in csv.DictReader(open(fp)):
            st=int(r.get("stars") or r.get("metric") or 0)
            tier="org" if st>=1000 else ("small" if st>=100 else "individual")
            add(r["name"],"github",r.get("topics",r.get("cats","")),0,st,tier)
for r in csv.DictReader(open("data/ai-curated.csv")):
    add(r["name"],"curated",r["category"],0,0,"curated")
for v in rows.values():
    cat="other"
    for tag,c in PRI:
        if tag in v["tags"]: cat=c; break
    v["category"]=cat
out=[]
for v in rows.values():
    v["sources"]=";".join(sorted(v["sources"])); v["tags"]=";".join(sorted(v["tags"]))
    out.append(v)
out.sort(key=lambda x:(x["tier"]!="curated",x["tier"]!="org",-x["downloads"],-x["stars"]))
with open("data/ai-orgs-census.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["name","sources","tier","category","downloads","stars","tags"])
    w.writeheader(); w.writerows(out)
c=collections.Counter(x["tier"] for x in out)
print("TOTAL",len(out),dict(c))
cc=collections.Counter((x["category"],x["tier"]) for x in out)
cats=sorted({x["category"] for x in out})
print("category | curated | org | small | individual")
for cat in cats:
    print(cat,cc.get((cat,"curated"),0),cc.get((cat,"org"),0),cc.get((cat,"small"),0),cc.get((cat,"individual"),0))
