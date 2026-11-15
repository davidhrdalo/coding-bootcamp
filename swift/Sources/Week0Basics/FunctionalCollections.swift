// map, filter, reduce and Dictionary
//
// Swift collections have powerful built-in higher-order functions. Use them instead of manual loops
// where they make the intent clearer.
//
// squaresOfEvens(nums)       the squares of the even numbers, in order (filter then map)
// sumOfSquares(nums)         the sum of every number squared (reduce)
// groupByLength(words)       [length: words of that length], keeping each group's original order
//                            (Dictionary(grouping:by:))
// wordFrequencies(text)      how often each word appears: lower-case it, and a word is a run of
//                            letters, digits or apostrophes
// topWords(frequencies, limit)
//                            the `limit` most frequent words, most frequent first, ties in alphabetical
//                            order (sorted(by:), prefix, map)
//
// Concepts: map, filter, reduce, compactMap, Dictionary subscripts with default:, sorting with a closure.

func squaresOfEvens(_ nums: [Int]) -> [Int] {
    return []
}

func sumOfSquares(_ nums: [Int]) -> Int {
    return 0
}

func groupByLength(_ words: [String]) -> [Int: [String]] {
    return [:]
}

func wordFrequencies(_ text: String) -> [String: Int] {
    return [:]
}

func topWords(_ frequencies: [String: Int], limit: Int) -> [String] {
    return []
}
