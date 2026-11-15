# 14 - Swift essentials

The Swift track (`swift/`) practises these. They are the topics iOS interviews return to again and
again, and the ones that explain *why* Swift code looks the way it does.

## Optionals

- An `Optional<T>` (written `T?`) is an enum: either `.some(value)` or `.none` (`nil`). The compiler will not let you use it as a plain `T` until you unwrap it.
- Safe unwrapping: `if let`, `guard let` (exit early, keep the unwrapped value for the rest of the function), `??` (default value), optional chaining `a?.b?.c`, `map` / `flatMap` on optionals.
- **Force unwrap `!`** crashes on nil. Use it only when nil would be a programmer error, and prefer a clear `guard` or `preconditionFailure`.
- `if let x` shorthand (Swift 5.7+) unwraps into the same name.

## Value types vs reference types (the classic question)

| | `struct` / `enum` | `class` |
|---|---|---|
| Assignment | copies the value | copies the reference (shared object) |
| Identity | none (`==` compares values) | has identity (`===`) |
| Inheritance | no | yes |
| Mutation | needs `var`; methods that change it are `mutating` | changes through any reference |
| Memory | usually inline or on the stack | heap, managed by ARC |

- Apple's guidance: **start with a struct**; use a class when you need shared mutable state, identity, inheritance or Objective-C interop.
- **Copy-on-write:** `Array`, `Dictionary`, `String` are structs, but they share their storage until one copy is mutated, so copying is cheap.
- Passing a struct to a function gives the function its own copy; use `inout` to let it modify the caller's value.

## ARC and retain cycles

- **ARC** (Automatic Reference Counting) frees a class instance when its strong reference count reaches zero. There is no garbage collector, and it is deterministic.
- **Retain cycle:** A holds B strongly and B holds A strongly, so neither is freed (a leak). `RetainCycles.swift` makes you fix one.
- **`weak`:** does not increase the count, is an optional `var`, becomes `nil` automatically when the object is freed. Use for delegates and back-references to a parent.
- **`unowned`:** does not increase the count, is non-optional, and **crashes** if the object is gone. Use only when the other object is guaranteed to outlive this one.
- **Closures capture strongly by default.** A closure stored on an object that uses `self` creates a cycle unless you write a capture list: `{ [weak self] in guard let self else { return }; ... }`. Closures that run immediately (`map`, `filter`) do not need it.

## Closures

- Closures capture variables **by reference**, so a captured `var` is shared and can change.
- `@escaping` marks a closure that outlives the function call (stored or run later). Non-escaping closures (the default) cannot be stored.
- Trailing closure syntax, shorthand `$0`, `$1`, and higher-order functions: `map`, `filter`, `reduce`, `compactMap`, `flatMap`, `sorted(by:)`.

## Protocols, generics and extensions

