# Video 2 Notes — Setting Up Claude Code & Git Basics

---

## 1. Installing Claude Code
- Go to Claude Code website → copy the install command → paste in Command Prompt → done
- To verify: open CMD → type `claude` → if it responds, it's installed

---

## 2. Working on a Project
- Download the project zip → extract it → open folder in VS Code → open terminal → type `claude`
- **Why not build from scratch?** In real jobs, you join projects midway. This simulates that.

---

## 3. Virtual Environment

**What:** A private room for your project's packages — keeps them separate from other projects.

**Why:** Different projects may need different versions of the same package. Without it, they'd clash.

**How:**
```
python -m venv venv          ← creates the environment
venv\Scripts\activate.bat    ← activates it (steps into the room)
```

**Creating = building the room. Activating = walking into it.**  
If you don't activate, packages install globally instead of in your project.

---

## 4. Installing Dependencies
```
pip install -r requirements.txt
```
- `requirements.txt` = a shopping list of all packages the project needs
- **Always activate your virtual environment first**, then install

**Full setup flow:** Create venv → Activate → Install dependencies

---

## 5. Running the Project
```
python app.py
```
- Opens a local server at `http://127.0.0.1:5001/`
- This runs only on YOUR computer — not on the internet
- Open this URL in your browser to see the website

---

## 6. Git & GitHub

### What is Git?
A "save game" system for code. Every save (called a **commit**) is a snapshot of your entire project. You can go back to any snapshot anytime.

### What is GitHub?
Online storage for your Git saves. Like Google Drive but for code.

### Git Commands — Step by Step

| Command | What it does | Analogy |
|---|---|---|
| `git init` | Start tracking this folder | Installing a camera in a room |
| `git add .` | Select all files for next save | Packing items into a box |
| `git commit -m "message"` | Save with a label | Sealing the box with a label |
| `git remote add origin URL` | Connect to GitHub | Saving a contact in your phone |
| `git branch -m master main` | Rename branch to match GitHub | Just a naming fix |
| `git push origin main` | Upload to GitHub | Sending the box to storage |

### Daily workflow (repeat these 3):
```
git add .                        ← select changed files
git commit -m "what I changed"   ← save locally
git push origin main             ← upload to GitHub
```

---

## 7. Using Claude Code in Projects (Bash Mode)
Instead of switching between terminals, run everything inside Claude's chat using `!` before commands. Claude sees your files, commands, and errors — so it has full context to help.

Example questions you can ask Claude:
- "What does this project do?"
- "What tech stack does this project use?"
- "Explain the project structure to me"

---

## 8. Errors I Faced & Fixes

### Error: "Running scripts is disabled on this system"
**When:** Trying to activate virtual environment in PowerShell  
**Why:** Windows blocks scripts by default for security  
**Fix (choose one):**
- Run in PowerShell: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
- OR switch to Command Prompt in VS Code (dropdown next to + button) and use `venv\Scripts\activate.bat` instead

### Error: Git "safe directory" warning
**When:** Running `git init`  
**Why:** Git couldn't verify folder ownership on Windows  
**Fix:** `git config --global --add safe.directory D:/your/project/path`

### Error: "Author identity unknown"
**When:** Running `git commit`  
**Why:** Git needs to know who is making saves  
**Fix (one time):**
```
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### Warning: "LF will be replaced by CRLF"
**When:** Running `git add .`  
**Why:** Windows and Linux use different invisible line-ending characters  
**Fix:** Ignore it. Completely harmless.

---

*Notes from Claude Code playlist — Video 2*
