from PySide6.QtWidgets import QTableWidgetItem
from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression

class MMultiplyExpression(BinaryExpression):
    def __init__(self, first_number, tableWidget):
        super().__init__(first_number, tableWidget)
        self.operation_prio = CalcPrios.Multiplication

    def calculate(self, number: float):
        result: float = self.first_number * number

        self.insert_scroll_table()
        self.protocol("M*:", 0)
        self.protocol(self.first_number, 1)
        self.protocol("*", 2)
        self.protocol(number, 3)
        self.protocol("=", 4)
        self.protocol_result(result, 5)

        return result