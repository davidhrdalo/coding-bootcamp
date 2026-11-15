"""Reverse a linked list

A singly linked list is made of ListNode objects, each holding a value and a
reference to the next node (None at the end). Reverse the list and return the
new head. Do it in place, in O(n) time and O(1) extra space.

Example: 1 -> 2 -> 3 -> None becomes 3 -> 2 -> 1 -> None

Concepts: references/pointers, linked lists. This is a very common interview
question. Draw the nodes on paper first.
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def reverse_list(head: "ListNode | None") -> "ListNode | None":
    raise NotImplementedError
