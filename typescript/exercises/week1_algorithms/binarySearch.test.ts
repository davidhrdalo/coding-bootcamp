import { test } from "node:test";
import assert from "node:assert/strict";
import { binarySearch } from "./binarySearch.ts";

test("finds every element", () => {
  const nums = [1, 3, 5, 7, 9];
  nums.forEach((value, i) => assert.equal(binarySearch(nums, value), i));
});

test("returns -1 when absent", () => {
  assert.equal(binarySearch([1, 3, 5, 7, 9], 4), -1);
  assert.equal(binarySearch([1, 3, 5, 7, 9], 0), -1);
  assert.equal(binarySearch([1, 3, 5, 7, 9], 10), -1);
});

test("empty and single element", () => {
  assert.equal(binarySearch([], 1), -1);
  assert.equal(binarySearch([5], 5), 0);
  assert.equal(binarySearch([5], 4), -1);
});

test("duplicates return a valid index", () => {
  const nums = [1, 2, 2, 2, 3];
  assert.equal(nums[binarySearch(nums, 2)], 2);
});

test("large array", () => {
  const nums = Array.from({ length: 1_000_000 }, (_, i) => i * 2);
  assert.equal(binarySearch(nums, 1_999_998), 999_999);
  assert.equal(binarySearch(nums, 1_999_999), -1);
});
