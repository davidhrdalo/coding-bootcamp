# 13 - JavaScript and TypeScript essentials

The TypeScript track (`typescript/exercises/`) practises these. TypeScript is JavaScript plus a type
checker that is erased before running (see `06-transpilers.md`), so everything about JavaScript
applies, and interviews often test both.

## Variables and scope

- Use **`const`** by default, **`let`** when the value changes. Avoid `var`.
- `let` and `const` are **block-scoped**; `var` is function-scoped and **hoisted** (the declaration moves to the top, set to `undefined`). Using a `let` or `const` before its line throws (the "temporal dead zone").
- **Closures:** a function remembers the variables where it was created. Classic bug: a `var` loop variable captured by callbacks, so every callback sees the final value.

## Equality, types and coercion

- Always use **`===`** (strict). `==` coerces types: `"5" == 5` is true, `null == undefined` is true, `[] == false` is true.
- `typeof null` is `"object"` (a historical bug). Check arrays with `Array.isArray`.
- Falsy values: `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, `NaN`. Everything else is truthy, including `[]` and `{}`.
- `NaN !== NaN`; use `Number.isNaN`. All numbers are 64-bit floats (see `12-data-types.md`).
- **`??`** (nullish coalescing) vs **`||`**: `0 || 5` is 5 but `0 ?? 5` is 0.
- Objects and arrays are compared **by reference**: `{} === {}` is false.

## Functions and `this`

- Functions are values: pass them around, return them, store them (**higher-order functions**).
- **Arrow functions** do not have their own `this`; they use the `this` of where they were written. Regular functions get `this` from *how they are called*, so `obj.method` passed as a callback loses it (`undefined` in strict mode). Fixes: arrow function, `.bind(obj)`.
- **Rest and spread:** `function f(...args)` collects arguments; `[...a, ...b]` and `{...a, ...b}` copy items and keys (a *shallow* copy).
- **Destructuring:** `const { name, age = 18 } = user;` and `const [first, ...rest] = list;`.

## Objects, prototypes and classes

- Every object has a **prototype**; property lookup walks the prototype chain. `class` is mostly clearer syntax over this.
- `Object.keys`, `Object.values`, `Object.entries`, `Map` (any key type, keeps insertion order) and `Set` (unique values).
- Prefer `Map` over a plain object when keys are not fixed or might be arbitrary strings.

## The event loop (a top interview topic)

JavaScript runs your code on **one thread**. Waiting work (timers, network, files) is handled outside, and callbacks are queued to run when the call stack is empty.

- **Call stack:** what is running now.
- **Macrotask queue:** timers (`setTimeout`), I/O, UI events. One macrotask runs per loop turn.
- **Microtask queue:** promise callbacks (`.then`, `await` continuations), `queueMicrotask`. **All microtasks run before the next macrotask.**

Predict the output:

```js
console.log("1");
setTimeout(() => console.log("2"), 0);
Promise.resolve().then(() => console.log("3"));
console.log("4");
```

Answer: `1, 4, 3, 2`. Synchronous code first (1, 4), then microtasks (3), then macrotasks (2).

A long synchronous loop **blocks everything**, including clicks and timers.

## Promises and async/await

- A **Promise** is a value that will arrive later: *pending*, then *fulfilled* or *rejected*.
- `async` functions always return a Promise; `await` pauses that function (not the thread) until the Promise settles.
- Errors: `try/catch` around `await`, or `.catch()`. An unhandled rejection is a bug.
- `Promise.all` (all must succeed, fails fast), `Promise.allSettled` (wait for all, never rejects), `Promise.race` (first to settle), `Promise.any` (first to succeed).
- **Sequential vs parallel:** `await` inside a `for` loop runs one at a time; start all promises first and `Promise.all` them to run in parallel (and limit concurrency if there are many: see `concurrency.ts`).

## Modules and tooling

- **ES modules:** `import { x } from "./file.js"` and `export`. **CommonJS:** `require` and `module.exports` (older Node style).
- **npm** installs packages listed in `package.json`; `node_modules` holds them; a lockfile pins versions.
- **Bundlers** (Vite, webpack, esbuild) combine and transform code for the browser.

## TypeScript essentials

- **Types are erased:** they give editor help and compile-time checks, but nothing is checked at runtime. Data from the outside world must be validated with real code (type guards, or a library such as Zod).
- **`unknown` vs `any`:** `any` switches checking off; `unknown` forces you to check before use. Prefer `unknown`.
- **Union types** `string | number`, **narrowing** with `typeof`, `in`, `===` and custom **type guards** (`value is Shape`).
- **Discriminated unions:** each variant has a literal tag (`kind: "circle"`); a `switch` on it narrows the type, and a `never` check in `default` makes the compiler flag missing cases.
- **`interface` vs `type`:** both describe object shapes; `type` can also name unions and other types; interfaces can be extended and merged. Either is fine; be consistent.
- **Generics:** `function first<T>(items: T[]): T | undefined`. Constraints: `<T extends { id: string }>`.
- **Utility types:** `Partial<T>`, `Required<T>`, `Pick<T, K>`, `Omit<T, K>`, `Record<K, V>`, `ReturnType<F>`.
- **`strict` mode** (strictNullChecks and friends) catches most bugs; always enable it.
- **Optional (`?`) vs `| undefined`:** an optional property may be absent; a required property of type `T | undefined` must be present but may be undefined.
- **`as` casts** only tell the compiler to trust you; overusing them removes the safety.

## Interview questions

1. What is the difference between `var`, `let` and `const`?
2. What is a closure? Give a use and a classic bug.
3. What is the difference between `==` and `===`?
4. Explain the event loop. In what order do `setTimeout`, a resolved promise and synchronous code run?
5. What does `this` refer to, and how do arrow functions change that?
6. What is a Promise? How do `Promise.all` and `Promise.allSettled` differ?
7. What is the difference between `null` and `undefined`? Between `??` and `||`?
8. What is the difference between `unknown` and `any`? Why validate data at runtime in TypeScript?
9. What is a discriminated union, and how does exhaustive checking with `never` work?
10. How do you copy an object, and what is the difference between a shallow and a deep copy?

## Learn more

- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [MDN: Concurrency model and the event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop)
- [javascript.info](https://javascript.info/): the best free, thorough JavaScript tutorial (closures, promises, classes)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [TypeScript Playground](https://www.typescriptlang.org/play)
- [Total TypeScript](https://www.totaltypescript.com/): free tutorials and articles by Matt Pocock
- [Node.js: running TypeScript natively](https://nodejs.org/api/typescript.html): how this repo runs `.ts` files without a build step
- [Node.js test runner](https://nodejs.org/api/test.html)
- [You Don't Know JS Yet (free book series)](https://github.com/getify/You-Dont-Know-JS)
