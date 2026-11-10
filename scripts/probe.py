import json
import re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

import requests

UA = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
ORGS = """
openai openai.com
anthropic anthropic.com
google deepmind deepmind.google
meta ai.meta.com
microsoft microsoft.com
nvidia nvidia.com
amd amd.com
intel intel.com
qualcomm qualcomm.com
ibm ibm.com
mistral mistral.ai
cohere cohere.com
huggingface huggingface.co
deepseek deepseek.com
qwen qwen.ai
moonshot kimi.ai
zhipu z.ai
minimax minimax.io
xiaomi mi.com
bytedance bytedance.com
tencent tencent.com
baidu baidu.com
iflytek iflytek.com
sensetime sensetime.com
01ai 01.ai
baichuan baichuan-ai.com
stepfun stepfun.com
liquid liquid.ai
groq groq.com
cerebras cerebras.ai
perplexity perplexity.ai
xai x.ai
stability stability.ai
character character.ai
elevenlabs elevenlabs.io
suno suno.com
runway runwayml.com
midjourney midjourney.com
pika pika.art
luma lumalabs.ai
heygen heygen.com
poolside poolside.ai
cognition devin.ai
cursor cursor.com
windsurf windsurf.com
replit replit.com
lovable lovable.dev
bolt bolt.new
v0 v0.dev
warp warp.dev
zed zed.dev
kiro kiro.dev
sourcegraph sourcegraph.com
tabnine tabnine.com
qodo qodo.ai
github github.com
gitlab gitlab.com
aws aws.amazon.com
cloudflare cloudflare.com
digitalocean digitalocean.com
vercel vercel.com
netlify netlify.com
supabase supabase.com
appwrite appwrite.io
firebase firebase.google.com
mongodb mongodb.com
neo4j neo4j.com
redis redis.io
elastic elastic.co
snowflake snowflake.com
databricks databricks.com
confluent confluent.io
hashicorp hashicorp.com
docker docker.com
cncf cncf.io
grafana grafana.com
jetbrains jetbrains.com
postman postman.com
twilio twilio.com
auth0 auth0.com
stripe stripe.com
razorpay razorpay.com
pinecone pinecone.io
weaviate weaviate.io
qdrant qdrant.tech
chroma trychroma.com
langchain langchain.com
llamaindex llamaindex.ai
wandb wandb.ai
scale scale.com
internshala internshala.com
unstop unstop.com
geeksforgeeks geeksforgeeks.org
codingninjas codingninjas.com
scaler scaler.com
pw pw.live
unacademy unacademy.com
vedantu vedantu.com
byjus byjus.com
simplilearn simplilearn.com
greatlearning mygreatlearning.com
upgrad upgrad.com
almabetter almabetter.com
letsupgrade letsupgrade.in
devtown devtown.in
naukreez naukreez.com
taskveda taskveda.in
campusunite campusunite.in
reskilll reskilll.com
smartbridge thesmartbridge.com
ctf7 ctf7.com
gajab gajab.com
mygov mygov.in
aicte aicte-india.org
hcltech hcltech.com
swiggy swiggy.com
zomato zomato.com
zepto zepto.com
blinkit blinkit.com
cred cred.club
groww groww.in
zerodha zerodha.com
upstox upstox.com
angelone angelone.in
paytm paytm.com
phonepe phonepe.com
nykaa nykaa.com
myntra myntra.com
boat boat-lifestyle.com
mamaearth mamaearth.in
lenskart lenskart.com
redbull redbull.com
cocacola coca-cola.com
ethereum ethereum.org
solana solana.com
polygon polygon.technology
near near.org
aptos aptoslabs.com
sui sui.io
ton ton.org
polkadot polkadot.com
cardano cardano.org
algorand algorand.com
stellar stellar.org
hedera hedera.com
chainlink chain.link
alchemy alchemy.com
filecoin filecoin.io
base base.org
optimism optimism.io
arbitrum arbitrum.io
uniswap uniswap.org
coindcx coindcx.com
wazirx wazirx.com
mudrex mudrex.com
binance binance.com
bybit bybit.com
okx okx.com
techfest techfest.org
moodi moodi.org
springfest springfest.in
kshitij kshitij.com
antaragni antaragni.in
cognizance cognizance.in
sphinx sphinx.org.in
ecell ecell.in
tryst tryst-iitdelhi.org
rendezvous rendezvous-iitd.org
saarang saarang.org
"""
rows = [
    (lambda p: (" ".join(p[:-1]), p[-1]))(line.split())
    for line in ORGS.strip().splitlines()
    if line.strip()
]
PATH = re.compile(
    r"(ambassador|ambassador|ambassador|campus|student|community|advocate|champion|expert|hero)",
    re.I,
)


def probe(pair):
    name, dom = pair
    out = {"name": name, "domain": dom, "hits": [], "http": None}
    for scheme in ("https://", "http://"):
        try:
            r = requests.get(scheme + dom, headers=UA, timeout=14, allow_redirects=True)
            out["http"] = r.status_code
            out["final"] = r.url
            html = r.text
            links = set()
            for m in re.finditer(r'href=["\']([^"\'#]+)["\']', html, re.I):
                h = m.group(1)
                if PATH.search(h):
                    links.add(urljoin(r.url, h))
            # also probe common paths
            for p in (
                "/ambassadors",
                "/ambassador",
                "/ambassador-program",
                "/campus",
                "/campus-ambassador",
                "/students",
                "/student-ambassador",
                "/community/ambassadors",
            ):
                links.add("https://" + dom + p)
            out["hits"] = sorted(links)[:25]
            break
        except Exception as e:
            out["err"] = str(e)[:80]
    return out


with ThreadPoolExecutor(max_workers=16) as ex:
    res = list(ex.map(probe, rows))
json.dump(res, open("data/probe/probe.json", "w"), indent=1)
print("done", len(res), "with hits", sum(1 for r in res if r["hits"]))
