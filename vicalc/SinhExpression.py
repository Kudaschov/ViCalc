import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression

class SinhExpression(UnaryExpression):
    def calculate(self, number: float):
        result: float = math.sinh(number)

        self.insert_scroll_table()
        self.protocol("sinh", 0)
        self.protocol(number, 1)
        self.protocol("=", 2)
        self.protocol_result(result, 3)

        return result