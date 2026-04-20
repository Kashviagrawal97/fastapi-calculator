import math

class Cal:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def power(self, x, y):
        return x ** y

    def log(self, x, y):
        return math.log(x, y)

    def factorial(self, x):
        return math.factorial(x)


obj = Cal()


def main(x, y, operation, obj):

    if operation == "add":
        return obj.add(x, y)

    elif operation == "subtract":
        return obj.subtract(x, y)

    elif operation == "multiply":
        return obj.multiply(x, y)

    elif operation == "divide":
        return obj.divide(x, y)

    elif operation == "power":
        return obj.power(x, y)

    elif operation == "log":
        return obj.log(x, y)

    elif operation == "factorial":
        return obj.factorial(x)


