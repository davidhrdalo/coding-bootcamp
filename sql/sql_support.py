"""Helpers for the SQL track: build the sample databases and compare query results.

You do not need to edit this file. It builds two databases in memory:

  small  the hand-written sample in data/seed_small.sql (read it: it is short)
  large  a bigger, generated database with the same tables and more rows

Your query must give the right answer on BOTH. The second database stops a query that hard-codes the
answer for the small one.
"""
import random
import sqlite3
from datetime import date, timedelta
from itertools import product
from pathlib import Path

DATA = Path(__file__).parent / "data"
DATASETS = ("small", "large")


def build_small(conn: sqlite3.Connection) -> None:
    conn.executescript((DATA / "schema.sql").read_text(encoding="utf-8"))
    conn.executescript((DATA / "seed_small.sql").read_text(encoding="utf-8"))


def build_large(conn: sqlite3.Connection) -> None:
    conn.executescript((DATA / "schema.sql").read_text(encoding="utf-8"))
    rng = random.Random(20241)

    firsts = ["Alice", "Aaron", "Amelia", "Ben", "Bella", "Carlos", "Chloe", "Dana", "Diego", "Eli", "Emma",
              "Fiona", "Greg", "Hana", "Ivan", "Jade", "Kai", "Lena", "Mia", "Noah", "Omar", "Priya", "Quinn",
              "Rosa", "Sam"]
    lasts = ["Adams", "Brooks", "Chen", "Diaz", "Evans", "Fox", "Grant", "Hill", "Ito", "Jones", "Khan", "Lopez",
             "Moore", "Nguyen", "Owens", "Patel", "Quinn", "Reyes", "Singh", "Tran", "Usman", "Vega", "Wong",
             "Xu", "Young"]
    combos = list(product(firsts, lasts))
    countries = ["Australia", "New Zealand", "Canada", "United Kingdom", "United States", "Ireland"]

    def random_date(start: date, days: int) -> str:
        return (start + timedelta(days=rng.randrange(days))).isoformat()

    # customers 1..60 (ids 51..60 never place an order)
    customer_names = [f"{a} {b}" for a, b in rng.sample(combos, 60)]
    for i, name in enumerate(customer_names, start=1):
        email = None if rng.random() < 0.15 else name.lower().replace(" ", ".") + "@example.com"
        conn.execute(
            "INSERT INTO customers (id, name, email, country, signup_date) VALUES (?, ?, ?, ?, ?)",
            (i, name, email, rng.choice(countries), random_date(date(2022, 1, 1), 900)),
        )

    # products (the last two in the list are never ordered)
    catalogue = {
        "Books": [("Python Pocket Guide", 12.5), ("Intro to Algorithms", 58.0), ("SQL in Practice", 27.0),
                  ("Cooking Basics", 18.0), ("History of Maths", 21.5)],
        "Electronics": [("Phone Charger", 14.99), ("Bluetooth Speaker", 49.0), ("Webcam HD", 65.0),
                        ("Laptop Stand", 39.5), ("Noise Cancelling Headphones", 199.0), ("Smart Watch", 249.0)],
        "Home": [("Scented Candle", 9.5), ("Throw Blanket", 32.0), ("Plant Pot", 15.0), ("Wall Clock", 24.0),
                 ("Storage Box", 11.0)],
        "Toys": [("Building Blocks", 29.0), ("Jigsaw 1000", 22.5), ("Card Game", 8.0), ("Remote Car", 44.0)],
        "Clothing": [("Cotton T-Shirt", 16.0), ("Wool Socks", 7.5), ("Rain Jacket", 85.0), ("Denim Jeans", 55.0),
                     ("Baseball Cap", 14.0)],
    }
    never_ordered = {"Smart Watch", "Baseball Cap"}
    prices = {}
    orderable = []
    pid = 0
    for category, items in catalogue.items():
        for name, price in items:
            pid += 1
            conn.execute(
                "INSERT INTO products (id, name, category, price, stock) VALUES (?, ?, ?, ?, ?)",
                (pid, name, category, price, rng.randrange(0, 200)),
            )
            prices[pid] = price
            if name not in never_ordered:
                orderable.append(pid)

    # orders and order items
    statuses = ["delivered"] * 11 + ["shipped"] * 3 + ["pending"] * 3 + ["cancelled"] * 3
    item_id = 0
    for order_id in range(1, 201):
        conn.execute(
            "INSERT INTO orders (id, customer_id, order_date, status) VALUES (?, ?, ?, ?)",
            (order_id, rng.randint(1, 50), random_date(date(2023, 1, 1), 731), rng.choice(statuses)),
        )
        for product_id in rng.sample(orderable, rng.randint(1, 4)):
            item_id += 1
            conn.execute(
                "INSERT INTO order_items (id, order_id, product_id, quantity, unit_price) VALUES (?, ?, ?, ?, ?)",
                (item_id, order_id, product_id, rng.randint(1, 5), prices[product_id]),
            )

    # employees: a random management tree rooted at employee 1
    employee_names = [f"{a} {b}" for a, b in rng.sample(combos, 40)]
    departments = ["Engineering", "Sales", "Marketing", "Finance"]
    for i, name in enumerate(employee_names, start=1):
        manager = None if i == 1 else rng.randint(1, i - 1)
        department = "Executive" if i == 1 else rng.choice(departments)
        conn.execute(
            "INSERT INTO employees (id, name, department, salary, manager_id, hire_date) VALUES (?, ?, ?, ?, ?, ?)",
            (i, name, department, rng.choice(range(60000, 200001, 5000)), manager, random_date(date(2015, 1, 1), 3000)),
        )

    conn.execute("INSERT INTO page_views (page, views) VALUES ('/home', 10), ('/about', 3)")


