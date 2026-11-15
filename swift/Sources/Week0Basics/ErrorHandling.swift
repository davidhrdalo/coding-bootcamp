// Errors: throws, try, Result
//
// Swift functions mark failure with `throws`, and callers must acknowledge it with try
// (try, try?, try!) inside do/catch. Result<Success, Failure> stores either outcome as a value.
//
// ParseError has three cases: .empty, .notANumber(String) and .outOfRange(Int).
//
// parsePercentage(text) throws
//     "" throws .empty; text that is not a whole number throws .notANumber(text); a number outside
//     0...100 throws .outOfRange(thatNumber); otherwise return the number.
//
// sumPercentages(items)
//     Parse every item and return .success(total). If any item fails, return .failure with the FIRST
//     error. (Use do/catch inside the function.)
//
// parsePercentageOrNil(text)
//     The same parse, but returns nil on failure. Use try?.
//
// Concepts: Error protocol, throw, do/catch, try?, Result, enums with associated values.

enum ParseError: Error, Equatable {
    case empty
    case notANumber(String)
    case outOfRange(Int)
}

func parsePercentage(_ text: String) throws -> Int {
    return 0
}

func sumPercentages(_ items: [String]) -> Result<Int, ParseError> {
    return .success(0)
}

func parsePercentageOrNil(_ text: String) -> Int? {
    return nil
}
