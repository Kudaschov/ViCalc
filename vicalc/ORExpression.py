from .CalcPrios import CalcPrios
from .IntegerBinaryExpression import IntegerBinaryExpression
from PySide6.QtWidgets import QTableWidgetItem

class ORExpression(IntegerBinaryExpression):
    def __init__(self, first_number):
        super().__init__(first_number)
        self.operation_prio = CalcPrios.OR

    def text(self):
        return self.first_number_to_string() + " OR "
    
    def calculate(self, number: float):
        super().calculate(number)  # Validate that both numbers are integers
    
        int_number = int(number)
        result: int = int(self.first_number) | int_number

        self.insert_scroll_table()
        self.protocol(int(self.first_number), 0)
        self.protocol("Bitwise OR", 1)
        self.protocol(int_number, 2)
        self.protocol("=", 3)
        self.protocol_result(result, 4)

        return float(result)