import math
from PySide6.QtWidgets import QTableWidgetItem
from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression

class PercentChangeExpression(BinaryExpression):
    def __init__(self, first_number):
        super().__init__(first_number)
        self.operation_prio = CalcPrios.Bracket

    def text(self):
        return "Old value: " + self.first_number_to_string()
    
    def calculate(self, number: float):
        result: float = (number - self.first_number) / self.first_number * 100

        self.insert_scroll_table()
        self.protocol("Old value", 0)
        self.protocol(self.first_number, 1)
        self.protocol("New value", 2)
        self.protocol(number, 3)
        self.protocol("Δ%", 4)
        self.protocol_result(result, 5)

        return result