func shortestPathLength(in graph: [String: [String]], from start: String, to goal: String) -> Int {
    if start == goal { return 0 }
    var visited: Set<String> = [start]
    var queue: [(node: String, distance: Int)] = [(start, 0)]
    var head = 0
    while head < queue.count {
        let (node, distance) = queue[head]
        head += 1
        for neighbour in graph[node] ?? [] {
            if neighbour == goal { return distance + 1 }
            if visited.insert(neighbour).inserted {
                queue.append((neighbour, distance + 1))
            }
        }
    }
    return -1
}
