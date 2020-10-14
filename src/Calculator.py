from src.Operations import Operations


class Calculator:

    def calculateSum(self, a, b):
        return Operations(a, b, "+", a + b).toJson()

    def calculateDiff(self, a, b):
        return Operations(a, b, "-", a - b).toJson()

    def calculateProduct(self, a, b):
        return Operations(a, b, '*', a * b).toJson()

    def calculateDiv(self, a, b):
        return Operations(a, b, '/', a / b).toJson()
