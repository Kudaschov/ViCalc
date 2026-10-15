import math
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class TaxMinusExpression(UnaryExpression):
    def calculate(self, number: float):
        result: float = number / (1.0 + AppGlobals.tax_rate / 100.0)
        tax_amount = number - result
        self.insert_scroll_table()

        self.protocol("Gross Amount ")
        self.protocol(number)
        self.protocol(" - Tax Rate ")
        self.protocol(AppGlobals.tax_rate)
        self.protocol("% = Net Amount ")
        self.protocol_result(result)
        self.protocol(" (Tax Deducted: ")
        self.protocol(tax_amount)
        self.protocol(")")

        return result