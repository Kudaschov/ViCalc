import cmath
from typing import Any
from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode
from .ComplexNumberForm import ComplexNumberForm

class LeftShiftArithmeticExpression(BinaryExpression):
    """Expression executing addition."""

    def __init__(self, first_number: float | complex, table_widget: Any = None) -> None:
        super().__init__(first_number, table_widget)
        self.operation_prio = CalcPrios.Bracket

    def text(self) -> str:
        return f"AshL {self.first_number_to_string()} << "
    
    def calculate(self, shift_bits: float):
        AppGlobals.assert_int(self.first_number)
        AppGlobals.assert_int(shift_bits)

        bits = AppGlobals.current_word_size.bits
        mask = AppGlobals.current_word_size.mask
        
        # Mask input value to ensure it fits the given word size
        masked_number = int(self.first_number) & mask
        
        # Limit shift range to prevent unnecessary huge shifts
        shift_amount = int(shift_bits) % bits
        
        # Perform arithmetic left shift (fills rightmost bits with 0s)
        result = (masked_number << shift_amount) & mask        
        self.insert_scroll_table()

        self.protocol("AshL", 0)
        self.protocol(masked_number, 1)
        self.protocol("<<", 2)
        self.protocol(shift_amount, 3)
        self.protocol(" =", 4)
        self.protocol_result(result, 5)
        return result