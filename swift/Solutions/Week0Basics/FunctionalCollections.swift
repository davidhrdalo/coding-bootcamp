func squaresOfEvens(_ nums: [Int]) -> [Int] {
    return nums.filter { $0 % 2 == 0 }.map { $0 * $0 }
}

func sumOfSquares(_ nums: [Int]) -> Int {
    return nums.reduce(0) { $0 + $1 * $1 }
}

func groupByLength(_ words: [String]) -> [Int: [String]] {
    return Dictionary(grouping: words, by: { $0.count })
}

func wordFrequencies(_ text: String) -> [String: Int] {
    var counts: [String: Int] = [:]
    var current = ""
    for character in text.lowercased() {
        if character.isLetter || character.isNumber || character == "'" {
            current.append(character)
        } else if !current.isEmpty {
            counts[current, default: 0] += 1
            current = ""
        }
    }
    if !current.isEmpty {
        counts[current, default: 0] += 1
    }
    return counts
}

func topWords(_ frequencies: [String: Int], limit: Int) -> [String] {
    return frequencies
        .sorted { $0.value != $1.value ? $0.value > $1.value : $0.key < $1.key }
        .prefix(limit)
        .map { $0.key }
}
