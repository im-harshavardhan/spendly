# Video 3 Notes — Slash Commands, Sessions & Models in Claude Code

---

## 1. Slash Commands

Shortcuts starting with `/` that trigger actions instantly — no need to write a full prompt.

- **Built-in commands** — come with Claude Code
- **Custom commands** — ones you create yourself

**💡 Pro tip:** Custom commands are a big deal in real work. For example, you could create a command like `/review` that automatically checks your code for bugs before committing. As you grow, learning to build custom commands will make you stand out.

---

## 2. Sessions

A session = one conversation with Claude Code, from `claude` to `/exit`.

Each session has a unique ID, saves your full message history, file reads, tool results, and working directory. Sessions are auto-saved to `~/.claude/projects/` and can be resumed anytime.

**💡 Think of it like this:** A session is like a meeting with a colleague. You discuss one topic, take notes (history), and when the meeting ends, the notes are saved. Next time you meet, you can pull up old notes and continue.

---

## 3. Best Practices

- **New session for every new task** — keeps things clean, won't mix up different tasks
- **Name your session immediately** — AI-generated names are based on your first question and usually aren't helpful. Use `/rename` to give it a clear name
- **Commit at milestones** — when you achieve something within a session, commit it with git
- **Use /btw for quick side questions** — if you have a random doubt while Claude is working on something, `/btw` answers it without polluting your conversation history
- **Export before big refactors** — `/export` saves the session to your project directory. You can later give this as context when making big changes

**💡 Why these matter for jobs:**
- Naming sessions and committing frequently shows **professional discipline**. In companies, messy git history and unnamed sessions make collaboration hard. Senior developers notice these habits.
- Frequent commits are a real workplace expectation. Don't build 10 features and commit once. Commit after each small working change. This way, if something breaks, you only lose a small amount of work.
- The `/btw` habit is underrated. In real projects, context pollution (mixing unrelated topics) confuses AI tools and wastes tokens. Clean history = better AI responses.

---

## 4. Command Reference

| Command | What it does |
|---|---|
| `/exit` | End the current session |
| `claude -r` | Resume a past conversation (from terminal) |
| `/resume` | Resume an old session (from inside Claude Code) |
| `/rename` | Rename your session (e.g. `/rename login-feature`) |
| `/btw` | Ask a quick side question without affecting history |
| `/export` | Save session to your project directory |
| `/login` | Sign in with your Anthropic account |
| `/logout` | Log out from your account |
| `/model` | Switch between models |
| `/usage` | See token usage for session and week |
| `/extra-usage` | Get more tokens if you've run out |
| `/stats` | Claude Code usage statistics |
| `/insights` | Generate a report analysing your usage |
| `/config` | Change Claude Code configurations |
| `/permission` | Allow or deny tool access (file read/write, bash, etc.) |
| `/theme` | Change the theme |
| `/voice` | Turn on voice mode |

**💡 Commands you'll use most often:** `/exit`, `/rename`, `/model`, `/usage`, and `/btw`. Focus on getting comfortable with these first. The others are situational.

---

## 5. Models in Claude Code

| Model | Strengths | Best for | Cost |
|---|---|---|---|
| **Opus** | Most powerful, deepest reasoning | Complex architecture, planning, specs | Most expensive |
| **Sonnet** | Great balance of speed and quality | Everyday coding (default for most users) | Moderate |
| **Haiku** | Fastest | Simple, repetitive, or exploratory tasks | Cheapest |

**Power-user tip from the video:** Use Opus for planning and architecture decisions, then switch to Sonnet for the actual code implementation. This saves tokens while keeping quality high.

**💡 My additions on models:**
- **Don't use Opus for everything** thinking it'll give better results. For straightforward tasks like "add a button to this page," Sonnet is equally good and much cheaper. Opus shines when the task requires deep thinking — like designing a database structure or debugging a complex issue.
- **Haiku is great for learning.** When you're just asking "what does this function do?" or "explain this error," use Haiku. Save your expensive tokens for actual building.
- **Token awareness is a real job skill.** Companies that use AI tools care about costs. A developer who uses 10x more tokens than needed because they use Opus for everything is wasting company money. Being smart about model selection will be valued.

---

## 6. Permissions

Claude Code may need access to tools like reading files, writing files, or running terminal commands. By default it asks permission each time. Using `/permission`, you can pre-approve tools so it stops asking repeatedly.

**💡 Be careful here:** When you're learning, it's actually good to let Claude ask for permission each time. You'll see exactly what it's doing — which files it's reading, what commands it's running. This teaches you how things work behind the scenes. Once you're comfortable and trust the workflow, then start pre-approving.

---

## 7. Small Corrections & Clarifications

- **"claude -r" vs "/resume":** You run `claude -r` in your regular terminal BEFORE entering Claude Code. Once you're already inside Claude Code, you use `/resume` instead. They do similar things but from different places.
- **Session naming tip:** Your notes had `/rename intro session`. Better practice is to use short, descriptive names without spaces, like `/rename intro-session` or `/rename expense-tracker-setup`. This matches how developers name things — no spaces, use hyphens.
- **Refactoring** (you wrote "refactoring" in your notes — just making sure you understand the term): It means restructuring existing code without changing what it does. Like rewriting a messy paragraph to be cleaner, but keeping the same meaning. Very common term in developer interviews.

---

*Notes from Claude Code playlist — Video 3*
