import Testing
@testable import Week1Algorithms

@Suite struct GraphBFSTests {
    let graph: [String: [String]] = [
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["F"],
        "E": ["F"],
        "F": [],
    ]

    @Test func startEqualsGoal() {
        #expect(shortestPathLength(in: graph, from: "A", to: "A") == 0)
    }

    @Test func directNeighbour() {
        #expect(shortestPathLength(in: graph, from: "A", to: "B") == 1)
    }

    @Test func picksTheShortestOfSeveralRoutes() {
        #expect(shortestPathLength(in: graph, from: "A", to: "F") == 3)
    }

    @Test func unreachableReturnsMinusOne() {
        #expect(shortestPathLength(in: graph, from: "F", to: "A") == -1)   // edges go one way
        #expect(shortestPathLength(in: ["A": [], "B": []], from: "A", to: "B") == -1)
    }

    @Test func cyclesDoNotLoopForever() {
        let cyclic = ["A": ["B"], "B": ["C"], "C": ["A", "D"], "D": []]
        #expect(shortestPathLength(in: cyclic, from: "A", to: "D") == 3)
        #expect(shortestPathLength(in: cyclic, from: "A", to: "Z") == -1)
    }

    @Test func veryLongChainNeedsAnIterativeSolution() {
        let n = 5000
        var chain: [String: [String]] = [:]
        for i in 0..<(n - 1) {
            chain[String(i)] = [String(i + 1)]
        }
        chain[String(n - 1)] = []
        #expect(shortestPathLength(in: chain, from: "0", to: String(n - 1)) == n - 1)
    }
}
