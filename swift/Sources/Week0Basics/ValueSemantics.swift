// Value types versus reference types
//
// In Swift, struct and enum are VALUE types: assigning one makes an independent copy.
// class is a REFERENCE type: assigning one makes a second name for the same object. This difference
// is one of the most common Swift interview questions.
//
// aliasingDemo()
//     Start with an Account (a struct) and an AccountRef (a class), both with balance 100. For each,
//     make a copy (let/var copy = original), add 50 to the COPY, and return all four balances:
//     (structOriginal, structCopy, classOriginal, classCopy). You should be able to predict the
//     result before running it: only one of the two originals changes.
//
// Stack<Element>
//     A generic stack that is a STRUCT. push and pop are `mutating` because they change the struct.
//       push(_:)    add to the top
//       pop()       remove and return the top element, or nil if empty
//       peek()      the top element without removing it, or nil if empty
//       count, isEmpty
//     Because it is a value type, copying a stack gives an independent stack.
//
// Concepts: struct vs class, copy semantics, mutating, generics, Optional return values.

struct Account {
    var balance: Int
}

final class AccountRef {
    var balance: Int

    init(balance: Int) {
        self.balance = balance
    }
}

func aliasingDemo() -> (structOriginal: Int, structCopy: Int, classOriginal: Int, classCopy: Int) {
    return (0, 0, 0, 0)
}

struct Stack<Element> {
    var count: Int {
        return 0
    }

    var isEmpty: Bool {
        return true
    }

    mutating func push(_ element: Element) {
    }

    mutating func pop() -> Element? {
        return nil
    }

    func peek() -> Element? {
        return nil
    }
}
