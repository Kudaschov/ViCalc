import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QMessageBox
from .ui.ui_cmpd_dialog import Ui_cmpdDialog
from .AppGlobals import AppGlobals
from .days_in_year import DaysInYear
from PySide6.QtGui import QKeySequence, QShortcut
import webbrowser
import numpy_financial as npf
from .payment_period import PaymentPeriod
from .cmpd_nper_expression import CmpdNperExpression
from .cmpd_annual_rate_expression import CmpdAnnualRateExpression
from .cmpd_pv_expression import CmpdPVExpression
from .cmpd_pmt_expression import CmpdPMTExpression
from .cmpd_fv_expression import CmpdFVExpression

class CMPDDialog(QDialog):
    def __init__(self, parent=None, angle_unit=None):
        super().__init__(parent)
        self.ui = Ui_cmpdDialog()
        self.ui.setupUi(self)
        self.conv_ok = False
        self.py = 0
        self.cy = 0
        self.nper = 0
        self.annual_rate = 0
        self.pv = 0
        self.pmt = 0
        self.fv = 0

        # 1. Setup the F1 keyboard shortcut scoped to this dialog
        self.f1_shortcut = QShortcut(QKeySequence(Qt.Key.Key_F1), self)
        self.f1_shortcut.activated.connect(self.open_help_topic)

        self.ui.beginRadioButton.setFocus()
        self.ui.beginRadioButton.toggled.connect(self.on_text_changed)
        self.ui.endRadioButton.toggled.connect(self.on_text_changed)
        self.ui.p_yLineEdit.textChanged.connect(self.on_text_changed)
        self.ui.c_yLineEdit.textChanged.connect(self.on_text_changed)
        self.ui.nLineEdit.textChanged.connect(self.on_text_changed)
        self.ui.annualRatePctLineEdit.textChanged.connect(self.on_text_changed)
        self.ui.pvLineEdit.textChanged.connect(self.on_text_changed)
        self.ui.pmtLineEdit.textChanged.connect(self.on_text_changed)
        self.ui.fvLineEdit.textChanged.connect(self.on_text_changed)

        self.ui.solveNPushButton.clicked.connect(self.solve_nper)
        self.ui.historyNPushButton.clicked.connect(self.history_nper)
        self.ui.solveAnnualRatePushButton.clicked.connect(self.solve_annual_rate)
        self.ui.historyAnnualRatePushButton.clicked.connect(self.history_annual_rate)
        self.ui.solvePVPushButton.clicked.connect(self.solve_pv)
        self.ui.historyPVPushButton.clicked.connect(self.history_pv)
        self.ui.solvePMTPushButton.clicked.connect(self.solve_pmt)
        self.ui.historyPMTPushButton.clicked.connect(self.history_pmt)
        self.ui.solveFVPushButton.clicked.connect(self.solve_fv)
        self.ui.historyFVPushButton.clicked.connect(self.history_fv)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

    def on_text_changed(self):
        self.conv_ok = True
        self.py, ok = AppGlobals.toInt(self.ui.p_yLineEdit.text())
        self.conv_ok = self.conv_ok and ok
        self.cy, ok = AppGlobals.toInt(self.ui.c_yLineEdit.text())
        self.conv_ok = self.conv_ok and ok
        self.nper, ok = AppGlobals.toDouble(self.ui.nLineEdit.text())
        self.conv_ok = self.conv_ok and ok
        self.annual_rate, ok = AppGlobals.toDouble(self.ui.annualRatePctLineEdit.text())
        self.conv_ok = self.conv_ok and ok
        self.pv, ok = AppGlobals.toDouble(self.ui.pvLineEdit.text())
        self.conv_ok = self.conv_ok and ok
        self.pmt, ok = AppGlobals.toDouble(self.ui.pmtLineEdit.text())
        self.conv_ok = self.conv_ok and ok
        self.fv, ok = AppGlobals.toDouble(self.ui.fvLineEdit.text())
        self.conv_ok = self.conv_ok and ok

        if self.conv_ok:
            self.ok_button.setEnabled(True)
            self.ui.solveNPushButton.setEnabled(True)
            self.ui.solveAnnualRatePushButton.setEnabled(True)
            self.ui.solvePVPushButton.setEnabled(True)
            self.ui.solvePMTPushButton.setEnabled(True)
            self.ui.solveFVPushButton.setEnabled(True)

            self.ui.historyNPushButton.setEnabled(True)
            self.ui.historyAnnualRatePushButton.setEnabled(True)
            self.ui.historyPVPushButton.setEnabled(True)
            self.ui.historyPMTPushButton.setEnabled(True)
            self.ui.historyFVPushButton.setEnabled(True)
        else:
            self.ok_button.setEnabled(False)
            self.ui.solveNPushButton.setEnabled(False)
            self.ui.solveAnnualRatePushButton.setEnabled(False)
            self.ui.solvePVPushButton.setEnabled(False)
            self.ui.solvePMTPushButton.setEnabled(False)
            self.ui.solveFVPushButton.setEnabled(False)

            self.ui.historyNPushButton.setEnabled(False)
            self.ui.historyAnnualRatePushButton.setEnabled(False)
            self.ui.historyPVPushButton.setEnabled(False)
            self.ui.historyPMTPushButton.setEnabled(False)
            self.ui.historyFVPushButton.setEnabled(False)

    def open_help_topic(self):
        help_path = AppGlobals.resource_path("help/site/compound_interest.html")

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
        
    def solve_nper(self):
        # Calculate the effective interest rate per payment period
        # i = (1 + nominal_rate / C/Y) ** (C/Y / P/Y) - 1
        periodic_rate = (1.0 + self.annual_rate / self.cy / 100.0) ** (self.cy / self.py) - 1.0

        # Calculate the number of payment periods (n) using numpy_financial
        self.nper = npf.nper(periodic_rate, self.pmt, self.pv, self.fv, when=self.get_when().name)
        self.ui.nLineEdit.setText(AppGlobals.to_normal_string(self.nper))

    def history_nper(self):
        self.solve_nper()
        CmpdNperExpression().calculate(self.get_when(), self.py, self.cy, self.annual_rate, self.pv, self.pmt, self.fv)
        AppGlobals.input_box.setTextSelect(AppGlobals.to_normal_string(self.nper))
        self.ok_button.click()

    def solve_annual_rate(self):
        # 1. Solve for the periodic interest rate using numpy_financial
        periodic_rate = npf.rate(self.nper, self.pmt, self.pv, self.fv, when=self.get_when().name)

        # 2. Reverse the formula to solve for the annual interest rate (%)
        self.annual_rate = ((1.0 + periodic_rate) ** (self.py / self.cy) - 1.0) * self.cy * 100.0        
        self.ui.annualRatePctLineEdit.setText(AppGlobals.to_normal_string(self.annual_rate))

    def history_annual_rate(self):
        self.solve_annual_rate()
        CmpdAnnualRateExpression().calculate(self.get_when(), self.py, self.cy, self.nper, self.pv, self.pmt, self.fv)
        AppGlobals.input_box.setTextSelect(AppGlobals.to_normal_string(self.annual_rate))
        self.ok_button.click()

    def solve_pv(self):
        # 1. Solve for the periodic interest rate using numpy_financial
        periodic_rate = (1.0 + self.annual_rate / self.cy / 100.0) ** (self.cy / self.py) - 1.0
        self.pv = npf.pv(rate=periodic_rate, nper=self.nper, pmt=self.pmt, fv=self.fv, when=self.get_when().name)
        self.ui.pvLineEdit.setText(AppGlobals.to_normal_string(self.pv))

    def history_pv(self):
        self.solve_pv()
        CmpdPVExpression().calculate(self.get_when(), self.py, self.cy, self.nper, self.annual_rate, self.pmt, self.fv)
        AppGlobals.input_box.setTextSelect(AppGlobals.to_normal_string(self.pv))
        self.ok_button.click()

    def solve_pmt(self):
        # 1. Solve for the periodic interest rate using numpy_financial
        periodic_rate = (1.0 + self.annual_rate / self.cy / 100.0) ** (self.cy / self.py) - 1.0
        self.pmt = npf.pmt(rate=periodic_rate, nper=self.nper, pv=self.pv, fv=self.fv, when=self.get_when().name)
        self.ui.pmtLineEdit.setText(AppGlobals.to_normal_string(self.pmt))

    def history_pmt(self):
        self.solve_pmt()
        CmpdPMTExpression().calculate(self.get_when(), self.py, self.cy, self.nper, self.annual_rate, self.pv, self.fv)
        AppGlobals.input_box.setTextSelect(AppGlobals.to_normal_string(self.pmt))
        self.ok_button.click()

    def solve_fv(self):
        # 1. Solve for the periodic interest rate using numpy_financial
        periodic_rate = (1.0 + self.annual_rate / self.cy / 100.0) ** (self.cy / self.py) - 1.0
        self.fv = npf.fv(rate=periodic_rate, nper=self.nper, pmt=self.pmt, pv=self.pv, when=self.get_when().name)
        self.ui.fvLineEdit.setText(AppGlobals.to_normal_string(self.fv))

    def history_fv(self):
        self.solve_fv()
        CmpdFVExpression().calculate(self.get_when(), self.py, self.cy, self.nper, self.annual_rate, self.pv, self.pmt)
        AppGlobals.input_box.setTextSelect(AppGlobals.to_normal_string(self.fv))
        self.ok_button.click()
