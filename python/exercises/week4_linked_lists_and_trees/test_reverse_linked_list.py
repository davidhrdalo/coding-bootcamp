from reverse_linked_list import ListNode, reverse_list


def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head):
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def test_reverses_several_nodes():
    assert to_list(reverse_list(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]


def test_single_node():
    assert to_list(reverse_list(build([1]))) == [1]


def test_empty_list():
    assert reverse_list(None) is None


def test_reverses_in_place_by_reusing_nodes():
    head = build([1, 2, 3])
    old_nodes = {id(head), id(head.next), id(head.next.next)}
    new_head = reverse_list(head)
    new_nodes = {id(new_head), id(new_head.next), id(new_head.next.next)}
    assert old_nodes == new_nodes
