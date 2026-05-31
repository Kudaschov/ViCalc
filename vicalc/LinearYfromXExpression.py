from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class LinearYfromXExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self, number:float) -> float:
        self.insert_scroll_table()
        self.protocol("Calculate Y", 0)
        self.protocol("from", 1)
        self.protocol("Linear Function", 2)
        self.insert_scroll_table()
        self.protocol("Slope (a)", 0)
        self.protocol(AppGlobals.linear_a, 1)
        self.protocol("Intercept (b)", 2)
        self.protocol(AppGlobals.linear_b, 3)

        self.insert_scroll_table()
        result = AppGlobals.linear_a * number + AppGlobals.linear_b
        self.protocol("x", 0)
        self.protocol(number, 1)
        self.protocol("y", 2)
        self.protocol_result(result, 3)

        return result