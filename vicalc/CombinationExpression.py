import math
from PySide6.QtCore import QLocale
from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression
from PySide6.QtWidgets import QTableWidgetItem
from .AppGlobals import AppGlobals

class CombinationExpression(BinaryExpression):
    def __init__(self, first_number):
        super().__init__(first_number)

    def calculate(self, number: float):
        n = int(self.first_number)
        r = int(number)
        result = math.comb(n, r)

        self.insert_scroll_table()
        self.protocol(float(self.first_number), 0)
        self.protocol("C", 1)
        self.protocol(float(number), 2)
        self.protocol("=", 3)
        self.protocol_result(float(result), 4)

        return result