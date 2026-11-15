# 06 - Transpilers

A **transpiler** (source-to-source compiler) reads source code in one language and outputs
source code in another language at a similar level of abstraction. A normal compiler
goes down to machine code; a transpiler goes sideways.

## Common examples

| Tool | From | To | Why |
|---|---|---|---|
| **TypeScript compiler (tsc)** | TypeScript | JavaScript | Browsers and Node run JavaScript, not types |
| **Babel** | Modern JavaScript (and JSX) | Older JavaScript | Support older browsers, convert JSX |
| **Sass** | Sass/SCSS | CSS | Variables and nesting for stylesheets |
| **Kotlin/JS** | Kotlin | JavaScript | Share code with the web |

## How it works

The same three stages as a compiler, with a different last step:

1. **Parse** the input into an AST.
2. **Transform** the tree (replace or rewrite nodes).
3. **Generate** output text from the new tree.

Babel is a pipeline of exactly this shape, with plugins doing the transforms. You build a
tiny one in `theory/exercises/tiny_transpiler.py`.

## Related ideas

- **Type erasure:** TypeScript's types exist only at compile time. The output JavaScript has none, so a wrong type can still fail at runtime if data came from outside (an API response, for example).
- **Polyfills vs transpiling:** transpiling rewrites *syntax* (arrow functions, `async`); a polyfill adds missing *features* (such as a new array method) at runtime.
- **Source maps:** a file linking output lines back to the original source, so debuggers and error messages show your TypeScript, not the generated JavaScript.
- **Bundlers (Vite, webpack, esbuild):** combine many modules into a few files, often transpiling and minifying as they go. Frameworks such as Next.js do this for you as part of their build.

## Interview questions

1. What is the difference between a compiler and a transpiler?
2. Why does TypeScript need a build step, and what is type erasure?
3. What is a source map?
4. What is the difference between transpiling and polyfilling?
5. What does Babel do, and how does it work internally?

## Learn more

- [The Super Tiny Compiler](https://github.com/jamiebuilds/the-super-tiny-compiler): a single readable file that does the same lisp-to-C transformation as your exercise; Babel's own docs recommend it
- [Babel docs](https://babeljs.io/docs)
- [TypeScript handbook](https://www.typescriptlang.org/docs/)
- [Transpiler vs compiler, with TypeScript (HowToDoInJava)](https://howtodoinjava.com/typescript/transpiler-vs-compiler)
