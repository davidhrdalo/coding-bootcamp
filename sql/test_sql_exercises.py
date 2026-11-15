"""Checks every SQL exercise.

For each exercise this runs YOUR .sql file and the reference solution on two databases
(a small hand-written one and a larger generated one) and compares the results.
Run it with:  python -m pytest sql
"""
import json
import re
import sqlite3
from pathlib import Path

import pytest

import sql_support as support

HERE = Path(__file__).parent
EXERCISES = json.loads((HERE / "exercises.json").read_text(encoding="utf-8"))
PLACEHOLDER = "select null as todo"

DATASET_NAMES = {
    "small": "the small database (sql/data/seed_small.sql)",
    "large": "the large generated database",
}


def is_placeholder(sql: str) -> bool:
    without_comments = re.sub(r"--[^\n]*", "", sql)
    return PLACEHOLDER in without_comments.lower()


def fail(message: str):
    pytest.fail(message, pytrace=False)


def error_text(error: sqlite3.Error) -> str:
    text = str(error)
    if "one statement at a time" in text:
        return "this exercise needs ONE statement (a single SELECT, optionally starting with WITH)."
    return text


def check_query(exercise, student_sql, solution_sql, dataset):
    reference = support.connect(dataset, read_only=True)
    expected_cols, expected_rows = support.run_query(reference, solution_sql)

    attempt = support.connect(dataset, read_only=True)
    error = None
    try:
        actual_cols, actual_rows = support.run_query(attempt, student_sql)
    except sqlite3.Error as caught:
        error = caught
    if error is not None:
        fail(f"Your query failed on {DATASET_NAMES[dataset]}: {error_text(error)}")

    problem = support.describe_difference(
        expected_cols, expected_rows, actual_cols, actual_rows, exercise.get("ordered", True)
    )
    if problem:
        fail(f"Wrong answer on {DATASET_NAMES[dataset]}.\n{problem}")


def check_script(exercise, student_sql, solution_sql, dataset):
    reference = support.connect(dataset, foreign_keys=True)
    reference.executescript(solution_sql)

    attempt = support.connect(dataset, foreign_keys=True)
    error = None
    try:
        attempt.executescript(student_sql)
    except sqlite3.Error as caught:
        error = caught
    if error is not None:
        fail(f"Your statements failed on {DATASET_NAMES[dataset]}: {error}")

    for verify_sql in exercise.get("verify", []):
        expected_cols, expected_rows = support.run_query(reference, verify_sql)
        error = None
        try:
            actual_cols, actual_rows = support.run_query(attempt, verify_sql)
        except sqlite3.Error as caught:
            error = caught
        if error is not None:
            fail(f"The check query failed ({error}). Did you create everything the task asks for?")
        problem = support.describe_difference(expected_cols, expected_rows, actual_cols, actual_rows, True)
        if problem:
            fail(
                f"The database is not in the expected state on {DATASET_NAMES[dataset]}.\n"
                f"Checked with: {verify_sql}\n{problem}"
            )

    if dataset == "small":
        for probe in exercise.get("probes", []):
            check_probe(attempt, probe)


def check_probe(conn, probe):
    if "sql" in probe:
        conn.execute("SAVEPOINT probe")
        try:
            conn.execute(probe["sql"])
            succeeded = True
        except sqlite3.Error:
            succeeded = False
        finally:
            conn.execute("ROLLBACK TO probe")
            conn.execute("RELEASE probe")
        want_success = probe["expect"] == "ok"
        if succeeded != want_success:
            outcome = "should have worked" if want_success else "should have been rejected"
            fail(f"This statement {outcome}: {probe['sql']}\n({probe.get('why', '')})")
    else:
        rows = conn.execute("EXPLAIN QUERY PLAN " + probe["plan"]).fetchall()
        detail = " | ".join(row[3] for row in rows).upper()
        for needed in probe.get("must_contain", []):
            if needed.upper() not in detail:
                fail(f"The query plan for: {probe['plan']}\n  is: {detail}\n  but should mention {needed}. {probe.get('why', '')}")
        for banned in probe.get("must_not_contain", []):
            if banned.upper() in detail:
                fail(f"The query plan for: {probe['plan']}\n  is: {detail}\n  but should not mention {banned}. {probe.get('why', '')}")


@pytest.mark.parametrize("exercise", EXERCISES, ids=[f"{e['block']}-{e['id']}" for e in EXERCISES])
def test_exercise(exercise):
    student_path = HERE / "exercises" / exercise["block"] / f"{exercise['id']}.sql"
    solution_path = HERE / "solutions" / f"{exercise['id']}.sql"
    student_sql = student_path.read_text(encoding="utf-8-sig")
    solution_sql = solution_path.read_text(encoding="utf-8")

    if is_placeholder(student_sql):
        fail(f"Not implemented yet: replace the placeholder 'SELECT NULL AS todo;' in {student_path.name}.")

    for dataset in support.DATASETS:
        if exercise["mode"] == "query":
            check_query(exercise, student_sql, solution_sql, dataset)
        else:
            check_script(exercise, student_sql, solution_sql, dataset)
