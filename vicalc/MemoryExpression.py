from PySide6.QtWidgets import QTableWidgetItem
from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression

class MemoryExpression(BinaryExpression):
    def __init__(self, first_number, tableWidget):
        super().__init__(first_number, tableWidget)
        self.operation_prio = CalcPrios.Addition

    def show_in_history(self, before, after: float):
        self.insert_scroll_table()
        self.protocol("Memory:", 0)
        self.protocol(before, 1)
        self.protocol("->", 2)
        self.protocol_result(after, 3)
