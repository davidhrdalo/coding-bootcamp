/**
 * Closures: counter, once and memoize
 *
 * A closure is a function that remembers the variables from where it was created, even
 * after that outer function has returned. This powers counters, caches and callbacks.
 *
 * makeCounter(start = 0): returns an object with increment() (adds 1 and returns the new
 * value), decrement() (subtracts 1 and returns the new value) and value() (returns the
 * current value). Each counter has its own private count.
 *
 * once(fn): returns a function that calls fn the first time and afterwards returns the SAME
 * result without calling fn again.
 *
 * memoize(fn): for a function of one string or number argument, return a version that
 * remembers results: calling it again with the same argument returns the stored result
 * without calling fn again.
 *
 * Concepts: closures, higher-order functions, private state, caching.
 */

export function makeCounter(start = 0): {
  increment: () => number;
  decrement: () => number;
  value: () => number;
} {
  throw new Error("Not implemented");
}

export function once<T>(fn: () => T): () => T {
  throw new Error("Not implemented");
}

export function memoize<A extends string | number, R>(fn: (arg: A) => R): (arg: A) => R {
  throw new Error("Not implemented");
}
