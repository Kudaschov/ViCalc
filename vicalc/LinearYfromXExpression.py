from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class LinearYfromXExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self, number:float) -> float:
        self.insert_scroll_table()
        self.protocol_result("Calculate Y from linear function", 2)
        self.insert_scroll_table()
        self.protocol("Slope (a): ")
        self.protocol(AppGlobals.linear_a)
        self.protocol("; Intercept (b): ")
        self.protocol(AppGlobals.linear_b, 3)
        result = AppGlobals.linear_a * number + AppGlobals.linear_b
        self.protocol("; x = ")
        self.protocol(number)
        self.protocol("; y = ", 2)
        self.protocol_result(result, 3)

        return result