import math, cmath
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .ui.input_polar_form import Ui_InputComplexNumberInPolarFormDialog
from .AppGlobals import AppGlobals

class InputPolarForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InputComplexNumberInPolarFormDialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

        # Connect signals
        self.ui.rLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.thetaLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.rLineEdit.setFocus()

        self.validate_inputs()

    def validate_inputs(self):
        r, r_valid = AppGlobals.toDouble(self.ui.rLineEdit.text())
        theta, theta_valid = AppGlobals.toDouble(self.ui.thetaLineEdit.text())

        vars_valid = r_valid and theta_valid
        self.ok_button.setEnabled(vars_valid)

        if vars_valid:
            z = cmath.rect(r, AppGlobals.angle_unit.to_rad(theta))
            self.ui.realPartLineEdit.setText(AppGlobals.to_format_string(z.real))
            self.ui.imagPartLineEdit.setText(AppGlobals.to_format_string(z.imag))
        else:
            self.ui.realPartLineEdit.setText("- - -")
            self.ui.imagPartLineEdit.setText("- - -")
