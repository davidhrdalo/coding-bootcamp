# Software engineering theory

Short, interview-focused notes on how software actually works. Each note has plain
explanations, a few "say it out loud" questions, and links to go deeper. Four of them have
a hands-on exercise with tests, so you can prove you understand it.

| # | Note | Hands-on exercise (`theory/exercises/`) |
|---|---|---|
| 01 | [How code actually runs](01-how-code-runs.md): compiled, interpreted, bytecode, JIT | (try `dis` and Compiler Explorer, see the note) |
| 02 | [The stack, the heap and memory](02-stack-and-heap.md) | `explicit_stack.py`: replace recursion with your own stack |
| 03 | [Data structures cheat sheet](03-data-structures.md) | built in `python/`: hash table, stack, queue, linked list, BST, graph, heap (weeks 2 to 4) |
| 04 | [Buffers and streams](04-buffers-and-streams.md) | `ring_buffer.py`: a circular buffer |
| 05 | [The compilation pipeline](05-compilation-pipeline.md): lexer, parser, AST | `calculator.py`: a tokenizer and expression parser |
| 06 | [Transpilers](06-transpilers.md) | `tiny_transpiler.py`: Lisp-style calls to C-style calls |
| 07 | [Big-O](07-big-o.md) | used in every `python/` exercise |
| 08 | [Concurrency basics](08-concurrency.md) | (notes only) |
| 09 | [How the web works: HTTP, DNS, auth](09-web-and-networking.md) | (notes only: OAuth, OIDC, tokens, SSO) |
| 10 | [Databases and SQL](10-databases-and-sql.md) | `sql/exercises/` (31 exercises) |
| 11 | [Design principles and testing](11-design-and-testing.md) | (notes only) |
| 12 | [Data types](12-data-types.md): floats, strings and Unicode, mutability, null, type systems | `python/exercises/week0_data_types/` |
| 13 | [JavaScript and TypeScript essentials](13-javascript-and-typescript.md): closures, `this`, the event loop, promises, TypeScript types | `typescript/exercises/` |
| 14 | [Swift essentials](14-swift-essentials.md): optionals, value vs reference types, ARC, protocols, async/await and actors, SwiftUI state | `swift/Sources/` |

## How to use these

1. Read one note (about 10 minutes), without trying to memorise it.
2. Do its exercise if it has one: `python -m pytest theory/exercises/test_ring_buffer.py`
3. Close the note and explain it out loud as if to an interviewer. Where you stall, re-read.
4. Answer the interview questions at the bottom of the note, out loud, in two or three sentences.

Suggested order: 12, 01, 07, 02, 03, 04, 05, 06, then 08 to 11, 13 alongside the TypeScript track, and 14 alongside the Swift track.

## Honest scope

These are the topics that most often come up in UK software interviews for someone with your
profile. They are summaries, not textbooks: the "Learn more" links and
[RESOURCES.md](../RESOURCES.md) are where depth lives.
