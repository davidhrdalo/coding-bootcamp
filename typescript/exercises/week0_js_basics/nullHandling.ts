/**
 * Nullish values: ?? and ?. versus ||
 *
 * null and undefined both mean "no value". Two operators make them easier to handle:
 *   a ?? b   uses b only when a is null or undefined
 *   a?.b     gives undefined instead of crashing when a is null or undefined
 *
 * The older a || b uses b for ANY falsy a, including 0 and "", which causes bugs.
 *
 * getCity(user): return user.address.city, or "Unknown" when user, address or city is
 * null or undefined. An empty string city "" is a real value and must be kept.
 *
 * countOrDefault(count, fallback): return count, or fallback when count is undefined. A count
 * of 0 is a real value and must be kept.
 *
 * Concepts: optional chaining, nullish coalescing, why || is wrong here.
 */

export interface User {
  name: string;
  address?: { city?: string | null } | null;
}

export function getCity(user: User | null | undefined): string {
  throw new Error("Not implemented");
}

export function countOrDefault(count: number | undefined, fallback: number): number {
  throw new Error("Not implemented");
}
