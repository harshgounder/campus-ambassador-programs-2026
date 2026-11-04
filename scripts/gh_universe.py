import json,subprocess,csv,sys
TOPICS=["llm","llm-inference","ai-agents","rag","text-to-image","diffusion-models","world-models","speech-recognition","vector-database","mcp","agent-framework","fine-tuning","llmops","evaluation","guardrails","embeddings","multimodal","vision-language-model","model-serving","local-llm","inference-engine","ai-gateway"]
rows={}
for t in TOPICS:
    try:
        out=subprocess.run(["gh","search","repos","--topic",t,"--limit","300","--json","owner,name,description,stargazersCount"],capture_output=True,text=True,timeout=90)
        d=json.loads(out.stdout or "[]")
    except Exception as e:
        print("fail",t,e); continue
    for r in d:
        o=r.get("owner") or {}; login=o.get("login") or ""
        if not login: continue
        k=login.lower()
        if k not in rows:
            rows[k]={"name":login,"handle":login,"source":"github","kind":"org" if o.get("type")=="Organization" else "user","category":"gh:"+t,"url":"https://github.com/"+login,"metric":0,"cats":set()}
        rows[k]["cats"].add("gh:"+t)
        st=int(r.get("stargazersCount") or 0)
        if st>int(rows[k]["metric"]): rows[k]["metric"]=st
    print(t,len(d),len(rows)); sys.stdout.flush()
out=[]
for v in rows.values():
    v["cats"]=";".join(sorted(v["cats"])); out.append(v)
out.sort(key=lambda x:-int(x["metric"]))
with open("data/ai-gh.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["name","handle","source","kind","category","url","metric","cats"])
    w.writeheader(); w.writerows(out)
print("TOTAL",len(out))
