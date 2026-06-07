import math
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .ui.mm2_to_awg_dialog import Ui_mm2_to_awg_dialog
from .AppGlobals import AppGlobals

class Mm2ToAwgDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_mm2_to_awg_dialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

        # Connect signals
        self.ui.areaMm2LineEdit.textChanged.connect(self.validate_inputs)
        self.ui.areaMm2LineEdit.setFocus()

        self.validate_inputs()

    def validate_inputs(self):
        mm2, mm2_valid = AppGlobals.toDouble(self.ui.areaMm2LineEdit.text())

        vars_valid = mm2_valid
        self.ok_button.setEnabled(vars_valid)

        if vars_valid:
            awg = AppGlobals.mm2_to_awg_calculation(mm2)
            self.ui.awgLineEdit.setText(AppGlobals.to_normal_string(awg))
            diameter_inch = AppGlobals.mm2_to_diameter_inch_calculation(mm2)
            self.ui.diameterInchLineEdit.setText(AppGlobals.to_normal_string(diameter_inch))
            diameter_mm = math.sqrt((4 * mm2) / math.pi)
            self.ui.diameterMmLineEdit.setText(AppGlobals.to_normal_string(diameter_mm))
            area_kcmil = AppGlobals.mm2_to_kcmil_calculation(mm2)
            self.ui.areaKcmilLineEdit.setText(AppGlobals.to_normal_string(area_kcmil))
        else:
            self.ui.awgLineEdit.setText("- - -")