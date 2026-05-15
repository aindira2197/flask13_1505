
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        return "0 ga bolib bolmaydi"

calc = Calculator()

print(calc.add(5, 3))
print(calc.subtract(9, 2))
print(calc.multiply(4, 7))
print(calc.divide(10, 2))
print(calc.divide(5, 0))
