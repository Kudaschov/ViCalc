import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression

class CubeExpression(UnaryExpression):
    def calculate(self, number: float):
        result: float = number * number * number

        self.insert_scroll_table()
        self.protocol(number, 0)
        self.protocol("^3 =", 1)
        self.protocol_result(result, 2)

        return result