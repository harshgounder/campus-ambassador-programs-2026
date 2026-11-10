import csv,json,os,requests,concurrent.futures,threading
key=os.getenv('MCP_PARALLEL_SEARCH_API_KEY','')
if not key:
 with open(os.path.expanduser('~/.hermes/.env')) as f:
  for line in f:
   if line.startswith('MCP_PARALLEL_SEARCH_API_KEY='):key=line.split('=',1)[1].strip().strip('"\'');break
c=list(csv.DictReader(open('/home/liebert511/campus-ambassador-hunt/data/ai-orgs-census.csv')))
m={r['name'].strip().lower() for r in csv.DictReader(open('/home/liebert511/campus-ambassador-hunt/data/master-ai.csv'))}
r=[x for x in c if x['tier']=='org' and x['name'].lower().strip() not in m]
r.sort(key=lambda x:int(x['downloads'] or 0),reverse=True);r=r[3500:]
lock=threading.Lock();path='work/parallel-census-wave6.jsonl'
def go(x):
 n=x['name'];q=f'{n} official ambassador student campus developer advocate program apply'
 try:
  resp=requests.post('https://api.parallel.ai/v1beta/search',headers={'x-api-key':key,'Content-Type':'application/json'},json={'objective':f'Find official ambassador, campus, student or developer advocacy programs for {n}; source status on 9 November 2026; distinguish unrelated similarly named organizations.','search_queries':[q],'max_results':4},timeout=60)
  v={'name':n,'category':x['category'],'http':resp.status_code,'data':resp.json() if resp.status_code==200 else {'error':resp.text[:120]}}
 except Exception as e:v={'name':n,'category':x['category'],'error':str(e)[:100]}
 with lock:
  with open(path,'a') as f:f.write(json.dumps(v)+'\n')
 return v
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e: res=list(e.map(go,r))
with open('outputs/census-organization-search-wave6-2026-11-09.csv','w',newline='') as f:
 w=csv.writer(f);w.writerow(['organization','category','http','number_of_results','source_urls','status'])
 for x in res:
  z=x.get('data',{}).get('results',[]);w.writerow([x['name'],x['category'],x.get('http',x.get('error')),len(z),' | '.join(t.get('url','') for t in z),'SEARCHED ONLY; IDENTITY AND PROGRAM STATUS NOT VERIFIED'])
print('Census searched',len(res),'successful',sum(x.get('http')==200 for x in res),'failed',sum(x.get('http')!=200 for x in res),'results',sum(len(x.get('data',{}).get('results',[])) for x in res))
