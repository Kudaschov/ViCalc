import math, cmath
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .ui.input_rectangular_form import Ui_InputComplexNumberInRectangularFormDialog
from .AppGlobals import AppGlobals

class InputRectangularForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InputComplexNumberInRectangularFormDialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

        # Connect signals
        self.ui.realPartLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.imagPartLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.realPartLineEdit.setFocus()

        self.validate_inputs()

    def validate_inputs(self):
        real_part, real_part_valid = AppGlobals.toDouble(self.ui.realPartLineEdit.text())
        imag_part, imag_part_valid = AppGlobals.toDouble(self.ui.imagPartLineEdit.text())

        vars_valid = real_part_valid and imag_part_valid
        self.ok_button.setEnabled(vars_valid)

        if vars_valid:
            z = complex(real_part, imag_part)
            r, theta = cmath.polar(z)
            self.ui.rLineEdit.setText(AppGlobals.to_format_string(r))
            self.ui.thetaLineEdit.setText(AppGlobals.to_format_string(AppGlobals.angle_unit.from_rad(theta)))
        else:
            self.ui.rLineEdit.setText("- - -")
            self.ui.thetaLineEdit.setText("- - -")
