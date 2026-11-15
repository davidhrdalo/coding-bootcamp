// Reverse a linked list
//
// Each ListNode holds a value and a reference to the next node (nil at the end). Reverse the list IN
// PLACE and return the new head. O(n) time, O(1) extra space.
//
//   1 -> 2 -> 3 -> nil  becomes  3 -> 2 -> 1 -> nil
//
// ListNode is a class (a reference type), so changing `next` changes the shared node.
//
// Concepts: references, optionals, linked lists, in-place algorithms. Draw the nodes on paper first.

final class ListNode {
    var val: Int
    var next: ListNode?

    init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

func reverseList(_ head: ListNode?) -> ListNode? {
    return head
}
