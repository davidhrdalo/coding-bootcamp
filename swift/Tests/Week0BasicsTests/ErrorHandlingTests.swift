import Testing
@testable import Week0Basics

@Suite struct ErrorHandlingTests {
    @Test func parsesValidPercentages() throws {
        #expect(try parsePercentage("0") == 0)
        #expect(try parsePercentage("55") == 55)
        #expect(try parsePercentage("100") == 100)
    }

    @Test func emptyTextThrowsEmpty() {
        #expect(throws: ParseError.empty) {
            try parsePercentage("")
        }
    }

    @Test func nonNumbersThrowNotANumber() {
        #expect(throws: ParseError.notANumber("abc")) {
            try parsePercentage("abc")
        }
        #expect(throws: ParseError.notANumber("4.5")) {
            try parsePercentage("4.5")
        }
    }

    @Test func numbersOutsideTheRangeThrowOutOfRange() {
        #expect(throws: ParseError.outOfRange(101)) {
            try parsePercentage("101")
        }
        #expect(throws: ParseError.outOfRange(-5)) {
            try parsePercentage("-5")
        }
    }

    @Test func sumAddsEverythingWhenAllAreValid() {
        #expect(sumPercentages(["10", "20", "30"]) == .success(60))
        #expect(sumPercentages([]) == .success(0))
    }

    @Test func sumReturnsTheFirstError() {
        #expect(sumPercentages(["10", "abc", "200"]) == .failure(.notANumber("abc")))
        #expect(sumPercentages(["10", "200", "abc"]) == .failure(.outOfRange(200)))
        #expect(sumPercentages([""]) == .failure(.empty))
    }

    @Test func orNilVersionReturnsNilOnFailure() {
        #expect(parsePercentageOrNil("42") == 42)
        #expect(parsePercentageOrNil("abc") == nil)
        #expect(parsePercentageOrNil("") == nil)
        #expect(parsePercentageOrNil("101") == nil)
    }
}
