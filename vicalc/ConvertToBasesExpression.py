import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

# converts decimal number to bases 2, 8, and 16
class ConvertToBasesExpression(UnaryExpression):
    def calculate(self, number):
        i_number: int = int(number)

        self.insert_scroll_table()
        self.protocol(f"{bin(i_number)}", 0)
        self.protocol(f"{oct(i_number)}", 1)
        self.protocol_result(str(i_number), 2)

        hex_column = 3

        if (i_number >= 0):
            signed_int, signed = AppGlobals.uint_to_signed_int(i_number)
            if signed:
                hex_column = 4
                self.protocol_result(f"{str(signed_int)} ({AppGlobals.current_word_size.status_text})", 3)

        self.protocol(AppGlobals.int_to_hex_with_prefix(i_number), hex_column)

        return i_number