# 🚀 Anti-Skills: The Ultimate AI Agent Skill Catalog (2,760+ Skills)

> A production-grade, highly curated collection of 2,760+ specialized engineering skills and workflow instruction modules for **Google Antigravity**, **Claude Code**, **Cursor**, **Codex CLI**, and **OpenAI Agents**.

---

## 🌟 Overview

Skills are modular, progressive instruction sets that transform AI coding assistants into domain experts. Each skill provides precise guidelines, architectural patterns, battle-tested edge cases, and CLI workflows tailored for specific languages, frameworks, cloud platforms, security standards, and business domains.

Whether you need strict test-driven development, deep low-level Rust systems programming, full-stack Next.js 15 architectures, OWASP AppSec hardening, or bioinformatics workflows, Anti-Skills gives your agent the right context at the right time.

---

## ⚡ Key Highlights

- **2,760+ Verified Skills**: Fully validated YAML frontmatter, standardized structure, and UTF-8 encoding.
- **Offline CLI Discovery Engine**: Instant sub-millisecond keyword and token search via `scripts/find_skill.py`.
- **Global Antigravity Integration**: Designed for Antigravity's on-demand skill discovery architecture.
- **Zero Bloat & Dependency-Free**: Pure Markdown and Python standard library for search and orchestration.
- **Granular Workflow Bundles**: Pre-packaged pipelines connecting architecture, development, review, and deployment.

---

## 🔍 Fast Skill Discovery

Search across all 2,760+ skills instantly using the included search tool:

```bash
# General search
python scripts/find_skill.py "fastapi postgres"

# Limit results and search by pack
python scripts/find_skill.py "kubernetes deployment" --top 5

# View detailed skill metadata
python scripts/find_skill.py --info "systematic-debugging"

# List all packs and categories
python scripts/find_skill.py --list-packs
```

---

## 📂 Repository Structure

Each skill lives in its own dedicated directory following standard agent skill anatomy:

```text
Anti-Skills/
├── <skill-name>/            # Individual skill module
│   ├── SKILL.md             # Core skill specification and system instructions (required)
│   ├── scripts/             # Optional automation and utility scripts
│   ├── examples/            # Reference implementations and patterns
│   └── resources/           # Templates, schemas, and checklist assets
├── data/
│   └── skills_index.json    # Complete metadata catalog of all 2,760+ skills
├── scripts/
│   └── find_skill.py        # High-performance search and recommendation engine
├── docs/                    # Architectural guides, audits, and contributor docs
├── workflow_bundles_readme.md # Multi-skill orchestration recipes
└── README.md                # Master catalog documentation
```

---

## 🎯 Skill Categories & Domain Breakdown

Anti-Skills is structured into cohesive domains:

