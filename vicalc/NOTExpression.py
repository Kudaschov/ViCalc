import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class NOTExpression(UnaryExpression):
    def calculate(self, number: float):
        result: int = (~int(number)) & AppGlobals.current_word_size.mask

        self.insert_scroll_table()
        self.protocol("Bitwise NOT", 0)
        self.protocol(number, 1)
        self.protocol("=", 2)
        self.protocol_result(result, 3)

        return float(result)