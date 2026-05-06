from datetime import datetime

from database.db import get_db


def get_user_by_id(user_id):
    conn = get_db()
    try:
        row = conn.execute(
            "SELECT id, name, email, created_at FROM users WHERE id = ?",
            (user_id,),
        ).fetchone()
    finally:
        conn.close()

    if row is None:
        return None

    name = row["name"]
    initials = "".join(w[0].upper() for w in name.split()[:2])
    member_since = datetime.strptime(
        row["created_at"][:10], "%Y-%m-%d"
    ).strftime("%B %Y")

    return {
        "name": name,
        "email": row["email"],
        "initials": initials,
        "member_since": member_since,
    }


def get_summary_stats(user_id):
    conn = get_db()
    try:
        rows = conn.execute(
            """
            SELECT category, COALESCE(SUM(amount), 0) as total, COUNT(*) as cnt
            FROM expenses
            WHERE user_id = ?
            GROUP BY category
            ORDER BY total DESC
            """,
            (user_id,),
        ).fetchall()
    finally:
        conn.close()

    if not rows:
        return {"total_spent": "₹0.00", "transaction_count": 0, "top_category": "—"}

    transaction_count = sum(row["cnt"] for row in rows)
    grand_total = sum(row["total"] for row in rows)
    top_category = rows[0]["category"]

    return {
        "total_spent": f"₹{grand_total:,.2f}",
        "transaction_count": transaction_count,
        "top_category": top_category,
    }


def get_recent_transactions(user_id, limit=10):
    conn = get_db()
    try:
        rows = conn.execute(
            """
            SELECT date, description, category, amount
            FROM expenses
            WHERE user_id = ?
            ORDER BY date DESC, created_at DESC
            LIMIT ?
            """,
            (user_id, limit),
        ).fetchall()
    finally:
        conn.close()

    if not rows:
        return []

    return [
        {
            "date": datetime.strptime(row["date"], "%Y-%m-%d").strftime("%d %b %Y"),
            "description": row["description"],
            "category": row["category"],
            "amount": f"₹{row['amount']:,.2f}",
        }
        for row in rows
    ]


def get_category_breakdown(user_id):
    conn = get_db()
    try:
        rows = conn.execute(
            """
            SELECT category, SUM(amount) as total
            FROM expenses
            WHERE user_id = ?
            GROUP BY category
            ORDER BY total DESC
            """,
            (user_id,),
        ).fetchall()
    finally:
        conn.close()

    if not rows:
        return []

    grand_total = sum(row["total"] for row in rows)
    raw_pcts = [round(row["total"] / grand_total * 100) for row in rows]
    diff = 100 - sum(raw_pcts)
    raw_pcts[0] += diff  # absorb rounding remainder in largest category

    return [
        {
            "name": row["category"],
            "amount": f"₹{row['total']:,.2f}",
            "pct": pct,
        }
        for row, pct in zip(rows, raw_pcts)
    ]