| Domain | Focus Areas | Key Skills |
| :--- | :--- | :--- |
| **Workflow Essentials** | TDD, Root Cause Analysis, Planning, Code Reviews | `test-driven-development`, `systematic-debugging`, `writing-plans`, `code-review-checklist`, `verification-before-completion` |
| **Frontend & Web** | React 19, Next.js 15, Vue 3, Svelte, Angular, Astro | `nextjs-app-router-patterns`, `react-patterns`, `vue-best-practices`, `sveltekit`, `astro` |
| **Styling & Motion** | Tailwind CSS, Three.js, Canvas, GSAP, WebGL | `tailwind-patterns`, `threejs-fundamentals`, `threejs-shaders`, `animejs-animation` |
| **Backend & APIs** | FastAPI, Express, NestJS, Go, Django, GraphQL, gRPC | `fastapi-pro`, `fastapi-router-py`, `nestjs-expert`, `trpc-fullstack`, `api-design-principles` |
| **Systems & Native** | Rust, C++, C#, Java, Go, Swift, Low-level | `systems-programming-rust-project`, `arm-cortex-expert`, `springboot-patterns`, `swift-concurrency-expert` |
| **Autonomous Agents** | Harness Construction, Multi-Agent Swarms, Tool Design | `autonomous-agent-harness`, `agent-orchestrator`, `agent-evaluation`, `subagent-driven-development` |
| **LLM & RAG** | Vector Databases, Embeddings, Context Optimization | `vector-database-engineer`, `vector-index-tuning`, `token-budget-advisor`, `prompt-engineering` |
| **AI Toolkits** | LangChain, LlamaIndex, OpenAI, Anthropic, Gemini, Vercel | `vercel-ai-sdk-expert`, `azure-ai-projects-py`, `ai-engineering-toolkit` |
| **Cloud Infrastructure**| AWS, Azure, GCP, Serverless, CloudFormation | `aws-skills`, `azure-functions`, `aws-serverless`, `azd-deployment` |
| **DevOps & Containers** | Docker, Kubernetes, Terraform, Helm, CI/CD, SRE | `terraform-infrastructure`, `terraform-aws-modules`, `turborepo-caching`, `appdeploy` |
| **AppSec & Hardening** | OWASP Top 10, Auth, Encryption, Secrets, Input Validation | `api-security-best-practices`, `auth-implementation-patterns`, `springboot-security`, `zeroize-audit` |
| **Offensive Security** | Ethical Hacking, Fuzzing, Penetration Testing, STRIDE | `api-fuzzing-bug-bounty`, `sqlmap-database-pentesting`, `wireshark-analysis`, `threat-modeling-expert` |
| **Data & Databases** | PostgreSQL, SQL Optimization, Redis, Kafka, DuckDB | `sql-pro`, `sql-optimization-patterns`, `spark-optimization`, `airflow-dag-patterns` |
| **Mobile Apps** | iOS/SwiftUI, Android Compose, Flutter, React Native | `swiftui-patterns`, `android-jetpack-compose-expert`, `android-clean-architecture`, `upgrading-expo` |
| **QA & Verification** | Playwright, Cypress, Vitest, E2E, Regression | `webapp-testing`, `tdd-orchestrator`, `ui-visual-validator`, `ai-regression-testing` |
| **Automation & SaaS** | Slack, Stripe, Zapier, Webhooks, CRM, Apify | `stripe-integration`, `apify-actor-development`, `telegram-bot-builder`, `zapier-make-patterns` |
| **Documents & Office** | Word (DOCX), Excel (XLSX), PDF, PPTX, LibreOffice | `xlsx-official`, `libreoffice/writer`, `libreoffice/calc`, `pdf-processing` |
| **Creative & Media** | Unity, Unreal Engine, Audio, Video, Image Synthesis | `unity-developer`, `unreal-engine-cpp-pro`, `videodb-skills`, `spline-3d-integration` |
| **Web3 & Blockchain** | Solidity, Ethereum, Smart Contracts, DeFi Protocols | `solidity-security`, `web3-testing`, `smart-contract-auditor` |
| **Product & Growth** | Market Research, Pricing, Metrics, Pitch Decks | `startup-metrics-framework`, `startup-financial-modeling`, `ai-product` |
| **Bio & Science** | Bioinformatics, Genomics, Cheminformatics, Medical | `alphafold-database-fetch-and-analyze`, `uniprot-database`, `chembl-database`, `pdb-database` |

---

## 🛠️ How to Use Skills

### Option 1: Direct Mention in Agent Chats
When working with coding agents (Antigravity, Claude Code, Cursor), invoke any skill by referencing its name:

```markdown
@test-driven-development Write tests for the user authentication service before implementing it.
@fastapi-pro Scaffold a production-grade async router with Pydantic V2 schemas.
@threat-modeling-expert Perform a STRIDE security analysis on our payment processing webhook.
```

### Option 2: Global Installation for Google Antigravity
To make these skills available globally across all your workspaces in Antigravity:
1. Place the skills in your global Antigravity config directory (`~/.gemini/config/plugins/` or `~/.gemini/config/skills/`).
2. Antigravity will discover them automatically via the global rules or `@global-skill-finder` router.

---

## 🤝 Contributing

We welcome additions, fixes, and updates to skill modules!
1. Fork this repository.
2. Create a new branch: `git checkout -b feat/my-new-skill`.
3. Add your skill folder with a complete `SKILL.md` (valid YAML frontmatter with `name` and `description`).
4. Validate the skill: ensure clean UTF-8 encoding without BOM and valid Markdown.
5. Submit a Pull Request.

---

## 📄 License

This repository is distributed under the MIT License. See [LICENSE](LICENSE) or individual skill source attributions for details.
