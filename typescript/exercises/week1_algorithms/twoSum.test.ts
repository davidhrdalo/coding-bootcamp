import { test } from "node:test";
import assert from "node:assert/strict";
import { twoSum } from "./twoSum.ts";

const sorted = (pair: number[]) => [...pair].sort((a, b) => a - b);

test("basic", () => {
  assert.deepEqual(sorted(twoSum([2, 7, 11, 15], 9)), [0, 1]);
});

test("not the first elements", () => {
  assert.deepEqual(sorted(twoSum([3, 2, 4], 6)), [1, 2]);
});

test("duplicate values", () => {
  assert.deepEqual(sorted(twoSum([3, 3], 6)), [0, 1]);
});

test("negative numbers", () => {
  assert.deepEqual(sorted(twoSum([-1, -2, -3, -4, -5], -8)), [2, 4]);
});

test("large input needs linear time", () => {
  const nums = Array.from({ length: 20000 }, (_, i) => i);
  assert.deepEqual(sorted(twoSum(nums, 19999 + 19998)), [19998, 19999]);
});
