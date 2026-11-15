from bst import BST


def build(values):
    tree = BST()
    for v in values:
        tree.insert(v)
    return tree


def test_empty_tree():
    t = BST()
    assert len(t) == 0
    assert t.height() == 0
    assert t.inorder() == []
    assert t.contains(1) is False


def test_insert_and_contains():
    t = build([5, 3, 8, 1, 4])
    for v in (5, 3, 8, 1, 4):
        assert t.contains(v) is True
    assert t.contains(7) is False


def test_inorder_is_sorted():
    t = build([5, 3, 8, 1, 4, 9, 7])
    assert t.inorder() == [1, 3, 4, 5, 7, 8, 9]


def test_duplicates_are_ignored():
    t = build([2, 2, 2, 1, 1])
    assert len(t) == 2
    assert t.inorder() == [1, 2]


def test_height_of_a_balanced_tree():
    t = build([4, 2, 6, 1, 3, 5, 7])
    assert t.height() == 3


def test_sorted_inserts_degrade_into_a_chain():
    t = build(range(1, 401))
    assert t.height() == 400
    assert t.inorder() == list(range(1, 401))


def test_negative_numbers():
    t = build([0, -5, 5, -10])
    assert t.inorder() == [-10, -5, 0, 5]
