import Testing
@testable import Week1Algorithms

@Suite struct MergeSortTests {
    @Test func basic() {
        #expect(mergeSort([5, 2, 9, 1]) == [1, 2, 5, 9])
    }

    @Test func emptyAndSingle() {
        #expect(mergeSort([]) == [])
        #expect(mergeSort([3]) == [3])
    }

    @Test func alreadySortedAndReversed() {
        #expect(mergeSort([1, 2, 3, 4]) == [1, 2, 3, 4])
        #expect(mergeSort([4, 3, 2, 1]) == [1, 2, 3, 4])
    }

    @Test func duplicatesAndNegatives() {
        #expect(mergeSort([3, -1, 3, 0, -1]) == [-1, -1, 0, 3, 3])
    }

    @Test func matchesTheBuiltInSortOnPseudoRandomData() {
        for size in [2, 10, 101, 1000] {
            let data = (0..<size).map { ($0 &* 7919 &+ 13) % 1009 - 500 }
            #expect(mergeSort(data) == data.sorted())
        }
    }

    @Test func largeInput() {
        let data = (0..<100_000).map { ($0 &* 2_654_435_761) % 100_003 }
        #expect(mergeSort(data) == data.sorted())
    }
}
