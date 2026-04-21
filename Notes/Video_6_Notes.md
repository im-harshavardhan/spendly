# Video 6 Notes — CLAUDE.md: The Most Important File
**Claude Code Learning Journey**

---

## 🎯 Topics Covered
- What CLAUDE.md is and why it exists
- How to create it using `/init`
- What to put inside it
- The `.claude` folder and its types
- Types of CLAUDE.md files
- Auto Memory

---

## 🧠 Why CLAUDE.md Exists — The Problem It Solves

**LLMs have no memory.** Every time you start a new Claude Code session, Claude remembers nothing from before.

This means without CLAUDE.md, you'd have to repeatedly tell Claude:
- How your project is structured
- What libraries you're using
- What coding conventions to follow
- How to run/build/test the project

Repeating this every session is:
- ❌ Cumbersome
- ❌ Easy to forget things
- ❌ Leads to inconsistent code generation

> **Analogy:** Imagine hiring a contractor who forgets everything about your house every morning. You'd have to re-explain the floor plan, materials used, and house rules every single day. CLAUDE.md is the permanent briefing document you hand them so they're always up to speed.

**CLAUDE.md** is a special project-level instruction file that Claude Code automatically reads at the start of every session.

> Think of it as a **persistent system prompt for your project.**

💡 **Job Tip:** In real teams, onboarding documents exist for the same reason — so new developers (or forgetful ones) don't have to ask basic questions every day. CLAUDE.md is that document for Claude.

---

## 📝 Creating CLAUDE.md

### Important: Always use capital letters → `CLAUDE.md`

### Option 1 — Use `/init` (Recommended starting point)

Run this inside Claude Code:
```
/init
```

**What `/init` does internally:**
1. Triggers an internal agent that takes over scanning
2. Scans high-signal config files first — `package.json`, `requirements.txt`, `Makefile`, `README.md`
3. Reads the full directory/folder structure
4. Infers tech stack, folder layout, and naming conventions
5. Writes a `CLAUDE.md` to the project root automatically

### When `/init` is especially useful:

| Situation | Why `/init` helps |
|---|---|
| Onboarding an existing codebase you didn't write | Faster than reading everything yourself |
| Large repos with many files | Claude spots patterns you might forget to document |
| You're new to CLAUDE.md | Good way to see what the format looks like |
| Quick prototypes | Don't want to invest time writing docs |

### ⚠️ Important Reality Check:
> The generated CLAUDE.md is roughly **30% useful**.
> The remaining **70%** — workflows, constraints, what to avoid, deployment targets, naming conventions — **you have to write yourself.**

💡 **Job Tip:** `/init` gives you a solid starting skeleton. Your job is to fill in the parts Claude couldn't infer — the *why*, the *don'ts*, and the *team conventions*.

---

## 🗂️ Ideal CLAUDE.md Structure

### 1. Project Context
A short description so Claude immediately understands what it's working on.
```
This is a FastAPI backend for a health-tracking application
that stores patient BMI records and exposes CRUD APIs.
```

---

### 2. Architecture
Explains how the codebase is structured and where things belong.
```
- Routes live in `routers/`
- Business logic lives in `services/`
- Schemas live in `schemas/`
- Persistence logic lives in `repository/`
```

> **Why this matters:** Without this, Claude might put code in the wrong folder, breaking the team's structure.

---

### 3. Code Style
Tells Claude how code should look and what conventions to follow.
```
- Use Python type hints everywhere
- Prefer Pydantic models for request and response schemas
- Keep functions small and focused
```

---

### 4. Preferred Libraries
Constrains what tools/frameworks should be used — and critically, what NOT to add.
```
- Use FastAPI for APIs
- Use Pydantic for validation
- Use SQLAlchemy for ORM
- Do not introduce new dependencies unless necessary
```

💡 **Job Tip:** The line *"do not introduce new dependencies"* is critical in real teams. Adding a random library without discussion can break other people's work or violate company policy.

---

### 5. Commands
Lists exact commands for running, testing, and maintaining the project.
```
- Install dependencies: pip install -r requirements.txt
- Run dev server: uvicorn main:app --reload
- Run tests: pytest
```

---

### 6. Critical Rules
Highlights warnings, edge cases, and things Claude must never do.
```
- Do not modify `database.py` unless absolutely necessary
- Patient IDs are provided by the client; do not auto-generate UUIDs
```

💡 **Job Tip:** Critical rules prevent Claude from confidently doing the wrong thing. In real projects, some files are sacred — touching them breaks everything. Document those here.

---

## 📁 The `.claude` Folder — Claude Code's Toolbox

The `.claude` folder is Claude Code's **local configuration directory**. It stores all config-related info about skills, custom slash commands, sub-agents, and more.

### Two Types:

| | Project-level `.claude/` | Global `~/.claude/` |
|---|---|---|
| **Location** | Inside your project folder | Your home directory (`~/`) |
| **Scope** | This project only | Every project on your machine |
| **Shared with team?** | ✅ Yes — lives in the repo | ❌ No — only on your machine |
| **Use for** | Project-specific commands, workflows | Personal commands you want everywhere |

