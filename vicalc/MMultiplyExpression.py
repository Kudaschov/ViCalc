from PySide6.QtWidgets import QTableWidgetItem
from .CalcPrios import CalcPrios
from .MemoryExpression import MemoryExpression

class MMultiplyExpression(MemoryExpression):
    def calculate(self, number: float):
        result: float = self.first_number * number

        self.insert_scroll_table()
        self.protocol(self.first_number, 0)
        self.protocol("*", 1)
        self.protocol(number, 2)
        self.protocol("=", 3)
        self.protocol_result(result, 4)
        self.protocol("Memory", 5)

        return result