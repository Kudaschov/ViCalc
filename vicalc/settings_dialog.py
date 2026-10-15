from PySide6.QtWidgets import QDialog, QDialogButtonBox
from .ui.ui_settings_dialog import Ui_SettingsDialog
from .AppGlobals import AppGlobals

class SettingsDialog(QDialog):
    def __init__(self, parent=None, angle_unit=None):
        super().__init__(parent)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.ui.taxRateLineEdit.setFocus()
        self.ui.taxRateLineEdit.textChanged.connect(self.on_text_changed)
        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

    def on_text_changed(self):
        val, ok = AppGlobals.toDouble(self.ui.taxRateLineEdit.text())
        if ok:
            self.ok_button.setEnabled(True)
        else:
            self.ok_button.setEnabled(False)