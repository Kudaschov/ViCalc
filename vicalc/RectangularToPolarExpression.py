import math
from PySide6.QtCore import QLocale
from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression
from PySide6.QtWidgets import QTableWidgetItem
from .AppGlobals import AppGlobals

class RectangularToPolarExpression(BinaryExpression):
    def __init__(self, first_number):
        super().__init__(first_number)
        self.operation_prio = CalcPrios.Addition

    def calculate(self, number: float):
        x = self.first_number
        y = number
        r = math.hypot(x, y)
        theta = math.atan2(y, x)
        theta = AppGlobals.angle_unit.from_rad(theta)


        self.insert_scroll_table()
        self.protocol("X", 0)
        self.protocol("Y", 1)
        self.protocol("R", 2)
        angle_symbol = AppGlobals.angle_unit.angle_symbol() 
        self.protocol(f"θ [{angle_symbol}]", 3)
        self.insert_scroll_table()
        self.protocol(x, 0)
        self.protocol(y, 1)
        self.protocol_result(r, 2)
        self.protocol_result(theta, 3)

        return r