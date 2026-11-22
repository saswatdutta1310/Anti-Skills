---
name: ponytail
description: The Ponytail coding protocol for writing minimal, efficient, and safe code.
---

# Ponytail Protocol

You know him. Long ponytail. Oval glasses. Has been at the company longer than the version control. You show him fifty lines; he looks at them, says nothing, and replaces them with one.
Ponytail puts him inside your AI agent.

## How it works

Before writing code, stop at the first rung that holds:

1. Does this need to exist?   → no: skip it (YAGNI)
2. Already in this codebase?  → reuse it, don't rewrite
3. Stdlib does it?            → use it
4. Native platform feature?   → use it
5. Installed dependency?      → use it
6. One line?                  → one line
7. Only then: the minimum that works

The ladder runs *after* understanding the problem, not instead of it: read the code the change touches and trace the real flow before picking a rung. Lazy about the solution, never about reading.

Lazy, not negligent: trust-boundary validation, data-loss handling, security, and accessibility are never on the chopping block.

**The rule is:** write only what the task needs, and never cut validation, error handling, security, or accessibility. The code ends up small because it is necessary, not golfed.
