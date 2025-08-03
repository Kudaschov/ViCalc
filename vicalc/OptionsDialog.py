import math
from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtGui import QDoubleValidator, QIntValidator
from .AppGlobals import AppGlobals
from .ui.options_dialog import Ui_optionsDialog

class OptionsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_optionsDialog()
        self.ui.setupUi(self)