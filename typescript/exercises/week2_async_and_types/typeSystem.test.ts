import { test } from "node:test";
import assert from "node:assert/strict";
import { area, err, isShape, mapResult, ok, parseNumber } from "./typeSystem.ts";

const close = (a: number, b: number) => Math.abs(a - b) < 1e-9;

test("area of each shape", () => {
  assert.ok(close(area({ kind: "circle", radius: 2 }), Math.PI * 4));
  assert.equal(area({ kind: "rectangle", width: 3, height: 4 }), 12);
  assert.equal(area({ kind: "square", side: 5 }), 25);
});

test("isShape accepts valid shapes", () => {
  assert.equal(isShape({ kind: "circle", radius: 1 }), true);
  assert.equal(isShape({ kind: "rectangle", width: 2, height: 3 }), true);
  assert.equal(isShape({ kind: "square", side: 4 }), true);
});

test("isShape rejects non-objects and unknown kinds", () => {
  assert.equal(isShape(null), false);
  assert.equal(isShape(undefined), false);
  assert.equal(isShape("circle"), false);
  assert.equal(isShape(42), false);
  assert.equal(isShape([]), false);
  assert.equal(isShape({ kind: "triangle", base: 1 }), false);
  assert.equal(isShape({}), false);
});

test("isShape rejects missing or invalid dimensions", () => {
  assert.equal(isShape({ kind: "circle" }), false);
  assert.equal(isShape({ kind: "circle", radius: -1 }), false);
  assert.equal(isShape({ kind: "circle", radius: 0 }), false);
  assert.equal(isShape({ kind: "circle", radius: "2" }), false);
  assert.equal(isShape({ kind: "circle", radius: NaN }), false);
  assert.equal(isShape({ kind: "circle", radius: Infinity }), false);
  assert.equal(isShape({ kind: "rectangle", width: 2 }), false);
  assert.equal(isShape({ kind: "square", side: null }), false);
});

test("ok and err build tagged results", () => {
  assert.deepEqual(ok(5), { ok: true, value: 5 });
  assert.deepEqual(err("bad"), { ok: false, error: "bad" });
});

test("mapResult transforms ok values and leaves errors alone", () => {
  assert.deepEqual(mapResult(ok(2), (n: number) => n * 10), ok(20));
  let called = false;
  const failed = mapResult(err("nope"), (n: number) => {
    called = true;
    return n;
  });
  assert.deepEqual(failed, err("nope"));
  assert.equal(called, false);
});

test("parseNumber", () => {
  assert.deepEqual(parseNumber("42"), ok(42));
  assert.deepEqual(parseNumber(" 3.5 "), ok(3.5));
  assert.deepEqual(parseNumber("-7"), ok(-7));
  assert.deepEqual(parseNumber(""), err("empty"));
  assert.deepEqual(parseNumber("   "), err("empty"));
  assert.deepEqual(parseNumber("abc"), err("not a number"));
  assert.deepEqual(parseNumber("12abc"), err("not a number"));
  assert.deepEqual(parseNumber("Infinity"), err("not a number"));
});
