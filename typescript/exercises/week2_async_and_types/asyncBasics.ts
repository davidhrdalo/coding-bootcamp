/**
 * Promises: sleep, withTimeout and retry
 *
 * JavaScript runs one thing at a time. Waiting work (timers, network, files) is handled with
 * Promises and async/await. Implement three building blocks.
 *
 * sleep(ms): return a Promise that resolves (with no value) after ms milliseconds.
 *
 * withTimeout(promise, ms): return a Promise that behaves like `promise`, unless it takes longer
 * than ms milliseconds, in which case it rejects with new Error("timeout"). Clear the timer when
 * the promise settles.
 *
 * retry(fn, attempts): call the async function fn. If it rejects, call it again, up to `attempts`
 * calls in total. Resolve with the first success. If every attempt fails, reject with the LAST
 * error. If attempts < 1, reject with a RangeError.
 *
 * Concepts: Promise, setTimeout, async/await, try/catch, event loop (read theory/13).
 */

export function sleep(ms: number): Promise<void> {
  throw new Error("Not implemented");
}

export function withTimeout<T>(promise: Promise<T>, ms: number): Promise<T> {
  throw new Error("Not implemented");
}

export function retry<T>(fn: () => Promise<T>, attempts: number): Promise<T> {
  throw new Error("Not implemented");
}
