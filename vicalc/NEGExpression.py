import math
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode
from .NumberBase import NumberBase

class NEGExpression(UnaryExpression):
    def calculate(self, number: float):
        AppGlobals.assert_int(number)
        int_number = int(number)
        mask: int = AppGlobals.current_word_size.mask
        masked_number = int_number & mask
        raw_result = (~masked_number + 1) & mask
        result = AppGlobals.check_for_signed_number(raw_result)

        self.insert_scroll_table()
        self.protocol("NEG", 0)
        self.protocol(AppGlobals.check_for_signed_number(masked_number), 1)
        self.protocol("=", 2)
        self.protocol_result(result, 3)

        return result