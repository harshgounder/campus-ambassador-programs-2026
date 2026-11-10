import csv,requests,re,html,concurrent.futures,collections,threading
r=list(csv.DictReader(open('outputs/distinct-ambassador-source-leads-2026-11-09.csv')))
lock=threading.Lock()
def chk(x):
 u=x['source_url']; out={'http':'','final_url':'','title':'','status_terms':'','deadline_snippets':'','error':''}
 if not u.startswith(('http://','https://')):out['error']='Not a web URL';return out
 if re.search(r'(^|//|\.)((x|twitter)\.com)',u,re.I):out['error']='Skipped: X to be checked in Brave';return out
 try:
  a=requests.get(u,timeout=12,headers={'User-Agent':'Mozilla/5.0 (compatible; ambassador research)'})
  out['http']=a.status_code;out['final_url']=a.url
  t=re.search(r'<title[^>]*>(.*?)</title>',a.text,re.S|re.I);out['title']=html.unescape(t.group(1).strip())[:160] if t else ''
  s=re.sub(r'<(script|style)\b[^>]*>.*?</\1>',' ',a.text[:1000000],flags=re.S|re.I);s=html.unescape(re.sub('<[^>]+>',' ',s));s=re.sub(r'\s+',' ',s)
  pat=r'[^.]{0,100}(?:applications?\s+(?:(?:are|is)\s+)?(?:now\s+)?(?:open|closed)|no longer accepting|not accepting (?:new )?applications|apply now|apply by|deadline)[^.]{0,100}'
  out['status_terms']=' | '.join(dict.fromkeys(m.group(0).strip() for m in list(re.finditer(pat,s,re.I))[:4]))[:650]
  d=r'[^.]{0,60}(?:\b(?:Nov(?:ember)?|Dec(?:ember)?|Jan(?:uary)?)\s+\d{1,2}(?:,?\s*20\d\d)?|\b\d{1,2}\s+(?:Nov(?:ember)?|Dec(?:ember)?|Jan(?:uary)?)\s*20\d\d)[^.]{0,70}'
  out['deadline_snippets']=' | '.join(dict.fromkeys(m.group(0).strip() for m in list(re.finditer(d,s,re.I))[:3]))[:400]
 except Exception as e:out['error']=str(e)[:150]
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as ex: result=list(ex.map(chk,r))
fields=list(r[0])+['http','final_url','title','status_terms','deadline_snippets','error','verification_status']
with open('outputs/distinct-source-page-screen-2026-11-09.csv','w',newline='',encoding='utf8') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for a,b in zip(r,result):w.writerow({**a,**b,'verification_status':'AUTOMATED SCREEN ONLY; MANUAL IDENTITY DATE AND APPLICATION REVIEW REQUIRED'})
print('Sources',len(result),'HTTP',dict(collections.Counter(str(x['http']) if x['http'] else 'ERROR/SKIPPED' for x in result)),'pages with status terms',sum(bool(x['status_terms']) for x in result))
