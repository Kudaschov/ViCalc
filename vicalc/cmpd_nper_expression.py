import math
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .days_in_year import DaysInYear
from .payment_period import PaymentPeriod
import numpy_financial as npf

class CmpdNperExpression(UnaryExpression):
    def calculate(self, when: PaymentPeriod, py: int, cy: int, annual_rate: float, pv: float, pmt: float, fv: float):
        # Calculate the number of payment periods (n) using numpy_financial
        # Calculate the effective interest rate per payment period
        # i = (1 + nominal_rate / C/Y) ** (C/Y / P/Y) - 1
        periodic_rate = (1.0 + annual_rate / cy / 100.0) ** (cy / py) - 1.0
        nper = npf.nper(periodic_rate, pmt, pv, fv, when=when.name)
        
        self.insert_scroll_table()
        self.protocol_result("Compound Interest. Number of Payments (N) Calculation")
        AppGlobals.history.append("")
        self.protocol_result("Inputs: ")
        self.protocol("Payment Period: ")
        self.protocol(when.history)
        self.protocol(" | P/Y: ")
        self.protocol(py)
        self.protocol(" | C/Y: ")
        self.protocol(cy)
        self.protocol(" | I/Y: ")
        self.protocol(annual_rate)
        self.protocol(" % | PV: ")
        self.protocol(pv)
        self.protocol(" | PMT: ")
        self.protocol(pmt)
        self.protocol(" | FV: ")
        self.protocol(fv)
        AppGlobals.history.append("")
        self.protocol_result("Results: ")
        self.protocol("Number of Payments (N): ")
        self.protocol_result(nper)
        return nper
