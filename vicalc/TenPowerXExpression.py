import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression

class TenPowerXExpression(UnaryExpression):
    def calculate(self, number: float):
        result: float = math.pow(10, number)

        self.insert_scroll_table()
        self.protocol("10^", 0)
        self.protocol(number, 1)
        self.protocol("=", 2)
        self.protocol_result(result, 3)

        return result