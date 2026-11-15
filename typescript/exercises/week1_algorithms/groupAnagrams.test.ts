import { test } from "node:test";
import assert from "node:assert/strict";
import { groupAnagrams } from "./groupAnagrams.ts";

const normalise = (groups: string[][]) =>
  groups.map((g) => [...g].sort()).sort((a, b) => a[0].localeCompare(b[0]));

test("example", () => {
  const result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]);
  assert.deepEqual(normalise(result), [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]);
});

test("empty list", () => {
  assert.deepEqual(groupAnagrams([]), []);
});

test("single empty string", () => {
  assert.deepEqual(normalise(groupAnagrams([""])), [[""]]);
});

test("no anagrams", () => {
  assert.deepEqual(normalise(groupAnagrams(["a", "b", "c"])), [["a"], ["b"], ["c"]]);
});
