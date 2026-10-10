import math
from PySide6.QtCore import QLocale
from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression
from .AppGlobals import AppGlobals

class PolarToRectangularExpression(BinaryExpression):
    def __init__(self, first_number):
        super().__init__(first_number)
        self.operation_prio = CalcPrios.Addition
        self.operation_prio = CalcPrios.Bracket

    def text(self) -> str:
        return f"P→R; r = {self.first_number_to_string()}; θ = "

    def calculate(self, number: float):
        r = self.first_number
        theta = number
        theta_rad = AppGlobals.angle_unit.to_rad(theta)
        x = r * math.cos(theta_rad)
        y = r * math.sin(theta_rad)

        self.insert_scroll_table()
        self.protocol("r= ")
        self.protocol(r)
        self.protocol("; θ= ")
        self.protocol(theta)
        angle_symbol = AppGlobals.angle_unit.angle_symbol() 
        self.protocol(angle_symbol)
        self.protocol(" ▶ x= ")
        self.protocol_result(x)
        self.protocol("; y= ")
        self.protocol_result(y)

        return x