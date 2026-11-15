import { test } from "node:test";
import assert from "node:assert/strict";
import { sortByLength, sortNumbers } from "./sortTraps.ts";

test("sorts numerically, not alphabetically", () => {
  assert.deepEqual(sortNumbers([10, 9, 1, 100]), [1, 9, 10, 100]);
});

test("handles negatives, decimals and duplicates", () => {
  assert.deepEqual(sortNumbers([3, -1, 2.5, 3, 0]), [-1, 0, 2.5, 3, 3]);
});

test("does not modify the input", () => {
  const input = [3, 1, 2];
  const result = sortNumbers(input);
  assert.deepEqual(input, [3, 1, 2]);
  assert.notEqual(result, input);
});

test("empty array", () => {
  assert.deepEqual(sortNumbers([]), []);
});

test("sortByLength orders by length and keeps ties stable", () => {
  assert.deepEqual(sortByLength(["bb", "a", "cc", "d", "eee"]), ["a", "d", "bb", "cc", "eee"]);
});

test("sortByLength does not modify the input", () => {
  const words = ["ccc", "a", "bb"];
  sortByLength(words);
  assert.deepEqual(words, ["ccc", "a", "bb"]);
});
