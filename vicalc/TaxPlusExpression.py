import math
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class TaxPlusExpression(UnaryExpression):
    def calculate(self, number: float):
        tax_amount:float = number * AppGlobals.tax_rate / 100.0
        result: float = number + tax_amount
        self.insert_scroll_table()

        self.protocol("Amount ")
        self.protocol(number)
        self.protocol(" + Tax Rate ")
        self.protocol(AppGlobals.tax_rate)
        self.protocol("% = Total ")
        self.protocol_result(result)
        self.protocol(" (Tax Amount: ")
        self.protocol(tax_amount)
        self.protocol(")")

        return result