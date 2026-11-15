import Testing
@testable import Week1Algorithms

@Suite struct ReverseListTests {
    private func build(_ values: [Int]) -> ListNode? {
        var head: ListNode? = nil
        for value in values.reversed() {
            head = ListNode(value, head)
        }
        return head
    }

    private func toArray(_ head: ListNode?) -> [Int] {
        var result: [Int] = []
        var node = head
        while let current = node {
            result.append(current.val)
            node = current.next
        }
        return result
    }

    @Test func reversesSeveralNodes() {
        #expect(toArray(reverseList(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1])
    }

    @Test func singleNodeAndEmptyList() {
        #expect(toArray(reverseList(build([1]))) == [1])
        #expect(reverseList(nil) == nil)
    }

    @Test func reusesTheExistingNodes() {
        let first = ListNode(1)
        let second = ListNode(2)
        let third = ListNode(3)
        first.next = second
        second.next = third
        let newHead = reverseList(first)
        #expect(newHead === third)
        #expect(newHead?.next === second)
        #expect(second.next === first)
        #expect(first.next == nil)
    }
}
