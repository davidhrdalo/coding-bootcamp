from max_depth import TreeNode, max_depth


def test_empty_tree():
    assert max_depth(None) == 0


def test_single_node():
    assert max_depth(TreeNode(1)) == 1


def test_balanced_example():
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(tree) == 3


def test_left_leaning_chain():
    tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert max_depth(tree) == 4


def test_uneven_branches():
    tree = TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(4, None, TreeNode(5))))
    assert max_depth(tree) == 4
