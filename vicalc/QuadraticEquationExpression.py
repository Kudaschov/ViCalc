from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class QuadraticEquationExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self)-> float:
        self.insert_scroll_table()
        self.protocol_result("Quadratic", 0)
        self.protocol_result("Equation", 1)
        self.insert_scroll_table()
        self.protocol("a", 0)
        self.protocol(AppGlobals.quadratic_a, 1)
        self.protocol("b", 2)
        self.protocol(AppGlobals.quadratic_b, 3)
        self.protocol("c", 4)
        self.protocol(AppGlobals.quadratic_c, 5)
        self.insert_scroll_table()
        self.protocol("Discriminant (D)", 0)
        D: float = AppGlobals.discriminant(AppGlobals.quadratic_a, AppGlobals.quadratic_b, AppGlobals.quadratic_c)
        self.protocol(D, 1)

        if D > 0:
            sqrt_D = D ** 0.5
            x1 = (-AppGlobals.quadratic_b + sqrt_D) / (2 * AppGlobals.quadratic_a)
            x2 = (-AppGlobals.quadratic_b - sqrt_D) / (2 * AppGlobals.quadratic_a)
            self.protocol("Two Real Roots", 2)
            self.insert_scroll_table()
            self.protocol("x1", 0)
            self.protocol_result(x1, 1)
            self.protocol("x2", 2)
            self.protocol_result(x2, 3)
            return x1
        elif D == 0:
            x1 = -AppGlobals.quadratic_b / (2 * AppGlobals.quadratic_a)
            self.protocol("One Real Root", 2)
            self.insert_scroll_table()
            self.protocol("x1", 0)
            self.protocol_result(x1, 1)
            return x1
        else:
            real = -AppGlobals.quadratic_b / (2 * AppGlobals.quadratic_a)
            imag = (-D) ** 0.5 / (2 * AppGlobals.quadratic_a)
            self.protocol("Two Complex", 2)
            self.protocol("Roots", 3)
            self.insert_scroll_table()
            self.protocol("x1", 0)
            self.protocol_result(real, 1)
            self.protocol("+", 2)
            self.protocol_result(imag, 3)
            self.protocol("i", 4)
            self.insert_scroll_table()
            self.protocol("x2", 0)
            self.protocol_result(real, 1)
            self.protocol("-", 2)
            self.protocol_result(imag, 3)
            self.protocol("i", 4)
            return real
