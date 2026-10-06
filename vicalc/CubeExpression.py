import math
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class CubeExpression(UnaryExpression):
    def calculate(self, number: float | complex):
        result = number ** 3
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(number, " ^ 3 = ", False, "")
            self.protocol_complex(result, "", True)
        else:
            self.protocol(number, 0)
            self.protocol(" ^ 3 = ", 1)
            self.protocol_result(result, 2)
        return result