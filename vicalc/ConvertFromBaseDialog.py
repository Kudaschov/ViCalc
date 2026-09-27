from PySide6.QtWidgets import QDialog, QDialogButtonBox
from .ui.convert_from_base_dialog import Ui_ConvertFromBaseDialog
from .AppGlobals import AppGlobals
from .NumberBase import NumberBase
from .CalcMode import CalcMode

class ConvertFromBaseDialog(QDialog):
    def __init__(self, parent=None, base_expression=None):
        super().__init__(parent)
        self.ui = Ui_ConvertFromBaseDialog()
        self.ui.setupUi(self)
        self.base_expression = base_expression
        self.ui.numberLineEdit.textChanged.connect(self.on_text_changed)
        self.ok_button = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)


    def on_text_changed(self):
        if self.base_expression.conv_from_string(self.ui.numberLineEdit.text()):
            self.ui.binaryLineEdit.setText(self.base_expression.to_binary())
            self.ui.octalLineEdit.setText(self.base_expression.to_octal())
            self.ui.decimalLineEdit.setText(self.base_expression.to_decimal())
            self.ui.hexadecimalLineEdit.setText(self.base_expression.to_hexadecimal())
            self.ok_button.setEnabled(True)
        else:
            self.ui.binaryLineEdit.setText("- - -")
            self.ui.octalLineEdit.setText("- - -")
            self.ui.decimalLineEdit.setText("- - -")
            self.ui.hexadecimalLineEdit.setText("- - -")
            self.ok_button.setEnabled(False)

    def add_to_log(self):
        if self.base_expression.conv_from_string(self.ui.numberLineEdit.text()):
            if AppGlobals.calc_mode == CalcMode.base_n:
                match AppGlobals.number_base:
                    case NumberBase.BIN:
                        return True, self.base_expression.to_binary()
                    case NumberBase.OCT:
                        return True, self.base_expression.to_octal()
                    case NumberBase.DEC:
                        return True, self.base_expression.to_decimal()
                    case NumberBase.HEX:
                        return True, self.base_expression.to_hexadecimal()
                    case _:
                        return False, ""
            else:
                return True, self.base_expression.to_decimal()

        else:
            return False, ""
