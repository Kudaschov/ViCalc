from PySide6.QtWidgets import QTableWidgetItem
from .CalcPrios import CalcPrios
from .MemoryExpression import MemoryExpression

class MMinusExpression(MemoryExpression):
    def calculate(self, number: float):
        result: float = self.first_number - number

        self.insert_scroll_table()
        self.protocol("M-", 0)
        self.protocol(number, 1)
        self.show_in_history(self.first_number, result)

        return result