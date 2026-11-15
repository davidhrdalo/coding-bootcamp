import Testing
@testable import Week2Concurrency

@Suite struct ActorsTests {
    @Test func counterSurvivesConcurrentIncrements() async {
        let counter = Counter()
        await withTaskGroup(of: Void.self) { group in
            for _ in 0..<1000 {
                group.addTask { await counter.increment() }
            }
        }
        #expect(await counter.value() == 1000)
    }

    @Test func depositAndWithdraw() async throws {
        let account = BankAccount(balance: 100)
        try await account.deposit(50)
        try await account.withdraw(30)
        #expect(await account.balance() == 120)
    }

    @Test func newAccountStartsAtZero() async {
        #expect(await BankAccount().balance() == 0)
    }

    @Test func invalidAmountsAreRejected() async {
        let account = BankAccount(balance: 100)
        await #expect(throws: BankError.invalidAmount) { try await account.deposit(0) }
        await #expect(throws: BankError.invalidAmount) { try await account.deposit(-5) }
        await #expect(throws: BankError.invalidAmount) { try await account.withdraw(0) }
        #expect(await account.balance() == 100)
    }

    @Test func cannotWithdrawMoreThanTheBalance() async {
        let account = BankAccount(balance: 20)
        await #expect(throws: BankError.insufficientFunds) { try await account.withdraw(21) }
        #expect(await account.balance() == 20)
    }

    @Test func transferMovesMoney() async throws {
        let a = BankAccount(balance: 100)
        let b = BankAccount(balance: 0)
        try await transfer(from: a, to: b, amount: 40)
        #expect(await a.balance() == 60)
        #expect(await b.balance() == 40)
    }

    @Test func failedTransferChangesNothing() async {
        let a = BankAccount(balance: 10)
        let b = BankAccount(balance: 0)
        await #expect(throws: BankError.insufficientFunds) {
            try await transfer(from: a, to: b, amount: 50)
        }
        #expect(await a.balance() == 10)
        #expect(await b.balance() == 0)
    }

    @Test func concurrentTransfersNeverCreateOrDestroyMoney() async {
        let a = BankAccount(balance: 500)
        let b = BankAccount(balance: 500)
        await withTaskGroup(of: Void.self) { group in
            for i in 0..<200 {
                group.addTask {
                    if i % 2 == 0 {
                        try? await transfer(from: a, to: b, amount: 3)
                    } else {
                        try? await transfer(from: b, to: a, amount: 2)
                    }
                }
            }
        }
        let total = await a.balance() + b.balance()
        #expect(total == 1000)
    }
}
