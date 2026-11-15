import Testing
@testable import Week2Concurrency

@Suite struct ObservableValueTests {
    @Test func subscribingDeliversTheCurrentValueImmediately() {
        let observable = ObservableValue(5)
        var received: [Int] = []
        _ = observable.subscribe { received.append($0) }
        #expect(received == [5])
    }

    @Test func changingTheValueNotifiesSubscribers() {
        let observable = ObservableValue("a")
        var received: [String] = []
        _ = observable.subscribe { received.append($0) }
        observable.value = "b"
        observable.value = "c"
        #expect(received == ["a", "b", "c"])
    }

    @Test func subscribersAreCalledInSubscriptionOrder() {
        let observable = ObservableValue(0)
        var log: [String] = []
        _ = observable.subscribe { log.append("first:\($0)") }
        _ = observable.subscribe { log.append("second:\($0)") }
        log.removeAll()
        observable.value = 1
        #expect(log == ["first:1", "second:1"])
    }

    @Test func cancelStopsFurtherNotifications() {
        let observable = ObservableValue(0)
        var received: [Int] = []
        let subscription = observable.subscribe { received.append($0) }
        observable.value = 1
        subscription.cancel()
        observable.value = 2
        #expect(received == [0, 1])
    }

    @Test func cancelOnlyAffectsThatSubscriber() {
        let observable = ObservableValue(0)
        var first: [Int] = []
        var second: [Int] = []
        let subscription = observable.subscribe { first.append($0) }
        _ = observable.subscribe { second.append($0) }
        subscription.cancel()
        observable.value = 9
        #expect(first == [0])
        #expect(second == [0, 9])
    }

    @Test func cancellingTwiceIsHarmless() {
        let observable = ObservableValue(0)
        var received: [Int] = []
        let subscription = observable.subscribe { received.append($0) }
        subscription.cancel()
        subscription.cancel()
        observable.value = 1
        #expect(received == [0])
    }

    @Test func aSubscriptionDoesNotKeepTheObservableAlive() {
        var subscription: Subscription?
        weak var weakObservable: ObservableValue<Int>?
        do {
            let observable = ObservableValue(1)
            weakObservable = observable
            subscription = observable.subscribe { _ in }
        }
        #expect(weakObservable == nil)
        subscription?.cancel()   // must not crash after the observable is gone
    }
}
