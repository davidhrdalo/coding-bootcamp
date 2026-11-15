import { test } from "node:test";
import assert from "node:assert/strict";
import { deepClone, deepEqual } from "./references.ts";

test("two objects with the same content are not the same object (why deepEqual exists)", () => {
  const first = { a: 1 };
  const second = { a: 1 };
  assert.equal(Object.is(first, second), false);
});

test("deepClone copies nested data independently", () => {
  const original = { name: "x", list: [1, 2, { deep: true }], inner: { n: 1 } };
  const copy = deepClone(original);
  assert.deepEqual(copy, original);
  copy.list.push(3);
  (copy.list[2] as { deep: boolean }).deep = false;
  copy.inner.n = 99;
  assert.deepEqual(original, { name: "x", list: [1, 2, { deep: true }], inner: { n: 1 } });
});

test("deepClone handles primitives and null", () => {
  assert.equal(deepClone(5), 5);
  assert.equal(deepClone("s"), "s");
  assert.equal(deepClone(null), null);
});

test("deepClone returns new objects, not the same ones", () => {
  const original = { a: [1] };
  const copy = deepClone(original);
  assert.notEqual(copy, original);
  assert.notEqual(copy.a, original.a);
});

test("deepEqual: equal structures", () => {
  assert.equal(deepEqual({ x: [1, { y: 2 }] }, { x: [1, { y: 2 }] }), true);
  assert.equal(deepEqual([], []), true);
  assert.equal(deepEqual(null, null), true);
  assert.equal(deepEqual("a", "a"), true);
});

test("deepEqual: key order does not matter, array order does", () => {
  assert.equal(deepEqual({ a: 1, b: 2 }, { b: 2, a: 1 }), true);
  assert.equal(deepEqual([1, 2], [2, 1]), false);
});

test("deepEqual: differences are detected", () => {
  assert.equal(deepEqual({ a: 1 }, { a: 2 }), false);
  assert.equal(deepEqual({ a: 1 }, { a: 1, b: 2 }), false);
  assert.equal(deepEqual([1, 2], [1, 2, 3]), false);
  assert.equal(deepEqual({ a: [1] }, { a: [2] }), false);
});

test("deepEqual: different types are never equal", () => {
  assert.equal(deepEqual([], {}), false);
  assert.equal(deepEqual(null, {}), false);
  assert.equal(deepEqual(1, "1"), false);
  assert.equal(deepEqual(0, false), false);
});
