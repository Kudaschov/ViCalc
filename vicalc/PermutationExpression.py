import math
from PySide6.QtCore import QLocale
from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression
from .AppGlobals import AppGlobals

class PermutationExpression(BinaryExpression):
    def __init__(self, first_number):
        super().__init__(first_number)

    def text(self) -> str:
        return f"{self.first_number_to_string()} nPr; r = "

    def calculate(self, number: float):
        n = int(self.first_number)
        AppGlobals.assert_int(number)
        r = int(number)
        result = math.perm(n, r)

        self.insert_scroll_table()
        self.protocol("Permutation P(")
        self.protocol(n)
        self.protocol(", ")
        self.protocol(r)
        self.protocol(") = ")
        self.protocol_result(result)

        return result