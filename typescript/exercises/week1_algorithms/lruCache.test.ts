import { test } from "node:test";
import assert from "node:assert/strict";
import { LRUCache } from "./lruCache.ts";

test("capacity must be at least 1", () => {
  assert.throws(() => new LRUCache<number, number>(0), RangeError);
});

test("stores and retrieves values", () => {
  const cache = new LRUCache<string, number>(2);
  cache.put("a", 1);
  cache.put("b", 2);
  assert.equal(cache.get("a"), 1);
  assert.equal(cache.get("b"), 2);
  assert.equal(cache.get("missing"), undefined);
});

test("evicts the least recently used entry", () => {
  const cache = new LRUCache<number, number>(2);
  cache.put(1, 1);
  cache.put(2, 2);
  assert.equal(cache.get(1), 1); // 1 is now more recent than 2
  cache.put(3, 3); // evicts 2
  assert.equal(cache.get(2), undefined);
  cache.put(4, 4); // evicts 1
  assert.equal(cache.get(1), undefined);
  assert.equal(cache.get(3), 3);
  assert.equal(cache.get(4), 4);
});

test("updating an existing key does not evict and refreshes it", () => {
  const cache = new LRUCache<string, number>(2);
  cache.put("a", 1);
  cache.put("b", 2);
  cache.put("a", 10); // update, "b" is now least recent
  cache.put("c", 3); // evicts "b"
  assert.equal(cache.get("a"), 10);
  assert.equal(cache.get("b"), undefined);
  assert.equal(cache.get("c"), 3);
});

test("size never exceeds capacity", () => {
  const cache = new LRUCache<number, number>(3);
  for (let i = 0; i < 10; i++) cache.put(i, i);
  assert.equal(cache.size, 3);
});

test("a stored falsy value is still a hit", () => {
  const cache = new LRUCache<string, number>(1);
  cache.put("zero", 0);
  assert.equal(cache.get("zero"), 0);
});

test("works at scale", () => {
  const cache = new LRUCache<number, number>(1000);
  for (let i = 0; i < 200_000; i++) cache.put(i, i);
  assert.equal(cache.size, 1000);
  assert.equal(cache.get(199_999), 199_999);
  assert.equal(cache.get(0), undefined);
});
