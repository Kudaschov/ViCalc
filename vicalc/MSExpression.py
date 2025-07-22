import math
from PySide6.QtWidgets import QTableWidgetItem
from UnaryExpression import UnaryExpression

class MSExpression(UnaryExpression):
    def calculate(self, number: float):
        self.insert_scroll_table()
        self.protocol("Memory:", 0)
        self.protocol_result(number, 1)
        return number