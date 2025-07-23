import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression

class CubeRootExpression(UnaryExpression):
    def calculate(self, number: float):
        result: float = math.pow(number, 1.0 / 3.0)

        self.insert_scroll_table()
        self.protocol("³√", 0)
        self.protocol(number, 1)
        self.protocol("=", 2)
        self.protocol_result(result, 3)

        return result