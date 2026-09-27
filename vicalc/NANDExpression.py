from .CalcPrios import CalcPrios
from .IntegerBinaryExpression import IntegerBinaryExpression
from PySide6.QtWidgets import QTableWidgetItem
from .AppGlobals import AppGlobals

class NANDExpression(IntegerBinaryExpression):
    def __init__(self, first_number):
        super().__init__(first_number)
        self.operation_prio = CalcPrios.AND

    def text(self):
        return self.first_number_to_string() + " NAND "
    
    def calculate(self, number: float):
        super().calculate(number)  # Validate that both numbers are integers
    
        int_number = int(number) & AppGlobals.current_word_size.mask
        int_first_number = int(self.first_number) & AppGlobals.current_word_size.mask
        result: int = ~(int_first_number & int_number) & AppGlobals.current_word_size.mask

        self.insert_scroll_table()
        self.protocol(int_first_number, 0)
        self.protocol("NAND", 1)
        self.protocol(int_number, 2)
        self.protocol("=", 3)
        self.protocol_result(result, 4)

        return result