import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class FourthPowerExpression(UnaryExpression):
    def calculate(self, number: float):
        result: float = number ** 4
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(number, " ^ 4 =", False, "")
            self.insert_scroll_table()
            self.protocol_complex(result, "", True)
        else:
            self.protocol(number, 0)
            self.protocol("^4 =", 1)
            self.protocol_result(result, 2)

        return result