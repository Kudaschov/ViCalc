import math
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .ui.linear_y_from_x_dialog import Ui_linear_y_from_x_dialog
from .AppGlobals import AppGlobals
from .ui.linear_two_points_dialog import Ui_linear_two_points_dialog
from .LinearTwoPointsDialog import LinearTwoPointsDialog

class LinearYfromXDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_linear_y_from_x_dialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

        self.ui.aLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.linear_a))
        self.ui.bLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.linear_b))

        # Connect signals
        self.ui.aLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.bLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.xLineEdit.textChanged.connect(self.validate_inputs)

        self.ui.fromTwoPointsPushButton.clicked.connect(self.open_two_points_dialog)

        self.ui.xLineEdit.setFocus()

        self.validate_inputs()

    def validate_inputs(self):
        x, x_valid = AppGlobals.toDouble(self.ui.xLineEdit.text())
        a, a_valid = AppGlobals.toDouble(self.ui.aLineEdit.text())
        b, b_valid = AppGlobals.toDouble(self.ui.bLineEdit.text())

        vars_valid = x_valid and a_valid and b_valid
        self.ok_button.setEnabled(vars_valid)
        if vars_valid:
            y: float = a * x + b
            self.ui.yLineEdit.setText(AppGlobals.to_normal_string(y))
        else:
            self.ui.yLineEdit.setText("- - -")

    def open_two_points_dialog(self):

        dialog = LinearTwoPointsDialog()

        if dialog.exec():
            AppGlobals.linear_x0, ok = AppGlobals.toDouble(dialog.ui.x0LineEdit.text())
            AppGlobals.linear_y0, ok = AppGlobals.toDouble(dialog.ui.y0LineEdit.text())
            AppGlobals.linear_x1, ok = AppGlobals.toDouble(dialog.ui.x1LineEdit.text())
            AppGlobals.linear_y1, ok = AppGlobals.toDouble(dialog.ui.y1LineEdit.text())
            AppGlobals.linear_a = (AppGlobals.linear_y1 - AppGlobals.linear_y0) / (AppGlobals.linear_x1 - AppGlobals.linear_x0)
            AppGlobals.linear_b = AppGlobals.linear_y0 - AppGlobals.linear_a * AppGlobals.linear_x0
            self.ui.aLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.linear_a))
            self.ui.bLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.linear_b))