import { test } from "node:test";
import assert from "node:assert/strict";
import { mapWithConcurrency } from "./concurrency.ts";

const sleep = (ms: number) => new Promise<void>((resolve) => setTimeout(resolve, ms));

test("returns results in the original order", async () => {
  const result = await mapWithConcurrency([30, 5, 15], 2, async (ms, i) => {
    await sleep(ms);
    return i * 10;
  });
  assert.deepEqual(result, [0, 10, 20]);
});

test("never runs more than `limit` calls at once", async () => {
  let running = 0;
  let peak = 0;
  const result = await mapWithConcurrency([1, 2, 3, 4, 5, 6, 7, 8], 3, async (n) => {
    running++;
    peak = Math.max(peak, running);
    await sleep(10);
    running--;
    return n * 2;
  });
  assert.deepEqual(result, [2, 4, 6, 8, 10, 12, 14, 16]);
  assert.equal(peak, 3);
});

test("a limit larger than the number of items is fine", async () => {
  const result = await mapWithConcurrency([1, 2], 10, async (n) => n + 1);
  assert.deepEqual(result, [2, 3]);
});

test("empty input", async () => {
  assert.deepEqual(await mapWithConcurrency([], 3, async (n: number) => n), []);
});

test("a failing call rejects the whole result", async () => {
  await assert.rejects(
    mapWithConcurrency([1, 2, 3], 2, async (n) => {
      if (n === 2) throw new Error("bad item");
      return n;
    }),
    { message: "bad item" },
  );
});

test("limit must be at least 1", async () => {
  await assert.rejects(mapWithConcurrency([1], 0, async (n) => n), RangeError);
});
