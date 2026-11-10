import csv,json,os,requests,concurrent.futures
key=os.getenv('MCP_PARALLEL_SEARCH_API_KEY','')
if not key:
 with open(os.path.expanduser('~/.hermes/.env')) as f:
  for l in f:
   if l.startswith('MCP_PARALLEL_SEARCH_API_KEY='):key=l.split('=',1)[1].strip().strip('"\'');break
rows=[r for r in csv.DictReader(open('/home/liebert511/campus-ambassador-hunt/data/registry.csv')) if r['status']=='OPEN']
def go(x):
 name=x['name'];org=x['org'];u=x['apply_url']
 body={'objective':f'For {name} by {org}, discover reliable current official evidence for application opening or closure, deadline and geographic eligibility as of 9 November 2026. Distinguish programs with similar names.','search_queries':[f'"{name}" {org} application open closed deadline 2026 ambassador','"'+name+'" application country eligibility'], 'max_results':5}
 try:
  r=requests.post('https://api.parallel.ai/v1beta/search',headers={'x-api-key':key,'Content-Type':'application/json'},json=body,timeout=60)
  return {'name':name,'org':org,'old_url':u,'http':r.status_code,'data':r.json() if r.status_code==200 else {'error':r.text[:150]}}
 except Exception as e:return {'name':name,'org':org,'old_url':u,'error':str(e)[:100]}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as e: out=list(e.map(go,rows))
with open('work/parallel-original-programs.json','w') as f:json.dump(out,f,indent=2)
with open('outputs/original-open-program-research-2026-11-09.csv','w',newline='',encoding='utf8') as f:
 w=csv.writer(f);w.writerow(['original_program','organizer','original_url','http','source_title','source_url','source_excerpt','review_status'])
 for x in out:
  z=x.get('data',{}).get('results',[])
  if not z:w.writerow([x['name'],x['org'],x['old_url'],x.get('http',x.get('error')),'','','','UNREVIEWED'])
  for y in z:w.writerow([x['name'],x['org'],x['old_url'],x.get('http',x.get('error')),y.get('title',''),y.get('url',''),' | '.join(y.get('excerpts',[]))[:1800],'UNREVIEWED SEARCH RESULT'])
print('Programs searched',len(out),'successful',sum(x.get('http')==200 for x in out),'search results',sum(len(x.get('data',{}).get('results',[])) for x in out))
