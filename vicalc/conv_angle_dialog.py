from PySide6.QtWidgets import QDialog, QDialogButtonBox
from .AppGlobals import AppGlobals
from .NumberBase import NumberBase
from .CalcMode import CalcMode
from .ui.ui_conv_angle_dialog import Ui_ConvAngleDialog
from .DegUnit import DegUnit
from .RadUnit import RadUnit
from .GraUnit import GraUnit

class ConvAngleDialog(QDialog):
    def __init__(self, parent=None, angle_unit=None):
        super().__init__(parent)
        self.ui = Ui_ConvAngleDialog()
        self.ui.setupUi(self)
        self.angle_unit = angle_unit
        self.ui.number_label.setText(f"&Angle [{self.angle_unit.angle_symbol()}]")
        self.ui.numberLineEdit.textChanged.connect(self.on_text_changed)
        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

    def on_text_changed(self):
        val, ok = AppGlobals.toDouble(self.ui.numberLineEdit.text())
        if ok:
            self.ui.degLineEdit.setText(AppGlobals.to_format_string(self.angle_unit.to_deg(val)))
            self.ui.radLineEdit.setText(AppGlobals.to_format_string(self.angle_unit.to_rad(val)))
            self.ui.graLineEdit.setText(AppGlobals.to_format_string(self.angle_unit.to_gra(val)))
            self.ok_button.setEnabled(True)
        else:
            self.ui.degLineEdit.setText("- - -")
            self.ui.radLineEdit.setText("- - -")
            self.ui.graLineEdit.setText("- - -")
            self.ok_button.setEnabled(False)

    def add_to_log(self):
        val, ok = AppGlobals.toDouble(self.ui.numberLineEdit.text())

        if isinstance(AppGlobals.angle_unit, RadUnit):
            return self.angle_unit.to_rad_with_protocol(val)
        elif isinstance(AppGlobals.angle_unit, GraUnit):
            return self.angle_unit.to_gra_with_protocol(val)
        else:
            return self.angle_unit.to_deg_with_protocol(val)
