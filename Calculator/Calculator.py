from Calculator.Addition import addition
from Calculator.Subtraction import subtract
from Calculator.Multiply import multiply
from Calculator.Division import divide

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtract(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def divide(self, a, b):
        self.result = divide(a, b)
        return self.result