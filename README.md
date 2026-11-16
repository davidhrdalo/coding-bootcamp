# Coding Bootcamp

A self-paced refresher for technical interviews, built to be run and checked automatically
(a bit like LeetCode, but local). It assumes you have a degree but have not coded for a while,
so it starts from the basics and moves quickly.

**Tracks**

| Track | Status |
|---|---|
| `python/`: 50 exercises: data types, data structures and algorithms (weeks 0 to 4), then HTTP, building a REST API and object-oriented design (weeks 5 to 7) | ready |
| `theory/`: 17 notes and 4 hands-on exercises on data types, stacks, buffers, compilers, transpilers, JavaScript, Swift, SQL, web fundamentals, object-oriented design, React and more | ready |
| `typescript/`: 20 exercises: JavaScript basics and data types, algorithms, async and the type system | ready |
| `swift/`: 22 exercises: Swift basics, algorithms, concurrency and Codable (a Swift package) | ready |
| `sql/`: 31 exercises: SELECT, joins, aggregates, subqueries, window functions, and changing data (runs on SQLite) | ready |
| `web/`: 17 exercises: the DOM, fetch and retry, and a React refresher with hooks, context, reducers and forms (Vitest + Testing Library) | ready |

See [RESOURCES.md](RESOURCES.md) for external courses, videos, podcasts and practice sites.

## Quick start

Every command is `python run.py <task>`. It works the same on macOS, Windows and Linux and needs
nothing installed beyond Python 3.10 or newer. On macOS and Linux `make <task>` does the same thing.

| | macOS / Linux | Windows (PowerShell) |
|---|---|---|
| Run a task | `python3 run.py week0` (or `make week0`) | `py run.py week0` |
| List tasks | `python3 run.py` | `py run.py` |

```bash
git clone <your-repo-url> coding-bootcamp   # or just open this folder
cd coding-bootcamp
python3 run.py setup                         # Windows: py run.py setup   (creates .venv, installs pytest)
python3 run.py test                          # everything fails at first: that is the starting point
```

`run.py` finds the `.venv` on its own, so you do not need to activate it. In the examples below,
`make x` means `python3 run.py x` (Windows: `py run.py x`). Where an example shows `python -m pytest`,
use `python3 -m pytest` on macOS or `py -m pytest` on Windows, after activating the venv
(`source .venv/bin/activate` or `.venv\Scripts\activate`).

## Working on macOS and Windows with git

Keep `main` as the clean starting point and do your work on a branch:

```bash
git switch -c attempt        # once; afterwards: git switch attempt
# ... solve exercises ...
git add -A
git commit -m "Solve week 1"
git push -u origin attempt   # then on the other computer: git pull
```

`.gitattributes` keeps line endings identical on both systems, so switching computers does not
create phantom changes. The `.venv` and `node_modules` folders are not committed: run
`run.py setup` once on each computer. The Swift track needs a Swift toolchain, which in practice
means macOS; on Windows the Swift tasks report "not installed" and everything else works.

**TypeScript track:** needs only Node.js 22.18 or newer (check with `node --version`). Node runs `.ts`
files directly, so there is nothing to install:

```bash
make ts0      # JavaScript basics
make ts       # everything in typescript/
```

Optional: `make setup-ts` installs TypeScript so `make typecheck` can also show type errors.
Type-stripping limits: use plain TypeScript (no `enum`, `namespace` or constructor parameter
properties such as `constructor(private x: number)`), and import other files with the `.ts` extension.

**Swift track:** a Swift package that needs Xcode 16 or newer (or a Swift 6 toolchain). Check with
`swift --version`.

```bash
make swift0   # Swift basics (first build takes about a minute)
make swift    # everything in swift/
```

The tests use Swift Testing (`@Test`, `#expect`). Each week is its own module, so a compile error in
one week does not stop the others from building. If you run a test with code that crashes (for
example an array index out of range), Swift stops the whole test run, so fix crashes first.