> **Analogy:** Project-level is like the rules pinned on an office noticeboard — everyone on the team sees them. Global is like your personal notebook that travels with you to every job.

---

## 📄 Types of CLAUDE.md Files

### 1. Project Root → `./CLAUDE.md`
The main file. Lives at the top of your project. Claude reads this automatically every session.

---

### 2. Inside `.claude` folder → `./.claude/CLAUDE.md`
Claude understands the file no matter the location — whether it's in the project root or inside the `.claude` folder at project or user level.

---

### 3. Local/Personal → `./CLAUDE.local.md`
- Lives in your project root
- Claude reads it alongside the main `CLAUDE.md`
- **Automatically gitignored** — your personal tweaks never get shared with the team
- Use for personal preferences that only apply to you

---

### 4. Global → `~/.claude/CLAUDE.md`
- Your personal preferences that apply **across all projects**
- Things like your coding style defaults, preferred tools, general working style
- Available in every project on your machine

---

### 5. Subdirectory → `./some/folder/CLAUDE.md`
- Claude Code starts from the current directory and reads upward
- Useful for **large repositories** where different sections have different rules
- Each subfolder can have its own CLAUDE.md with specific instructions

---

## ✅ Good Practices for CLAUDE.md

| Practice | Why |
|---|---|
| Start with `/init`, then prune aggressively | Remove noise, add what matters |
| Commit it to Git | Team shares the same context |
| Only include universally applicable things | Don't put feature-specific details in the global file |
| Use emphasis sparingly for critical rules | If everything is IMPORTANT, nothing is |
| Keep it under 200–300 lines | More instructions = worse instruction-following |
| Ask: *"Would removing this cause Claude to make mistakes?"* | If no → cut it |

---

## 📂 When CLAUDE.md Gets Too Big — Split It

If your CLAUDE.md grows too large, split it into separate files inside `.claude/rules/`:

**Before (one big file):**
```
# CLAUDE.md
## Code style — 20 lines
## Testing — 20 lines
## Security — 20 lines
## API conventions — 20 lines
```

**After (split into separate files):**
```
.claude/rules/
├── code-style.md
├── testing.md
├── security.md
└── api-conventions.md
```

**Key difference:** Files in `.claude/rules/` are **NOT loaded automatically**. Claude only loads them when they're relevant to the current task — saving context and improving focus.

Then in your main CLAUDE.md, reference them:
```markdown
## API Conventions
See @docs/api-guidelines.md

## Git Workflow
See @docs/contributing.md
```

💡 **Job Tip:** The `@` import trick works here too — same concept as directing Claude to a file in prompts. Keeps the main file lean while the detail lives elsewhere.

---

## 🧠 Concept: What is `~/` (Tilde)?

You'll see `~/.claude/` mentioned above.

`~/` means your **home directory** — the personal folder on your computer that belongs to you.

- On Windows: `C:\Users\YourName\`
- On Mac/Linux: `/Users/YourName/` or `/home/YourName/`

So `~/.claude/` = a hidden folder in your personal area that stores your global Claude settings.

---

## 🔄 Treat CLAUDE.md as a Living Document

Don't try to write the perfect CLAUDE.md upfront. Build it organically:

> **Correct once, then codify.**

If Claude makes a mistake (wrong naming convention, wrong folder), correct it in the session — then add that rule to CLAUDE.md so it never happens again.

Also **audit it periodically** — instructions drift over time as projects evolve.

---

## 🧠 Auto Memory — Claude Remembering Project Insights

**Auto Memory** is a persistent directory where Claude records learnings, patterns, and insights as it works — across sessions.

### How it works:
When Claude discovers something about your project mid-session (e.g. *"this app uses INR instead of USD"*), it saves that to auto-memory. Next session, it already knows — no need to repeat yourself.

### Where it lives:
```
~/.claude/projects/<project-name>/memory/
```

### Difference from CLAUDE.md:

| | CLAUDE.md | Auto Memory |
|---|---|---|
| Written by | You | Claude (automatically) |
| Purpose | Your instructions to Claude | Claude's own discovered learnings |
| Location | Your project folder | `~/.claude/projects/` |
| Shared with team | Yes (if committed) | No — personal to your machine |

> **Analogy:** CLAUDE.md is the briefing document **you** give Claude. Auto Memory is Claude's own personal notebook where it jots things down as it learns your project.

---

## 🧠 Key Takeaways

1. **CLAUDE.md = persistent memory** — Claude reads it automatically every session
2. **`/init` gives you 30%** — the rest you write yourself
3. **Project `.claude/` = team shared | Global `~/.claude/` = personal**
4. **Keep CLAUDE.md under 300 lines** — quality drops as length increases
5. **Split big files** into `.claude/rules/` — loaded on demand, not always
6. **Auto Memory** = Claude's own notes about your project, saved automatically
7. **Treat it as a living document** — correct once, codify, audit regularly

---
*Notes from Video 6 | Claude Code Learning Journey*
