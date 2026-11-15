import Testing
@testable import Week0Basics

@Suite struct ClosuresTests {
    @Test func counterCountsUp() {
        let counter = makeCounter()
        #expect(counter.increment() == 1)
        #expect(counter.increment() == 2)
        #expect(counter.value() == 2)
    }

    @Test func counterStartsWhereAsked() {
        #expect(makeCounter(start: 10).increment() == 11)
    }

    @Test func eachCounterHasItsOwnState() {
        let a = makeCounter()
        let b = makeCounter()
        _ = a.increment()
        _ = a.increment()
        #expect(a.value() == 2)
        #expect(b.value() == 0)
    }

    @Test func composeAppliesTheFirstFunctionFirst() {
        let addOneThenDouble = compose({ $0 + 1 }, { $0 * 2 })
        #expect(addOneThenDouble(3) == 8)
        let doubleThenAddOne = compose({ $0 * 2 }, { $0 + 1 })
        #expect(doubleThenAddOne(3) == 7)
    }

    @Test func onceRunsTheWorkASingleTime() {
        var calls = 0
        let load = once {
            calls += 1
            return 42
        }
        #expect(load() == 42)
        #expect(load() == 42)
        #expect(calls == 1)
    }

    @Test func memoizeRemembersResults() {
        var calls = 0
        let square = memoize { (n: Int) -> Int in
            calls += 1
            return n * n
        }
        #expect(square(4) == 16)
        #expect(square(4) == 16)
        #expect(calls == 1)
        #expect(square(5) == 25)
        #expect(calls == 2)
    }

    @Test func memoizeRemembersZeroResultsToo() {
        var calls = 0
        let zero = memoize { (_: Int) -> Int in
            calls += 1
            return 0
        }
        _ = zero(1)
        _ = zero(1)
        #expect(calls == 1)
    }
}