**SQL track:** runs on SQLite through Python's built-in `sqlite3` module (same setup as the Python
track, nothing extra to install). Each exercise is a `.sql` file: you write the query, and the checker
runs it and a reference query on two databases and compares the results.

```bash
make sql1                       # SELECT basics
make sql                        # all SQL exercises
python sql/playground.py        # build sql/playground.db to explore with your own queries
sqlite3 sql/playground.db       # (then: .headers on, .mode column, SELECT * FROM customers;)
```

**Web and React track:** the DOM, `fetch` and React exercises run in a fake browser (jsdom) with Vitest and
React Testing Library. This is the one track that needs an install (Node.js 20 or newer):

```bash
make setup-web   # once: npm install inside web/ (Windows: py run.py setup-web)
make web-dom     # DOM exercises
make web-api     # fetch, retry, debounce
make web-react   # React lessons
make web         # everything in web/
```

## How an exercise works

1. Open an exercise file, for example `python/exercises/week1_basics/fizzbuzz.py`
   (or `typescript/exercises/week1_algorithms/twoSum.ts`).
2. Read the docstring or comment at the top: it explains the task, gives examples and a hint.
3. Replace `raise NotImplementedError` (or `throw new Error("Not implemented")`) with your code.
4. Run its tests and read the result:

```bash
python -m pytest python/exercises/week1_basics/test_fizzbuzz.py
node --test --test-reporter=spec typescript/exercises/week1_algorithms/twoSum.test.ts
```

- A green line (`passed`) means you are right.
- A red `FAILED` shows which test failed and the input it failed on.

Useful commands:

| Command | What it runs |
|---|---|
| `make week0` ... `make week7` | one week of Python exercises (5: HTTP, 6: REST API, 7: object-oriented design) |
| `make theory` | the theory exercises |
| `make test` | all Python exercises |
| `make ts0`, `make ts1`, `make ts2`, `make ts` | TypeScript exercises, by week or all |
| `make typecheck` | TypeScript compiler check (after `make setup-ts`) |
| `make swift0`, `make swift1`, `make swift2`, `make swift` | Swift exercises, by week or all |
| `swift test --package-path swift --filter TwoSumTests` | one Swift exercise |
| `make sql1` ... `make sql4`, `make sql` | SQL exercises, by block or all |
| `make setup-web`, then `make web-dom`, `make web-api`, `make web-react`, `make web` | web and React exercises (`make web-typecheck` runs the compiler) |
| `npm --prefix web run test -- Counter` | one web exercise (any part of its file name) |
| `python -m pytest sql -k 05_date` | one SQL exercise |
| `python -m pytest -k fizzbuzz` | only tests whose name matches |
| `python -m pytest -x` | stop at the first failure |
| `make verify` | checks the reference solutions pass (does not touch your files) |

## Rules that make it work

- **Time-box yourself.** Try for 20 to 30 minutes. Re-read the hint. Only then look at the reference solution in `python/solutions/`, `typescript/solutions/`, `swift/Solutions/`, `sql/solutions/`, `web/solutions/` or `theory/solutions/`.
- **After passing, do it again a different way** (loop then recursion, slice then manual) and say the Big-O out loud.
- **Do not edit the tests.** If a test seems wrong, find out why first: the surprise is the learning.
- **Little and often beats long and rare:** an hour a day is better than a weekend.

## Study plan: week 0 plus four weeks

About an hour a day. Do the read, then the exercise, then explain it out loud.
Do the exercises in each week in the order listed.

