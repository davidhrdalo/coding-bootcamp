import Testing
@testable import Week1Algorithms

@Suite struct TwoSumTests {
    @Test func basic() {
        #expect(twoSum([2, 7, 11, 15], 9).sorted() == [0, 1])
    }

    @Test func notTheFirstElements() {
        #expect(twoSum([3, 2, 4], 6).sorted() == [1, 2])
    }

    @Test func duplicateValues() {
        #expect(twoSum([3, 3], 6).sorted() == [0, 1])
    }

    @Test func negativeNumbers() {
        #expect(twoSum([-1, -2, -3, -4, -5], -8).sorted() == [2, 4])
    }

    @Test func largeInputNeedsLinearTime() {
        let nums = Array(0..<20_000)
        #expect(twoSum(nums, 19_999 + 19_998).sorted() == [19_998, 19_999])
    }
}
