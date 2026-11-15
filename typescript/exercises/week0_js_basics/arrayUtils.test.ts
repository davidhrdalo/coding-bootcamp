import { test } from "node:test";
import assert from "node:assert/strict";
import { chunk, groupBy, unique, zip } from "./arrayUtils.ts";

test("groupBy groups and keeps order", () => {
  const result = groupBy([1, 2, 3, 4], (n) => (n % 2 === 0 ? "even" : "odd"));
  assert.deepEqual(result, { odd: [1, 3], even: [2, 4] });
});

test("groupBy works on objects and empty input", () => {
  const people = [
    { name: "Ann", team: "a" },
    { name: "Bob", team: "b" },
    { name: "Cy", team: "a" },
  ];
  assert.deepEqual(
    groupBy(people, (p) => p.team),
    { a: [people[0], people[2]], b: [people[1]] },
  );
  assert.deepEqual(groupBy([], () => "x"), {});
});

test("chunk splits into pieces", () => {
  assert.deepEqual(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]);
  assert.deepEqual(chunk([1, 2, 3], 3), [[1, 2, 3]]);
  assert.deepEqual(chunk([1, 2], 5), [[1, 2]]);
  assert.deepEqual(chunk([], 2), []);
});

test("chunk rejects a size below 1", () => {
  assert.throws(() => chunk([1], 0), RangeError);
});

test("unique keeps the first occurrence", () => {
  assert.deepEqual(unique([3, 1, 3, 2, 1]), [3, 1, 2]);
  assert.deepEqual(unique([]), []);
  assert.deepEqual(unique(["a", "a"]), ["a"]);
});

test("zip pairs by position and stops at the shorter array", () => {
  assert.deepEqual(zip([1, 2, 3], ["a", "b"]), [[1, "a"], [2, "b"]]);
  assert.deepEqual(zip([], [1]), []);
});
