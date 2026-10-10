import math
from PySide6.QtCore import QLocale
from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression
from .AppGlobals import AppGlobals

class RectangularToPolarExpression(BinaryExpression):
    def __init__(self, first_number):
        super().__init__(first_number)
        self.operation_prio = CalcPrios.Bracket

    def text(self) -> str:
        return f"R→P; x = {self.first_number_to_string()}; y = "
    
    def calculate(self, number: float):
        x = self.first_number
        y = number
        r = math.hypot(x, y)
        theta = math.atan2(y, x)
        theta = AppGlobals.angle_unit.from_rad(theta)

        self.insert_scroll_table()
        self.protocol("x= ")
        self.protocol(x)
        self.protocol("; y= ")
        self.protocol(y)
        self.protocol(" ▶ r= ")
        self.protocol_result(r)
        self.protocol("; θ= ")
        self.protocol_result(theta)
        angle_symbol = AppGlobals.angle_unit.angle_symbol() 
        self.protocol(f" {angle_symbol}")

        return r