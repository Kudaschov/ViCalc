import math
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .ui.awg_to_mm2_dialog import Ui_awg_to_mm2_dialog
from .AppGlobals import AppGlobals

class AwgToMm2Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_awg_to_mm2_dialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

        # Connect signals
        self.ui.awgLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.awgLineEdit.setFocus()

        self.validate_inputs()

    def validate_inputs(self):
        awg, awg_valid = AppGlobals.toDouble(self.ui.awgLineEdit.text())

        vars_valid = awg_valid
        self.ok_button.setEnabled(vars_valid)

        if vars_valid:
            self.ui.diameterInchLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.awg_to_diameter_inch_calculation(awg)))
            self.ui.diameterMmLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.awg_to_diameter_mm_calculation(awg)))
            self.ui.areaKcmilLineEdit.setText(AppGlobals.to_normal_string(AppGlobals.awg_to_kcmil_calculation(awg)))
            self.ui.areaMm2LineEdit.setText(AppGlobals.to_normal_string(AppGlobals.awg_to_mm2_calculation(awg)))
        else:
            self.ui.areaMm2LineEdit.setText("- - -")