class Calculator:
    def add(self, a, b):
        return a + b


def new_add(self, a, b):
        return a + b + 10


Calculator.add = new_add

calculator = Calculator()
print(calculator.add(2, 3))
# 15
