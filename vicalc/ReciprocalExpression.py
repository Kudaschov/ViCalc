import math
from PySide6.QtWidgets import QTableWidgetItem
from UnaryExpression import UnaryExpression

class ReciprocalExpression(UnaryExpression):
    def calculate(self, number: float):
        result: float = 1.0 / number

        self.insert_scroll_table()
        self.protocol("1", 0)
        self.protocol("/", 1)
        self.protocol(number, 2)
        self.protocol("=", 3)
        self.protocol_result(result, 4)

        return result