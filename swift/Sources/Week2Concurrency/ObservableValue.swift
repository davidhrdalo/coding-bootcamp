// The observer pattern: an observable value
//
// SwiftUI, Combine and every UI framework are built on the observer pattern: something holds a value
// and tells its subscribers when it changes. Build a small version.
//
// ObservableValue<Value>
//     init(_ value: Value)
//     value                 the current value. SETTING it calls every active subscriber with the new
//                           value, in the order they subscribed.
//     subscribe(_ handler)  registers a handler and calls it IMMEDIATELY once with the current value.
//                           It returns a Subscription.
//
// Subscription
//     cancel()              stops that handler from being called again. Cancelling twice is harmless.
//                           Other subscribers are unaffected.
//
// Concepts: observer pattern, closures stored as properties, property observers (didSet), escaping
// closures, capture lists and weak references (a Subscription must not keep the observable alive).

final class Subscription {
    func cancel() {
    }
}

final class ObservableValue<Value> {
    var value: Value

    init(_ value: Value) {
        self.value = value
    }

    func subscribe(_ handler: @escaping (Value) -> Void) -> Subscription {
        return Subscription()
    }
}
