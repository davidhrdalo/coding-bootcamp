import { test } from "node:test";
import assert from "node:assert/strict";
import { isValidParentheses } from "./validParentheses.ts";

test("valid examples", () => {
  assert.equal(isValidParentheses("()"), true);
  assert.equal(isValidParentheses("()[]{}"), true);
  assert.equal(isValidParentheses("{[()]}"), true);
});

test("wrong type and wrong order", () => {
  assert.equal(isValidParentheses("(]"), false);
  assert.equal(isValidParentheses("([)]"), false);
});

test("unclosed and unopened", () => {
  assert.equal(isValidParentheses("("), false);
  assert.equal(isValidParentheses(")"), false);
  assert.equal(isValidParentheses("(()"), false);
});

test("empty string is valid", () => {
  assert.equal(isValidParentheses(""), true);
});
