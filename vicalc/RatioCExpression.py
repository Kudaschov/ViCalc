from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class RatioCExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self):
        result: float = AppGlobals.ratio_c_a * AppGlobals.ratio_c_d / AppGlobals.ratio_c_b
        self.insert_scroll_table()
        self.protocol("a / b = X / d; ")
        self.protocol(AppGlobals.ratio_c_a)
        self.protocol(" / ")
        self.protocol(AppGlobals.ratio_c_b)
        self.protocol(" = X / ")
        self.protocol(AppGlobals.ratio_c_d)
        self.protocol("; X = ")
        self.protocol_result(result)

        return result