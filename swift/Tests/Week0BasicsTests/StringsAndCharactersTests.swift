import Testing
@testable import Week0Basics

@Suite struct StringsAndCharactersTests {
    @Test func capitalizesWords() {
        #expect(capitalizeWords("hello wORLD") == "Hello World")
        #expect(capitalizeWords("don't stop") == "Don't Stop")
        #expect(capitalizeWords("multiple  spaces") == "Multiple  Spaces")
        #expect(capitalizeWords("") == "")
    }

    @Test func reversesWordOrder() {
        #expect(reversedWords("hello big world") == "world big hello")
        #expect(reversedWords("one") == "one")
        #expect(reversedWords("") == "")
    }

    @Test func palindromes() {
        #expect(isPalindrome("A man, a plan, a canal: Panama"))
        #expect(isPalindrome("12321"))
        #expect(isPalindrome(""))
        #expect(!isPalindrome("race a car"))
        #expect(!isPalindrome("12345"))
    }

    @Test func graphemeClustersAreOneCharacter() {
        #expect(graphemeCount("hello") == 5)
        #expect(graphemeCount("\u{1F1E6}\u{1F1FA}") == 1)   // a flag is two scalars, one Character
        #expect(graphemeCount("e\u{301}") == 1)             // e plus a combining accent
        #expect(graphemeCount("\u{65E5}\u{672C}") == 2)
        #expect(graphemeCount("") == 0)
    }

    @Test func utf8BytesDifferFromCharacters() {
        #expect(utf8ByteCount("hello") == 5)
        #expect(utf8ByteCount("\u{E9}") == 2)               // precomposed e-acute
        #expect(utf8ByteCount("e\u{301}") == 3)             // decomposed e-acute: same Character, more bytes
        #expect(utf8ByteCount("\u{65E5}\u{672C}") == 6)
        #expect(utf8ByteCount("\u{1F1E6}\u{1F1FA}") == 8)
    }

    @Test func shiftsLettersAndLeavesOtherCharacters() {
        #expect(caesarShift("abc", by: 1) == "bcd")
        #expect(caesarShift("xyz", by: 3) == "abc")
        #expect(caesarShift("Hello, World!", by: 3) == "Khoor, Zruog!")
        #expect(caesarShift("abc", by: -1) == "zab")
        #expect(caesarShift("abc", by: 26) == "abc")
        #expect(caesarShift("abc", by: 53) == "bcd")
        #expect(caesarShift("caf\u{E9}", by: 1) == "dbg\u{E9}")
    }
}
