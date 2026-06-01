from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class LinearSystemExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self)-> float:
        self.insert_scroll_table()
        self.protocol_result("Linear System", 0)
        self.protocol_result("of", 1)
        self.protocol_result("Two Equations", 2)
        self.insert_scroll_table()
        self.protocol("a", 0)
        self.protocol("b", 1)
        self.protocol("c", 2)
        self.insert_scroll_table()
        self.protocol(AppGlobals.lse_a1, 0)
        self.protocol(AppGlobals.lse_b1, 1)
        self.protocol(AppGlobals.lse_c1, 2)
        self.insert_scroll_table()
        self.protocol(AppGlobals.lse_a2, 0)
        self.protocol(AppGlobals.lse_b2, 1)
        self.protocol(AppGlobals.lse_c2, 2)
        self.insert_scroll_table()
        D: float = AppGlobals.lse_discriminant(AppGlobals.lse_a1, AppGlobals.lse_b1, AppGlobals.lse_a2, AppGlobals.lse_b2)
        x: float = (AppGlobals.lse_c1 * AppGlobals.lse_b2 - AppGlobals.lse_c2 * AppGlobals.lse_b1) / D
        self.protocol("x", 0)
        self.protocol_result(x, 1)
        self.protocol("y", 2)
        self.protocol_result((AppGlobals.lse_a1 * AppGlobals.lse_c2 - AppGlobals.lse_a2 * AppGlobals.lse_c1) / D, 3)

        return x
