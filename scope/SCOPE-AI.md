# Scope: the AI and ML universe

Written 5 November 2026, before the list. This file defines what counts, so a missing company
is a visible gap and not a judgement call.

## Inclusion rule

An organisation goes in if it does at least one of these:

1. Trains or releases AI models (any modality).
2. Builds software that trains, serves, evaluates, guards, retrieves for, or orchestrates models.
3. Sells compute, chips, or infrastructure whose primary demand is AI.
4. Builds AI-native products where the model is the product, not a feature.
5. Funds, governs, or researches AI as its main activity.

Excluded: companies that only use AI internally (a bank with a chatbot), generic IT services,
and consultancies. Those can appear in the vertical category only if they ship a named AI product.

## Category codes

| code | category | definition | examples |
|---|---|---|---|
| FM | Frontier model labs | trains frontier general models, closed weights | OpenAI, Anthropic, DeepMind |
| OM | Open-weight model labs | releases downloadable weights | Meta Llama, Qwen, DeepSeek |
| SLM | Small and edge models | sub-10B, on-device, embedded | Phi, Gemma, SmolLM, MiniCPM |
| IMG | Image generation and editing | diffusion, autoregressive image | Midjourney, FLUX, Ideogram |
| VID | Video generation | text-to-video, avatar, dubbing | Runway, Pika, Sora, HeyGen |
| WM | World models, 3D, spatial | simulation, NeRF, Gaussian splat, robotics sim | World Labs, Decart, Genie |
| AUD | Speech, music, voice | ASR, TTS, voice cloning, music gen | ElevenLabs, Suno, Deepgram |
| CODE | Code AI and coding agents | IDE copilots, autonomous SWE | Cursor, Copilot, Devin, Kiro |
| AGT | Agent harnesses and orchestration | frameworks, runtimes, memory, browser agents | LangChain, CrewAI, E2B, Mem0 |
| INF | Inference, serving, routing | engines, gateways, optimizers | vLLM, SGLang, OpenRouter |
| TRN | Training, fine-tuning, MLOps | distributed training, LoRA, experiment tracking | Unsloth, W&B, MLflow |
| EVAL | Evaluation, observability, guardrails | evals, tracing, safety filters | LangSmith, Lakera, Braintrust |
| DATA | Data, labeling, synthetic data, RLHF | annotation, marketplaces, synthetic | Scale, Surge, Mercor |
| VEC | Vector, retrieval, embeddings, RAG | vector DBs, embedding models | Pinecone, Qdrant, Voyage |
| INFRA | Chips, cloud, neoclouds | GPUs, accelerators, AI cloud | NVIDIA, Cerebras, CoreWeave |
| ROB | Robotics and embodied AI | humanoids, autonomy, drones | Figure, 1X, Waymo, Skild |
| SAFE | Safety, policy, research institutes | alignment, evals, governance | MIRI, METR, UK AISI |
| VERT | Vertical AI applications | health, legal, finance, agri, education | Qure.ai, Harvey, Sarvam |
| CON | Consumer AI assistants and apps | chat apps, companions, search | ChatGPT, Perplexity, Character |
| CRE | Creative and design tools | design, photo, writing, presentation | Canva, Figma, Adobe Firefly |
| DEV | Developer platforms with AI | cloud, devtools, databases adding AI | GitHub, Supabase, Cloudflare |
| HW | AI hardware devices | pins, glasses, recorders, robots-as-product | Humane, Rabbit, Plaud |
| FND | Foundations, communities, open source | nonprofits, foundations, consortiums | Linux Foundation AI, AAIF, EleutherAI |
| REG | Regional ecosystems | national champions and government AI | Sarvam, Krutrim, G42, Naver |

## Geography rule

Every row gets a country or region. `global` means headquarters in one country but the product
and program are worldwide. The regional section repeats a company only when its program is
region-locked, for example a China-only campus ambassador scheme.

## What comes after the list

For every organisation: does a campus, student, ambassador, champion, fellow or community
program exist, is it open on 3 November 2026 or opening soon, and can a student in India apply.
Status vocabulary is in `scope/SCOPE.md`.

## Coverage target

- Tier 1: every organisation in the curated master list, target 400 or more.
- Tier 2: every publisher in the top 1,000 models of 28 Hugging Face pipeline tags, 9,195 names.
- Tier 3: every owner in 22 GitHub AI topics, 4,567 names.
The long tail is in `data/ai-universe.csv` and is a denominator, not a claim of quality.
