import math
import cmath
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class LeftShiftRotateCarryExpression(UnaryExpression):
    def calculate(self, number: float):
        AppGlobals.assert_int(number)
        bits = AppGlobals.current_word_size.bits
        mask = AppGlobals.current_word_size.mask
        # Mask input value to ensure it fits the given word size        
        masked_number = int(number) & mask
        # Extract the Most Significant Bit (MSB) that will wrap around
        msb = (masked_number >> (bits - 1)) & 1
        # Rotate through carry bit
        carry = AppGlobals.carry_flag & 1
        # new carry flag
        AppGlobals.carry_flag = msb
        result = ((masked_number << 1) | carry) & mask
        result_text = "RoLC ("

        self.insert_scroll_table()
        self.protocol(result_text, 0)
        self.protocol(masked_number, 1)
        self.protocol(") =", 2)
        self.protocol_result(result, 3)

        # show carry flag change in history
        self.protocol(f"CF: {carry}->{AppGlobals.carry_flag}", 4)
        return result