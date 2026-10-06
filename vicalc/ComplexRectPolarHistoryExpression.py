import math, cmath
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class ComplexRectPolarHistoryExpression(UnaryExpression):
    def calculate(self, number):
        z = number

        self.insert_scroll_table()
        self.protocol("(")
        self.protocol(z.real)

        if z.imag >= 0:
            self.protocol("+")

        self.protocol(z.imag)
        self.protocol("i) = ", 3)
        r, theta = cmath.polar(z)
        self.protocol(r)
        self.protocol("∠")
        self.protocol(AppGlobals.angle_unit.from_rad(theta))
        self.protocol(f" {AppGlobals.angle_unit.angle_symbol()}")

        return z