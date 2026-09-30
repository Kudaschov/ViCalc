import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class MSExpression(UnaryExpression):
    def calculate(self, number: int | float | complex):
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(number, "", True, "Memory: (")
        else:
            self.protocol("Memory:", 0)
            self.protocol_result(number, 1)
            if number == 0:
                self.protocol("Cleared", 2)
            
        return number