import math
from PySide6.QtWidgets import QTableWidgetItem
from .TrigExpression import TrigExpression

class TanExpression(TrigExpression):
    def calculate(self, number: float):
        result: float = math.tan(self.angle_unit.to_rad(number))

        self.insert_scroll_table()
        self.protocol("tan", 0)
        self.protocol(number, 1)
        self.protocol(self.angle_unit.angle_symbol() + " =", 2)
        self.protocol_result(result, 3)

        return result