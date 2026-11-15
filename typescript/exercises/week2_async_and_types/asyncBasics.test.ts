import { test } from "node:test";
import assert from "node:assert/strict";
import { retry, sleep, withTimeout } from "./asyncBasics.ts";

test("sleep resolves after roughly the delay", async () => {
  const start = Date.now();
  const value = await sleep(30);
  assert.equal(value, undefined);
  assert.ok(Date.now() - start >= 25, "should wait about 30ms");
});

test("withTimeout passes through a fast result", async () => {
  const result = await withTimeout(sleep(5).then(() => "ok"), 200);
  assert.equal(result, "ok");
});

test("withTimeout rejects when the promise is too slow", async () => {
  await assert.rejects(withTimeout(sleep(100), 10), { message: "timeout" });
});

test("withTimeout passes through the original rejection", async () => {
  await assert.rejects(withTimeout(Promise.reject(new Error("boom")), 200), { message: "boom" });
});

test("retry returns the first success", async () => {
  let calls = 0;
  const result = await retry(async () => {
    calls++;
    return "done";
  }, 3);
  assert.equal(result, "done");
  assert.equal(calls, 1);
});

test("retry tries again after failures", async () => {
  let calls = 0;
  const result = await retry(async () => {
    calls++;
    if (calls < 3) throw new Error("fail " + calls);
    return "finally";
  }, 5);
  assert.equal(result, "finally");
  assert.equal(calls, 3);
});

test("retry rejects with the last error when attempts run out", async () => {
  let calls = 0;
  await assert.rejects(
    retry(async () => {
      calls++;
      throw new Error("fail " + calls);
    }, 3),
    { message: "fail 3" },
  );
  assert.equal(calls, 3);
});

test("retry requires at least one attempt", async () => {
  await assert.rejects(retry(async () => 1, 0), RangeError);
});
