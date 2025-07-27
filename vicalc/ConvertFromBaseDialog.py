from PySide6.QtWidgets import QDialog

from .ui.convert_from_base_dialog import Ui_ConvertFromBaseDialog

class ConvertFromBaseDialog(QDialog):
    def __init__(self, parent=None, base_expression=None):
        super().__init__(parent)
        self.ui = Ui_ConvertFromBaseDialog()
        self.ui.setupUi(self)
        self.base_expression = base_expression
        self.ui.numberLineEdit.textChanged.connect(self.on_text_changed)

    def on_text_changed(self):
        if self.base_expression.conv_from_string(self.ui.numberLineEdit.text()):
            self.ui.binaryLineEdit.setText(self.base_expression.to_binary())
            self.ui.octalLineEdit.setText(self.base_expression.to_octal())
            self.ui.decimalLineEdit.setText(self.base_expression.to_decimal())
            self.ui.hexadecimalLineEdit.setText(self.base_expression.to_hexadecimal())
        else:
            self.ui.binaryLineEdit.setText("- - -")
            self.ui.octalLineEdit.setText("- - -")
            self.ui.decimalLineEdit.setText("- - -")
            self.ui.hexadecimalLineEdit.setText("- - -")

    def log(self):
        if self.base_expression.conv_from_string(self.ui.numberLineEdit.text()):
            self.base_expression.log()
            return True, self.base_expression.to_decimal()
        else:
            return False, ""
