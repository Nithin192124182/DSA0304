from pyparsing import Word, Literal, Keyword, infixNotation, opAssoc

# Define the logical operators and symbols
and_ = Keyword("and")
or_ = Keyword("or")
not_ = Keyword("not")

# Define the variable
variable = Word("xy", exact=1)

# Define the grammar for basic logical expressions
expr = infixNotation(variable, [
    (not_, 1, opAssoc.RIGHT),
    (and_, 2, opAssoc.LEFT),
    (or_, 2, opAssoc.LEFT),
])

# Given expressions
expressions = [
    "x and y",
    "x or (not y)",
    "x and (y or (not x))",
]

# Parse and evaluate each expression
for i, expression in enumerate(expressions):
    print(f"\nExpression {i + 1}: {expression}")
    try:
        result = expr.parseString(expression)[0]
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")