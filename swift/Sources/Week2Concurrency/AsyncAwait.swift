// async/await: sleep, retry, fetchAll and a concurrency limit
//
// Swift's structured concurrency uses async functions, await, Task and task groups. Implement:
//
// sleep(milliseconds:)    suspend for that long (Task.sleep). It is an async function that never throws.
//
// retry(attempts:operation:)
//                         call `operation` (an async throwing closure). Return the first success. If it
//                         throws, call it again, up to `attempts` calls in total, and if every call
//                         fails rethrow the LAST error. If attempts < 1 throw TaskError.invalidAttempts.
//
// fetchAll(ids:fetch:)    run `fetch` for every id AT THE SAME TIME (use a task group, withTaskGroup)
//                         and return the results in the ORIGINAL id order, not the order they finish.
//
// mapWithConcurrency(_:limit:_:)
//                         like map with an async throwing transform, but never more than `limit`
//                         transforms run at once. Results keep the original order. If a transform
//                         throws, the call throws. If limit < 1 throw TaskError.invalidLimit.
//                         Idea: start `limit` child tasks, and each time one finishes start the next
//                         item (withThrowingTaskGroup, group.next()).
//
// Concepts: async/await, Task.sleep, task groups, child tasks, structured concurrency, Sendable
// (the closures are marked @Sendable because they run on other tasks).

enum TaskError: Error, Equatable {
    case invalidAttempts
    case invalidLimit
}

func sleep(milliseconds: Int) async {
}

func retry<T>(attempts: Int, operation: () async throws -> T) async throws -> T {
    throw TaskError.invalidAttempts
}

func fetchAll(ids: [Int], fetch: @escaping @Sendable (Int) async -> String) async -> [String] {
    return []
}

func mapWithConcurrency<T, R>(
    _ items: [T],
    limit: Int,
    _ transform: @escaping @Sendable (T) async throws -> R
) async throws -> [R] {
    return []
}
