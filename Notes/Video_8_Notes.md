# Video 8 Notes — Plan Mode & Ultra Plan Mode in Claude Code
**Claude Code Learning Journey**

---

## 🎯 What This Video Is About
- How to use **Plan Mode** in Claude Code before writing any code
- The full professional workflow: spec → plan → implement → validate → commit → push → PR → merge
- Setting up the database for the Spendly project

---

## 🗂️ What Was Built in This Video
Three things were set up for the database:
1. **Setup tables** — the structure of the database
2. **Fill dummy data** — fake data so the app has something to show
3. **Setup `db.py` file** — reusable functions for the database that future features can use

> This is a **fundamental feature** — once built, it becomes the foundation everything else is built on top of.

---

## 🔁 The Full Professional Workflow Used

This is the complete step-by-step workflow from the video — this is how real development teams work:

```
1. Start new Claude session
2. Rename session → 'database setup'
3. Pull latest code from GitHub
4. Create and switch to a new branch
5. Write the Spec document
6. Review the spec
7. Save spec to .claude/specs/
8. Enter Plan Mode → generate implementation plan
9. Save plan to .claude/plans/
10. Implement the plan
11. Validate against the spec
12. Iterate if needed
13. Commit changes
14. Push branch to GitHub
15. Create Pull Request on GitHub → Merge → Delete branch on GitHub
16. Switch back to main locally
17. Pull latest code (now includes your merged feature)
18. Delete the feature branch locally
```

💡 **Job Tip:** This is called a **feature branch workflow** — it's the standard in almost every professional development team in the world. Learning it now means you'll fit into any team immediately.

---

## 🧠 All Git Commands in This Video — Explained

### Step 1 — Pull the latest code from GitHub
```bash
git pull origin main
```
**What it does:** Downloads any new changes from GitHub onto your local computer.

- `pull` = download and apply
- `origin` = from GitHub
- `main` = from the main branch

> **Analogy:** You're checking if a colleague pushed any new work since you last opened your laptop. If yes, you download it. If no (as in this video), it just says "already up to date."

Not strictly necessary when working alone, but a great habit — especially in teams where others push code while you're away.

---

### Step 2 — Create and switch to a new branch
```bash
git checkout -b feature/database-setup
```
**What is a branch?**
A branch is a **separate copy of your code timeline** where you can make changes freely without touching the main version.

> **Analogy:** Your main branch is the final draft of a book. You photocopy it and write your new chapter on the copy. If the chapter works, you merge it in. If not, you throw the copy away. The original was never touched.

**Breaking down the command:**

| Part | What it means |
|---|---|
| `git checkout` | Switch to a branch |
| `-b` | Create it first, then switch |
| `feature/database-setup` | The name of the new branch |

The `feature/` prefix is a naming convention used by professional teams — it makes the Git history easy to scan.

💡 **Job Tip:** In real teams, `main` is protected. Nobody codes directly on it. Every piece of work — no matter how small — gets its own branch. This keeps the live version of the app always stable.

---

### Step 3 — Stage all changes
```bash
!git add .
```
**What it does:** Selects all changed files and prepares them to be saved (committed).

- `git add` = put files in the box ready to commit
- `.` = everything that changed

> **Analogy:** Packing items into a parcel box before posting. You're choosing what goes in before sealing it.

The `!` prefix means you're running this from inside Claude Code — Claude sees the output too.

---

### Step 4 — Save a checkpoint
```bash
!git commit -m 'create database setup'
```
**What it does:** Saves a permanent checkpoint of your staged changes with a descriptive label.

| Part | What it means |
|---|---|
| `git commit` | Save the checkpoint |
| `-m` | I want to write a message inline |
| `'create database setup'` | The label describing what this commit contains |

💡 **Job Tip:** Clear commit messages are a professional habit. Future you (and your teammates) will thank you when scanning history weeks later.

---

### Step 5 — Push branch to GitHub
```bash
!git push origin feature/database-setup
```
**What it does:** Uploads your branch to GitHub so it exists there too.

| Part | What it means |
|---|---|
| `git push` | Upload to GitHub |
| `origin` | Send it to GitHub (our remote) |
| `feature/database-setup` | Push THIS branch specifically — not main |

---

### Step 6 — Switch back to main
```bash
git checkout main
```
**What it does:** Switches you from the feature branch back to the main branch.

No `-b` needed here — `main` already exists. `-b` is only used when creating a brand new branch.

> **Analogy:** You finished working in the side room. You walk back to the main office. The side room still exists — you're just not in it anymore.

---

### Step 7 — Pull the merged code (important step!)
```bash
git pull origin main
```
After merging your PR on GitHub, your local `main` is behind — it doesn't have the merged changes yet. This command downloads the updated `main` to your computer.

> **Always pull before deleting the branch** — this is the correct order.

---

### Step 8 — Delete the feature branch locally
```bash
git branch -D feature/database-setup
```
**What it does:** Deletes the branch from your computer. The feature is done — the branch has served its purpose.

