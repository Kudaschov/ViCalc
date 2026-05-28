from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class RatioDExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self):
        result: float = AppGlobals.ratio_d_b * AppGlobals.ratio_d_c / AppGlobals.ratio_d_a

        self.insert_scroll_table()
        self.protocol("Ratio Calculation", 0)
        self.protocol("Unknown D", 1)
        self.insert_scroll_table()
        self.protocol("a", 0)
        self.protocol(AppGlobals.ratio_d_a, 1)
        self.protocol("c", 2)
        self.protocol(AppGlobals.ratio_d_c, 3)
        self.insert_scroll_table()
        self.protocol("b", 0)
        self.protocol(AppGlobals.ratio_d_b, 1)
        self.protocol("d", 2)
        self.protocol_result(result, 3)

        return result