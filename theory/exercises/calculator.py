"""Mini calculator: a lexer and a parser

This is the front half of a compiler in miniature. Read
theory/05-compilation-pipeline.md first.

1. tokenize(src) is the LEXER. It turns text into a list of token strings:
   numbers (integers or decimals such as 12 or 3.5), the operators + - * / and
   the parentheses ( ). Spaces are ignored. Any other character raises ValueError.
     tokenize("12 + 3*(4-1)") -> ["12", "+", "3", "*", "(", "4", "-", "1", ")"]

2. evaluate(src) is the PARSER plus an evaluator. It returns the numeric value
   of the expression and must respect normal precedence: * and / bind tighter
   than + and -, parentheses override, and a leading minus is allowed (-3, -(2+1)).
     evaluate("2 + 3 * 4") -> 14
     evaluate("(2 + 3) * 4") -> 20
     evaluate("10 / 4") -> 2.5
   Malformed input ("2 +", "(1 + 2", "2 3", ")") raises ValueError.

Suggested approach (recursive descent), one function per grammar rule:
   expression := term (("+" | "-") term)*
   term       := factor (("*" | "/") factor)*
   factor     := "-" factor | NUMBER | "(" expression ")"

Do NOT use eval(). The point is to build the parser yourself.
"""


def tokenize(src: str) -> list[str]:
    raise NotImplementedError


def evaluate(src: str) -> float:
    raise NotImplementedError
