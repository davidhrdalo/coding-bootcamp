# 04 - Buffers and streams

## What a buffer is

A **buffer** is a chunk of memory that holds data temporarily while it moves from
one place to another, usually because the producer and the consumer work at
different speeds.

- Typing: keystrokes wait in a buffer until the program reads them.
- Files and networks: data is read in blocks (for example 4 KB at a time), not byte by byte, because each system call is expensive.
- Audio and video: playback reads from a buffer that is refilled continuously, so a slow moment does not cause a gap.
- Printing: `print()` usually writes into an output buffer that is flushed to the terminal later (line-buffered on a terminal, fully buffered when redirected to a file).

In an app like Sayelle, streaming a tutor reply token by token and feeding audio to speech recognition or text to speech both rely on buffers.

## Streams

A **stream** processes data piece by piece as it arrives instead of loading everything first.
Reading a 4 GB file with `for line in open(path)` uses a small buffer and constant memory.
`open(path).read()` loads all 4 GB into memory.

## Ring (circular) buffer

A fixed-size buffer where the write position wraps back to the start. When full, new data
overwrites the oldest. It never allocates, which is why it is used for audio, logs and
network packets. You build one in `theory/exercises/ring_buffer.py`.

## Bounded vs unbounded, and backpressure

- An **unbounded** buffer grows without limit. If the producer is faster than the consumer, memory runs out.
- A **bounded** buffer has a maximum size. When full you can **block** the producer, **drop** data (like the ring buffer), or signal **backpressure**: tell the producer to slow down.

## Buffer overflow

In languages such as C, writing past the end of an array silently overwrites the
neighbouring memory. If that memory held a return address on the stack, an attacker can
redirect the program. This is a **buffer overflow**, a classic security bug.
Memory-safe languages (Python, Swift, Kotlin, JavaScript) check bounds and raise an error instead.

## Interview questions

1. What is a buffer, and why do we use one?
2. What is the difference between streaming a file and reading it all at once?
3. What is a ring buffer, and when would you use one?
4. What happens when a producer is faster than a consumer? How do you handle it?
5. What is a buffer overflow, and why are memory-safe languages less vulnerable?

## Learn more

- Computerphile (YouTube): search "Running a Buffer Overflow Attack" and "Why do buffers overflow" (see [RESOURCES.md](../RESOURCES.md))
- [Circular buffer (Wikipedia)](https://en.wikipedia.org/wiki/Circular_buffer)
- [Python io module: buffered streams](https://docs.python.org/3/library/io.html)
- [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) (the I/O and file system chapters)
