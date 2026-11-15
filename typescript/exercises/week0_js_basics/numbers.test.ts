import { test } from "node:test";
import assert from "node:assert/strict";
import { areClose, factorialBig } from "./numbers.ts";

test("the classic float example", () => {
  assert.equal(0.1 + 0.2 === 0.3, false); // this is why areClose exists
  assert.equal(areClose(0.1 + 0.2, 0.3), true);
});

test("clearly different numbers", () => {
  assert.equal(areClose(1, 1.1), false);
});

test("relative tolerance scales with size", () => {
  assert.equal(areClose(1e10, 1e10 + 1), true);
  assert.equal(areClose(1e10, 1e10 + 100), false);
});

test("near zero needs an absolute tolerance", () => {
  assert.equal(areClose(0, 1e-12), false);
  assert.equal(areClose(0, 1e-12, 1e-9, 1e-9), true);
});

test("integers stop being exact above MAX_SAFE_INTEGER", () => {
  assert.equal(Number.MAX_SAFE_INTEGER + 1 === Number.MAX_SAFE_INTEGER + 2, true);
});

test("factorialBig stays exact for large values", () => {
  assert.equal(factorialBig(0), 1n);
  assert.equal(factorialBig(5), 120n);
  assert.equal(factorialBig(20), 2432902008176640000n);
  assert.equal(factorialBig(25), 15511210043330985984000000n);
});

test("factorialBig rejects invalid input", () => {
  assert.throws(() => factorialBig(-1), RangeError);
  assert.throws(() => factorialBig(2.5), RangeError);
});
