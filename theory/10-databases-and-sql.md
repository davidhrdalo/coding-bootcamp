# 10 - Databases and SQL

## The model

A **relational database** stores data in **tables** (rows and columns). **Keys** link tables:
a **primary key** uniquely identifies a row; a **foreign key** points to a row in another table.
You query it with **SQL**. (Postgres is a very common choice, including behind hosted services such as Supabase.)

## The SQL you must know

```sql
SELECT name, COUNT(*) AS orders
FROM users u
JOIN orders o ON o.user_id = u.id      -- combine tables
WHERE o.created_at >= '2026-01-01'     -- filter rows
GROUP BY name                          -- group rows
HAVING COUNT(*) > 2                    -- filter groups
ORDER BY orders DESC
LIMIT 10;
```

- **Joins:** INNER (only matches), LEFT (all left rows, matches if any), RIGHT, FULL.
- **WHERE vs HAVING:** WHERE filters rows before grouping; HAVING filters groups after.
- **Aggregates:** COUNT, SUM, AVG, MIN, MAX. **Subqueries** and **CTEs** (`WITH ...`) break big queries into steps.
- **NULL** is "unknown", not zero: `x = NULL` is never true; use `IS NULL`.

## Indexes

An **index** is an extra data structure (usually a B-tree) that lets the database find rows
without scanning the whole table, like a book index. Reads get faster; writes get slower and use
more space. Index columns you filter, join or sort on. Use `EXPLAIN` to see whether a query uses one.

## Transactions and ACID

A **transaction** groups steps so they all succeed or all fail (transferring money = subtract + add).

- **Atomicity** - all or nothing
- **Consistency** - rules (constraints) always hold
- **Isolation** - concurrent transactions do not see each other's half-done work
- **Durability** - once committed, it survives a crash

## Design and performance ideas

- **Normalisation:** avoid storing the same fact in many places; split data into related tables.
- **N+1 query problem:** one query to get a list, then one more query per item. Fix with a join or a batched query.
- **Row-level security (RLS):** Postgres can enforce who may see which rows inside the database itself; Supabase, for example, builds on this.
- **SQL vs NoSQL:** SQL for structured, related data and strong guarantees; NoSQL (document, key-value) when the shape varies or for extreme scale and simple access patterns.

## Interview questions

1. What is the difference between INNER JOIN and LEFT JOIN?
2. What is an index, and what is its cost?
3. What does ACID mean?
4. What is the difference between WHERE and HAVING?
5. What is the N+1 problem?
6. When would you pick NoSQL over SQL?

## Practice

Do the `sql/` track of this repo (31 exercises, checked automatically; start with `make sql1`), and use
SQLBolt and SQLZoo alongside it for extra repetition.

## SQLite vs the databases you will use at work

The exercises run on SQLite because it needs no setup. The core SQL is the same elsewhere; know these
differences:

- **Types:** SQLite is loosely typed (a column's type is a hint). Postgres, MySQL and SQL Server enforce types.
- **Dates:** SQLite stores dates as text and uses `strftime`; Postgres has real `date` and `timestamp` types and `date_trunc`, `EXTRACT`.
- **Booleans and auto IDs:** Postgres uses `boolean` and `SERIAL` / `GENERATED ... AS IDENTITY`; MySQL uses `AUTO_INCREMENT`; SQLite uses `INTEGER PRIMARY KEY`.
- **Limit syntax:** `LIMIT n OFFSET m` (SQLite, Postgres, MySQL); SQL Server uses `TOP n` or `OFFSET ... FETCH`.
- **Upsert:** `ON CONFLICT ... DO UPDATE` (SQLite, Postgres); MySQL uses `ON DUPLICATE KEY UPDATE`.
- **Concurrency:** SQLite allows one writer at a time; server databases handle many connections and have richer isolation levels.

## Learn more

- [SQLBolt](https://sqlbolt.com/): short interactive lessons
- [SQLZoo](https://sqlzoo.net/)
- [Mode SQL tutorial](https://mode.com/sql-tutorial)
- [Use The Index, Luke](https://use-the-index-luke.com/): how indexes really work
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
