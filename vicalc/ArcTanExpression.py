import math, cmath
from PySide6.QtWidgets import QTableWidgetItem
from .TrigExpression import TrigExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class ArcTanExpression(TrigExpression):
    def calculate(self, number: float):
        result: float | complex
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            result = cmath.atan(number)
            self.protocol_complex(number, " =", False, "arctan(")
            self.insert_scroll_table()
            self.protocol_complex(result, "", True)
        else:
            result: float = AppGlobals.angle_unit.from_rad(math.atan(number))
            self.protocol("arctan", 0)
            self.protocol(number, 1)
            self.protocol("=", 2)
            self.protocol_result(result, 3)
            self.protocol(AppGlobals.angle_unit.angle_symbol(), 4)
        return result