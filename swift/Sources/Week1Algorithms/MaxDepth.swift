// Maximum depth of a binary tree
//
// Each TreeNode has a value, a left child and a right child (either may be nil). Return the maximum
// depth: the number of nodes on the longest path from the root down to a leaf. An empty tree (nil)
// has depth 0.
//
// Example: root 3 with children 9 and 20, where 20 has children 15 and 7, has depth 3.
//
// Concepts: trees, recursion, base cases, optionals. Bonus: write a second version with a queue.

final class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?

    init(_ val: Int = 0, _ left: TreeNode? = nil, _ right: TreeNode? = nil) {
        self.val = val
        self.left = left
        self.right = right
    }
}

func maxDepth(_ root: TreeNode?) -> Int {
    return 0
}
