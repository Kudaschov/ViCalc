import math
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .ui.linear_two_points_dialog import Ui_linear_two_points_dialog
from .AppGlobals import AppGlobals

class LinearTwoPointsDialog(QDialog):
    a: float = None
    b: float = None
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_linear_two_points_dialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

        self.ui.x0LineEdit.setText(AppGlobals.to_normal_string(AppGlobals.linear_x0))
        self.ui.y0LineEdit.setText(AppGlobals.to_normal_string(AppGlobals.linear_y0))
        self.ui.x1LineEdit.setText(AppGlobals.to_normal_string(AppGlobals.linear_x1))
        self.ui.y1LineEdit.setText(AppGlobals.to_normal_string(AppGlobals.linear_y1))

        # Connect signals
        self.ui.x0LineEdit.textChanged.connect(self.validate_inputs)
        self.ui.x1LineEdit.textChanged.connect(self.validate_inputs)
        self.ui.y0LineEdit.textChanged.connect(self.validate_inputs)
        self.ui.y1LineEdit.textChanged.connect(self.validate_inputs)
        self.ui.x0LineEdit.setFocus()

        self.validate_inputs()

    def validate_inputs(self):
        x0, x0_valid = AppGlobals.toDouble(self.ui.x0LineEdit.text())
        x1, x1_valid = AppGlobals.toDouble(self.ui.x1LineEdit.text())
        y0, y0_valid = AppGlobals.toDouble(self.ui.y0LineEdit.text())
        y1, y1_valid = AppGlobals.toDouble(self.ui.y1LineEdit.text())

        vars_valid = x0_valid and x1_valid and y0_valid and y1_valid and (x1 != x0)
        self.ok_button.setEnabled(vars_valid)
        if vars_valid:
            self.a = (y1 - y0) / (x1 - x0)
            self.ui.aLineEdit.setText(AppGlobals.to_normal_string(self.a))
            self.b = y0 - self.a * x0
            self.ui.bLineEdit.setText(AppGlobals.to_normal_string(self.b))
        else:
            self.ui.aLineEdit.setText("- - -")
            self.ui.bLineEdit.setText("- - -")