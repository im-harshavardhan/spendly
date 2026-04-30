import sqlite3

from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash

from database.db import create_user, get_db, get_user_by_email, init_db, seed_db

app = Flask(__name__)
app.secret_key = "dev-secret-key"

with app.app_context():
    init_db()
    seed_db()


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    if session.get("user_id"):
        return redirect(url_for("profile"))
    return render_template("landing.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("user_id"):
        return redirect(url_for("profile"))
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not all([name, email, password, confirm_password]):
            flash("All fields are required.", "error")
            return render_template("register.html")

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return render_template("register.html")

        try:
            create_user(name, email, password)
        except sqlite3.IntegrityError:
            flash("Email already registered.", "error")
            return render_template("register.html")

        flash("Account created! Please sign in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user_id"):
        return redirect(url_for("profile"))
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        user = get_user_by_email(email)
        if not user or not check_password_hash(user["password_hash"], password):
            flash("Invalid email or password.", "error")
            return render_template("login.html")

        session["user_id"] = user["id"]
        session["user_name"] = user["name"]
        return redirect(url_for("profile"))

    return render_template("login.html")


# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
# ------------------------------------------------------------------ #

@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("landing"))


@app.route("/profile")
def profile():
    if not session.get("user_id"):
        return redirect(url_for("login"))

    user = {
        "name": "Harsha Vardhan",
        "email": "demo@spendly.com",
        "initials": "HV",
        "member_since": "01 Jan 2025",
    }

    stats = {
        "total_spent": "₹3,800.00",
        "transaction_count": 8,
        "top_category": "Bills",
    }

    transactions = [
        {"date": "08 Apr 2026", "description": "Lunch with colleagues", "category": "Food",          "amount": "₹180.00"},
        {"date": "08 Apr 2026", "description": "Miscellaneous",          "category": "Other",         "amount": "₹200.00"},
        {"date": "07 Apr 2026", "description": "New earphones",          "category": "Shopping",      "amount": "₹800.00"},
        {"date": "06 Apr 2026", "description": "Movie tickets",          "category": "Entertainment", "amount": "₹500.00"},
        {"date": "05 Apr 2026", "description": "Pharmacy — vitamins",    "category": "Health",        "amount": "₹350.00"},
    ]

    categories = [
        {"name": "Bills",         "amount": "₹1,200.00", "pct": 32},
        {"name": "Shopping",      "amount": "₹800.00",   "pct": 21},
        {"name": "Food",          "amount": "₹630.00",   "pct": 17},
        {"name": "Entertainment", "amount": "₹500.00",   "pct": 13},
        {"name": "Health",        "amount": "₹350.00",   "pct": 9},
        {"name": "Other",         "amount": "₹200.00",   "pct": 5},
        {"name": "Transport",     "amount": "₹120.00",   "pct": 3},
    ]

    return render_template("profile.html", user=user, stats=stats,
                           transactions=transactions, categories=categories)


@app.route("/expenses/add")
def add_expense():
    return "Add expense — coming in Step 7"


@app.route("/expenses/<int:id>/edit")
def edit_expense(id):
    return "Edit expense — coming in Step 8"


@app.route("/expenses/<int:id>/delete")
def delete_expense(id):
    return "Delete expense — coming in Step 9"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
