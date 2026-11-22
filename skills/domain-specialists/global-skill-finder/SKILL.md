---
name: global-skill-finder
description: >-
  Search and load any of the 2,700+ globally installed skills across all domain
  plugins on demand. Use whenever a task touches a specialized framework,
  language, cloud/DevOps tool, security audit, document format, integration,
  game/3D engine, or workflow not already loaded in active skills.
---

# Global Skill Finder (2,700+ Installed Skills)

All skills on this machine are installed globally in domain plugin packs under
`C:\Users\VICTUS\.gemini\config\plugins\skills-*\skills\`. Only `skills-essentials`
is active by default to keep your context fast and prevent prompt/truncation
bloat; the other domain packs are toggleable in Customizations and **always
searchable on demand** via this skill.

## How to Search and Load Any Skill

1. **Search the global index** (fast, zero external dependencies):
   ```powershell
   python C:\Users\VICTUS\.gemini\config\skills\global-skill-finder\scripts\find_skill.py "<keywords>" --top 8
   ```
   Optional filters:
   - `--pack <pack-name>` (e.g., `--pack skills-web-frontend`)
   - `--list-packs` (show all domain plugin packs and skill counts)
   - `--info <slug>` (show full metadata and exact path for a skill)

2. **Read the best match's `SKILL.md`** using `read_file` on the printed path.
   - Check if that skill directory also has `references/` or `scripts/` and read
     relevant sections when executing complex workflows.

3. **Suggest enabling a pack for heavy sessions** (optional):
   - If the user is doing sustained work in one domain (e.g., Kubernetes or
     React/Next.js), tell them they can toggle that plugin pack on in
     Antigravity's Customizations page (`[Pack Name](customization://<pack-dir>)`)
     so its skills appear directly in `@skill` autocomplete.
