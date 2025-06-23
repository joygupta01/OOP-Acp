class Expression:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        result = eval(self.expression)
        return result

expr = Expression("5 + 10 * 2")
print("Result:", expr.evaluate())
