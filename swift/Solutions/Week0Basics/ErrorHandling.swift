enum ParseError: Error, Equatable {
    case empty
    case notANumber(String)
    case outOfRange(Int)
}

func parsePercentage(_ text: String) throws -> Int {
    if text.isEmpty { throw ParseError.empty }
    guard let value = Int(text) else { throw ParseError.notANumber(text) }
    guard (0...100).contains(value) else { throw ParseError.outOfRange(value) }
    return value
}

func sumPercentages(_ items: [String]) -> Result<Int, ParseError> {
    var total = 0
    for item in items {
        do {
            total += try parsePercentage(item)
        } catch let error as ParseError {
            return .failure(error)
        } catch {
            return .failure(.notANumber(item))
        }
    }
    return .success(total)
}

func parsePercentageOrNil(_ text: String) -> Int? {
    return try? parsePercentage(text)
}
