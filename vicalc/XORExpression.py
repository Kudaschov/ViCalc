from .CalcPrios import CalcPrios
from .IntegerBinaryExpression import IntegerBinaryExpression
from PySide6.QtWidgets import QTableWidgetItem

class XORExpression(IntegerBinaryExpression):
    def __init__(self, first_number):
        super().__init__(first_number)
        self.operation_prio = CalcPrios.XOR

    def text(self):
        return self.first_number_to_string() + " XOR "
    
    def calculate(self, number: float):
        super().calculate(number)  # Validate that both numbers are integers
    
        int_number = int(number)
        result: float = float(int(self.first_number) ^ int_number)

        self.insert_scroll_table()
        self.protocol(float(self.first_number), 0)
        self.protocol("XOR", 1)
        self.protocol(number, 2)
        self.protocol("=", 3)
        self.protocol_result(float(result), 4)

        return result