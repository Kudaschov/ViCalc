from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class RatioCExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self):
        result: float = AppGlobals.ratio_c_a * AppGlobals.ratio_c_d / AppGlobals.ratio_c_b

        self.insert_scroll_table()
        self.protocol_result("Ratio", 0)
        self.protocol_result("Calculation", 1)
        self.protocol_result("Unknown C", 2)
        self.insert_scroll_table()
        self.protocol("a", 0)
        self.protocol(AppGlobals.ratio_c_a, 1)
        self.protocol("c", 2)
        self.protocol_result(result, 3)
        self.insert_scroll_table()
        self.protocol("b", 0)
        self.protocol(AppGlobals.ratio_c_b, 1)
        self.protocol("d", 2)
        self.protocol(AppGlobals.ratio_c_d, 3)

        return result