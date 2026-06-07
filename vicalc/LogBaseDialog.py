import math
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .ui.log_base_dialog import Ui_log_base_dialog
from .AppGlobals import AppGlobals

class LogBaseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_log_base_dialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

        self.ui.baseLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.log_base))

        # Connect signals
        self.ui.numberLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.baseLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.numberLineEdit.setFocus()

        self.validate_inputs()

    def validate_inputs(self):
        number, number_valid = AppGlobals.toDouble(self.ui.numberLineEdit.text())
        base, base_valid = AppGlobals.toDouble(self.ui.baseLineEdit.text())

        vars_valid = number_valid and base_valid and base > 0 and base != 1.0 and number > 0
        self.ok_button.setEnabled(vars_valid)

        if vars_valid:
            result = AppGlobals.log_base_calculation(number, base)
            self.ui.resultLineEdit.setText(AppGlobals.to_normal_string(result))
        else:
            self.ui.resultLineEdit.setText("- - -")