import Testing
@testable import Week0Basics

@Suite struct OptionalsTests {
    @Test func safeDivideReturnsNilWhenDividingByZero() {
        #expect(safeDivide(10, 2) == 5)
        #expect(safeDivide(7, 2) == 3)
        #expect(safeDivide(0, 5) == 0)
        #expect(safeDivide(1, 0) == nil)
    }

    @Test func parseAgeAcceptsValidAges() {
        #expect(parseAge("42") == 42)
        #expect(parseAge("0") == 0)
        #expect(parseAge("150") == 150)
    }

    @Test(arguments: ["", "abc", "-1", "151", "4.2", "12a", "1 2"])
    func parseAgeRejectsBadInput(_ bad: String) {
        #expect(parseAge(bad) == nil)
    }

    @Test func displayNameUsesWhatExists() {
        #expect(displayName(first: "Ada", last: "Lovelace") == "Ada Lovelace")
        #expect(displayName(first: "Ada", last: nil) == "Ada")
        #expect(displayName(first: nil, last: "Lovelace") == "Lovelace")
        #expect(displayName(first: nil, last: nil) == "Anonymous")
    }

    @Test func displayNameTreatsEmptyStringsAsMissing() {
        #expect(displayName(first: "", last: "Lovelace") == "Lovelace")
        #expect(displayName(first: "", last: "") == "Anonymous")
    }

    @Test func firstLongWordFindsTheFirstMatch() {
        #expect(firstLongWord(in: ["a", "bb", "ccc", "dddd"], minLength: 3) == "ccc")
        #expect(firstLongWord(in: ["a", "bb"], minLength: 3) == nil)
        #expect(firstLongWord(in: [], minLength: 1) == nil)
    }
}
