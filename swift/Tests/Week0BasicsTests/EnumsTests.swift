import Testing
@testable import Week0Basics

@Suite struct EnumsTests {
    let sample = Expr.add(.number(1), .multiply(.number(2), .number(3)))

    @Test func evaluatesNestedExpressions() {
        #expect(evaluate(sample) == 7)
        #expect(evaluate(.number(2.5)) == 2.5)
        #expect(evaluate(.negate(.number(4))) == -4)
        #expect(evaluate(.multiply(.add(.number(1), .number(2)), .number(3))) == 9)
    }

    @Test func rendersWholeNumbersWithoutDecimals() {
        #expect(render(.number(3)) == "3")
        #expect(render(.number(2.5)) == "2.5")
        #expect(render(.number(-7)) == "-7")
    }

    @Test func rendersOperatorsWithParentheses() {
        #expect(render(sample) == "(1 + (2 * 3))")
        #expect(render(.negate(.number(4))) == "-4")
        #expect(render(.negate(.add(.number(1), .number(2)))) == "-(1 + 2)")
    }

    @Test func depthCountsTheLongestPath() {
        #expect(depth(.number(1)) == 1)
        #expect(depth(sample) == 3)
        #expect(depth(.negate(.negate(.number(1)))) == 3)
    }
}
