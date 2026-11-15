func makeCounter(start: Int = 0) -> (increment: () -> Int, value: () -> Int) {
    var count = start
    return (
        increment: {
            count += 1
            return count
        },
        value: { count }
    )
}

func compose(_ f: @escaping (Int) -> Int, _ g: @escaping (Int) -> Int) -> (Int) -> Int {
    return { g(f($0)) }
}

func once(_ work: @escaping () -> Int) -> () -> Int {
    var result: Int?
    return {
        if let result = result { return result }
        let value = work()
        result = value
        return value
    }
}

func memoize(_ f: @escaping (Int) -> Int) -> (Int) -> Int {
    var cache: [Int: Int] = [:]
    return { input in
        if let cached = cache[input] { return cached }
        let value = f(input)
        cache[input] = value
        return value
    }
}
