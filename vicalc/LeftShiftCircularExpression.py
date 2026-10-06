import math
import cmath
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class LeftShiftCircularExpression(UnaryExpression):
    def calculate(self, number: float):
        AppGlobals.assert_int(number)
        bits = AppGlobals.current_word_size.bits
        mask = AppGlobals.current_word_size.mask
        # Mask input value to ensure it fits the given word size        
        masked_number = int(number) & mask
        # Extract the Most Significant Bit (MSB) that will wrap around
        msb = (masked_number >> (bits - 1)) & 1

        # Shift left by 1 bit, insert the MSB at the Least Significant Bit (LSB) position,
        # and restrict the result to the word size using the mask.
        result = ((masked_number << 1) | msb) & mask
        self.insert_scroll_table()
        self.protocol("RoL (", 0)
        self.protocol(masked_number, 1)
        self.protocol(") =", 2)
        self.protocol_result(result, 3)
        return result