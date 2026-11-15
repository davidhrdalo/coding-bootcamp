import { test } from "node:test";
import assert from "node:assert/strict";
import { wordCount } from "./wordCount.ts";

test("basic sentence", () => {
  assert.deepEqual(
    wordCount("The cat and the hat."),
    new Map([["the", 2], ["cat", 1], ["and", 1], ["hat", 1]]),
  );
});

test("case insensitive", () => {
  assert.deepEqual(wordCount("Go go GO"), new Map([["go", 3]]));
});

test("punctuation separates words", () => {
  assert.deepEqual(wordCount("hello,world! hello?"), new Map([["hello", 2], ["world", 1]]));
});

test("apostrophes and digits are kept", () => {
  assert.deepEqual(
    wordCount("don't stop 2 stop"),
    new Map([["don't", 1], ["stop", 2], ["2", 1]]),
  );
});

test("empty text", () => {
  assert.equal(wordCount("").size, 0);
  assert.equal(wordCount("  ...  ").size, 0);
});
