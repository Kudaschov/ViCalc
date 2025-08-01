from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .ui.dms_to_dd_dialog import Ui_DMStoDD_Dialog

class DMStoDD_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DMStoDD_Dialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

        # Connect signals
        self.ui.degreesLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.minutesLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.secondsLineEdit.textChanged.connect(self.validate_inputs)

        self.validate_inputs()

    def validate_inputs(self):
        degrees, degrees_valid = QLocale().toInt(self.ui.degreesLineEdit.text())
        minutes, minutes_valid = QLocale().toUInt(self.ui.minutesLineEdit.text())
        seconds, seconds_valid = QLocale().toDouble(self.ui.secondsLineEdit.text())

        self.ok_button.setEnabled(degrees_valid and minutes_valid and seconds_valid)