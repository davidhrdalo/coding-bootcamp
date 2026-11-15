func capitalizeWords(_ s: String) -> String {
    return s.split(separator: " ", omittingEmptySubsequences: false)
        .map { word in word.prefix(1).uppercased() + word.dropFirst().lowercased() }
        .joined(separator: " ")
}

func reversedWords(_ s: String) -> String {
    return s.split(separator: " ", omittingEmptySubsequences: false).reversed().joined(separator: " ")
}

func isPalindrome(_ s: String) -> Bool {
    let cleaned = s.filter { $0.isLetter || $0.isNumber }.lowercased()
    return cleaned == String(cleaned.reversed())
}

func graphemeCount(_ s: String) -> Int {
    return s.count
}

func utf8ByteCount(_ s: String) -> Int {
    return s.utf8.count
}

func caesarShift(_ s: String, by k: Int) -> String {
    let shift = ((k % 26) + 26) % 26
    return String(s.map { character -> Character in
        guard let value = character.asciiValue else { return character }
        let base: Int
        switch value {
        case 97...122: base = 97
        case 65...90: base = 65
        default: return character
        }
        let shifted = (Int(value) - base + shift) % 26 + base
        return Character(UnicodeScalar(UInt8(shifted)))
    })
}
