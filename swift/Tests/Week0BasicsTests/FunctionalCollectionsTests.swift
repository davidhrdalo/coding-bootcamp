import Testing
@testable import Week0Basics

@Suite struct FunctionalCollectionsTests {
    @Test func squaresOfEvensKeepsOrder() {
        #expect(squaresOfEvens([1, 2, 3, 4, 6]) == [4, 16, 36])
        #expect(squaresOfEvens([1, 3]) == [])
        #expect(squaresOfEvens([]) == [])
    }

    @Test func sumOfSquaresAddsThemUp() {
        #expect(sumOfSquares([1, 2, 3]) == 14)
        #expect(sumOfSquares([]) == 0)
        #expect(sumOfSquares([-2, 2]) == 8)
    }

    @Test func groupsWordsByLength() {
        let groups = groupByLength(["a", "bb", "c", "dd", "eee"])
        #expect(groups == [1: ["a", "c"], 2: ["bb", "dd"], 3: ["eee"]])
        #expect(groupByLength([]).isEmpty)
    }

    @Test func countsWordFrequencies() {
        #expect(wordFrequencies("The cat and the hat.") == ["the": 2, "cat": 1, "and": 1, "hat": 1])
        #expect(wordFrequencies("Go go GO") == ["go": 3])
        #expect(wordFrequencies("don't stop 2 stop") == ["don't": 1, "stop": 2, "2": 1])
        #expect(wordFrequencies("  ...  ").isEmpty)
    }

    @Test func topWordsOrdersByCountThenAlphabetically() {
        let frequencies = ["apple": 3, "pear": 1, "fig": 3, "kiwi": 2]
        #expect(topWords(frequencies, limit: 3) == ["apple", "fig", "kiwi"])
        #expect(topWords(frequencies, limit: 1) == ["apple"])
        #expect(topWords(frequencies, limit: 10) == ["apple", "fig", "kiwi", "pear"])
        #expect(topWords([:], limit: 3) == [])
    }
}
