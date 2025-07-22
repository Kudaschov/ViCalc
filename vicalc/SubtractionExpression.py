from CalcPrios import CalcPrios
from BinaryExpression import BinaryExpression
from PySide6.QtWidgets import QTableWidgetItem

class SubtractionExpression(BinaryExpression):
    def __init__(self, number, tableWidget):
        super().__init__(number, tableWidget)
        self.operation_prio = CalcPrios.Addition

    def text(self):
        return self.first_number_to_string() + " - "
    
    def calculate(self, number: float):
        result: float = self.first_number - number

        self.insert_scroll_table()
        self.protocol(self.first_number, 0)
        self.protocol("-", 1)
        self.protocol(number, 2)
        self.protocol("=", 3)
        self.protocol_result(result, 4)

        return result