import { test } from "node:test";
import assert from "node:assert/strict";
import { makeCounter, memoize, once } from "./closures.ts";

test("counter counts up and down", () => {
  const c = makeCounter();
  assert.equal(c.increment(), 1);
  assert.equal(c.increment(), 2);
  assert.equal(c.decrement(), 1);
  assert.equal(c.value(), 1);
});

test("counter accepts a starting value", () => {
  assert.equal(makeCounter(10).increment(), 11);
});

test("each counter has its own private state", () => {
  const a = makeCounter();
  const b = makeCounter();
  a.increment();
  a.increment();
  assert.equal(a.value(), 2);
  assert.equal(b.value(), 0);
});

test("once calls the function a single time", () => {
  let calls = 0;
  const init = once(() => {
    calls++;
    return "ready";
  });
  assert.equal(init(), "ready");
  assert.equal(init(), "ready");
  assert.equal(calls, 1);
});

test("memoize caches results per argument", () => {
  let calls = 0;
  const square = memoize((n: number) => {
    calls++;
    return n * n;
  });
  assert.equal(square(4), 16);
  assert.equal(square(4), 16);
  assert.equal(calls, 1);
  assert.equal(square(5), 25);
  assert.equal(calls, 2);
});

test("memoize remembers falsy results too", () => {
  let calls = 0;
  const zero = memoize((_n: number) => {
    calls++;
    return 0;
  });
  zero(1);
  zero(1);
  assert.equal(calls, 1);
});