- **Protocol-oriented programming:** define behaviour with protocols, add default implementations in **protocol extensions**, and conform value types to them. Prefer composition over class inheritance.
- **Generics:** `func f<T: Equatable>(_ x: T)`. Use `where` clauses for extra constraints (`extension Sequence where Element: Numeric`).
- **`some` vs `any`:** `some Shape` is one specific hidden type (fast, resolved at compile time; SwiftUI's `some View`). `any Shape` is an existential box that can hold different types at runtime (flexible, slightly slower).
- **Associated types** make protocols generic (`Sequence.Element`), which is why such protocols cannot be used as plain types without `some`/`any`.
- **Extensions** add methods, computed properties, initialisers and protocol conformances to existing types, including standard-library ones.

## Enums, pattern matching and errors

- Enums can carry **associated values** and have methods; `switch` must be **exhaustive**. `indirect` enums can contain themselves (trees).
- `if case let .number(n) = expr` and `guard case` match a single pattern.
- **Errors:** `throws`, `try`, `try?` (nil on error), `try!` (crash on error), `do { } catch`, and `Result<Success, Failure>`. Custom errors conform to `Error`. Mark functions that call throwing closures with `rethrows`.
- `defer` runs code when leaving the scope: good for cleanup.

## Concurrency (Swift 5.5+)

- **`async`/`await`:** a function marked `async` can suspend; `await` marks the suspension points. It does not block the thread.
- **Structured concurrency:** `async let` and task groups start **child tasks** that finish before the parent does, and cancellation flows down. `Task { }` starts an unstructured task; `Task.detached` also drops the surrounding context.
- **Actors:** a reference type that serialises access to its mutable state. Calls from outside need `await`. **Reentrancy:** while an actor method is suspended at an `await`, other calls can run, so state may change across the `await`; re-check assumptions after it.
- **`@MainActor`:** runs code on the main thread. UI updates must be on it; mark view models `@MainActor`.
- **`Sendable`:** a type that is safe to pass across concurrency boundaries (value types of Sendable data, immutable classes, actors). Swift 6's strict mode turns data races into compile errors.
- **Older tools you will still meet:** Grand Central Dispatch (`DispatchQueue.main.async`), `OperationQueue`, completion handlers, and Combine publishers.

## Memory and performance

- Avoid unnecessary copies of large structs; arrays use copy-on-write.
- `final` on a class (and `private`) lets the compiler optimise method calls.
- `lazy var` computes a stored property on first use.
- Use **Instruments** (Time Profiler, Leaks, Allocations) and the memory graph debugger to find leaks and cycles.

## SwiftUI and app architecture (usual for iOS roles)

- **SwiftUI is declarative:** a `View` is a struct describing the UI for the current state; when state changes, SwiftUI recomputes the body and updates only what changed.
- **State tools:** `@State` (local value state owned by the view), `@Binding` (a two-way reference to someone else's state), `@StateObject` / `@ObservedObject` (view owns / observes an `ObservableObject`), `@EnvironmentObject` / `@Environment` (injected), and in iOS 17+ the `@Observable` macro with plain `@State`/`@Bindable`.
- **MVVM:** view -> view model (holds state and logic, no UI types) -> model/services. Inject dependencies through initialisers for testing.
- **UIKit still matters:** view controllers, the lifecycle (`viewDidLoad`, `viewWillAppear`), Auto Layout, `UITableView` cell reuse, and bridging with `UIViewRepresentable`.
- **Persistence and networking:** `Codable` + `URLSession` (`async` APIs), `UserDefaults`, Keychain for secrets, Core Data or SwiftData for databases.
- **Testing:** unit tests with Swift Testing (`@Test`, `#expect`) or XCTest, UI tests with XCUITest, and protocols plus fakes to replace network and storage.

## Interview questions

1. What is the difference between a struct and a class? When do you choose each?
2. How does ARC work? What is a retain cycle, and how do `weak` and `unowned` differ?
3. Why use `[weak self]` in a closure, and when is it unnecessary?
4. What is an optional? Name four ways to unwrap one, and say why force-unwrapping is risky.
5. What is the difference between `some` and `any`?
6. What is a protocol extension, and what is protocol-oriented programming?
7. How does `async`/`await` differ from completion handlers and GCD? What is an actor and what problem does it solve?
8. What is `@MainActor`, and why must UI updates happen on the main thread?
9. What does `Sendable` mean?
10. What is copy-on-write?
11. Explain `@State`, `@Binding` and `@ObservedObject` (or `@Observable`).
12. How would you decode JSON with different key names into a struct?

## Learn more

- [The Swift Programming Language (official book)](https://docs.swift.org/swift-book/)
- [Swift API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/)
- [Swift Testing documentation](https://developer.apple.com/documentation/testing)
- [Hacking with Swift](https://www.hackingwithswift.com/) and [100 Days of SwiftUI](https://www.hackingwithswift.com/100/swiftui)
- [Swift by Sundell](https://www.swiftbysundell.com/): articles and a podcast
- [Apple's SwiftUI tutorials](https://developer.apple.com/tutorials/swiftui)
- [Stanford CS193p: Developing Apps for iOS](https://cs193p.sites.stanford.edu/)
- [Point-Free](https://www.pointfree.co/) and [objc.io](https://www.objc.io/): deeper, advanced Swift
- [WWDC session videos](https://developer.apple.com/videos/): search for "Swift concurrency", "ARC" and "SwiftUI data flow"
- [Exercism: Swift track](https://exercism.org/tracks/swift)