def connect(dataset: str, foreign_keys: bool = False, read_only: bool = False) -> sqlite3.Connection:
    """A fresh in-memory database. Autocommit mode so scripts and savepoints behave predictably."""
    conn = sqlite3.connect(":memory:", isolation_level=None)
    (build_small if dataset == "small" else build_large)(conn)
    if foreign_keys:
        conn.execute("PRAGMA foreign_keys = ON")
    if read_only:
        conn.execute("PRAGMA query_only = ON")
    return conn


def run_query(conn: sqlite3.Connection, sql: str):
    cursor = conn.execute(sql)
    if cursor.description is None:
        raise sqlite3.ProgrammingError("the statement did not return any rows (is it a SELECT?)")
    columns = [d[0].lower() for d in cursor.description]
    return columns, cursor.fetchall()


def normalise(value):
    """Numbers compare to 4 decimal places, so 5 and 5.0 match and float noise is ignored."""
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float)):
        return round(float(value), 4)
    return value


def normalise_rows(rows):
    return [tuple(normalise(v) for v in row) for row in rows]


def describe_difference(expected_cols, expected_rows, actual_cols, actual_rows, ordered=True) -> str | None:
    """Return a short explanation of the first difference, or None when the results match."""
    if actual_cols != expected_cols:
        return f"The result columns are wrong.\n  expected: {expected_cols}\n  you got:  {actual_cols}"
    expected = normalise_rows(expected_rows)
    actual = normalise_rows(actual_rows)
    if len(actual) != len(expected):
        return (
            f"Wrong number of rows: expected {len(expected)}, you returned {len(actual)}.\n"
            f"  first expected rows: {expected[:3]}\n  first rows you returned: {actual[:3]}"
        )
    if not ordered:
        expected_sorted = sorted(expected, key=repr)
        actual_sorted = sorted(actual, key=repr)
        if expected_sorted == actual_sorted:
            return None
        expected, actual = expected_sorted, actual_sorted
    for index, (want, got) in enumerate(zip(expected, actual)):
        if want != got:
            return f"Row {index + 1} differs.\n  expected: {want}\n  you got:  {got}"
    return None
