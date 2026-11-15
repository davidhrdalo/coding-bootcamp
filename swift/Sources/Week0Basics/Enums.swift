// Enums with associated values and pattern matching
//
// Swift enums can carry data in each case, and a switch must handle every case (the compiler checks).
// An `indirect` enum can contain itself, which is perfect for expression trees. This is the same shape
// as the AST in theory/05-compilation-pipeline.md.
//
// Expr is an expression tree:
//   .number(Double), .add(Expr, Expr), .multiply(Expr, Expr), .negate(Expr)
//
// evaluate(expr)   the numeric value
// render(expr)     the expression as text. Numbers that are whole print without decimals ("3", not
//                  "3.0"); add prints "(a + b)"; multiply prints "(a * b)"; negate prints "-a".
//                  .add(.number(1), .multiply(.number(2), .number(3))) renders as "(1 + (2 * 3))"
// depth(expr)      a number alone has depth 1; an operator has 1 + the depth of its deepest child
//
// Concepts: enum associated values, indirect, exhaustive switch, recursion, pattern binding.

indirect enum Expr {
    case number(Double)
    case add(Expr, Expr)
    case multiply(Expr, Expr)
    case negate(Expr)
}

func evaluate(_ expr: Expr) -> Double {
    return 0
}

func render(_ expr: Expr) -> String {
    return ""
}

func depth(_ expr: Expr) -> Int {
    return 0
}
