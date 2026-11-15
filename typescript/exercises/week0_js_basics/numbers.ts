/**
 * Numbers: floats and BigInt
 *
 * Every JavaScript number is a 64-bit float, so 0.1 + 0.2 is 0.30000000000000004 and integers
 * are only exact up to Number.MAX_SAFE_INTEGER (2^53 - 1). Two tasks:
 *
 * areClose(a, b, relTol = 1e-9, absTol = 0): true when
 *   Math.abs(a - b) <= Math.max(relTol * Math.max(Math.abs(a), Math.abs(b)), absTol)
 *   areClose(0.1 + 0.2, 0.3) -> true     areClose(1, 1.1) -> false
 *
 * factorialBig(n): n! as a BigInt, so large results stay exact.
 *   factorialBig(20) -> 2432902008176640000n
 *   factorialBig(25) -> 15511210043330985984000000n
 * Throw a RangeError if n is negative or not an integer.
 *
 * Concepts: floating point, tolerance comparison, BigInt (the n suffix), Number.isInteger.
 */

export function areClose(a: number, b: number, relTol = 1e-9, absTol = 0): boolean {
  throw new Error("Not implemented");
}

export function factorialBig(n: number): bigint {
  throw new Error("Not implemented");
}
