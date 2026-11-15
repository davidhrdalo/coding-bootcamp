import Testing
@testable import Week1Algorithms

@Suite struct BinarySearchTests {
    @Test func findsEveryElement() {
        let nums = [1, 3, 5, 7, 9]
        for (index, value) in nums.enumerated() {
            #expect(binarySearch(nums, value) == index)
        }
    }

    @Test func returnsMinusOneWhenAbsent() {
        #expect(binarySearch([1, 3, 5, 7, 9], 4) == -1)
        #expect(binarySearch([1, 3, 5, 7, 9], 0) == -1)
        #expect(binarySearch([1, 3, 5, 7, 9], 10) == -1)
    }

    @Test func emptyAndSingleElement() {
        #expect(binarySearch([], 1) == -1)
        #expect(binarySearch([5], 5) == 0)
        #expect(binarySearch([5], 4) == -1)
    }

    @Test func duplicatesReturnAValidIndex() {
        let nums = [1, 2, 2, 2, 3]
        let index = binarySearch(nums, 2)
        #expect(index >= 0 && nums[index] == 2)
    }

    @Test func largeArray() {
        let nums = (0..<1_000_000).map { $0 * 2 }
        #expect(binarySearch(nums, 1_999_998) == 999_999)
        #expect(binarySearch(nums, 1_999_999) == -1)
    }
}
