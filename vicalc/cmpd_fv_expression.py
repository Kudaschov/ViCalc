import math
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .payment_period import PaymentPeriod
import numpy_financial as npf

class CmpdFVExpression(UnaryExpression):
    def calculate(self, when: PaymentPeriod, py: int, cy: int, nper: float, iy: float, pv: float, pmt: float):
        # Calculate the number of payment periods (n) using numpy_financial
        # Calculate the effective interest rate per payment period
        # i = (1 + nominal_rate / C/Y) ** (C/Y / P/Y) - 1
        periodic_rate = (1.0 + iy / cy / 100.0) ** (cy /py) - 1.0
        fv = npf.fv(rate=periodic_rate, nper=nper, pmt=pmt, pv=pv, when=when.npf_period)
        
        self.insert_scroll_table()
        self.protocol_result("Compound Interest. Calculation of Future Value (FV)")
        AppGlobals.history.append("")
        self.protocol_result("Inputs: ")
        self.protocol("Payment Period: ")
        self.protocol(when.history)
        self.protocol(" | P/Y: ")
        self.protocol(py)
        self.protocol(" | C/Y: ")
        self.protocol(cy)
        self.protocol(" | N: ")
        self.protocol(nper)
        self.protocol(" | I/Y: ")
        self.protocol(iy)
        self.protocol(" % | PV: ")
        self.protocol(pv)
        self.protocol(" | PMT: ")
        self.protocol(pmt)
        AppGlobals.history.append("")
        self.protocol_result("Results: ")
        self.protocol("Future Value (FV): ")
        self.protocol_result(fv)
        return fv