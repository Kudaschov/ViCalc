import math
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .ui.quadratic_equation_dialog import Ui_quadratic_equation_dialog
from .AppGlobals import AppGlobals

class QuadraticEquationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_quadratic_equation_dialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

        self.ui.aLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.quadratic_a))
        self.ui.bLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.quadratic_b))
        self.ui.cLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.quadratic_c))

        # Connect signals
        self.ui.aLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.bLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.cLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.aLineEdit.setFocus()

        self.validate_inputs()

    def validate_inputs(self):
        a, a_valid = AppGlobals.toDouble(self.ui.aLineEdit.text())
        b, b_valid = AppGlobals.toDouble(self.ui.bLineEdit.text())
        c, c_valid = AppGlobals.toDouble(self.ui.cLineEdit.text())

        vars_valid = a_valid and b_valid and c_valid and a != 0.0
        self.ok_button.setEnabled(vars_valid)
        D: float = AppGlobals.discriminant(a, b, c)
        if vars_valid:
            self.ui.DLineEdit.setText(AppGlobals.to_normal_string(D))
            if D > 0:
                sqrt_D = math.sqrt(D)
                x1 = (-b + sqrt_D) / (2 * a)
                x2 = (-b - sqrt_D) / (2 * a)
                self.ui.x1LineEdit.setText(AppGlobals.to_normal_string(x1))
                self.ui.x2LineEdit.setText(AppGlobals.to_normal_string(x2))
            elif D == 0:
                x1 = -b / (2 * a)
                self.ui.x1LineEdit.setText(AppGlobals.to_normal_string(x1))
                self.ui.x2LineEdit.setText("- - -")
            else:
                real = -b / (2*a)
                imag = math.sqrt(-D) / (2*a)
                self.ui.x1LineEdit.setText(f"{AppGlobals.to_normal_string(real)} + {AppGlobals.to_normal_string(imag)}i")
                self.ui.x2LineEdit.setText(f"{AppGlobals.to_normal_string(real)} - {AppGlobals.to_normal_string(imag)}i")
        else:
            self.ui.DLineEdit.setText("- - -")
            self.ui.x1LineEdit.setText("- - -")
            self.ui.x2LineEdit.setText("- - -")