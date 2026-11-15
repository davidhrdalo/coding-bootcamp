/**
 * typeName: what kind of value is this?
 *
 * JavaScript's typeof operator has famous quirks: typeof null is "object", typeof [] is
 * "object", and typeof NaN is "number". Write typeName(value), which returns:
 *
 *   "null"       for null
 *   "array"      for arrays
 *   "date"       for Date objects
 *   "nan"        for NaN
 *   "function", "object" (plain objects), and otherwise whatever typeof gives
 *   ("string", "number", "boolean", "undefined", "bigint", "symbol")
 *
 * Concepts: typeof, Array.isArray, instanceof, Number.isNaN.
 * Read theory/13-javascript-and-typescript.md.
 */

export function typeName(value: unknown): string {
  throw new Error("Not implemented");
}
