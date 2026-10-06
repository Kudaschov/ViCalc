import math
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class SquareExpression(UnaryExpression):
    def calculate(self, number: float | complex):
        result = number ** 2
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(number, " ^ 2 = ", False, "")
            self.protocol_complex(result, "", True)
        else:
            self.protocol(number, -1)
            self.protocol(" ^ 2 = ", -1)
            self.protocol_result(result, -1)
        return result