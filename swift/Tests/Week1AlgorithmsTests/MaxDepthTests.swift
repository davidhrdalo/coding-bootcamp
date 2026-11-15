import Testing
@testable import Week1Algorithms

@Suite struct MaxDepthTests {
    @Test func emptyTree() {
        #expect(maxDepth(nil) == 0)
    }

    @Test func singleNode() {
        #expect(maxDepth(TreeNode(1)) == 1)
    }

    @Test func balancedExample() {
        let tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        #expect(maxDepth(tree) == 3)
    }

    @Test func leftLeaningChain() {
        let tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        #expect(maxDepth(tree) == 4)
    }

    @Test func unevenBranches() {
        let tree = TreeNode(1, TreeNode(2), TreeNode(3, nil, TreeNode(4, nil, TreeNode(5))))
        #expect(maxDepth(tree) == 4)
    }
}
