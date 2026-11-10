import csv,json,os,requests,concurrent.futures
key=os.getenv('MCP_PARALLEL_SEARCH_API_KEY','')
if not key:
 with open(os.path.expanduser('~/.hermes/.env')) as f:
  for l in f:
   if l.startswith('MCP_PARALLEL_SEARCH_API_KEY='):key=l.split('=',1)[1].strip().strip('"\'');break
rows=list(csv.DictReader(open('/home/liebert511/campus-ambassador-hunt/data/master-ai.csv')))
seen=set(); selected=[]
for x in rows:
 n=x['name'].strip()
 if n.lower() not in seen: seen.add(n.lower());selected.append(x)
selected=selected[300:500]
def go(x):
 n=x['name'];q=f'{n} official ambassador student campus advocate champion program application 2026'
 try:
  r=requests.post('https://api.parallel.ai/v1beta/search',headers={'x-api-key':key,'Content-Type':'application/json'},json={'objective':f'Find official {n} student, campus, developer or community ambassador application; determine published eligibility and whether applications are open November 9 2026; do not infer from generic mentions.','search_queries':[q],'max_results':5},timeout=60)
  return {'name':n,'category':x['category'],'country':x['country'],'http':r.status_code,'body':r.json() if r.status_code==200 else {'error':r.text[:200]}}
 except Exception as e:return {'name':n,'category':x['category'],'country':x['country'],'error':str(e)[:120]}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: results=list(ex.map(go,selected))
with open('work/parallel-org-wave3.json','w') as f:json.dump(results,f,indent=2)
with open('outputs/organization-search-wave3-2026-11-09.csv','w',newline='',encoding='utf8') as f:
 w=csv.writer(f);w.writerow(['organization','category','country','search_http','result_count','result_urls','review_status'])
 for x in results:
  a=x.get('body',{}).get('results',[]);w.writerow([x['name'],x['category'],x['country'],x.get('http',x.get('error')),len(a),' | '.join(z.get('url','') for z in a),'SEARCHED ONLY - PROGRAM STATUS NOT VERIFIED'])
print('organizations',len(results),'successful',sum(r.get('http')==200 for r in results),'source results',sum(len(x.get('body',{}).get('results',[])) for x in results),'failures',[(r['name'],r.get('http',r.get('error'))) for r in results if r.get('http')!=200])
