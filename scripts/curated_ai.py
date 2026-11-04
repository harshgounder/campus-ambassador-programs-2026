import csv
C={
"frontier-llm":"OpenAI|Anthropic|Google DeepMind|Meta AI|xAI|SpaceXAI|Mistral AI|Cohere|AI21 Labs|Amazon AGI|Microsoft AI|Apple|Reka AI|Allen Institute for AI|EleutherAI|Nous Research|Liquid AI|Inflection AI|Character.AI|Perplexity AI|SambaNova Systems|Cerebras Systems|Groq|Together AI|Fireworks AI|DeepInfra|Replicate|Modal|Anyscale|RunPod|Lambda|CoreWeave|Crusoe|Nebius",
"open-model-lab":"Meta Llama|Qwen|Alibaba Tongyi|DeepSeek|Moonshot AI|Kimi|Zhipu AI|Z.ai|MiniMax|01.AI|Baichuan|StepFun|Shanghai AI Lab|InternLM|OpenBMB|BAAI|Tencent Hunyuan|ByteDance Seed|Baidu ERNIE|iFlytek Spark|SenseTime|Huawei Pangu|Xiaomi MiMo|InclusionAI|Ant Group|LG AI Research|EXAONE|Naver HyperCLOVA|Upstage|Sarvam AI|Krutrim|AI4Bharat|Project Indus|NVIDIA Nemotron|IBM Granite|Microsoft Phi|Apple OpenELM|Samsung Gauss|SK Telecom|KT Midm|FuriosaAI|Rebellions|Sber GigaChat|Yandex|TII Falcon|AI Singapore|SEA-LION|Cohere For AI|Ai2 OLMo",
"slm-edge":"Microsoft Phi|Google Gemma|Qwen Small|Llama Small|Hugging Face SmolLM|Stability StableLM|TinyLlama|MobileLLM|MiniCPM|Apple On-Device|Qualcomm AI|MediaTek|Samsung Exynos|Arm Ethos|Google Coral|Edge Impulse|Arduino|Qualcomm AI Hub|Hailo|Axelera AI|Sima.ai|Kneron|GreenWaves|Syntiant|Innatera",
"image-gen":"Midjourney|Stability AI|Black Forest Labs|FLUX|Ideogram|Leonardo.Ai|Playground AI|Recraft|Adobe Firefly|Canva|Krea|Freepik|Fal|Photoroom|Clipdrop|NightCafe|Civitai|Sogni|Bria AI|Getty Images|Shutterstock AI|Runway|Pika|Luma AI|Kling|Kuaishou|Hailuo|Vidu|Shengshu|Haiper|Genmo|Moonvalley|Higgsfield",
"video-gen":"Runway|Pika|Luma AI|Kling|Hailuo|Sora|OpenAI Sora|Veo|Google Veo|Haiper|Genmo|Moonvalley|Higgsfield|Synthesia|HeyGen|D-ID|Tavus|Rephrase|Colossyan|Hour One|Veed|Kapwing|Descript|Wondercraft|Captions",
"world-model-3d":"World Labs|Decart|Odyssey|Google Genie|Google Dreamer|Wayve|GAIA|Covariant|Physical Intelligence|Skild AI|Figure AI|1X Technologies|Tesla Optimus|Apptronik|Agility Robotics|Sanctuary AI|Unitree|UBTECH|Boston Dynamics|Nuro|Waabi|Aurora|Zoox|Waymo|Momenta|Pony.ai|WeRide|Cruise|Meshcapade|Tripo|Rodin|Meshy|Spline|Kaedim",
"speech-audio":"ElevenLabs|Suno|Udio|PlayHT|Resemble AI|Respeecher|AssemblyAI|Deepgram|Rev AI|Speechmatics|Cartesia|Rime|LMNT|Sesame|Hume AI|Voiceflow|Vapi|Retell|Bland|PolyAI|OpenAI Whisper|Meta AudioCraft|Google Lyria|Stability Audio|Landr|Boomy|Aiva|Soundraw|Mubert|Kits.AI",
"code-ai":"GitHub Copilot|Cursor|Anysphere|Windsurf|Codeium|Replit|Cognition Devin|Sourcegraph Cody|Tabnine|Qodo|Augment Code|Magic|Poolside|JetBrains AI|Amazon Q Developer|Google Gemini Code Assist|Continue.dev|Aider|Cline|Roo Code|OpenHands|SWE-agent|Factory|Sweep|CodeRabbit|Greptile|Graphite|Ellipsis|Kiro|AWS Kiro|Zed|Warp",
"embeddings-rerank":"Cohere Embed|Voyage AI|Jina AI|Mixedbread|Nomic AI|BGE|E5 Microsoft|Sentence Transformers|Pinecone|Weaviate|Qdrant|Chroma|Milvus|Zilliz|Vespa|pgvector|LanceDB|Marqo|Turbopuffer|Vectara|Redis|Elastic|MongoDB Atlas|Neo4j|SingleStore|KX",
"agent-harness":"LangChain|LangGraph|LlamaIndex|CrewAI|AutoGen|Semantic Kernel|Haystack|deepset|DSPy|OpenHands Agent|SWE-agent Harness|MetaGPT|ChatDev|AgentOps|Composio|E2B|Daytona|Browserbase|Stagehand|Skyvern|Letta|MemGPT|Mem0|Zep|Supermemory|Lindy|Zapier Agents|n8n|Make|Gumloop|Relevance AI|Beam AI|MultiOn|Adept|Simular|Rabbit|Humane",
"inference-serving":"vLLM|SGLang|TensorRT-LLM|llama.cpp|Ollama|LM Studio|Jan|GPT4All|LocalAI|text-generation-webui|ExLlama|MLC LLM|Triton|Ray Serve|KServe|BentoML|Modal Serving|Baseten|Replicate Serving|Fireworks Serving|Together Serving|DeepInfra Serving|OpenRouter|LiteLLM|Portkey|Helicone|Cloudflare AI Gateway|Martian|NotDiamond|RouteLLM|Predibase|OpenPipe|Lamini",
"training-finetune":"Hugging Face|Unsloth|Axolotl|PEFT|LoRA|DeepSpeed|Megatron-LM|FSDP|Colossal-AI|Ray Train|Determined AI|Weights and Biases|MLflow|Comet|Neptune|ClearML|Kaggle|Lightning AI|Predibase Train|OpenPipe Train|Lamini Train|Contextual AI|Writer|Adept Train|Databricks Mosaic AI",
"eval-guardrails":"LangSmith|Langfuse|Arize|Phoenix|Humanloop|Braintrust|Galileo|Patronus AI|Lakera|Robust Intelligence|Protect AI|HiddenLayer|CalypsoAI|Prompt Security|Guardrails AI|NeMo Guardrails|Giskard|DeepEval|Ragas|TruLens|Evidently|Fiddler|WhyLabs|Aporia|Credo AI|Holistic AI",
"data-labeling":"Scale AI|Surge AI|Mercor|Turing|Outlier|Handshake AI|Snorkel|Labelbox|Appen|TELUS Digital|iMerit|Shaip|Innodata|Defined.ai|Toloka|Sama|CloudFactory|Remotasks",
"ai-infra":"NVIDIA|AMD|Intel|Cerebras Hardware|SambaNova Hardware|Groq Hardware|Tenstorrent|Graphcore|d-Matrix|Etched|Enflame|Biren|Cambricon|MetaX|Iluvatar|AWS|Azure|Google Cloud|Oracle Cloud|CoreWeave Cloud|Lambda Cloud|Crusoe Cloud|Nebius Cloud|Vultr|DigitalOcean|Paperspace|RunPod Cloud|Modal Cloud|Baseten Cloud",
"ai-safety":"MIRI|ARC|Conjecture|Redwood Research|METR|Apollo Research|UK AISI|NIST|Stanford HAI|MIT CSAIL|Berkeley AI Research|CMU AI|Vector Institute|Mila|Alan Turing Institute|EleutherAI Safety|Ai2 Safety|Anthropic Safety|OpenAI Safety|DeepMind Safety",
"india-ai":"Sarvam AI|Krutrim|Fractal Analytics|Haptik|Uniphore|Observe.AI|Yellow.ai|Gupshup|CoRover|Bhashini|Tech Mahindra AI|Wipro AI|Infosys Topaz|TCS AI.Cloud|HCL AI|Zoho|Freshworks|Darwinbox|Mad Street Den|SigTuple|Qure.ai|Niramai|Artelus|Cropin|AgroStar|Intello Labs|Arya.ai|Absentia|NeuroPixels|AI4Bharat Research",
}
rows=[]
for cat,s in C.items():
    for n in s.split("|"):
        n=n.strip()
        if n: rows.append({"name":n,"handle":n,"source":"curated","kind":"org","category":cat,"url":"","metric":"","cats":cat})
with open("data/ai-curated.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["name","handle","source","kind","category","url","metric","cats"])
    w.writeheader(); w.writerows(rows)
print("curated",len(rows))
