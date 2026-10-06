import math
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class ReciprocalExpression(UnaryExpression):
    def calculate(self, number: float):
        result: float = 1.0 / number
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(number, " = ", False, "1 / (")
            self.protocol_complex(result, "", True)
        else:
            self.protocol("1 / ", -1)
            self.protocol(number, -1)
            self.protocol(" = ", -1)
            self.protocol_result(result, -1)
        return result