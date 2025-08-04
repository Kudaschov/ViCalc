import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression

class FourthPowerExpression(UnaryExpression):
    def calculate(self, number: float):
        result: float = math.pow(number, 4)

        self.insert_scroll_table()
        self.protocol(number, 0)
        self.protocol("^4 =", 1)
        self.protocol_result(result, 2)

        return result