import math
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .days_in_year import DaysInYear

class SimpleInterestExpression(UnaryExpression):
    def calculate(self, days: int, days_in_year: DaysInYear, pv: float, annual_rate: float):
        si, sfv = AppGlobals.calculate_si(days, days_in_year, pv, annual_rate)
        self.insert_scroll_table()
        self.protocol_result("Simple Interest")
        AppGlobals.history.append("")
        self.protocol_result("Inputs: ")
        self.protocol("Days in Year: ")
        self.protocol(days_in_year.days)
        self.protocol(" | Interest Period: ")
        self.protocol(days)
        self.protocol(" days | Annual Interest Rate: ")
        self.protocol(annual_rate)
        self.protocol(" % | Present Value (PV): ")
        self.protocol(pv)
        AppGlobals.history.append("")
        self.protocol_result("Results: ")
        self.protocol("Simple Interest (SI): ")
        self.protocol_result(si)
        self.protocol(" | Future Value (FV): ")
        self.protocol_result(sfv)
        return si
