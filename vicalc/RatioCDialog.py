import math
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .ui.ratio_c_dialog import Ui_ratio_c_dialog
from .AppGlobals import AppGlobals

class RatioCDialog(QDialog):
    result: float = None
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ratio_c_dialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

        # Connect signals
        self.ui.aLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.bLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.dLineEdit.textChanged.connect(self.validate_inputs)

        self.validate_inputs()

    def validate_inputs(self):
        a, a_valid = QLocale(QLocale.C).toDouble(self.ui.aLineEdit.text())
        b, b_valid = QLocale(QLocale.C).toDouble(self.ui.bLineEdit.text())
        d, d_valid = QLocale(QLocale.C).toDouble(self.ui.dLineEdit.text())

        vars_valid = a_valid and b_valid and d_valid and (b != 0)
        self.ok_button.setEnabled(vars_valid)
        if vars_valid:
            self.result = a * d / b
            self.ui.xLineEdit.setText(AppGlobals.to_normal_string(self.result))
        else:
            self.ui.xLineEdit.setText("- - -")