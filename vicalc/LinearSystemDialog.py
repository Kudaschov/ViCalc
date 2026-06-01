import math
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .ui.linear_system_dialog import Ui_linear_system_dialog
from .AppGlobals import AppGlobals

class LinearSystemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_linear_system_dialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

        self.ui.a1LineEdit.setText(AppGlobals.to_normal_string(AppGlobals.lse_a1))
        self.ui.b1LineEdit.setText(AppGlobals.to_normal_string(AppGlobals.lse_b1))
        self.ui.a2LineEdit.setText(AppGlobals.to_normal_string(AppGlobals.lse_a2))
        self.ui.b2LineEdit.setText(AppGlobals.to_normal_string(AppGlobals.lse_b2))
        self.ui.c1LineEdit.setText(AppGlobals.to_normal_string(AppGlobals.lse_c1))
        self.ui.c2LineEdit.setText(AppGlobals.to_normal_string(AppGlobals.lse_c2))

        # Connect signals
        self.ui.a1LineEdit.textChanged.connect(self.validate_inputs)
        self.ui.b1LineEdit.textChanged.connect(self.validate_inputs)
        self.ui.a2LineEdit.textChanged.connect(self.validate_inputs)
        self.ui.b2LineEdit.textChanged.connect(self.validate_inputs)
        self.ui.c1LineEdit.textChanged.connect(self.validate_inputs)
        self.ui.c2LineEdit.textChanged.connect(self.validate_inputs)

        self.ui.a1LineEdit.setFocus()

        self.validate_inputs()

    def validate_inputs(self):
        a1, a1_valid = AppGlobals.toDouble(self.ui.a1LineEdit.text())
        b1, b1_valid = AppGlobals.toDouble(self.ui.b1LineEdit.text())
        a2, a2_valid = AppGlobals.toDouble(self.ui.a2LineEdit.text())
        b2, b2_valid = AppGlobals.toDouble(self.ui.b2LineEdit.text())
        c1, c1_valid = AppGlobals.toDouble(self.ui.c1LineEdit.text())
        c2, c2_valid = AppGlobals.toDouble(self.ui.c2LineEdit.text())

        vars_valid = (a1_valid and b1_valid and a2_valid and b2_valid and c1_valid and c2_valid)
        D: float = AppGlobals.lse_discriminant(a1, b1, a2, b2)
        self.ui.DLineEdit.setText(AppGlobals.to_normal_string(D))
        vars_valid = vars_valid and D != 0
        self.ok_button.setEnabled(vars_valid)

        if vars_valid:
            x = (c1 * b2 - c2 * b1) / D
            y = (a1 * c2 - a2 * c1) / D
            self.ui.xLineEdit.setText(AppGlobals.to_normal_string(x))
            self.ui.yLineEdit.setText(AppGlobals.to_normal_string(y))
        else:
            self.ui.xLineEdit.setText("- - -")
            self.ui.yLineEdit.setText("- - -")