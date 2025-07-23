import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression

class FactorialExpression(UnaryExpression):
    def calculate(self, number: float):
        result = math.factorial(int(number))

        self.insert_scroll_table()
        self.protocol(number, 0)
        self.protocol("! =", 1)
        self.protocol_result(float(result), 2)

        return result