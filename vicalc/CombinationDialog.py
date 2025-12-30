import math
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .ui.combination_dialog import Ui_combinationDialog
from .AppGlobals import AppGlobals

class CombinationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_combinationDialog()
        self.ui.setupUi(self)

        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

        # Connect signals
        self.ui.nLineEdit.textChanged.connect(self.validate_inputs)
        self.ui.rLineEdit.textChanged.connect(self.validate_inputs)

        self.validate_inputs()

    def validate_inputs(self):
        n, n_valid = QLocale(QLocale.C).toInt(self.ui.nLineEdit.text())
        r, r_valid = QLocale(QLocale.C).toInt(self.ui.rLineEdit.text())

        self.ok_button.setEnabled(n_valid and r_valid)