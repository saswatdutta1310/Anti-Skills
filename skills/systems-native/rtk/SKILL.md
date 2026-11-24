---
name: rtk
description: Rust Token Killer (RTK) CLI proxy for compressing command output and minimizing LLM context tokens when executing bash/terminal commands.
---

# RTK (Rust Token Killer)


tk is a high-performance CLI proxy that drastically reduces LLM token consumption by filtering and compressing terminal command outputs (e.g., git, pnpm, cargo, docker, kubectl, vitest, test suites) before the agent reads them.

## When to Use

- Use 
tk when running verbose terminal commands:
  - 
tk git status, 
tk git diff, 
tk git log
  - 
tk cargo test, 
tk cargo build
  - 
tk pnpm test, 
tk npm test
  - 
tk docker ps, 
tk kubectl get pods
- Check token savings at any time:
  - 
tk gain
- Inspect raw uncompressed output if needed:
  - Add --raw or run the underlying command directly without 
tk.
