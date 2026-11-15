/**
 * References: deepClone and deepEqual
 *
 * Objects and arrays are compared and copied BY REFERENCE:
 *   {a: 1} === {a: 1}   is false (two different objects)
 *   const copy = {...original}   copies only the top level; nested objects are shared
 *
 * For JSON-like data (null, booleans, numbers, strings, arrays and plain objects):
 *
 * deepClone(value): return a completely independent copy. Changing anything inside the clone
 * must never change the original. (structuredClone exists, but write it yourself.)
 *
 * deepEqual(a, b): true when a and b have the same structure and values. Arrays must match in
 * order; objects must have the same keys with equal values, in any key order.
 *   deepEqual({x: [1, {y: 2}]}, {x: [1, {y: 2}]}) -> true
 *
 * Concepts: reference vs value, recursion, Array.isArray, Object.keys / Object.entries.
 */

export function deepClone<T>(value: T): T {
  throw new Error("Not implemented");
}

export function deepEqual(a: unknown, b: unknown): boolean {
  throw new Error("Not implemented");
}
