# The AI scope, and the list under it

Written 5 November 2026. Taxonomy first, then the list. 24 categories, 486 organisations, 34 countries and regions.

Full list: `data/master-ai.csv`. Long tail of 13,981 publishers: `data/ai-universe.csv`.

## Categories

| code | category | orgs | examples |
|---|---|---|---|
| OM | Open-weight model labs | 38 | Qwen, DeepSeek, Moonshot AI, Zhipu AI, MiniMax, 01.AI, Baichuan, StepFun, Shanghai AI Lab, OpenBMB, BAAI, Tenc |
| AGT | Agent harnesses and orchestration | 30 | LangChain, LangGraph, LlamaIndex, CrewAI, AutoGen, Semantic Kernel, Haystack, DSPy, MetaGPT, ChatDev, AgentOps |
| INF | Inference, serving, routing | 30 | vLLM, SGLang, TensorRT-LLM, llama.cpp, Ollama, LM Studio, Jan, GPT4All, LocalAI, MLC LLM, Triton, Ray, KServe, |
| FM | Frontier model labs | 27 | OpenAI, Anthropic, Google DeepMind, Meta AI, xAI, SpaceXAI, Mistral AI, Cohere, AI21 Labs, Amazon AGI, Microso |
| VERT | Vertical AI applications | 27 | Qure.ai, Niramai, SigTuple, Cropin, AgroStar, Intello Labs, Arya.ai, Haptik, Uniphore, Observe.AI, Yellow.ai,  |
| AUD | Speech, music, voice | 26 | ElevenLabs, Suno, Udio, PlayHT, Resemble AI, Respeecher, AssemblyAI, Deepgram, Rev AI, Speechmatics, Cartesia, |
| CODE | Code AI and coding agents | 26 | GitHub, Cursor, Windsurf, Replit, Cognition, Sourcegraph, Tabnine, Qodo, Augment Code, JetBrains, Amazon Q Dev |
| INFRA | Chips, cloud, neoclouds | 26 | AMD, Intel, Cerebras, SambaNova, Groq, Tenstorrent, Graphcore, d-Matrix, Etched, Enflame, Biren, Cambricon, Me |
| VID | Video generation | 24 | Runway, Pika, Luma AI, Kling, Hailuo, OpenAI Sora, Google Veo, Haiper, Genmo, Moonvalley, Higgsfield, Synthesi |
| EVAL | Evaluation, observability, guardrails | 23 | LangSmith, Langfuse, Arize, Humanloop, Braintrust, Galileo, Patronus AI, Lakera, Protect AI, HiddenLayer, Caly |
| ROB | Robotics and embodied AI | 22 | Figure, 1X Technologies, Tesla, Apptronik, Agility Robotics, Sanctuary AI, Unitree, UBTECH, Boston Dynamics, N |
| VEC | Vector, retrieval, embeddings | 21 | Voyage AI, Jina AI, Mixedbread, Nomic AI, Pinecone, Weaviate, Qdrant, Chroma, Milvus, Zilliz, Vespa, LanceDB,  |
| IMG | Image generation | 20 | Midjourney, Black Forest Labs, Ideogram, Leonardo.Ai, Playground AI, Recraft, Adobe, Canva, Krea, Freepik, Fal |
| DEV | Developer platforms with AI | 19 | GitLab, Supabase, Vercel, Netlify, Render, Railway, Firebase, Appwrite, Auth0, Okta, Twilio, Stripe, Razorpay, |
| DATA | Data, labeling, synthetic | 18 | Scale AI, Surge AI, Mercor, Turing, Outlier, Handshake AI, Snorkel, Labelbox, Appen, TELUS Digital, iMerit, Sh |
| TRN | Training, fine-tuning, MLOps | 17 | Unsloth, Axolotl, PEFT, DeepSpeed, Megatron-LM, Colossal-AI, Determined AI, Weights and Biases, MLflow, Comet, |
| SLM | Small and edge models | 16 | Hugging Face, Stability AI, Qualcomm, MediaTek, Arm, Edge Impulse, Arduino, Hailo, Axelera AI, Sima.ai, Kneron |
| SAFE | Safety, policy, research | 14 | MIRI, ARC, Redwood Research, METR, Apollo Research, UK AISI, NIST, Stanford HAI, MIT CSAIL, Berkeley AI Resear |
| WM | World models, 3D, spatial | 13 | World Labs, Decart, Odyssey, Wayve, Covariant, Physical Intelligence, Skild AI, Meshcapade, Tripo, Rodin, Mesh |
| CRE | Creative and design tools | 13 | Figma, Affinity, InVideo, Pictory, Lumen5, Gamma, Tome, Beautiful.ai, Notion, Coda, Airtable, Miro, ClickUp |
| CON | Consumer AI assistants | 10 | ChatGPT, Claude, Gemini, Copilot, Grok, Le Chat, Poe, You.com, Replika, HuggingChat |
| FND | Foundations and communities | 10 | Linux Foundation, Agentic AI Foundation, PyTorch Foundation, LAION, OpenCV, Apache Software Foundation, Mozill |
| HW | AI hardware devices | 8 | Rabbit, Humane, Plaud, Limitless, Omi, Xreal, Rokid, Brilliant Labs |
| REG | Regional ecosystems | 8 | G42, Aleph Alpha, LightOn, Silo AI, Tilde, Sea Group, Bhashini, Zhipu |

## Countries and regions

| country | orgs |
|---|---|
| US | 298 |
| CN | 44 |
| IN | 23 |
| UK | 21 |
| CA | 16 |
| IL | 13 |
| FR | 11 |
| DE | 9 |
| KR | 8 |
| NL | 6 |
| AU | 6 |
| SG | 3 |
| RU | 2 |
| AE | 2 |
| TW | 2 |
| ES | 2 |
| CZ | 2 |
| PL | 2 |
| UK/US | 1 |
| US/FR | 1 |
| IT | 1 |
| NO | 1 |
| VA | 1 |
| US/UK | 1 |
| UA | 1 |
| BE | 1 |
| JP | 1 |
| CY | 1 |
| CH | 1 |
| NP | 1 |
| PH | 1 |
| CN/DE | 1 |
| FI | 1 |
| LV | 1 |

## How to read the country column

`US` means headquartered there. `global` is not used here because every row needs one country
of origin; the program's own reach is a separate field in the program registry.

## What is deliberately out

- Banks, consultancies and IT services that only use AI internally.
- Companies whose AI is a marketing label with no model, dataset or tooling product.
- Research groups inside a university, unless they ship a named model or tool.

## Next step

For every row: does a campus, student, ambassador, champion, fellow or community program exist,
is it open on 3 November 2026 or opening soon, and can a student in India apply. That output
goes to `data/registry.csv`, with `REPORT.md` as the readable layer.
