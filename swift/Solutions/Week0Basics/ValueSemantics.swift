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
    let accountA = Account(balance: 100)
    var accountB = accountA
    accountB.balance += 50

    let refA = AccountRef(balance: 100)
    let refB = refA
    refB.balance += 50

    return (accountA.balance, accountB.balance, refA.balance, refB.balance)
}

struct Stack<Element> {
    private var items: [Element] = []

    var count: Int {
        return items.count
    }

    var isEmpty: Bool {
        return items.isEmpty
    }

    mutating func push(_ element: Element) {
        items.append(element)
    }

    mutating func pop() -> Element? {
        return items.popLast()
    }

    func peek() -> Element? {
        return items.last
    }
}
