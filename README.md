# 🚀 Anti-Skills: The Ultimate AI Agent Skill Catalog (2,760+ Skills)

> A production-grade, highly curated collection of 2,760+ specialized engineering skills and workflow instruction modules for **Google Antigravity**, **Claude Code**, **Cursor**, **Codex CLI**, and **OpenAI Agents**.

---

## 🌟 Overview

Skills are modular, progressive instruction sets that transform AI coding assistants into domain experts. Each skill provides precise guidelines, architectural patterns, battle-tested edge cases, and CLI workflows tailored for specific languages, frameworks, cloud platforms, security standards, and business domains.

Anti-Skills organizes all 2,760+ skills into **17 clean domain categories** to ensure full browsability, zero truncation on GitHub, and sub-millisecond local CLI search.

---

## ⚡ Key Highlights

- **2,760+ Verified Skills**: Fully validated YAML frontmatter, standardized structure, and UTF-8 encoding.
- **Categorized Zero-Truncation Layout**: Structured across 17 domain folders with zero GitHub 1,000-file directory truncation.
- **Offline CLI Discovery Engine**: Instant sub-millisecond keyword and token search via `scripts/find_skill.py`.
- **Global Antigravity Integration**: Designed for Antigravity's on-demand skill discovery architecture.
- **Zero Bloat & Dependency-Free**: Pure Markdown and Python standard library for search and orchestration.
- **Granular Workflow Bundles**: Pre-packaged pipelines connecting architecture, development, review, and deployment.

---

## 🔍 Fast Skill Discovery

Search across all 2,760+ skills instantly using the included search tool:

```bash
# General keyword search
python scripts/find_skill.py "fastapi postgres"

# Limit results and search by category
python scripts/find_skill.py "kubernetes deployment" --top 5

# View detailed skill metadata and path
python scripts/find_skill.py --info "systematic-debugging"

# List all categories and skill counts
python scripts/find_skill.py --list-categories
```

---

## 📂 Repository Structure

The repository is organized by domain categories:

```text
Anti-Skills/
├── skills/                  # Categorized skill collections (17 domains)
│   ├── ai-agents/           # Autonomous agent harnesses, multi-agent orchestration (427 skills)
│   ├── automation-integrations/ # Slack, Discord, Stripe, Zapier, Webhooks (171 skills)
│   ├── backend-apis/        # FastAPI, Express, NestJS, Go, Django, GraphQL (228 skills)
│   ├── blockchain-web3/     # Solidity, Ethereum, Smart Contracts, DeFi (24 skills)
│   ├── cloud-devops/        # AWS, Azure, GCP, Docker, Kubernetes, Terraform (336 skills)
│   ├── databases-data/      # PostgreSQL, MySQL, Redis, Kafka, ETL, Spark (101 skills)
│   ├── docs-office/         # Word, Excel, PDF, PPTX, LibreOffice, Technical Writing (125 skills)
│   ├── domain-specialists/  # Advisory personas and domain consulting (15 skills)
│   ├── essentials/          # TDD, Root Cause Debugging, Planning, Code Reviews (16 skills)
│   ├── gamedev-creative/    # Unity, Unreal Engine, Audio, Video, 3D Web (73 skills)
│   ├── health-science/      # Bioinformatics, Genomics, Cheminformatics, Medical (154 skills)
│   ├── mobile-apps/         # iOS/SwiftUI, Android Compose, Flutter, React Native (63 skills)
│   ├── product-marketing/   # Strategy, Business Models, Pricing, Growth SEO (227 skills)
│   ├── security-pentest/    # AppSec, OWASP, Penetration Testing, Hardening (286 skills)
│   ├── systems-native/      # Rust, C++, C#, Java, Go, Low-Level Systems (175 skills)
│   ├── testing-qa/          # Playwright, Cypress, Vitest, E2E, Regression (103 skills)
│   └── web-frontend/        # React 19, Next.js 15, Vue 3, Svelte, Tailwind (245 skills)
├── data/
│   └── skills_index.json    # Complete metadata catalog of all 2,760+ skills
├── scripts/
│   └── find_skill.py        # High-performance search and recommendation engine
├── docs/                    # Architectural guides, audits, and contributor docs
├── workflow_bundles_readme.md # Multi-skill orchestration recipes
└── README.md                # Master catalog documentation
```

