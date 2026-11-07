import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QMessageBox
from .ui.ui_amort_dialog import Ui_amortDialog
from .AppGlobals import AppGlobals
from .days_in_year import DaysInYear
from PySide6.QtGui import QKeySequence, QShortcut
import webbrowser
import numpy as np
import numpy_financial as npf
from .payment_period import PaymentPeriod
from .cmpd_nper_expression import CmpdNperExpression
from .amort_expression import AmortExpression

class AmortDialog(QDialog):
    def __init__(self, parent=None, angle_unit=None):
        super().__init__(parent)
        self.ui = Ui_amortDialog()
        self.ui.setupUi(self)
        self.conv_ok = False
        self.py = 0
        self.cy = 0
        self.annual_rate = 0
        self.pv = 0
        self.pmt = 0
        self.p1 = 0
        self.p2 = 0
        self.nper = 0

        # 1. Setup the F1 keyboard shortcut scoped to this dialog
        self.f1_shortcut = QShortcut(QKeySequence(Qt.Key.Key_F1), self)
        self.f1_shortcut.activated.connect(self.open_help_topic)

        self.ui.beginRadioButton.setFocus()
        self.ui.beginRadioButton.toggled.connect(self.on_text_changed)
        self.ui.endRadioButton.toggled.connect(self.on_text_changed)
        self.ui.nLineEdit.textChanged.connect(self.on_text_changed)
        self.ui.p_yLineEdit.textChanged.connect(self.on_text_changed)
        self.ui.c_yLineEdit.textChanged.connect(self.on_text_changed)
        self.ui.p1LineEdit.textChanged.connect(self.on_text_changed)
        self.ui.p2LineEdit.textChanged.connect(self.on_text_changed)
        self.ui.annualRatePctLineEdit.textChanged.connect(self.on_text_changed)
        self.ui.pvLineEdit.textChanged.connect(self.on_text_changed)

        self.ui.solvePushButton.clicked.connect(self.solve)
        self.ui.historyPushButton.clicked.connect(self.history)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

    def on_text_changed(self):
        self.conv_ok = True
        self.py, ok = AppGlobals.toInt(self.ui.p_yLineEdit.text())
        self.conv_ok = self.conv_ok and ok
        self.cy, ok = AppGlobals.toInt(self.ui.c_yLineEdit.text())
        self.conv_ok = self.conv_ok and ok
        self.p1, ok = AppGlobals.toInt(self.ui.p1LineEdit.text())
        self.conv_ok = self.conv_ok and ok
        self.p2, ok = AppGlobals.toInt(self.ui.p2LineEdit.text())
        self.conv_ok = self.conv_ok and ok
        self.annual_rate, ok = AppGlobals.toDouble(self.ui.annualRatePctLineEdit.text())
        self.conv_ok = self.conv_ok and ok
        self.pv, ok = AppGlobals.toDouble(self.ui.pvLineEdit.text())
        self.conv_ok = self.conv_ok and ok
        self.nper, ok = AppGlobals.toDouble(self.ui.nLineEdit.text())
        self.conv_ok = self.conv_ok and ok

        if self.conv_ok:
            self.ok_button.setEnabled(True)
            self.ui.solvePushButton.setEnabled(True)
            self.ui.historyPushButton.setEnabled(True)
        else:
            self.ok_button.setEnabled(False)
            self.ui.solvePushButton.setEnabled(False)
            self.ui.historyPushButton.setEnabled(False)

    def open_help_topic(self):
        help_path = AppGlobals.resource_path("help/site/amortization.html")

        if os.path.exists(help_path):
            webbrowser.open(f"file:///{help_path}")
        else:
            # Optional: Add a warning dialog here
            print("Help file not found. Run `mkdocs build` first.")
            QMessageBox.information(self, "Path not found!", help_path)

    def get_when(self):
        if self.ui.beginRadioButton.isChecked():
            return PaymentPeriod.BEGIN
        else:
            return PaymentPeriod.END
        
    def solve(self):
        # Calculate the effective interest rate per payment period
        # i = (1 + nominal_rate / C/Y) ** (C/Y / P/Y) - 1
        periodic_rate = (1.0 + self.annual_rate / self.cy / 100.0) ** (self.cy / self.py) - 1.0

        self.pmt = npf.pmt(rate=periodic_rate, nper=self.nper, pv=self.pv, when=self.get_when().npf_period)
        self.ui.pmtLineEdit.setText(AppGlobals.to_format_string(self.pmt))

        # Calculate cumulative principal from period 1 to p2
        all_periods_to_p2 = np.arange(1, self.p2 + 1)
        cumulative_prns = npf.ppmt(
            rate=periodic_rate,
            per=all_periods_to_p2,
            nper=self.nper,
            pv=self.pv,
            when=self.get_when().npf_period)

        # bal = abs(npf.fv(rate=periodic_rate, nper=self.p2, pmt=self.pmt, pv=self.pv, when=self.get_when().npf_period))
        self.bal = abs(self.pv + np.sum(cumulative_prns))
        self.ui.balLineEdit.setText(AppGlobals.to_format_string(self.bal))

        int_p1 = npf.ipmt(rate=periodic_rate, per=self.p1, nper=self.nper, pv=self.pv, when=self.get_when().npf_period)
        self.ui.intP1LineEdit.setText(AppGlobals.to_format_string(int_p1))
        prn_p1 = npf.ppmt(rate=periodic_rate, per=self.p1, nper=self.nper, pv=self.pv, when=self.get_when().npf_period)
        self.ui.prnP1LineEdit.setText(AppGlobals.to_format_string(prn_p1))

        """Calculates SumInt: Total interest paid between periods PM1 and PM2."""
        periods = np.arange(self.p1, self.p2 + 1)
        ints = npf.ipmt(rate=periodic_rate, per=periods, nper=self.nper, pv=self.pv, when=self.get_when().npf_period)
        self.ui.intLineEdit.setText(AppGlobals.to_format_string(np.sum(ints)))

        """Calculates SumPrn: Total principal paid between periods PM1 and PM2."""
        prns = npf.ppmt(rate=periodic_rate, per=periods, nper=self.nper, pv=self.pv, when=self.get_when().npf_period)
        self.ui.prnLineEdit.setText(AppGlobals.to_format_string(np.sum(prns)))

    def history(self):
        self.solve()
        amort_expr = AmortExpression()
        amort_expr.calculate(self.get_when(), self.py, self.cy, self.nper, self.p1, self.p2, self.annual_rate, self.pv)
        AppGlobals.input_box.setTextSelect(AppGlobals.to_normal_string(self.bal))
        self.ok_button.click()