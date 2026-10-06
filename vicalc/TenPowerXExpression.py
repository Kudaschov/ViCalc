from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class TenPowerXExpression(UnaryExpression):
    def calculate(self, number: float | complex):
        result: float | complex = 10 ** number
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(number, " = ", False, "10^(")
            self.protocol_complex(result, "", True)
        else:
            self.protocol("10 ^ ", 0)
            self.protocol(number, 1)
            self.protocol(" = ", 2)
            self.protocol_result(result, 3)
        return result