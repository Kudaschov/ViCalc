import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class ReciprocalExpression(UnaryExpression):
    def calculate(self, number: float):
        result: float = 1.0 / number
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(number, " =", False, "1 / (")
            self.insert_scroll_table()
            self.protocol_complex(result, "", True)
        else:
            self.protocol("1", 0)
            self.protocol("/", 1)
            self.protocol(number, 2)
            self.protocol("=", 3)
            self.protocol_result(result, 4)
        return result