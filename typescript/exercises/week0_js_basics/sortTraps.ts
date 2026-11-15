/**
 * Sorting traps
 *
 * Array.prototype.sort has two traps:
 *   1. With no argument it sorts as STRINGS: [10, 9, 1, 100].sort() gives [1, 10, 100, 9].
 *   2. It sorts the array IN PLACE, changing the original.
 *
 * sortNumbers(nums): return a NEW array of the numbers in ascending numeric order.
 * Do not modify nums.
 *
 * sortByLength(words): return a NEW array sorted by string length, shortest first. Words of
 * equal length must keep their original relative order (sort is stable in modern JavaScript).
 *
 * Concepts: comparator functions (a, b) => a - b, copying with the spread operator [...arr],
 * mutation vs returning a new value.
 */

export function sortNumbers(nums: number[]): number[] {
  throw new Error("Not implemented");
}

export function sortByLength(words: string[]): string[] {
  throw new Error("Not implemented");
}
