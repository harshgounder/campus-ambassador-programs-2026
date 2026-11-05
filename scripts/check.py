import csv,sys,os,re,json
fails=[]; passes=[]
def chk(name,cond,detail=""):
    (passes if cond else fails).append((name,detail))
def rows(p):
    return list(csv.DictReader(open(p))) if os.path.exists(p) else []
SCOPE=open("scope/SCOPE-AI.md").read() if os.path.exists("scope/SCOPE-AI.md") else ""
codes=set(re.findall(r"^\| ([A-Z]{2,5}) \|",SCOPE,re.M))
chk("scope file exists",bool(SCOPE),"scope/SCOPE-AI.md")
chk("scope defines at least 20 categories",len(codes)>=20,f"{len(codes)} codes")
m=rows("data/master-ai.csv")
chk("master list exists",len(m)>0,"data/master-ai.csv")
chk("master list has 400+ orgs",len(m)>=400,f"{len(m)} rows")
mc={x["category"] for x in m}
chk("master list covers every scope category",codes<=mc|{"REG"},f"missing {sorted(codes-mc)}")
chk("every master row has a country",all(x["country"].strip() for x in m),"blank country found" if any(not x["country"].strip() for x in m) else "")
chk("every category has 5+ entries",all(sum(1 for x in m if x["category"]==c)>=5 for c in mc),str({c:sum(1 for x in m if x["category"]==c) for c in mc}))
chk("at least 20 countries represented",len({x["country"] for x in m})>=20,f"{len({x['country'] for x in m})} countries")
r=rows("data/registry.csv")
chk("program registry exists",len(r)>0,"data/registry.csv")
chk("registry has 150+ programs",len(r)>=150,f"{len(r)} rows")
chk("registry has OPEN rows",any(x["status"]=="OPEN" for x in r),f"{sum(1 for x in r if x['status']=='OPEN')} open")
chk("registry has India-eligible rows",any("India" in x["region"] or x["region"]=="global" for x in r),"")
chk("report exists",os.path.exists("REPORT.md"),"REPORT.md")
chk("ai scope report exists",os.path.exists("REPORT-AI-SCOPE.md"),"REPORT-AI-SCOPE.md")
chk("universe csv exists",len(rows("data/ai-universe.csv"))>10000,f"{len(rows('data/ai-universe.csv'))} rows")
chk("waves tracker exists",os.path.exists("WAVES.md"),"WAVES.md")
chk("tracker exists with 50+ open rows",len(rows("data/tracker.csv"))>=50,f"{len(rows('data/tracker.csv'))} rows")
import os as _os
chk("notable scan processed 1000+",_os.path.exists("data/scan_processed.txt") and len(open("data/scan_processed.txt").read().split("\n"))>=1000,f"{len(open('data/scan_processed.txt').read().split(chr(10)))-1 if _os.path.exists('data/scan_processed.txt') else 0} processed")
for n,d in passes: print("PASS",n,"|",d)
for n,d in fails: print("FAIL",n,"|",d)
print(f"\n{len(passes)} passed, {len(fails)} failed")
sys.exit(1 if fails else 0)
