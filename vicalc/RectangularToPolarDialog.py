import math
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .ui.rectangular_to_polar_dialog import Ui_RectangularToPolarDialog
from .AppGlobals import AppGlobals

class RectangularToPolarDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RectangularToPolarDialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

        # Connect signals
        self.ui.xLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.yLineEdit.textChanged.connect(self.validate_inputs)

        self.validate_inputs()

    def validate_inputs(self):
        x, x_valid = QLocale().toDouble(self.ui.xLineEdit.text())
        y, y_valid = QLocale().toDouble(self.ui.yLineEdit.text())

        if x_valid and y_valid:
            r = math.hypot(x, y)
            theta = math.atan2(y, x)
            self.ui.distanceLineEdit.setText(AppGlobals.to_normal_string(r))
            self.ui.angleLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.angle_unit.from_rad(theta)))

        self.ok_button.setEnabled(x_valid and y_valid)