# 05 - The compilation pipeline

A compiler (or interpreter) turns text into something runnable in stages.
You build the first two in `theory/exercises/calculator.py`.

```
source text  ->  LEXER  ->  tokens  ->  PARSER  ->  AST  ->  analysis  ->  codegen  ->  output
"2 + 3"          ["2","+","3"]         tree of the code        types, scopes     machine code,
                                                                                  bytecode or JS
```

1. **Lexing (tokenising):** split text into tokens, the "words" of the language. `let x = 5;` becomes `let`, `x`, `=`, `5`, `;`.
2. **Parsing:** check the tokens follow the grammar and build an **abstract syntax tree (AST)**. For `2 + 3 * 4` the tree has `+` at the root with `2` on the left and `*` (holding 3 and 4) on the right. Precedence is encoded in the tree shape.
3. **Semantic analysis:** check the code makes sense beyond grammar: are variables declared, do the types match?
4. **Intermediate representation (IR):** a simpler, machine-independent form, easier to optimise (LLVM IR is the well-known one; Swift compiles through LLVM).
5. **Optimisation:** remove dead code, inline small functions, simplify constants.
6. **Code generation:** emit machine code, bytecode, or (for a transpiler) another language.
7. **Linking:** join pieces and libraries into one executable (for compiled languages).

## Interpreters

An interpreter can skip code generation: a **tree-walking interpreter** just evaluates the AST
directly (that is what your `evaluate` function does). A **bytecode VM** compiles to compact
instructions first, then loops over them. See `01-how-code-runs.md`.

## Grammars and recursive descent

A grammar describes valid programs. For arithmetic:

```
expression := term (("+" | "-") term)*
term       := factor (("*" | "/") factor)*
factor     := "-" factor | NUMBER | "(" expression ")"
```

**Recursive descent** writes one function per rule. Because `expression` calls `term`
calls `factor`, higher-precedence operators naturally bind tighter.

## Interview questions

1. Walk me through what happens between writing source code and it running.
2. What is an AST, and why do compilers use one?
3. What is the difference between a lexer and a parser?
4. Why do `2 + 3 * 4` and `(2 + 3) * 4` give different answers in terms of the tree?
5. What is the difference between a syntax error and a type error? When is each reported?

## Learn more

- [Crafting Interpreters](https://craftinginterpreters.com/): the best free book on this; read the "Scanning" and "Parsing Expressions" chapters
- [Let's Build A Simple Interpreter](https://ruslanspivak.com/lsbasi-part1/): a Python walkthrough, very close to your calculator exercise
- [Nand2Tetris](https://www.nand2tetris.org/): build a computer from logic gates up to a compiler
