# 08 - Concurrency basics

**Concurrency** is dealing with many things at once (interleaved). **Parallelism** is doing
many things at the same instant on different CPU cores. They are related but not the same.

## Processes and threads

- A **process** has its own memory. Processes are isolated and heavier to start.
- A **thread** lives inside a process and shares its memory with other threads. Lighter, but shared memory causes bugs.

## Async and the event loop

Instead of one thread per task, **async** code uses one thread that switches between tasks
whenever one is **waiting** (for the network, a file, a timer).

- JavaScript is single-threaded with an **event loop**: `await` hands control back until the awaited work finishes.
- Python has `asyncio` with `async`/`await`.
- Swift has `async`/`await`, **actors** and structured concurrency.
- Kotlin has **coroutines**.

Rule of thumb: use async for I/O-bound work (waiting) and threads or processes for CPU-bound work (heavy calculation).

## Things that go wrong

| Problem | What it is |
|---|---|
| **Race condition** | Result depends on the unlucky timing of two threads touching the same data |
| **Deadlock** | Two tasks each wait for something the other holds, so neither moves |
| **Starvation** | A task never gets a turn |
| **Blocking the main thread** | Doing slow work on the UI thread freezes the app |

Fixes: avoid shared mutable state, use **locks (mutexes)**, use thread-safe queues, make data
immutable, or use actors (Swift) or message passing so only one place changes the data.

## Language details worth knowing

- **Python's GIL** (global interpreter lock) lets only one thread run Python bytecode at a time in standard CPython, so threads do not speed up CPU-heavy code (use `multiprocessing`); they still help with I/O waits.
- **iOS:** UI updates must happen on the main thread (`@MainActor`). Long work (such as running a model) goes off the main thread so the interface stays responsive.
- **JavaScript:** a long synchronous loop blocks everything, including clicks.

## Interview questions

1. What is the difference between concurrency and parallelism?
2. What is a race condition? Give an example and a fix.
3. What is a deadlock, and how can you avoid one?
4. When would you use async/await instead of threads?
5. Why must UI updates happen on the main thread?

## Learn more

- [Python asyncio](https://docs.python.org/3/library/asyncio.html)
- [Swift: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)
- [MDN: the JavaScript event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop)
- [Python glossary: global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)
- [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) (the concurrency chapters: threads, locks, deadlock)
