import math
import cmath
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class RightShiftRotateCarryExpression(UnaryExpression):
    def calculate(self, number: int):
        AppGlobals.assert_int(number)
        bits = AppGlobals.current_word_size.bits
        mask = AppGlobals.current_word_size.mask
        # Mask input value to ensure it fits the given word size        
        masked_number = int(number) & mask
        # Extract the Least Significant Bit (LSB) that will wrap around
        lsb = masked_number & 1
        # rotate through carry bit
        carry = AppGlobals.carry_flag & 1
        # new carry flag
        AppGlobals.carry_flag = lsb
        result = ((masked_number >> 1) | (carry << (bits - 1))) & mask

        self.insert_scroll_table()
        self.protocol("RoRC (", 0)
        self.protocol(masked_number, 1)
        self.protocol(") = ", 2)
        self.protocol_result(result, 3)

        # show carry flag change in history
        self.protocol(f"  /  CF: {carry}->{AppGlobals.carry_flag}", 4)
        return result