"""Binary search tree

A binary search tree (BST) keeps its values ordered: for every node, all values in
its left subtree are smaller and all values in its right subtree are larger.
That makes searching O(log n) when the tree is balanced.

Implement BST with:
  insert(value)   add the value; ignore it if it is already present
  contains(value) True if the value is in the tree
  inorder()       list of all values in ascending order (left, node, right)
  height()        number of nodes on the longest root-to-leaf path (empty tree: 0)
  len(tree)       number of values stored (implement __len__)

Concepts: tree traversal, ordering invariants, balance. Notice what happens to
height() when you insert already-sorted values: the tree degrades into a linked
list (O(n) search). Real systems use self-balancing trees (AVL, red-black) to avoid that.
"""


class BST:
    def __init__(self) -> None:
        raise NotImplementedError

    def insert(self, value: int) -> None:
        raise NotImplementedError

    def contains(self, value: int) -> bool:
        raise NotImplementedError

    def inorder(self) -> list[int]:
        raise NotImplementedError

    def height(self) -> int:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
