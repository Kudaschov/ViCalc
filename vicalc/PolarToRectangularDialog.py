import math
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .ui.polar_to_rectangular_dialog import Ui_PolarToRectangularDialog
from .AppGlobals import AppGlobals

class PolarToRectangularDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PolarToRectangularDialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

        # Connect signals
        self.ui.radiusLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.angleLineEdit.textChanged.connect(self.validate_inputs)

        self.validate_inputs()

    def validate_inputs(self):
        r, radius_valid = QLocale(QLocale.C).toDouble(self.ui.radiusLineEdit.text())
        a, angle_valid = QLocale(QLocale.C).toDouble(self.ui.angleLineEdit.text())

        if radius_valid and angle_valid:
            x = r * math.cos(AppGlobals.angle_unit.to_rad(a))
            y = r * math.sin(AppGlobals.angle_unit.to_rad(a))

            self.ui.xLineEdit.setText(AppGlobals.to_normal_string(x))
            self.ui.yLineEdit.setText(AppGlobals.to_normal_string(y))

        self.ok_button.setEnabled(radius_valid and angle_valid)