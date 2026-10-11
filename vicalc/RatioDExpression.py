from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class RatioDExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self):
        result: float = AppGlobals.ratio_d_b * AppGlobals.ratio_d_c / AppGlobals.ratio_d_a

        self.insert_scroll_table()
        self.protocol("a / b = c / X; ")
        self.protocol(AppGlobals.ratio_d_a)
        self.protocol(" / ")
        self.protocol(AppGlobals.ratio_d_b, 3)
        self.protocol(" = ")
        self.protocol(AppGlobals.ratio_d_c, 1)
        self.protocol(" / X; X =")
        self.protocol_result(result, 3)

        return result