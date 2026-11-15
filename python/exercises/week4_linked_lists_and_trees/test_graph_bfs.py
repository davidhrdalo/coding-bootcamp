from graph_bfs import shortest_path_length

GRAPH = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": [],
}


def test_start_equals_goal():
    assert shortest_path_length(GRAPH, "A", "A") == 0


def test_direct_neighbour():
    assert shortest_path_length(GRAPH, "A", "B") == 1


def test_picks_the_shortest_of_several_routes():
    assert shortest_path_length(GRAPH, "A", "F") == 3


def test_unreachable_returns_minus_one():
    assert shortest_path_length(GRAPH, "F", "A") == -1  # edges only go one way
    assert shortest_path_length({"A": [], "B": []}, "A", "B") == -1


def test_cycles_do_not_loop_forever():
    graph = {"A": ["B"], "B": ["C"], "C": ["A", "D"], "D": []}
    assert shortest_path_length(graph, "A", "D") == 3
    assert shortest_path_length(graph, "A", "Z") == -1


def test_undirected_graph():
    graph = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}
    assert shortest_path_length(graph, 3, 4) == 3


def test_very_long_chain_needs_an_iterative_solution():
    n = 5000
    graph = {i: [i + 1] for i in range(n - 1)}
    graph[n - 1] = []
    assert shortest_path_length(graph, 0, n - 1) == n - 1
