enum TaskError: Error, Equatable {
    case invalidAttempts
    case invalidLimit
}

func sleep(milliseconds: Int) async {
    try? await Task.sleep(nanoseconds: UInt64(milliseconds) * 1_000_000)
}

func retry<T>(attempts: Int, operation: () async throws -> T) async throws -> T {
    guard attempts >= 1 else { throw TaskError.invalidAttempts }
    var lastError: Error = TaskError.invalidAttempts
    for _ in 0..<attempts {
        do {
            return try await operation()
        } catch {
            lastError = error
        }
    }
    throw lastError
}

func fetchAll(ids: [Int], fetch: @escaping @Sendable (Int) async -> String) async -> [String] {
    var results = [String](repeating: "", count: ids.count)
    await withTaskGroup(of: (Int, String).self) { group in
        for (index, id) in ids.enumerated() {
            group.addTask { (index, await fetch(id)) }
        }
        for await (index, value) in group {
            results[index] = value
        }
    }
    return results
}

func mapWithConcurrency<T, R>(
    _ items: [T],
    limit: Int,
    _ transform: @escaping @Sendable (T) async throws -> R
) async throws -> [R] {
    guard limit >= 1 else { throw TaskError.invalidLimit }
    var results = [R?](repeating: nil, count: items.count)
    try await withThrowingTaskGroup(of: (Int, R).self) { group in
        var next = 0
        while next < min(limit, items.count) {
            let index = next
            group.addTask { (index, try await transform(items[index])) }
            next += 1
        }
        while let (index, value) = try await group.next() {
            results[index] = value
            if next < items.count {
                let nextIndex = next
                group.addTask { (nextIndex, try await transform(items[nextIndex])) }
                next += 1
            }
        }
    }
    return results.map { $0! }
}
