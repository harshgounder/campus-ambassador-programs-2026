import json,subprocess,csv,re,sys,time
import requests
from collections import defaultdict
UA={"User-Agent":"Mozilla/5.0 research"}
HF_TAGS=["text-generation","text-to-image","text-to-video","image-text-to-text","automatic-speech-recognition",
"text-to-speech","feature-extraction","image-classification","object-detection","image-segmentation",
"depth-estimation","video-classification","audio-classification","translation","summarization","question-answering",
"fill-mask","sentence-similarity","reranking","text-to-audio","any-to-any","robotics","reinforcement-learning",
"image-to-image","image-to-video","zero-shot-image-classification","visual-question-answering","document-question-answering"]
rows={}
def add(name,source,kind,cat,url,metric=""):
    k=name.lower().strip()
    if not k or len(k)<2: return
    if k not in rows:
        rows[k]={"name":name,"handle":name,"source":source,"kind":kind,"category":cat,"url":url,"metric":metric,"cats":set()}
    rows[k]["cats"].add(cat)
for i,t in enumerate(HF_TAGS):
    try:
        r=requests.get(f"https://huggingface.co/api/models?limit=1000&sort=downloads&direction=-1&pipeline_tag={t}",headers=UA,timeout=40)
        d=r.json()
    except Exception as e:
        print("hf fail",t,e); continue
    for m in d:
        mid=m.get("id","")
        if "/" not in mid: continue
        a=mid.split("/")[0]
        add(a,"huggingface","org","hf:"+t,f"https://huggingface.co/{a}",m.get("downloads",0))
    print("hf",t,len(d),len(rows)); sys.stdout.flush()
TOPICS=["llm","llm-inference","ai-agents","rag","text-to-image","diffusion-models","world-models",
"speech-recognition","vector-database","mcp","agent-framework","fine-tuning","llmops","evaluation",
"guardrails","embeddings","multimodal","vision-language-model","model-serving","prompt-engineering",
"ai-gateway","observability","dataset","inference-engine","local-llm"]
for t in TOPICS:
    try:
        out=subprocess.run(["gh","search","repos","--topic",t,"--limit","800","--json","owner,name,description,stargazersCount"],capture_output=True,text=True,timeout=120)
        d=json.loads(out.stdout or "[]")
    except Exception as e:
        print("gh fail",t,e); continue
    for r in d:
        o=r.get("owner",{}) or {}
        login=o.get("login") or ""
        if not login: continue
        add(login,"github","org" if o.get("type")=="Organization" else "user","gh:"+t,f"https://github.com/{login}",r.get("stargazersCount",0))
    print("gh",t,len(d),len(rows)); sys.stdout.flush()
out=[]
for k,v in rows.items():
    v["cats"]=";".join(sorted(v["cats"]))
    out.append(v)
out.sort(key=lambda x:(x["source"],-int(x["metric"] or 0)))
with open("data/ai-universe.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["name","handle","source","kind","category","url","metric","cats"])
    w.writeheader(); w.writerows(out)
print("TOTAL",len(out),"HF",sum(1 for x in out if x['source']=='huggingface'),"GH",sum(1 for x in out if x['source']=='github'))