---

## 🎯 Domain Directory Quick Links

Browse individual skills directly by clicking any category below:

| Domain Category | Directory Link | Skills | Focus Areas & Key Highlights |
| :--- | :--- | :---: | :--- |
| **Workflow Essentials** | [`skills/essentials/`](skills/essentials/) | 16 | TDD, Root Cause Analysis, Planning, Code Reviews, Verification |
| **AI & Autonomous Agents** | [`skills/ai-agents/`](skills/ai-agents/) | 427 | Agent harnesses, multi-agent swarms, loops, introspection |
| **Cloud & DevOps** | [`skills/cloud-devops/`](skills/cloud-devops/) | 336 | AWS, Azure, GCP, Docker, Kubernetes, Terraform, CI/CD, SRE |
| **Security & Pentesting** | [`skills/security-pentest/`](skills/security-pentest/) | 286 | AppSec, OWASP Top 10, penetration testing, threat modeling |
| **Web & Frontend** | [`skills/web-frontend/`](skills/web-frontend/) | 245 | React 19, Next.js 15, Vue 3, Svelte, Tailwind CSS, Three.js |
| **Backend & APIs** | [`skills/backend-apis/`](skills/backend-apis/) | 228 | FastAPI, Express, NestJS, Go, Django, GraphQL, REST, gRPC |
| **Product & Marketing** | [`skills/product-marketing/`](skills/product-marketing/) | 227 | Startup metrics, financial models, pricing strategy, growth SEO |
| **Systems & Native** | [`skills/systems-native/`](skills/systems-native/) | 175 | Rust, C++, C#, Java, Go, low-level architecture, ARM |
| **Automation & Integrations** | [`skills/automation-integrations/`](skills/automation-integrations/) | 171 | Slack, Discord, Stripe, Zapier, Make, SaaS webhooks |
| **Health, Bio & Science** | [`skills/health-science/`](skills/health-science/) | 154 | AlphaFold, UniProt, ChEMBL, PDB, BLAST, Genomics, Med |
| **Documents & Office** | [`skills/docs-office/`](skills/docs-office/) | 125 | DOCX, XLSX, PDF, PPTX, LibreOffice (Writer, Calc, Impress) |
| **Testing & QA** | [`skills/testing-qa/`](skills/testing-qa/) | 103 | Playwright, Cypress, Vitest, unit tests, visual validation |
| **Databases & Data** | [`skills/databases-data/`](skills/databases-data/) | 101 | PostgreSQL, SQL optimization, Redis, Kafka, DuckDB, Spark |
| **Creative & GameDev** | [`skills/gamedev-creative/`](skills/gamedev-creative/) | 73 | Unity, Unreal Engine, Audio/Video, Spline 3D, Design |
| **Mobile Applications** | [`skills/mobile-apps/`](skills/mobile-apps/) | 63 | iOS/SwiftUI, Android Compose, Flutter, React Native, Expo |
| **Blockchain & Web3** | [`skills/blockchain-web3/`](skills/blockchain-web3/) | 24 | Solidity, Web3, Smart Contracts, DeFi Protocols |
| **Domain Specialists** | [`skills/domain-specialists/`](skills/domain-specialists/) | 15 | Expert personas, strategy consultants, specialized advisors |

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
3. Add your skill folder under the appropriate domain directory in `skills/<category>/<skill-name>/` with a complete `SKILL.md` (valid YAML frontmatter with `name` and `description`).
4. Validate the skill: ensure clean UTF-8 encoding without BOM and valid Markdown.
5. Submit a Pull Request.

---

## 📄 License

This repository is distributed under the MIT License. See [LICENSE](LICENSE) or individual skill source attributions for details.
