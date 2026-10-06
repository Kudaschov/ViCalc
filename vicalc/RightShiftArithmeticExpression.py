import cmath
from typing import Any
from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode
from .ComplexNumberForm import ComplexNumberForm

class RightShiftArithmeticExpression(BinaryExpression):
    """Expression executing arithmetic right shift."""

    def __init__(self, first_number: float | complex, table_widget: Any = None) -> None:
        super().__init__(first_number, table_widget)
        self.operation_prio = CalcPrios.Bracket

    def text(self) -> str:
        return f"AshR {self.first_number_to_string()} >> "
    
    def calculate(self, shift_bits: float):
        AppGlobals.assert_int(self.first_number)
        AppGlobals.assert_int(shift_bits)

        bits = AppGlobals.current_word_size.bits
        mask = AppGlobals.current_word_size.mask
        
        # Mask input value to ensure it fits the given word size
        masked_number = int(self.first_number) & mask
        
        # Limit shift range to prevent unnecessary huge shifts
        shift_amount = int(shift_bits) % bits
        
        # Check if Most Significant Bit (MSB/Sign Bit) is set
        sign_bit_set = (masked_number & (1 << (bits - 1))) != 0
        
        # Perform arithmetic right shift preserving the sign bit (Sign Extension)
        shifted = masked_number >> shift_amount
        if sign_bit_set:
            # Fill highest bits with 1s if sign bit was set
            pad_mask = ((1 << shift_amount) - 1) << (bits - shift_amount)
            result = (shifted | pad_mask) & mask
        else:
            result = shifted & mask
            
        self.insert_scroll_table()

        self.protocol("AshR: ", 0)
        self.protocol(masked_number, 1)
        self.protocol(" >> ", 2)
        self.protocol(shift_amount, 3)
        self.protocol(" = ", 4)
        self.protocol_result(result, 5)
        return result