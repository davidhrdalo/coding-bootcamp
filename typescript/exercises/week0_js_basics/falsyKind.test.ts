import { test } from "node:test";
import assert from "node:assert/strict";
import { falsyKind } from "./falsyKind.ts";

test("the falsy values", () => {
  assert.equal(falsyKind(null), "null");
  assert.equal(falsyKind(undefined), "undefined");
  assert.equal(falsyKind(false), "false");
  assert.equal(falsyKind(NaN), "nan");
  assert.equal(falsyKind(0), "zero");
  assert.equal(falsyKind(-0), "zero");
  assert.equal(falsyKind(0n), "zero");
  assert.equal(falsyKind(""), "empty-string");
});

test("surprising truthy values", () => {
  assert.equal(falsyKind("0"), "truthy");
  assert.equal(falsyKind("false"), "truthy");
  assert.equal(falsyKind([]), "truthy");
  assert.equal(falsyKind({}), "truthy");
  assert.equal(falsyKind(() => 0), "truthy");
  assert.equal(falsyKind(new Date()), "truthy");
});

test("ordinary truthy values", () => {
  assert.equal(falsyKind(true), "truthy");
  assert.equal(falsyKind(1), "truthy");
  assert.equal(falsyKind(-1), "truthy");
  assert.equal(falsyKind("hi"), "truthy");
  assert.equal(falsyKind(Infinity), "truthy");
});
