import { test } from "node:test";
import assert from "node:assert/strict";
import { ListNode, reverseList } from "./reverseList.ts";

function build(values: number[]): ListNode | null {
  let head: ListNode | null = null;
  for (const v of [...values].reverse()) head = new ListNode(v, head);
  return head;
}

function toArray(head: ListNode | null): number[] {
  const out: number[] = [];
  for (let node = head; node !== null; node = node.next) out.push(node.val);
  return out;
}

test("reverses several nodes", () => {
  assert.deepEqual(toArray(reverseList(build([1, 2, 3, 4, 5]))), [5, 4, 3, 2, 1]);
});

test("single node and empty list", () => {
  assert.deepEqual(toArray(reverseList(build([1]))), [1]);
  assert.equal(reverseList(null), null);
});

test("reuses the existing nodes (in place)", () => {
  const head = build([1, 2, 3]) as ListNode;
  const second = head.next as ListNode;
  const third = second.next as ListNode;
  const newHead = reverseList(head);
  assert.equal(newHead, third);
  assert.equal(newHead?.next, second);
  assert.equal(second.next, head);
  assert.equal(head.next, null);
});
