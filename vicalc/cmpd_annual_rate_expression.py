import math
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .days_in_year import DaysInYear
from .payment_period import PaymentPeriod
import numpy_financial as npf

class CmpdAnnualRateExpression(UnaryExpression):
    def calculate(self, when: PaymentPeriod, py: int, cy: int, nper: float, pv: float, pmt: float, fv: float):
        # Calculate the number of payment periods (n) using numpy_financial
        # Calculate the effective interest rate per payment period
        # i = (1 + nominal_rate / C/Y) ** (C/Y / P/Y) - 1
        periodic_rate = npf.rate(nper, pmt, pv, fv, when=when.npf_period)
        annual_rate = ((1.0 + periodic_rate) ** (py / cy) - 1.0) * cy * 100.0        
        
        self.insert_scroll_table()
        self.protocol_result("Compound Interest. Calculation of Annual Interest Rate (I/Y) [%]")
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
        self.protocol(" | PV: ")
        self.protocol(pv)
        self.protocol(" | PMT: ")
        self.protocol(pmt)
        self.protocol(" | FV: ")
        self.protocol(fv)
        AppGlobals.history.append("")
        self.protocol_result("Results: ")
        self.protocol("Annual Interest Rate (I/Y): ")
        self.protocol_result(annual_rate)
        self.protocol(" %")
        return annual_rate