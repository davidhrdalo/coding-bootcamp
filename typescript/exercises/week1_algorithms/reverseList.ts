/**
 * Reverse a linked list
 *
 * Each ListNode holds a value and a reference to the next node (null at the end). Reverse the
 * list IN PLACE and return the new head. O(n) time, O(1) extra space.
 *
 *   1 -> 2 -> 3 -> null  becomes  3 -> 2 -> 1 -> null
 *
 * Concepts: references, linked lists. Draw the nodes on paper first.
 */

export class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val = 0, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

export function reverseList(head: ListNode | null): ListNode | null {
  throw new Error("Not implemented");
}
