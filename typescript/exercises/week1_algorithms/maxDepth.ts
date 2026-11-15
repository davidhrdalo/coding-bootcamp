/**
 * Maximum depth of a binary tree
 *
 * Each TreeNode has a value, a left child and a right child (either may be null). Return the
 * maximum depth: the number of nodes on the longest path from the root down to a leaf. An empty
 * tree (null) has depth 0.
 *
 * Example: root 3 with children 9 and 20, where 20 has children 15 and 7, has depth 3.
 *
 * Concepts: trees, recursion, base cases. Bonus: write a second version using a queue.
 */

export class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;

  constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

export function maxDepth(root: TreeNode | null): number {
  throw new Error("Not implemented");
}
