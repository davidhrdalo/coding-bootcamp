/**
 * falsyKind: which falsy value is it?
 *
 * In JavaScript the FALSY values are: false, 0 (and -0), 0n, "" (empty string), null,
 * undefined and NaN. Everything else is truthy, including "0", "false", [] and {}.
 * (This is different from Python, where [] and {} are falsy.)
 *
 * falsyKind(value) returns a string:
 *   "null"          for null
 *   "undefined"     for undefined
 *   "false"         for the boolean false
 *   "nan"           for NaN
 *   "zero"          for 0, -0 and 0n
 *   "empty-string"  for ""
 *   "truthy"        for everything else
 *
 * Concepts: truthiness, strict equality (===), Number.isNaN, -0.
 */

export function falsyKind(value: unknown): string {
  throw new Error("Not implemented");
}
