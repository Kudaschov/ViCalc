import math, cmath
from .UnaryExpression import UnaryExpression
from .CalcMode import CalcMode
from .AppGlobals import AppGlobals

class CoshExpression(UnaryExpression):
    def calculate(self, number: float | complex):
        result: float | complex
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            result = cmath.cosh(number)
            self.protocol_complex(number, " = ", False, "cosh(")
            self.protocol_complex(result, "", True)
        else:
            result: float = math.cosh(number)
            self.protocol("cosh(", 0)
            self.protocol(number, 1)
            self.protocol(") = ", 2)
            self.protocol_result(result, 3)
        return result