import sqlite3

import pytest
from werkzeug.security import generate_password_hash

from database.db import get_db
from database.queries import (
    get_category_breakdown,
    get_recent_transactions,
    get_summary_stats,
    get_user_by_id,
)


# ------------------------------------------------------------------ #
# In-memory DB fixture                                                #
# ------------------------------------------------------------------ #

@pytest.fixture
def db_conn(monkeypatch):
    """Return an in-memory SQLite connection and patch get_db to use it."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript("""
        CREATE TABLE users (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            name          TEXT    NOT NULL,
            email         TEXT    UNIQUE NOT NULL,
            password_hash TEXT    NOT NULL,
            created_at    TEXT    DEFAULT (datetime('now'))
        );
        CREATE TABLE expenses (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL REFERENCES users(id),
            amount      REAL    NOT NULL,
            category    TEXT    NOT NULL,
            date        TEXT    NOT NULL,
            description TEXT,
            created_at  TEXT    DEFAULT (datetime('now'))
        );
    """)
    monkeypatch.setattr("database.queries.get_db", lambda: conn)
    yield conn
    conn.close()


@pytest.fixture
def seed_user(db_conn):
    """Insert the demo user with 8 expenses; return user_id."""
    cur = db_conn.execute(
        "INSERT INTO users (name, email, password_hash, created_at) VALUES (?, ?, ?, ?)",
        ("Demo User", "demo@spendly.com", generate_password_hash("demo123"), "2026-01-15 10:00:00"),
    )
    db_conn.commit()
    user_id = cur.lastrowid

    expenses = [
        (user_id, 450.00,  "Food",          "2026-04-01", "Groceries from D-Mart"),
        (user_id, 120.00,  "Transport",     "2026-04-02", "Metro card recharge"),
        (user_id, 1200.00, "Bills",         "2026-04-03", "Electricity bill"),
        (user_id, 350.00,  "Health",        "2026-04-05", "Pharmacy — vitamins"),
        (user_id, 500.00,  "Entertainment", "2026-04-06", "Movie tickets"),
        (user_id, 800.00,  "Shopping",      "2026-04-07", "New earphones"),
        (user_id, 200.00,  "Other",         "2026-04-08", "Miscellaneous"),
        (user_id, 180.00,  "Food",          "2026-04-08", "Lunch with colleagues"),
    ]
    db_conn.executemany(
        "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
        expenses,
    )
    db_conn.commit()
    return user_id


@pytest.fixture
def empty_user(db_conn):
    """Insert a user with no expenses; return user_id."""
    cur = db_conn.execute(
        "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        ("New User", "new@example.com", generate_password_hash("pass")),
    )
    db_conn.commit()
    return cur.lastrowid


# ------------------------------------------------------------------ #
# get_user_by_id                                                      #
# ------------------------------------------------------------------ #

def test_get_user_by_id_valid(seed_user):
    result = get_user_by_id(seed_user)
    assert result is not None
    assert result["name"] == "Demo User"
    assert result["email"] == "demo@spendly.com"
    assert result["initials"] == "DU"
    assert result["member_since"] == "January 2026"


def test_get_user_by_id_missing():
    result = get_user_by_id(9999)
    assert result is None


# ------------------------------------------------------------------ #
# get_summary_stats                                                   #
# ------------------------------------------------------------------ #

def test_get_summary_stats_with_expenses(seed_user):
    result = get_summary_stats(seed_user)
    assert result["total_spent"] == "₹3,800.00"
    assert result["transaction_count"] == 8
    assert result["top_category"] == "Bills"


def test_get_summary_stats_no_expenses(empty_user):
    result = get_summary_stats(empty_user)
    assert result == {"total_spent": "₹0.00", "transaction_count": 0, "top_category": "—"}


# ------------------------------------------------------------------ #
# get_recent_transactions                                             #
# ------------------------------------------------------------------ #

def test_get_recent_transactions_with_data(seed_user):
    result = get_recent_transactions(seed_user)
    assert len(result) == 8
    # newest first — both 2026-04-08 rows come before 2026-04-07
    assert result[0]["date"] == "08 Apr 2026"
    assert result[-1]["date"] == "01 Apr 2026"
    first = result[0]
    assert "date" in first
    assert "description" in first
    assert "category" in first
    assert "amount" in first
    assert first["amount"].startswith("₹")


def test_get_recent_transactions_no_data(empty_user):
    assert get_recent_transactions(empty_user) == []


def test_get_recent_transactions_limit(seed_user):
    result = get_recent_transactions(seed_user, limit=3)
    assert len(result) == 3


# ------------------------------------------------------------------ #
# get_category_breakdown                                              #
# ------------------------------------------------------------------ #

def test_get_category_breakdown_with_data(seed_user):
    result = get_category_breakdown(seed_user)
    assert len(result) == 7
    # ordered by amount descending — Bills is largest
    assert result[0]["name"] == "Bills"
    assert result[0]["amount"] == "₹1,200.00"
    # percentages sum to 100
    assert sum(cat["pct"] for cat in result) == 100
    # all pcts are integers
    for cat in result:
        assert isinstance(cat["pct"], int)


def test_get_category_breakdown_no_data(empty_user):
    assert get_category_breakdown(empty_user) == []


# ------------------------------------------------------------------ #
# Route tests                                                         #
# ------------------------------------------------------------------ #

def test_profile_unauthenticated(client):
    response = client.get("/profile")
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


def test_profile_authenticated(client):
    with client.session_transaction() as sess:
        sess["user_id"] = 1  # seed user created by app startup seed_db()

    response = client.get("/profile")
    assert response.status_code == 200
    html = response.data.decode()
    assert "Demo User" in html
    assert "demo@spendly.com" in html
    assert "₹" in html
    assert "Bills" in html
