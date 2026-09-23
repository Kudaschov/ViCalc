import math, cmath
from PySide6.QtWidgets import QTableWidgetItem
from .TrigExpression import TrigExpression
from .CalcMode import CalcMode
from .AppGlobals import AppGlobals

class ArcSinExpression(TrigExpression):
    def calculate(self, number: float | complex):
        result: float | complex
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            result = cmath.asin(number)
            self.protocol_complex(number, " =", False, "arcsin(")
            self.insert_scroll_table()
            self.protocol_complex(result, "", True)
        else:
            result: float = AppGlobals.angle_unit.from_rad(math.asin(number))
            self.protocol("arcsin", 0)
            self.protocol(number, 1)
            self.protocol("=", 2)
            self.protocol_result(result, 3)
            self.protocol(AppGlobals.angle_unit.angle_symbol(), 4)
        return result