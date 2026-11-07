import math
from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals
from .payment_period import PaymentPeriod
import numpy as np
import numpy_financial as npf

class AmortExpression(UnaryExpression):
    def calculate(self, when: PaymentPeriod, py: int, cy: int, nper: float, p1: int, p2: int, iy: float, pv: float):
        # Calculate the effective interest rate per payment period
        # i = (1 + nominal_rate / C/Y) ** (C/Y / P/Y) - 1
        periodic_rate = (1.0 + iy / cy / 100.0) ** (cy /py) - 1.0

        AppGlobals.pmt = npf.pmt(rate=periodic_rate, nper=nper, pv=pv, when=when.npf_period)

        # Calculate cumulative principal from period 1 to p2
        all_periods_to_p2 = np.arange(1, p2 + 1)
        cumulative_prns = npf.ppmt(
            rate=periodic_rate,
            per=all_periods_to_p2,
            nper=nper,
            pv=pv,
            when=when.npf_period)

        # bal = abs(npf.fv(rate=periodic_rate, nper=self.p2, pmt=self.pmt, pv=self.pv, when=self.get_when().npf_period))
        bal = abs(pv + np.sum(cumulative_prns))
        
        int_p1 = npf.ipmt(rate=periodic_rate, per=p1, nper=nper, pv=pv, when=when.npf_period)
        prn_p1 = npf.ppmt(rate=periodic_rate, per=p1, nper=nper, pv=pv, when=when.npf_period)

        """Calculates SumInt: Total interest paid between periods PM1 and PM2."""
        periods = np.arange(p1, p2 + 1)
        ints = npf.ipmt(rate=periodic_rate, per=periods, nper=nper, pv=pv, when=when.npf_period)

        """Calculates SumPrn: Total principal paid between periods PM1 and PM2."""
        prns = npf.ppmt(rate=periodic_rate, per=periods, nper=nper, pv=pv, when=when.npf_period)

        self.insert_scroll_table()
        self.protocol_result("Amortization")
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
        self.protocol(" | P1: ")
        self.protocol(p1)
        self.protocol(" | P2: ")
        self.protocol(p2)
        self.protocol(" | I/Y: ")
        self.protocol(iy)
        self.protocol(" % | PV: ")
        self.protocol(pv)
        AppGlobals.history.append("")
        self.protocol_result("Results: ")
        self.protocol("PMT: ")
        self.protocol(AppGlobals.pmt)
        self.protocol(" | BAL: ")
        self.protocol_result(bal)
        self.protocol(" | INT(P1): ")
        self.protocol(int_p1)
        self.protocol(" | PRN(P1): ")
        self.protocol(prn_p1)
        self.protocol(" | INT: ")
        self.protocol_result(np.sum(ints))
        self.protocol(" | PRN: ")
        self.protocol_result(np.sum(prns))
        return bal