| Week | Python exercises | Theory reading and exercises |
|---|---|---|
| **0: Data types** (3 to 4 days) | float_compare, money_cents, string_basics, mutability, truthiness, type_conversion, tuples_and_dataclasses | Read 12 (data types) first, then 01 (how code runs). |
| **1: Basics** | fizzbuzz, reverse_string, is_palindrome, factorial, fibonacci | Read 07 (Big-O). Do `explicit_stack` after factorial, with note 02. |
| **2: Collections** | two_sum, contains_duplicate, valid_anagram, word_count, group_anagrams, hash_table | Read 03 (data structures). Notice how every solution trades memory for speed. |
| **3: Stacks, queues and sorting** | valid_parentheses, stack_class, queue_from_stacks, binary_search, merge_sorted_lists, merge_sort | Read 04 (buffers); do `ring_buffer`. |
| **4: Linked lists, trees, graphs and heaps** | reverse_linked_list, max_depth, bst, graph_bfs, k_largest | Read 05 and 06; do `calculator` then `tiny_transpiler`. Skim 08 to 11. |
| **5: HTTP and the web** (`make week5`) | parse_http_request, build_http_response, parse_query_string, url_parts, parse_cookies, status_codes, jwt_payload | Read 15 (web fundamentals), then 09 again. |
| **6: Building a REST API** (`make week6`) | route_matching, router, todo_api, auth_middleware, pagination, rate_limiter | Read the REST part of 15. Do route_matching and router before todo_api. |
| **7: Object-oriented design** (`make week7`) | bank_account, shapes_polymorphism, notifier_composition, protocols_duck_typing, dependency_injection, discount_rules, event_bus, order_state_machine | Read 16. |

Weeks 5 to 7 are optional for pure algorithm practice but worth doing for any web, full-stack or backend role: job
advertisements keep asking for HTTP, REST and object-oriented design.

### TypeScript track (about two weeks, after Python weeks 0 to 2)

Pick this up for web and full-stack roles (and it is useful for mobile interviews that allow any
language). The algorithms repeat ideas from Python, so they should go faster.

| Block | Exercises | Read |
|---|---|---|
| **TS 0: JavaScript basics and data types** (`make ts0`) | typeName, falsyKind, numbers, nullHandling, sortTraps, references, closures, arrayUtils | Note 13, the first half |
| **TS 1: algorithms** (`make ts1`) | twoSum, validParentheses, wordCount, groupAnagrams, binarySearch, reverseList, maxDepth, lruCache | Note 07 again |
| **TS 2: async and the type system** (`make ts2`) | asyncBasics, concurrency, eventEmitter, typeSystem | Note 13, the event loop, promises and TypeScript sections |

### Swift track (about two to three weeks, after Python weeks 0 to 2)

For iOS and mobile roles. Compared with the other tracks it spends more time on the things Swift
interviews are known for: optionals, value vs reference types, ARC, closures, protocols and
concurrency.

| Block | Exercises | Read |
|---|---|---|
| **Swift 0: the language** (`make swift0`) | Optionals, ValueSemantics, RetainCycles, ErrorHandling, StringsAndCharacters, FunctionalCollections, ProtocolsAndGenerics, Enums, Closures | Note 14, the first half; note 02 for memory |
| **Swift 1: algorithms** (`make swift1`) | TwoSum, ValidParentheses, GroupAnagrams, BinarySearch, MergeSort, ReverseList, MaxDepth, LRUCache, GraphBFS | Note 07 again |
| **Swift 2: concurrency and data** (`make swift2`) | AsyncAwait, Actors, ObservableValue, CodableJSON | Note 14, concurrency and SwiftUI sections; note 08 |

### SQL track (about two weeks, can start any time after Python week 0)

SQL comes up in almost every software interview. Read note 10 first, then work through the blocks.
Open `sql/data/seed_small.sql` and look at the rows before you write any queries, and use
`python sql/playground.py` to try ideas freely. Each exercise tells you the exact columns and the
ORDER BY to use, so the answer is checkable.

