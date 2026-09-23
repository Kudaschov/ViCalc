import cmath
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class AbsExpression(UnaryExpression):
    def calculate(self, number: float):
        result: float = abs(number)
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(number, " =", False, "Absolute value (")
            self.insert_scroll_table()
            self.protocol_complex(result, "", True)
        else:
            self.protocol("Absolute value", 0)
            self.protocol(number, 1)
            self.protocol("=", 2)
            self.protocol_result(result, 3)

        return result