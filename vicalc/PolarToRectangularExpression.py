import math
from PySide6.QtCore import QLocale
from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression
from PySide6.QtWidgets import QTableWidgetItem
from .AppGlobals import AppGlobals

class PolarToRectangularExpression(BinaryExpression):
    def __init__(self, first_number):
        super().__init__(first_number)
        self.operation_prio = CalcPrios.Addition

    def calculate(self, number: float):
        r = self.first_number
        theta = number
        theta_rad = AppGlobals.angle_unit.to_rad(theta)
        x = r * math.cos(theta_rad)
        y = r * math.sin(theta_rad)

        self.insert_scroll_table()
        self.protocol_result("X", 0)
        self.protocol_result("Y", 1)
        self.protocol_result("R", 2)
        angle_symbol = AppGlobals.angle_unit.angle_symbol() 
        self.protocol_result(f"θ [{angle_symbol}]", 3)
        self.insert_scroll_table()
        self.protocol(x, 0)
        self.protocol(y, 1)
        self.protocol(r, 2)
        self.protocol(theta, 3)

        return x