import math
from PySide6.QtCore import QLocale
from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression

class CombinationExpression(BinaryExpression):
    def __init__(self, first_number):
        super().__init__(first_number)

    def calculate(self, number: float):
        n = int(self.first_number)
        r = int(number)
        result = math.comb(n, r)

        self.insert_scroll_table()
        self.protocol("Combination C(")
        self.protocol(n)
        self.protocol(", ")
        self.protocol(r)
        self.protocol(") = ")
        self.protocol_result(result)

        return result