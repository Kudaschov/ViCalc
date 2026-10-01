import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class CubeRootExpression(UnaryExpression):
    def calculate(self, number: float):
        result: float = number ** (1.0 / 3.0)
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(number, " =", False, "³√(")
            self.insert_scroll_table()
            self.protocol_complex(result, "", True)
        else:
            self.protocol("³√", 0)
            self.protocol(number, 1)
            self.protocol("=", 2)
            self.protocol_result(result, 3)
        return result