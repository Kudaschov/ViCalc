import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression

class ArsinhExpression(UnaryExpression):
    def calculate(self, number: float):
        result: float = math.asinh(number)

        self.insert_scroll_table()
        self.protocol("arsinh", 0)
        self.protocol(number, 1)
        self.protocol("=", 2)
        self.protocol_result(result, 3)

        return result