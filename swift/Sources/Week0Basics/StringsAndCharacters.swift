// Strings, Characters and Unicode
//
// A Swift String is a collection of Characters, where one Character is an extended grapheme cluster:
// what a person sees as one symbol. So string.count is NOT the number of bytes, and strings cannot be
// indexed with plain integers.
//
// capitalizeWords(s)    upper-case the first letter of each word and lower-case the rest. Words are
//                       separated by single spaces; keep the spacing exactly. "don't stop" -> "Don't Stop"
// reversedWords(s)      reverse the order of the words: "hello big world" -> "world big hello"
// isPalindrome(s)       true if s reads the same both ways, ignoring case and anything that is not a
//                       letter or a number
// graphemeCount(s)      how many Characters s has (s.count)
// utf8ByteCount(s)      how many bytes s uses in UTF-8 (s.utf8.count)
// caesarShift(s, by:)   shift the ASCII letters k places (k may be negative or above 26), keep case,
//                       and leave every other character unchanged
//
// Concepts: Character, grapheme clusters, String vs utf8 views, split, map/filter, asciiValue.

func capitalizeWords(_ s: String) -> String {
    return s
}

func reversedWords(_ s: String) -> String {
    return s
}

func isPalindrome(_ s: String) -> Bool {
    return false
}

func graphemeCount(_ s: String) -> Int {
    return 0
}

func utf8ByteCount(_ s: String) -> Int {
    return 0
}

func caesarShift(_ s: String, by k: Int) -> String {
    return s
}
