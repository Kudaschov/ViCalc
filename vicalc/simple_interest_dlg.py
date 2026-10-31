import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QMessageBox
from .ui.ui_simple_interest_dlg import Ui_SimpleInterestDialog
from .AppGlobals import AppGlobals
from .days_in_year import DaysInYear
from PySide6.QtGui import QKeySequence, QShortcut
import webbrowser

class SimpleInterestDialog(QDialog):
    def __init__(self, parent=None, angle_unit=None):
        super().__init__(parent)
        self.ui = Ui_SimpleInterestDialog()
        self.ui.setupUi(self)

        # 1. Setup the F1 keyboard shortcut scoped to this dialog
        self.f1_shortcut = QShortcut(QKeySequence(Qt.Key.Key_F1), self)
        self.f1_shortcut.activated.connect(self.open_help_topic)

        self.ui.days360RadioButton.setFocus()
        self.ui.days360RadioButton.toggled.connect(self.on_text_changed)
        self.ui.days365RadioButton.toggled.connect(self.on_text_changed)
        self.ui.daysLineEdit.textChanged.connect(self.on_text_changed)
        self.ui.annualRatePctLineEdit.textChanged.connect(self.on_text_changed)
        self.ui.pvLineEdit.textChanged.connect(self.on_text_changed)
        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

    def on_text_changed(self):
        total_ok = True
        days, ok = AppGlobals.toInt(self.ui.daysLineEdit.text())
        total_ok = total_ok and ok
        annual_rate, ok = AppGlobals.toDouble(self.ui.annualRatePctLineEdit.text())
        total_ok = total_ok and ok
        PV, ok = AppGlobals.toDouble(self.ui.pvLineEdit.text())
        total_ok = total_ok and ok

        if total_ok:
            if self.ui.days360RadioButton.isChecked():
                days_in_year = DaysInYear.days360
            else:
                days_in_year = DaysInYear.days365

            si, sfv = AppGlobals.calculate_si(days, days_in_year, PV, annual_rate)
            self.ui.siLineEdit.setText(AppGlobals.to_format_string(si))
            self.ui.sfvLineEdit.setText(AppGlobals.to_format_string(sfv))
            self.ok_button.setEnabled(True)
        else:
            self.ok_button.setEnabled(False)

    def open_help_topic(self):
        help_path = AppGlobals.resource_path("help/site/simple_interest.html")

        if os.path.exists(help_path):
            webbrowser.open(f"file:///{help_path}")
        else:
            # Optional: Add a warning dialog here
            print("Help file not found. Run `mkdocs build` first.")
            QMessageBox.information(self, "Path not found!", help_path)
