from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIntValidator
from .ui.num_format_dialog import Ui_FormatDialog

class NumFormatDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FormatDialog()
        self.ui.setupUi(self)
