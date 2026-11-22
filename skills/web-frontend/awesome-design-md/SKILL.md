---
name: awesome-design-md
description: "A curated collection of 60+ premium DESIGN.md templates inspired by top-tier developer-focused websites (Stripe, Linear, Vercel, etc.). Use to apply high-end aesthetics to your project."
risk: safe
source: "https://github.com/VoltAgent/awesome-design-md"
date_added: "2026-04-21"
---

# Awesome DESIGN.md Skill

This skill provides access to a curated collection of `DESIGN.md` files extracted from popular, well-designed websites. These files capture a site's complete visual language in a format that AI agents (like me) and Google Stitch can read to generate consistent, pixel-perfect UI.

## When to Use This Skill

Use this skill when:
- You want to apply a specific "look and feel" to a project (e.g., "Make it look like Linear").
- You are starting a new project and need a premium design system baseline.
- You want to browse high-quality design tokens and layout principles for inspiration.

## Available Design Templates

The collection includes 60+ templates across several categories:

### AI & LLM Platforms
- **Claude**: Warm terracotta accent, clean editorial layout.
- **Mistral AI**: French-engineered minimalism, purple-toned.
- **Ollama**: Terminal-first, monochrome simplicity.
- **OpenCode AI**: Developer-centric dark theme.
- **Replicate**: Clean white canvas, code-forward.
- **Together AI**: Technical, blueprint-style design.
- **xAI**: Stark monochrome, futuristic minimalism.

### Developer Tools & IDEs
- **Cursor**: AI-first code editor. Sleek dark interface, gradient accents.
- **Expo**: Dark theme, tight letter-spacing, code-centric.
- **Raycast**: Productivity launcher. Sleek dark chrome, vibrant gradient accents.
- **Vercel**: Black and white precision, Geist font.
- **Warp**: Dark IDE-like interface, block-based command UI.

### Fintech & Crypto
- **Coinbase**: Clean blue identity, trust-focused.
- **Revolut**: Sleek dark interface, fintech precision.
- **Stripe**: Signature purple gradients, weight-300 elegance.
- **Wise**: Bright green accent, friendly and clear.

### Productivity & SaaS
- **Linear**: Ultra-minimal, precise, purple accent.
- **Notion**: Warm minimalism, soft surfaces.
- **Resend**: Minimal dark theme, monospace accents.

### Brands & Others
- **Apple**: Premium white space, SF Pro, cinematic imagery.
- **Nike**: Monochrome UI, massive uppercase Futura.
- **Tesla**: Radical subtraction, cinematic photography.
- **SpaceX**: Stark black and white, futuristic.

## How to Use a Template

1. **Browse**: Look through the list above or explore the `design-md/` directory in this skill.
2. **Apply**: To use a template, copy the `DESIGN.md` from the corresponding directory to your project root.

### Example: Applying the Linear Design System
```bash
cp [skill_path]/design-md/linear.app/DESIGN.md ./DESIGN.md
```

Once copied, tell me: "Use the DESIGN.md in the root to build my next screens." I will then align all subsequent code generation with that design system.

## Integration with Stitch
These files follow the official Google Stitch `DESIGN.md` format. When you have a `DESIGN.md` file in your root, Stitch MCP tools will automatically respect these design tokens when generating or editing screens.

## Related Skills
- `design-md`: Analyze and create your own `DESIGN.md` files.
- `stitch-loop`: Iteratively build websites using Stitch.
