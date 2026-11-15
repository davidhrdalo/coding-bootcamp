import Testing
@testable import Week0Basics

@Suite struct ValueSemanticsTests {
    @Test func copyingAStructIsIndependentButCopyingAClassIsShared() {
        let result = aliasingDemo()
        #expect(result.structOriginal == 100)
        #expect(result.structCopy == 150)
        #expect(result.classOriginal == 150)
        #expect(result.classCopy == 150)
    }

    @Test func newStackIsEmpty() {
        let stack = Stack<Int>()
        #expect(stack.isEmpty)
        #expect(stack.count == 0)
        #expect(stack.peek() == nil)
    }

    @Test func popReturnsItemsLastInFirstOut() {
        var stack = Stack<String>()
        stack.push("a")
        stack.push("b")
        stack.push("c")
        #expect(stack.pop() == "c")
        #expect(stack.pop() == "b")
        #expect(stack.pop() == "a")
        #expect(stack.pop() == nil)
    }

    @Test func peekDoesNotRemove() {
        var stack = Stack<Int>()
        stack.push(1)
        stack.push(2)
        #expect(stack.peek() == 2)
        #expect(stack.count == 2)
    }

    @Test func countAndIsEmptyTrackContents() {
        var stack = Stack<Int>()
        stack.push(1)
        #expect(!stack.isEmpty)
        stack.push(2)
        #expect(stack.count == 2)
        _ = stack.pop()
        _ = stack.pop()
        #expect(stack.isEmpty)
    }

    @Test func copiesOfAStackAreIndependent() {
        var original = Stack<Int>()
        original.push(1)
        var copy = original
        copy.push(2)
        #expect(original.count == 1)
        #expect(copy.count == 2)
    }
}
