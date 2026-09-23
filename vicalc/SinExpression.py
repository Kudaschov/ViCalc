import math, cmath
from PySide6.QtWidgets import QTableWidgetItem
from .TrigExpression import TrigExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class SinExpression(TrigExpression):
    def calculate(self, number: float | complex):
        result: float | complex
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            result = cmath.sin(number)
            self.protocol_complex(number, " =", False, "sin(")
            self.insert_scroll_table()
            self.protocol_complex(result, "", True)
        else:
            result = math.sin(AppGlobals.angle_unit.to_rad(number))
            self.protocol("sin", 0)
            self.protocol(number, 1)
            self.protocol(AppGlobals.angle_unit.angle_symbol() + " =", 2)
            self.protocol_result(result, 3)
        return result