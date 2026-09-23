import math, cmath
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class LnExpression(UnaryExpression):
    def calculate(self, number: float | complex):
        result: float| complex
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            result = cmath.log(number)
            self.protocol_complex(number, " =", False, "ln(")
            self.insert_scroll_table()
            self.protocol_complex(result, "", True)
        else:
            result = math.log(number)
            self.protocol("ln", 0)
            self.protocol(number, 1)
            self.protocol("=", 2)
            self.protocol_result(result, 3)
        return result