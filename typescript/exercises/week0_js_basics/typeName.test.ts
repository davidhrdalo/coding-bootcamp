import { test } from "node:test";
import assert from "node:assert/strict";
import { typeName } from "./typeName.ts";

test("primitives", () => {
  assert.equal(typeName("hi"), "string");
  assert.equal(typeName(5), "number");
  assert.equal(typeName(true), "boolean");
  assert.equal(typeName(undefined), "undefined");
  assert.equal(typeName(10n), "bigint");
  assert.equal(typeName(Symbol("x")), "symbol");
});

test("null is not an object", () => {
  assert.equal(typeName(null), "null");
});

test("arrays, dates, functions and plain objects", () => {
  assert.equal(typeName([]), "array");
  assert.equal(typeName([1, 2]), "array");
  assert.equal(typeName(new Date()), "date");
  assert.equal(typeName(() => 1), "function");
  assert.equal(typeName({}), "object");
  assert.equal(typeName({ a: 1 }), "object");
});

test("NaN is a number that is not a number", () => {
  assert.equal(typeName(NaN), "nan");
  assert.equal(typeName(0), "number");
  assert.equal(typeName(Infinity), "number");
});
