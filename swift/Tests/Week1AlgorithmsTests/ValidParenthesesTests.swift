import Testing
@testable import Week1Algorithms

@Suite struct ValidParenthesesTests {
    @Test func validExamples() {
        #expect(isValidParentheses("()"))
        #expect(isValidParentheses("()[]{}"))
        #expect(isValidParentheses("{[()]}"))
    }

    @Test func wrongTypeAndWrongOrder() {
        #expect(!isValidParentheses("(]"))
        #expect(!isValidParentheses("([)]"))
    }

    @Test func unclosedAndUnopened() {
        #expect(!isValidParentheses("("))
        #expect(!isValidParentheses(")"))
        #expect(!isValidParentheses("(()"))
    }

    @Test func emptyStringIsValid() {
        #expect(isValidParentheses(""))
    }
}
