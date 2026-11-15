// Shortest path in a graph (BFS)
//
// A graph is stored as a dictionary from each node to the array of nodes it connects to:
//
//     ["A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []]
//
// shortestPathLength(in:from:to:) returns the minimum NUMBER OF EDGES on a path from start to goal, or
// -1 if goal cannot be reached. If start == goal the answer is 0.
//
// Use breadth-first search (BFS): explore everything 1 step away, then 2 steps, and so on, with a QUEUE
// and a Set of visited nodes (so cycles do not loop forever). The first time you reach the goal is the
// shortest route. Do NOT use recursion: one test has a chain of 5,000 nodes.
//
// Tip: an Array makes a poor queue because removeFirst() is O(n). Keep an index into the array
// instead of removing from the front.
//
// Concepts: graphs, queues, BFS, Set, dictionary default values.

func shortestPathLength(in graph: [String: [String]], from start: String, to goal: String) -> Int {
    return -2
}
