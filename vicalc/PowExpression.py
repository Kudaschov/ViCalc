import math
from CalcPrios import CalcPrios
from BinaryExpression import BinaryExpression
from PySide6.QtWidgets import QTableWidgetItem

class PowExpression(BinaryExpression):
    def __init__(self, first_number, tableWidget):
        super().__init__(first_number, tableWidget)
        self.operation_prio = CalcPrios.Power

    def text(self):
        return self.first_number_to_string() + " ^ "
    
    def calculate(self, number: float):
        result: float = math.pow(self.first_number, number)

        self.insert_scroll_table()
        self.protocol(self.first_number, 0)
        self.protocol("^", 1)
        self.protocol(number, 2)
        self.protocol("=", 3)
        self.protocol_result(result, 4)

        return result