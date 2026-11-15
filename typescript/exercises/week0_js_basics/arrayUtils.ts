/**
 * Array utilities (generics)
 *
 * Implement four everyday helpers. Use generics so they work for any item type.
 *
 * groupBy(items, keyFn): return an object that maps each key to the array of items that
 * produced that key, keeping the original order.
 *   groupBy([1, 2, 3, 4], n => n % 2 === 0 ? "even" : "odd") -> { odd: [1, 3], even: [2, 4] }
 *
 * chunk(items, size): split into arrays of at most size items. Throw a RangeError if size < 1.
 *   chunk([1, 2, 3, 4, 5], 2) -> [[1, 2], [3, 4], [5]]
 *
 * unique(items): remove duplicates, keeping the first occurrence of each, in order.
 *   unique([3, 1, 3, 2, 1]) -> [3, 1, 2]
 *
 * zip(a, b): pair items by position, stopping at the shorter array.
 *   zip([1, 2, 3], ["a", "b"]) -> [[1, "a"], [2, "b"]]
 *
 * Concepts: generics <T>, Record, Set, map/filter/reduce, array methods.
 */

export function groupBy<T>(items: T[], keyFn: (item: T) => string): Record<string, T[]> {
  throw new Error("Not implemented");
}

export function chunk<T>(items: T[], size: number): T[][] {
  throw new Error("Not implemented");
}

export function unique<T>(items: T[]): T[] {
  throw new Error("Not implemented");
}

export function zip<A, B>(a: A[], b: B[]): [A, B][] {
  throw new Error("Not implemented");
}
