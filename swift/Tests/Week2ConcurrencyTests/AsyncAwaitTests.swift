import Testing
@testable import Week2Concurrency

actor Gauge {
    private(set) var current = 0
    private(set) var peak = 0

    func enter() {
        current += 1
        peak = max(peak, current)
    }

    func leave() {
        current -= 1
    }
}

actor CallCounter {
    private(set) var calls = 0

    func record() -> Int {
        calls += 1
        return calls
    }
}

struct Boom: Error, Equatable {
    let message: String
}

@Suite struct AsyncAwaitTests {
    @Test func sleepWaitsForRoughlyTheRequestedTime() async {
        let clock = ContinuousClock()
        let start = clock.now
        await sleep(milliseconds: 30)
        let elapsed = start.duration(to: clock.now)
        #expect(elapsed >= .milliseconds(25))
    }

    @Test func retryReturnsTheFirstSuccess() async throws {
        let counter = CallCounter()
        let result = try await retry(attempts: 3) { () async throws -> String in
            _ = await counter.record()
            return "done"
        }
        #expect(result == "done")
        #expect(await counter.calls == 1)
    }

    @Test func retryTriesAgainAfterFailures() async throws {
        let counter = CallCounter()
        let result = try await retry(attempts: 5) { () async throws -> String in
            let call = await counter.record()
            if call < 3 { throw Boom(message: "fail \(call)") }
            return "finally"
        }
        #expect(result == "finally")
        #expect(await counter.calls == 3)
    }

    @Test func retryThrowsTheLastErrorWhenAttemptsRunOut() async {
        let counter = CallCounter()
        await #expect(throws: Boom(message: "fail 3")) {
            try await retry(attempts: 3) { () async throws -> Int in
                let call = await counter.record()
                throw Boom(message: "fail \(call)")
            }
        }
        #expect(await counter.calls == 3)
    }

    @Test func retryNeedsAtLeastOneAttempt() async {
        await #expect(throws: TaskError.invalidAttempts) {
            try await retry(attempts: 0) { () async throws -> Int in 1 }
        }
    }

    @Test func fetchAllKeepsTheOriginalOrder() async {
        let results = await fetchAll(ids: [3, 1, 2]) { id in
            try? await Task.sleep(nanoseconds: UInt64(id) * 20_000_000)   // id 1 finishes first
            return "item\(id)"
        }
        #expect(results == ["item3", "item1", "item2"])
    }

    @Test func fetchAllRunsTheRequestsConcurrently() async {
        let gauge = Gauge()
        _ = await fetchAll(ids: Array(1...5)) { id in
            await gauge.enter()
            try? await Task.sleep(nanoseconds: 30_000_000)
            await gauge.leave()
            return "item\(id)"
        }
        #expect(await gauge.peak > 1, "requests should overlap")
    }

    @Test func mapWithConcurrencyKeepsOrderAndRespectsTheLimit() async throws {
        let gauge = Gauge()
        let results = try await mapWithConcurrency(Array(1...8), limit: 3) { n in
            await gauge.enter()
            try await Task.sleep(nanoseconds: 15_000_000)
            await gauge.leave()
            return n * 2
        }
        #expect(results == [2, 4, 6, 8, 10, 12, 14, 16])
        #expect(await gauge.peak == 3)
    }

    @Test func mapWithConcurrencyHandlesEdgeCases() async throws {
        let empty: [Int] = try await mapWithConcurrency([Int](), limit: 3) { $0 }
        #expect(empty == [])
        let wide = try await mapWithConcurrency([1, 2], limit: 10) { $0 + 1 }
        #expect(wide == [2, 3])
    }

    @Test func mapWithConcurrencyPropagatesErrors() async {
        await #expect(throws: Boom(message: "bad item")) {
            try await mapWithConcurrency([1, 2, 3], limit: 2) { (n: Int) async throws -> Int in
                if n == 2 { throw Boom(message: "bad item") }
                return n
            }
        }
    }

    @Test func mapWithConcurrencyNeedsPositiveLimit() async {
        await #expect(throws: TaskError.invalidLimit) {
            try await mapWithConcurrency([1], limit: 0) { $0 }
        }
    }
}
