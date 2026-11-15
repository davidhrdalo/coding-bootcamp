import { test } from "node:test";
import assert from "node:assert/strict";
import { TreeNode, maxDepth } from "./maxDepth.ts";

test("empty tree", () => {
  assert.equal(maxDepth(null), 0);
});

test("single node", () => {
  assert.equal(maxDepth(new TreeNode(1)), 1);
});

test("balanced example", () => {
  const tree = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
  assert.equal(maxDepth(tree), 3);
});

test("left-leaning chain", () => {
  const tree = new TreeNode(1, new TreeNode(2, new TreeNode(3, new TreeNode(4))));
  assert.equal(maxDepth(tree), 4);
});

test("uneven branches", () => {
  const tree = new TreeNode(
    1,
    new TreeNode(2),
    new TreeNode(3, null, new TreeNode(4, null, new TreeNode(5))),
  );
  assert.equal(maxDepth(tree), 4);
});
