# Universal Skills Guide: Lifetime Retention & Multi-Project Usage

## 1. Assurance: Skills Are Stored Globally & Permanently

Your skills will **not** be deleted or removed when switching projects.

### Where Skills Live:
All **8,000+ skills** are installed in global user profile directories that are independent of any specific project:
- `C:\Users\VICTUS\.gemini\config\skills\` (Anti-Skills core & global catalog)
- `C:\Users\VICTUS\.gemini\antigravity-cli\skills\` (Antigravity CLI skills)
- `C:\Users\VICTUS\.gemini\skills\` (User-level shared skills)
- `C:\Users\VICTUS\.gemini\config\plugins\` (Domain plugin packs)

Because these directories exist in your Windows User profile (`C:\Users\VICTUS\.gemini\`), **they persist across restarts, system reboots, and any project directory you open**.

---

## 2. How to Use Skills in ANY Project

Whenever you start a project (e.g., in `D:\MyProjects\App`, `C:\workspace\backend`, etc.), Antigravity automatically detects your global skills directory.

### Method A: Natural Language Invocation (Automatic)
You don't need to manually import skills into your repo. Simply mention what you need in your prompt. The agent recognizes matching skills automatically:

- **Security Audits:** *"Perform a red-team review of this authentication flow using hunt-auth-bypass."*
- **Database & Architecture:** *"Design the DB schema using aria and monopoly-patterns."*
- **Frontend / UI:** *"Audit this UI component against accessibility standards using ui-a11y and styleseed."*
- **DevOps / Deployment:** *"Generate a production Dockerfile and Kubernetes manifests using docker-management and k8s-manifest-generator."*

---

### Method B: Finding Any Skill on Demand (`global-skill-finder`)
If you don't know the exact name of a skill for a specific stack or task, run the search script:

```powershell
python C:\Users\VICTUS\.gemini\config\skills\global-skill-finder\scripts\find_skill.py "<keywords>"
```

**Examples:**
```powershell
# Search for PostgreSQL skills:
python C:\Users\VICTUS\.gemini\config\skills\global-skill-finder\scripts\find_skill.py "postgres"

# Search for React/Next.js skills:
python C:\Users\VICTUS\.gemini\config\skills\global-skill-finder\scripts\find_skill.py "nextjs"

# Inspect exact details and path of a skill:
python C:\Users\VICTUS\.gemini\config\skills\global-skill-finder\scripts\find_skill.py --info "nextjs-best-practices"
```

---

### Method C: Enforcing Skills in a Specific Project (`AGENTS.md`)
To make sure an agent always follows specific skills inside a particular project repository:

1. Create or edit an `AGENTS.md` (or `GEMINI.md`) file in the root of your project:
```markdown
# Project Guidelines

## Active Skills & Standards
- Always apply **`super-code-typescript`** and **`nextjs-app-router-patterns`** when modifying frontend code.
- Apply **`tdd-workflow`** before writing new business logic.
- Run **`security-review`** checks on all PR changes.
```
2. When Antigravity opens that workspace, it reads this file automatically and loads the instructions from your global skills storage.

---

## 3. Recommended Safety & Backup Checklist

To ensure your skills never get lost due to disk cleanup or accidental deletion:

1. **Do not run aggressive temp/cleaner tools** on `C:\Users\VICTUS\.gemini\`.
2. **Optional One-Line Backup (Git or Zip):**
   You can periodically back up your configuration and skills directory:
   ```powershell
   Compress-Archive -Path "C:\Users\VICTUS\.gemini\config", "C:\Users\VICTUS\.gemini\skills" -DestinationPath "$HOME\Desktop\gemini_skills_backup.zip" -Force
   ```
3. **MCP Tools Persistence:**
   Your MCP servers (`craft-anything`, `graphify`, `rea`) are registered globally in:
   `C:\Users\VICTUS\.gemini\config\mcp_config.json`
   They remain active across all CLI and GUI sessions.
