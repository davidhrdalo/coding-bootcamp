# 01 - How code actually runs

Computers only run machine code (CPU instructions). Every other language gets
there by one of a few routes. Being able to explain this clearly is a very common
interview question.

## The four routes

| Route | What happens | Examples |
|---|---|---|
| **Compiled (ahead of time)** | A compiler translates the whole program to machine code before you run it. | Swift, C, C++, Rust, Go |
| **Interpreted** | An interpreter reads the program and carries it out directly, step by step. | Early shells, simple scripting languages |
| **Bytecode + virtual machine** | Source is compiled to a compact intermediate form (bytecode), and a virtual machine (VM) runs it. | Python (CPython), Java (JVM), Kotlin on the JVM |
| **JIT (just in time)** | A VM watches the running program and compiles the hot (often-used) parts to machine code while it runs. | JavaScript (V8), Java (JVM) |

Many languages mix these. CPython compiles your .py to bytecode and runs it on
its VM. V8 starts by interpreting JavaScript, then compiles hot functions.
Kotlin on Android compiles to bytecode that is converted for Android's runtime.

## Transpiled code

A **transpiler** converts source in one language into source in another language
at a similar level. TypeScript becomes JavaScript, and modern JavaScript becomes
older JavaScript. It still needs to be run afterwards. See `06-transpilers.md`.

## Key ideas to be able to say out loud

- **Compiled vs interpreted** is about *when* translation happens (before running vs during).
- Compiled code is usually faster at runtime; interpreted or VM code is more portable and quicker to start developing with.
- **Static typing** checks types before running (Swift, Kotlin, TypeScript). **Dynamic typing** checks while running (Python, JavaScript).
- A **VM** is a program that pretends to be a computer, so the same bytecode runs on any machine that has the VM.
- "Is Python compiled or interpreted?" The honest answer is both: compiled to bytecode, then interpreted by the VM.

## Try it

- Run `python3 -c "import dis; dis.dis(lambda x: x + 1)"` to see Python's bytecode.
- Paste a small function into Compiler Explorer (godbolt.org) with a Swift or C compiler and read the machine code it produces.
- Write TypeScript in the TypeScript Playground and look at the JavaScript output tab.

## Interview questions

1. What is the difference between a compiler and an interpreter?
2. What does a JIT compiler do, and why is it useful?
3. Is Python compiled or interpreted?
4. What is bytecode, and why not compile straight to machine code?
5. What does it mean that TypeScript is "transpiled"?

## Learn more

- [Crafting Interpreters](https://craftinginterpreters.com/) (free online book; see the introduction and the "A Map of the Territory" chapter)
- [Compiler Explorer](https://godbolt.org/)
- [TypeScript Playground](https://www.typescriptlang.org/play)
- [Python dis module](https://docs.python.org/3/library/dis.html)
- Computerphile (YouTube): search for the episode "Just In Time (JIT) Compilers"; see [RESOURCES.md](../RESOURCES.md)
