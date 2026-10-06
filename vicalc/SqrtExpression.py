import math
import cmath
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class SqrtExpression(UnaryExpression):
    def calculate(self, number: float):
        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            result = cmath.sqrt(number)
        else:
            result: float = math.sqrt(number)
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(number, " = ", False, "√(")
            self.protocol_complex(result, "", True)
        else:
            self.protocol("√", -1)
            self.protocol(number, -1)
            self.protocol(" = ", -1)
            self.protocol_result(result, -1)

        return result