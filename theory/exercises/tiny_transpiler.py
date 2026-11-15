"""A tiny transpiler: Lisp-style calls to C-style calls

A transpiler (source-to-source compiler) reads code in one language and writes
code in another. Read theory/06-transpilers.md first.

Build a tiny one. The input language writes a function call as (name arg arg).
Arguments are words or numbers separated by spaces, and calls can be nested.
The output language writes the same call as name(arg, arg) and ends each
top-level call with a semicolon.

  transpile("(add 2 2)")                 -> "add(2, 2);"
  transpile("(add 2 (subtract 4 2))")    -> "add(2, subtract(4, 2));"
  transpile("(add 1 2) (mul 3 4)")       -> "add(1, 2);" newline "mul(3, 4);"
  transpile("")                          -> ""

Several top-level calls are joined with a newline. Raise ValueError for an
unbalanced parenthesis, an empty call "()" or a stray ")".

Follow the three classic stages (this is how Babel and TypeScript work too):
  1. tokenize: text -> list of tokens ("(", ")", words)
  2. parse:    tokens -> a tree (nested lists)
  3. generate: tree -> output text
Write each stage as its own function so you can test them separately.
"""


def tokenize(src: str) -> list[str]:
    raise NotImplementedError


def parse(tokens: list[str]) -> list:
    raise NotImplementedError


def generate(node) -> str:
    raise NotImplementedError


def transpile(src: str) -> str:
    raise NotImplementedError
