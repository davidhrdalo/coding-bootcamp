// Optionals: values that might be missing
//
// A Swift Optional (Int?, String?) holds either a value or nil. The compiler forces you to deal with
// the nil case, which prevents a whole class of crashes. Use if let, guard let, ?? and optional
// chaining; avoid force-unwrapping with !.
//
// safeDivide(a, b)       a / b, or nil when b is 0
// parseAge(text)         the Int in text if it is a whole number from 0 to 150, otherwise nil
// displayName(first:last:)
//                        "First Last" when both exist, just the one that exists otherwise, and
//                        "Anonymous" when neither exists. An empty string counts as missing.
// firstLongWord(in:minLength:)
//                        the first word with at least minLength characters, or nil
//
// Concepts: Optional, nil, if let / guard let, nil-coalescing ??, Int(String) returning Int?.
// Read theory/14-swift-essentials.md.

func safeDivide(_ a: Int, _ b: Int) -> Int? {
    return nil
}

func parseAge(_ text: String) -> Int? {
    return nil
}

func displayName(first: String?, last: String?) -> String {
    return ""
}

func firstLongWord(in words: [String], minLength: Int) -> String? {
    return nil
}