| Block | What you practise | Exercises |
|---|---|---|
| **SQL 1: SELECT** (`make sql1`) | WHERE, NULL, LIKE and IN, date ranges, CASE, DISTINCT, LIMIT and OFFSET | 01 to 08 |
| **SQL 2: joins and aggregates** (`make sql2`) | COUNT, SUM, AVG, GROUP BY and HAVING, INNER and LEFT JOIN, top N, grouping by month | 09 to 16 |
| **SQL 3: subqueries and windows** (`make sql3`) | subqueries, EXISTS, WITH (CTEs), self joins, RANK and ROW_NUMBER, running totals, recursive CTEs, EXCEPT | 17 to 25 |
| **SQL 4: changing data and design** (`make sql4`) | INSERT, UPDATE, DELETE and foreign keys, UPSERT, CREATE TABLE with constraints, indexes and query plans | 26 to 31 |

SQLite differs slightly from the databases you will meet at work (Postgres, MySQL, SQL Server). The core
ideas are the same, and note 10 mentions the main differences.

### Web and React track (about two weeks, after TypeScript block 0)

Needs `make setup-web` once. Read note 15 for the DOM and fetch blocks, and note 17 for the React block. The
React lessons are a refresher: each exercise is one idea that interviews like to probe.

| Block | Exercises | Read |
|---|---|---|
| **Web 1: the DOM** (`make web-dom`) | buildList, eventDelegation, validateForm, tabs | Note 15, the browser section |
| **Web 2: fetch and timing** (`make web-api`) | fetchJson, fetchWithRetry, debounce (and throttle) | Note 15, REST and retries |
| **Web 3: React** (`make web-react`) | Greeting, Counter, TodoList, FilterableList, hooks, UserProfile, ThemeContext, Cart, SignupForm, Picker | Note 17 |

After the Python weeks and the TypeScript, Swift, SQL and web blocks: repeat the exercises you found hard,
then move to LeetCode Easy (NeetCode 150 order) and its database problems.

## Layout

```
python/
  exercises/week0_data_types/         stubs and tests: this is where you work
  exercises/week1_basics/
  exercises/week2_collections/
  exercises/week3_stacks_and_search/
  exercises/week4_linked_lists_and_trees/
  exercises/week5_web_http/
  exercises/week6_rest_api/
  exercises/week7_oo_design/
  solutions/                          reference solutions (no peeking)
typescript/
  exercises/week0_js_basics/          stubs (.ts) and tests (.test.ts)
  exercises/week1_algorithms/
  exercises/week2_async_and_types/
  solutions/
  tsconfig.json                       used by `make typecheck`
swift/
  Package.swift
  Sources/Week0Basics/                stubs: this is where you work
  Sources/Week1Algorithms/
  Sources/Week2Concurrency/
  Tests/...Tests/                     the tests
  Solutions/                          reference solutions (no peeking)
sql/
  exercises/block1_select/ ...        .sql files you fill in
  solutions/                          reference queries (no peeking)
  data/schema.sql, seed_small.sql     the sample database
  sql_support.py, test_sql_exercises.py, exercises.json   the checker
  playground.py                       builds sql/playground.db to explore
web/
  exercises/dom/ api/ react/          stubs (.ts, .tsx) and tests (.test.ts, .test.tsx)
  solutions/                          reference solutions (no peeking)
  package.json, vitest.config.ts      its own dependencies (run `make setup-web` once)
theory/
  01-...md to 17-...md                notes
  exercises/                          hands-on exercises and tests
  solutions/
scripts/verify_solutions.py           checks every Python reference solution passes
scripts/verify_typescript.mjs         the same for TypeScript
scripts/verify_swift.py               the same for Swift (skipped if Swift is not installed)
scripts/verify_web.mjs                the same for the web track (skipped until `make setup-web`)
run.py  Makefile  pytest.ini  requirements.txt  package.json  .gitattributes
```

## Putting it on GitHub

```bash
cd ~/repos/coding-bootcamp
git init
git add .
git commit -m "Initial commit"
gh repo create coding-bootcamp --private --source=. --push
```

If you want your own progress private but this repo public, keep your filled-in exercise files on
a separate branch.
