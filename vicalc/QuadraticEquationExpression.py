from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class QuadraticEquationExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self)-> float:
        self.insert_scroll_table()
        self.protocol_result("Quadratic Equation")
        self.insert_scroll_table()
        self.protocol("a = ")
        self.protocol(AppGlobals.quadratic_a)
        self.protocol("; b = ")
        self.protocol(AppGlobals.quadratic_b)
        self.protocol("; c = ")
        self.protocol(AppGlobals.quadratic_c)
        self.protocol("; discriminant (D) = ", 0)
        D: float = AppGlobals.discriminant(AppGlobals.quadratic_a, AppGlobals.quadratic_b, AppGlobals.quadratic_c)
        self.protocol(D)

        if D > 0:
            sqrt_D = D ** 0.5
            x1 = (-AppGlobals.quadratic_b + sqrt_D) / (2 * AppGlobals.quadratic_a)
            x2 = (-AppGlobals.quadratic_b - sqrt_D) / (2 * AppGlobals.quadratic_a)
            self.protocol("; two real roots")
            self.insert_scroll_table()
            self.protocol("x₁ = ")
            self.protocol_result(x1)
            self.protocol("; x₂ = ")
            self.protocol_result(x2)
            return x1
        elif D == 0:
            x1 = -AppGlobals.quadratic_b / (2 * AppGlobals.quadratic_a)
            self.protocol("; one real root")
            self.insert_scroll_table()
            self.protocol("x₁ = ")
            self.protocol_result(x1)
            return x1
        else:
            real = -AppGlobals.quadratic_b / (2 * AppGlobals.quadratic_a)
            imag = (-D) ** 0.5 / (2 * AppGlobals.quadratic_a)
            z1 = complex(real, imag)
            z2 = complex(real, -imag)
            self.protocol("; two complex roots")
            self.insert_scroll_table()
            self.protocol_complex(z1, "", True, "x₁ = (")
            self.protocol_complex(z2, "", True, "; x₂ = (")
            return real
