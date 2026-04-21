# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Activate virtual environment (Windows Git Bash)
source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Run the development server (http://localhost:5001, debug mode on)
python app.py

# Run tests
pytest
pytest -v                        # verbose
pytest tests/test_file.py        # single file
```

## Architecture
**Spendly** is a personal expense tracker built with Flask + SQLite + Jinja2 + vanilla JS.

All routes are defined in `app.py` (single file). The app currently has landing, auth, terms, and privacy pages fully implemented; expense CRUD routes (`/expenses/*`) and `/profile` are stubs pending future implementation steps.

**Key files:**
- `app.py` — Flask app, all 10 routes
- `database/db.py` — SQLite layer stub; expects `get_db()`, `init_db()`, `seed_db()` to be implemented
- `templates/base.html` — master Jinja2 template (blocks: `title`, `head`, `content`, `scripts`)
- `static/css/style.css` — design system using CSS custom properties (`--ink-*`, `--accent`, `--accent-2`, `--paper-*`)
- `static/js/main.js` — YouTube modal handler for the landing page

**Data flow (planned):** User registers/logs in → Flask validates + stores in SQLite → authenticated routes unlock expense CRUD → expenses stored and filtered by category/date.

**Currency:** Indian Rupee (₹).

**Database:** SQLite file (`expense_tracker.db`) is gitignored and not yet initialized. The `database/db.py` stub should set up the connection with row factory and foreign keys enabled.
