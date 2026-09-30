import math, cmath
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class ComplexRectPolarHistoryExpression(UnaryExpression):
    def calculate(self, number):
        z = number

        self.insert_scroll_table()
        self.protocol_result("Real part", 0)

        if (z.imag < 0):
            self.protocol_result("Imag part", 1)
        else:
            self.protocol_result("Imag part", 2)

        next_column = 3
        if z.imag >= 0:
            next_column += 1
        self.protocol_result("r", next_column)
        next_column += 1
        angle_symbol = AppGlobals.angle_unit.angle_symbol() 
        self.protocol_result(f"θ [{angle_symbol}]", next_column)
       
        self.insert_scroll_table()
        self.protocol(z.real, 0)

        next_column = 1
        if z.imag >= 0:
            self.protocol("+", next_column)
            next_column += 1

        self.protocol(z.imag, next_column)
        next_column += 1
        self.protocol("i =", next_column)
        r, theta = cmath.polar(z)
        next_column += 1
        self.protocol(r, next_column)
        next_column += 1
        self.protocol(AppGlobals.angle_unit.from_rad(theta), next_column)

        return z