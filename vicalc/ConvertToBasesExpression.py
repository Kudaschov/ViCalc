import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode
from .NumberBase import NumberBase

# converts decimal number to bases 2, 8, and 16
class ConvertToBasesExpression(UnaryExpression):
    def calculate(self, number: int):
        AppGlobals.assert_int(number)
        if AppGlobals.calc_mode is CalcMode.base_n:
            mask = AppGlobals.current_word_size.mask
            i_number: int = int(number) & mask
        else:
            i_number = int(number)
        self.insert_scroll_table()
        self.protocol(AppGlobals.to_format_string(i_number, NumberBase.BIN), 0)
        self.protocol(AppGlobals.to_format_string(i_number, NumberBase.OCT), 1)
        self.protocol_result(f"{i_number}", 2)

        hex_column = 3

        if AppGlobals.calc_mode is CalcMode.base_n:
            signed_val, signed = AppGlobals.uint_to_signed_int(i_number)
            if signed:
                self.protocol_result(f"{signed_val}", 3)
                hex_column = hex_column + 1
                
        self.protocol(AppGlobals.to_format_string(i_number, NumberBase.HEX), hex_column)

        return i_number