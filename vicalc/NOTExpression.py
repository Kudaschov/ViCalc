import math
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode
from .NumberBase import NumberBase

class NOTExpression(UnaryExpression):
    def calculate(self, number: int):
        AppGlobals.assert_int(number)
        int_number = int(number)

        # Apply bitwise NOT and mask to fit the target word size
        mask: int = AppGlobals.current_word_size.mask
        masked_number = int_number & mask
        result: int = (~masked_number) & mask
        result = AppGlobals.check_for_signed_number(result)

        self.insert_scroll_table()
        self.protocol("NOT ", 0)
        self.protocol(AppGlobals.check_for_signed_number(masked_number), 1)
        self.protocol(" = ", 2)
        self.protocol_result(result, 3)

        return result