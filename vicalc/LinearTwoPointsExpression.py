from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class LinearTwoPointsExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self):
        a: float = (AppGlobals.linear_y1 - AppGlobals.linear_y0) / (AppGlobals.linear_x1 - AppGlobals.linear_x0)
        b: float = AppGlobals.linear_y0 - a * AppGlobals.linear_x0

        self.insert_scroll_table()
        self.protocol_result("Linear Function", 0)
        self.protocol_result("from", 1)
        self.protocol_result("Two Points", 2)
        self.insert_scroll_table()
        self.protocol("x0", 0)
        self.protocol(AppGlobals.linear_x0, 1)
        self.protocol("y0", 2)
        self.protocol(AppGlobals.linear_y0, 3)
        self.insert_scroll_table()
        self.protocol("x1", 0)
        self.protocol(AppGlobals.linear_x1, 1)
        self.protocol("y1", 2)
        self.protocol(AppGlobals.linear_y1, 3)
        self.insert_scroll_table()
        self.protocol("y =", 0)
        self.protocol_result(a, 1)
        self.protocol("* x", 2)

        if (b >= 0):
            self.protocol("+", 3)
            self.protocol_result(b, 4)
        else:
            self.protocol_result(b, 3)

        return a