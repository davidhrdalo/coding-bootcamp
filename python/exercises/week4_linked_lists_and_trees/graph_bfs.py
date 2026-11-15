"""Shortest path in a graph (BFS)

A graph is stored as a dict mapping each node to the list of nodes it connects to
(its neighbours):

    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}

shortest_path_length(graph, start, goal) returns the minimum NUMBER OF EDGES on a
path from start to goal, or -1 if goal cannot be reached. If start == goal the
answer is 0.

Use breadth-first search (BFS): explore all nodes 1 step away, then 2 steps, and so
on, using a QUEUE (collections.deque) and a set of visited nodes (so cycles do
not loop forever). The first time you reach goal is the shortest route.

Do NOT use recursion: one test has a chain of 5,000 nodes, which would overflow
the call stack with a recursive depth-first search.

Concepts: graphs, queues, BFS, visited sets. Edges are directed as given: if
the graph is undirected, both directions are listed.
"""


def shortest_path_length(graph: dict, start, goal) -> int:
    raise NotImplementedError
