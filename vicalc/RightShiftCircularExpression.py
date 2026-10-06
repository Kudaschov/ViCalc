import math
import cmath
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class RightShiftCircularExpression(UnaryExpression):
    def calculate(self, number: int):
        AppGlobals.assert_int(number)
        bits = AppGlobals.current_word_size.bits
        mask = AppGlobals.current_word_size.mask
        # Mask input value to ensure it fits the given word size        
        masked_number = int(number) & mask
        # Extract the Least Significant Bit (LSB) that will wrap around
        lsb = masked_number & 1

        # Shift right by 1 bit, insert the LSB at the Most Significant Bit (MSB) position,
        # and restrict the result to the word size using the mask.
        result = ((masked_number >> 1) | (lsb << (bits - 1))) & mask
        self.insert_scroll_table()
        self.protocol("RoR (", 0)
        self.protocol(masked_number, 1)
        self.protocol(") =", 2)
        self.protocol_result(result, 3)
        return result