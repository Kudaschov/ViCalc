import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression

# converts decimal number to bases 2, 8, and 16
class ConvertToBasesExpression(UnaryExpression):
    def calculate(self, number):
        result = number
        i_number = int(number)

        self.insert_scroll_table()
        self.protocol(f"{bin(i_number)}", 0)
        self.protocol(f"{oct(i_number)}", 1)
        self.protocol_result(result, 2)
        self.protocol(f"0x{i_number:X}", 3)

        return result