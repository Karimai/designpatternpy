class Context:
    def __init__(self):
        self.variables = {}

    def set_variable(self, variable, value):
        self.variables[variable] = value

    def get_variable(self, variable):
        return self.variables[variable]


class Expression:
    def interpreter(self, context: Context):
        pass


class VariableExpresion(Expression):
    def __init__(self, variable):
        self.variable = variable

    def interpreter(self, context: Context):
        return context.get_variable(self.variable)


class ConstantExpresion(Expression):
    def __init__(self, value):
        self.value = value

    def interpreter(self, context: Context):
        return self.value


class AddExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpreter(self, context: Context):
        return self.left.interpreter(context) + self.right.interpreter(context)


context = Context()
context.set_variable("x", 5)
context.set_variable("y", 20)

expression = AddExpression(VariableExpresion("x"), ConstantExpresion(15))

result = expression.interpreter(context)
print(result)
