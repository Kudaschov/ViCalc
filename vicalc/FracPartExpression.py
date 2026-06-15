import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression

class FracPartExpression(UnaryExpression):
    def calculate(self, number: float):
        frac, integer = math.modf(number)
        result: float = frac

        self.insert_scroll_table()
        self.protocol("Fractional part", 0)
        self.protocol(number, 1)
        self.protocol("=", 2)
        self.protocol_result(result, 3)

        return result