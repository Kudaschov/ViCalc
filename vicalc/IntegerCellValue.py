from PySide6.QtCore import Qt, QLocale
from PySide6.QtGui import QFont, QColor, QBrush
from .CellValue import CellValue
from .AppGlobals import AppGlobals
from .WordSize import WordSize
from .NumberBase import NumberBase

class IntegerCellValue(CellValue):
    def __init__(self, number: int, row = -1, col = -1):
        super().__init__(row, col)
        self.serialize_type = "IntegerCellValue"
        self.number: int = number

        if -1 != col and -1 != row:
            AppGlobals.current_row = row
            AppGlobals.current_column = col
            item = AppGlobals.table.item(row, col)
            if item:
                if AppGlobals.different_view_negative_number and self.number < 0:
                    resultFont = QFont()
                    item.setForeground(QBrush(QColor(AppGlobals.color_negative_number)))
                    item.setFont(resultFont)
                item.setText(self.to_string(row, col))

    def format_value(self) -> str:
        integer_value = self.number
        if AppGlobals.number_base == NumberBase.BIN:
            return f"0b{integer_value:b}"

        elif AppGlobals.number_base == NumberBase.OCT:
            return f"0o{integer_value:o}"

        elif AppGlobals.number_base == NumberBase.DEC:
            return str(integer_value)  # Keine Float-Konvertierung (verhindert e+19)

        elif AppGlobals.number_base == NumberBase.HEX:
            return f"0x{integer_value:X}"

        raise ValueError(f"Unsupported NumberBase: {AppGlobals.number_base}")                

    def to_string(self, row = -1, col = -1):
        return self.format_value()

    def value(self, row = -1, col = -1):
        return self.number