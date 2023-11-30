class FOPCParser:
    def __init__(self, variables):
        self.variables = variables

    def parse_expression(self, expression):
        tokens = expression.split()
        stack = []

        for token in tokens:
            if token in self.variables:
                stack.append(self.variables[token])
            elif token == 'and':
                if len(stack) >= 2:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    stack.append(operand1 and operand2)
                else:
                    return None  # Invalid expression
            elif token == 'or':
                if len(stack) >= 2:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    stack.append(operand1 or operand2)
                else:
                    return None  # Invalid expression
            elif token == 'not':
                if stack:
                    operand = stack.pop()
                    stack.append(not operand)
                else:
                    return None  # Invalid expression
            elif token.startswith('('):
                stack.append(token[1:])
            elif token.endswith(')'):
                subexpression = [stack.pop()]
                while stack and not subexpression[-1].startswith('('):
                    subexpression.append(stack.pop())
                if not stack:
                    return None  # Unmatched parentheses
                subexpression.reverse()
                subexpression = ' '.join(subexpression)
                stack.append(self.parse_expression(subexpression))
            else:
                stack.append(token.lower() == 'true')

        return stack[0] if stack else None

# Given variables
variables = {'p': True, 'q': True, 'r': False}

# Logical expressions
expressions = ["p and q", "p or r", "not p", "q and (r or p)", "((p and q) or r", "p and (q or r))"]

# Parse and evaluate each expression
parser = FOPCParser(variables)
for expression in expressions:
    result = parser.parse_expression(expression)
    if result is not None:
        print(f"{expression}: {result}")
    else:
        print(f"{expression}: Invalid expression")