// Closures: counters, compose, once and memoize
//
// A closure is a function that captures variables from the place where it is written, and keeps
// them alive. Closures are everywhere in Swift: callbacks, map/filter, SwiftUI, async code.
// Functions that are stored and called later are marked @escaping.
//
// makeCounter(start:)   returns a pair of closures, increment (adds 1 and returns the new value) and
//                       value (returns the current value), sharing one private count. Each call to
//                       makeCounter creates an independent counter.
// compose(f, g)         returns a function that applies f first and then g: compose(f, g)(x) == g(f(x))
// once(work)            returns a function that runs `work` the first time and afterwards returns the
//                       same result without running `work` again
// memoize(f)            returns a version of f that remembers results: calling it again with the same
//                       input returns the stored answer without calling f again
//
// These use Int to keep the signatures simple. Bonus: make compose, once and memoize generic.
//
// Concepts: closures and capture, @escaping, higher-order functions, private state, caching.
// Danger to know about: a closure stored on an object that captures `self` strongly causes a retain
// cycle; the fix is a capture list such as [weak self].

func makeCounter(start: Int = 0) -> (increment: () -> Int, value: () -> Int) {
    return ({ 0 }, { 0 })
}

func compose(_ f: @escaping (Int) -> Int, _ g: @escaping (Int) -> Int) -> (Int) -> Int {
    return { $0 }
}

func once(_ work: @escaping () -> Int) -> () -> Int {
    return { 0 }
}

func memoize(_ f: @escaping (Int) -> Int) -> (Int) -> Int {
    return f
}
