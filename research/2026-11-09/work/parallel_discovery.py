import os,requests,json,concurrent.futures,csv,time
key=os.getenv('MCP_PARALLEL_SEARCH_API_KEY','')
if not key:
 with open(os.path.expanduser('~/.hermes/.env')) as f:
  for line in f:
   if line.startswith('MCP_PARALLEL_SEARCH_API_KEY='):key=line.split('=',1)[1].strip().strip('"\'');break
sectors=['frontier AI model labs','open source AI model and research labs','AI agent frameworks and coding tools','image video voice AI companies','AI cloud infrastructure and GPU providers','cloud computing and developer tools','cybersecurity companies','robotics electronics and semiconductor','data science machine learning MLOps','open source foundations developer communities','university student competitions and festivals','student educational technology companies','entrepreneurship startup programs','finance fintech student','environment sustainability climate','public health medicine students','government international organizations youth','gaming entertainment music brands','fashion consumer brands','blockchain crypto web3','marketing creator influencer communities']
regions=['India','United States','Canada','United Kingdom','European Union','Nigeria','Kenya','South Africa','Egypt','United Arab Emirates','Saudi Arabia','Pakistan','Bangladesh','Indonesia','Philippines','Singapore','Malaysia','Australia','Brazil','Mexico','Spanish speaking Latin America','Japan','South Korea','China']
tasks=[('sector',s) for s in sectors]+[('region',s) for s in regions]
def go(t):
 typ,term=t; q=f'{term} campus student community ambassador program applications open November 2026 application deadline eligibility'
 body={'objective':f'Find distinct active ambassador program application pages and official announcements for {term} worldwide as of November 9 2026, list sources and deadlines.','search_queries':[q],'max_results':10}
 try:
  r=requests.post('https://api.parallel.ai/v1beta/search',headers={'x-api-key':key,'Content-Type':'application/json'},json=body,timeout=60)
  return {'type':typ,'topic':term,'status':r.status_code,'body':r.json() if r.status_code==200 else {'error':r.text[:250]}}
 except Exception as e:return {'type':typ,'topic':term,'error':str(e)[:200]}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p:
 results=list(p.map(go,tasks))
with open('work/parallel-discovery-wave2.json','w') as f:json.dump(results,f,indent=2)
found=[]
for r in results:
 for x in r.get('body',{}).get('results',[]):found.append({'search_area':r['topic'],'title':x.get('title',''),'url':x.get('url',''),'excerpts':' | '.join(x.get('excerpts',[]))[:1500],'review_status':'UNREVIEWED SEARCH RESULT - NOT A VERIFIED PROGRAM'})
with open('outputs/discovery-search-results-2026-11-09.csv','w',newline='',encoding='utf8') as f:
 w=csv.DictWriter(f,fieldnames=['search_area','title','url','excerpts','review_status']);w.writeheader();w.writerows(found)
print('Queries',len(results),'HTTP 200',sum(x.get('status')==200 for x in results),'results',len(found),'unique URLs',len(set(x['url'] for x in found)))
print('Failures',[(x['topic'],x.get('status',x.get('error'))) for x in results if x.get('status')!=200])
