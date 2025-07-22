import math
from PySide6.QtWidgets import QTableWidgetItem
from TrigExpression import TrigExpression

class ArcSinExpression(TrigExpression):
    def calculate(self, number: float):
        result: float = self.angle_unit.from_rad(math.asin(number))
        self.insert_scroll_table()
        self.protocol("arcsin", 0)
        self.protocol(number, 1)
        self.protocol("=", 2)
        self.protocol_result(result, 3)
        self.protocol(self.angle_unit.angle_symbol(), 4)

        return result