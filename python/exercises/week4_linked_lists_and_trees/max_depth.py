"""Maximum depth of a binary tree

Each TreeNode has a value, a left child and a right child (either may be None).
Return the maximum depth: the number of nodes along the longest path from the
root down to a leaf. An empty tree (None) has depth 0.

Example: the root is 3 with children 9 and 20, and 20 has children 15 and 7.
The longest path is 3 -> 20 -> 15, so the depth is 3.

Concepts: trees, recursion (and the call stack), base cases.
Bonus: write a second version without recursion using a queue or stack.
"""


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: "TreeNode | None") -> int:
    raise NotImplementedError
