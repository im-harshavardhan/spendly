# Spec: Login and Logout

## Overview
Implement session-based login and logout for Spendly. The existing `GET /login` stub becomes a full POST handler that validates credentials against the database, stores the authenticated user's ID and name in the session, and redirects to the profile page. The existing `GET /logout` stub clears the session, flashes a success message, and redirects to the landing page. The navbar in `base.html` is updated to conditionally show the logged-in user's name and a Sign out link. Flash messages are updated globally to support categories (`error` / `success`) throughout the app.

## Depends on
- Step 01 — Database setup (`users` table, `get_db()`)
- Step 02 — Registration (`create_user()`, confirmed password hashing with werkzeug)

## Routes
- `GET /login` — render login form — public (already exists as stub, upgrade it)
- `POST /login` — validate credentials, set `session["user_id"]` and `session["user_name"]`, redirect to `url_for("profile")` — public
- `GET /logout` — clear session, flash success, redirect to `url_for("landing")` — public (already exists as stub, upgrade it)

## Database changes
No new tables or columns. Requires one new helper in `database/db.py`:
- `get_user_by_email(email)` — fetches a single row from `users` by email; returns the row as `sqlite3.Row` or `None` if not found.

## Templates
- **Modify**: `templates/login.html`
  - Use `get_flashed_messages(with_categories=true)` and `auth-{{ category }}` class
- **Modify**: `templates/register.html`
  - Use `get_flashed_messages(with_categories=true)` and `auth-{{ category }}` class
- **Modify**: `templates/base.html`
  - Nav shows `{{ session.user_name }}` + Sign out link when `session.user_id` is set
  - Nav shows Sign in + Get started links when no session
  - Global flash message block in `<main>` using `with_categories=true`, class `flash flash-{{ category }}`

## Files to change
- `app.py` — upgrade `login()` and `logout()`; remove `login_required` decorator and `functools`/`abort` imports; add already-logged-in redirects to register and login; use flash categories; `secret_key = "dev-secret-key"`
- `database/db.py` — add `get_user_by_email()`; rename DB to `spendly.db`; use `executescript()` in `init_db()`; remove unused `check_password_hash` import
- `templates/login.html` — flash with categories
- `templates/register.html` — flash with categories
- `templates/base.html` — conditional nav + global flash block
- `static/css/style.css` — add `.auth-success`, `.flash`, `.flash-error`, `.flash-success` styles

## Files to create
None.

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only — never use f-strings in SQL
- Verify passwords with `werkzeug.security.check_password_hash` — never compare plaintext
- Store `session["user_id"]` (integer) and `session["user_name"]` (string) on login
- All flash calls use a category: `flash("message", "error")` or `flash("message", "success")`
- On login failure flash `"Invalid email or password."` with category `"error"`
- After successful login redirect to `url_for("profile")`
- On logout, call `session.clear()`, flash `"You have been logged out."` with `"success"`, redirect to `url_for("landing")`
- Nav uses `session.user_id` (dot notation) in Jinja2; username span uses class `nav-username`; Sign out link has no extra class
- DB file is `spendly.db`
- All templates extend `base.html`
- Use CSS variables — never hardcode hex values
- Use `url_for()` for every internal link

## Definition of done
- [x] `GET /login` renders the login form with email and password fields
- [x] Submitting valid credentials sets `session["user_id"]` and `session["user_name"]` and redirects to `/profile`
- [x] Submitting with a wrong password shows "Invalid email or password." flash and stays on login
- [x] Submitting with an unregistered email shows the same generic error flash
- [x] `GET /logout` clears the session, flashes success, and redirects to `/`
- [x] After logout, `session["user_id"]` is no longer present
- [x] Navbar shows `session.user_name` + Sign out when logged in
- [x] Navbar shows Sign in + Get started when logged out
- [x] Flash messages display with correct styling for `error` and `success` categories
- [x] Already-logged-in users visiting `/login` or `/register` are redirected to `/profile`
