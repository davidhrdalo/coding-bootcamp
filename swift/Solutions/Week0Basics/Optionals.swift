func safeDivide(_ a: Int, _ b: Int) -> Int? {
    guard b != 0 else { return nil }
    return a / b
}

func parseAge(_ text: String) -> Int? {
    guard let age = Int(text), (0...150).contains(age) else { return nil }
    return age
}

func displayName(first: String?, last: String?) -> String {
    let parts = [first, last].compactMap { $0 }.filter { !$0.isEmpty }
    return parts.isEmpty ? "Anonymous" : parts.joined(separator: " ")
}

func firstLongWord(in words: [String], minLength: Int) -> String? {
    return words.first { $0.count >= minLength }
}
