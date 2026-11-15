actor Counter {
    private var count = 0

    func increment() {
        count += 1
    }

    func value() -> Int {
        return count
    }
}

enum BankError: Error, Equatable {
    case invalidAmount
    case insufficientFunds
}

actor BankAccount {
    private var money: Int

    init(balance: Int = 0) {
        self.money = balance
    }

    func balance() -> Int {
        return money
    }

    func deposit(_ amount: Int) throws {
        guard amount > 0 else { throw BankError.invalidAmount }
        money += amount
    }

    func withdraw(_ amount: Int) throws {
        guard amount > 0 else { throw BankError.invalidAmount }
        guard amount <= money else { throw BankError.insufficientFunds }
        money -= amount
    }
}

func transfer(from source: BankAccount, to destination: BankAccount, amount: Int) async throws {
    try await source.withdraw(amount)
    try await destination.deposit(amount)
}