| Part | What it means |
|---|---|
| `git branch` | Work with branches |
| `-D` | Force delete |
| `feature/database-setup` | The branch to delete |

⚠️ This only deletes it **locally**. The branch on GitHub is deleted separately — either through the GitHub website (after merging the PR, GitHub offers a "Delete branch" button) or via command line.

---

## 🗂️ The `.claude` Folder — Specs & Plans

Two new subfolders were used in this video:

```
.claude/
├── specs/
│   └── 01-database-setup.md    ← the WHAT (requirements)
└── plans/
    └── 01-database-setup.md    ← the HOW (technical plan)
```

**Specs folder** = where your specification documents live (covered in Video 7)
**Plans folder** = where Claude saves the implementation plan it generates in Plan Mode

💡 **Job Tip:** Numbering files (`01-`, `02-`) keeps them in order as the project grows. When you have 20 features, you'll thank yourself for this habit.

---

## 🧠 Plan Mode — What It Is & How It Works

**Plan Mode** is a special mode in Claude Code where Claude **reads and thinks — but cannot write or edit any files.**

It's like putting Claude in "thinking only" mode — it analyses your codebase and spec document and produces a detailed implementation plan before a single line of code is touched.

> **Analogy:** Before a builder breaks ground, the architect draws blueprints. Plan Mode is Claude drawing the blueprints. No bricks are laid yet — just planning.

### How to enter Plan Mode:
- Press **Shift twice**, or
- Use the slash command: `/plan`

### What Claude does in Plan Mode:
1. Reads your spec document
2. Reads relevant existing files (`db.py`, `app.py`, etc.)
3. Thinks through the implementation
4. Generates a step-by-step plan
5. Saves it to `.claude/plans/`

### The prompt used:
```
Read .claude/specs/01-database-setup.md and the existing database/db.py
and app.py, then generate an implementation plan.
Save this plan to .claude/plans/01-database-setup.md
```

---

## ✅ What is "Definitions of Done"?

Before validating, you check the **Definitions of Done** — the list of conditions from your spec that must all be true for the feature to be considered complete.

> **Example:** "App runs without errors" → run `!python app.py` → open the website → if it loads correctly, this condition is met.

This is the **Validate** step from the SDD roadmap (Video 7):
```
Spec → Review → Design → Review → Tasks → Build → Validate ✅
```

---

## 🔀 What is a Pull Request (PR)?

After pushing your branch to GitHub, you create a **Pull Request** — a formal request to merge your branch into `main`.

On GitHub:
1. Go to your repository
2. GitHub notices your new branch and shows a prompt — click **"Compare & pull request"**
3. Add a description if needed
4. Click **"Merge pull request"**
5. Click **"Delete branch"** (GitHub offers this after merging)

> **Analogy:** A Pull Request is like submitting your work for approval before it becomes official. In real teams, colleagues review the code inside the PR and leave comments before approving the merge. It's a quality control step.

💡 **Job Tip:** PRs are one of the most common things you'll encounter in any development job. Even if you're not a developer, understanding what a PR is and why it exists is useful knowledge in any tech-adjacent role.

---

## ⚙️ Good Practices for Plan Mode

### 1. Model Selection
| Task | Best Model | Why |
|---|---|---|
| Planning | **Opus** | Most intelligent, best reasoning |
| Coding/Implementation | **Sonnet** | Fast, efficient, capable enough |

Opus consumes significantly more tokens — use it where it matters (planning) and switch to Sonnet for execution.

### 2. Extended Thinking
Normally Claude replies **token by token** as it generates — quick but shallower for complex problems.

**Extended Thinking** makes Claude do all its reasoning internally first, then reply — like thinking before speaking instead of thinking out loud.

> **Analogy:** Standard mode is like answering a question off the top of your head. Extended thinking is like taking 10 minutes to fully think it through before answering. Slower but much better for complex problems.

**How to enable:** Use `/config` to change the thinking setting before entering Plan Mode.

### 3. Effort Level
Controls how much time and tokens Claude spends thinking. Higher effort = deeper thinking = more token consumption.

**How to set:** Use `/effort` command.

> Start with a balanced setting. Only push effort higher for genuinely complex planning tasks — otherwise you'll burn through your token allowance quickly.

---

## 🧠 Key Takeaways

1. **Always branch before building** — never code directly on `main`
2. **Spec first → Plan → Build → Validate** — the professional sequence
3. **Plan Mode = read only** — Claude thinks and plans, writes nothing
4. **Opus for planning, Sonnet for coding** — use the right model for the right job
5. **Extended thinking** — turn it on for complex planning, off for simple tasks
6. **PR = formal merge request** — standard in all professional teams
7. **Pull before deleting branch** — always get the updated `main` first
8. **The feature branch workflow** — create → code → push → PR → merge → cleanup

---
*Notes from Video 8 | Claude Code Learning Journey*
