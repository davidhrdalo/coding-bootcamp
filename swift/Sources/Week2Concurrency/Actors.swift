// Actors: safe shared mutable state
//
// Two tasks changing the same variable at the same time is a DATA RACE. Swift's answer is the actor:
// a reference type whose state can only be touched by one task at a time. Calls from outside use
// `await` because they may have to wait their turn.
//
// actor Counter
//     increment() adds 1; value() returns the count. 1,000 concurrent increments must give exactly 1,000.
//
// actor BankAccount
//     init(balance: Int = 0)
//     balance()       the current balance
//     deposit(_:)     add money. Throws BankError.invalidAmount if the amount is not positive.
//     withdraw(_:)    remove money. Throws .invalidAmount if the amount is not positive and
//                     .insufficientFunds if it is more than the balance.
//
// transfer(from:to:amount:)
//     an async throws function that withdraws from one account and deposits into another. If the
//     withdrawal fails, nothing is deposited. The total money across both accounts must never change.
//
// Concepts: actors, actor isolation, await on actor methods, data races, throwing from actors.
// Interview angle: how is an actor different from a class with a lock (or a DispatchQueue)?

actor Counter {
    func increment() {
    }

    func value() -> Int {
        return 0
    }
}

enum BankError: Error, Equatable {
    case invalidAmount
    case insufficientFunds
}

actor BankAccount {
    init(balance: Int = 0) {
    }

    func balance() -> Int {
        return 0
    }

    func deposit(_ amount: Int) throws {
    }

    func withdraw(_ amount: Int) throws {
    }
}

func transfer(from source: BankAccount, to destination: BankAccount, amount: Int) async throws {
}
