import Testing
@testable import Week1Algorithms

@Suite struct GroupAnagramsTests {
    private func normalise(_ groups: [[String]]) -> [[String]] {
        return groups.map { $0.sorted() }.sorted { $0[0] < $1[0] }
    }

    @Test func example() {
        let result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        #expect(normalise(result) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])
    }

    @Test func emptyList() {
        #expect(groupAnagrams([]).isEmpty)
    }

    @Test func singleEmptyString() {
        #expect(normalise(groupAnagrams([""])) == [[""]])
    }

    @Test func noAnagrams() {
        #expect(normalise(groupAnagrams(["a", "b", "c"])) == [["a"], ["b"], ["c"]])
    }
}
