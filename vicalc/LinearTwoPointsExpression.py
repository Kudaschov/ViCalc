from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class LinearTwoPointsExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self):
        a: float = (AppGlobals.linear_y1 - AppGlobals.linear_y0) / (AppGlobals.linear_x1 - AppGlobals.linear_x0)
        b: float = AppGlobals.linear_y0 - a * AppGlobals.linear_x0

        self.insert_scroll_table()
        self.protocol_result("Linear function from two points")
        self.insert_scroll_table()
        self.protocol("x0 = ")
        self.protocol(AppGlobals.linear_x0)
        self.protocol("; y0 = ", 2)
        self.protocol(AppGlobals.linear_y0)
        self.protocol("; x1 = ", 0)
        self.protocol(AppGlobals.linear_x1)
        self.protocol("; y1 = ")
        self.protocol(AppGlobals.linear_y1)
        self.insert_scroll_table()
        self.protocol("y = ")
        self.protocol_result(a)
        self.protocol(" * x ")

        if (b >= 0):
            self.protocol("+ ", 3)
            self.protocol_result(b, 4)
        else:
            self.protocol_result(b, 3)

        return a