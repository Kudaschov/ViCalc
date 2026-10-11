from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class LinearSystemExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self)-> float:
        self.insert_scroll_table()
        self.protocol_result("Linear system of two equations", 2)
        self.insert_scroll_table()
        self.protocol("a₁ = ")
        self.protocol(AppGlobals.lse_a1)
        self.protocol("; b₁ = ")
        self.protocol(AppGlobals.lse_b1)
        self.protocol("; c₁ = ")
        self.protocol(AppGlobals.lse_c1)
        self.insert_scroll_table()
        self.protocol("a₂ = ")
        self.protocol(AppGlobals.lse_a2)
        self.protocol("; b₂ = ")
        self.protocol(AppGlobals.lse_b2)
        self.protocol("; c₂ = ")
        self.protocol(AppGlobals.lse_c2)
        self.insert_scroll_table()
        D: float = AppGlobals.lse_discriminant(AppGlobals.lse_a1, AppGlobals.lse_b1, AppGlobals.lse_a2, AppGlobals.lse_b2)
        x: float = (AppGlobals.lse_c1 * AppGlobals.lse_b2 - AppGlobals.lse_c2 * AppGlobals.lse_b1) / D
        self.protocol("x = ")
        self.protocol_result(x)
        self.protocol("; y = ")
        self.protocol_result((AppGlobals.lse_a1 * AppGlobals.lse_c2 - AppGlobals.lse_a2 * AppGlobals.lse_c1) / D, 3)

        return x
