from PySide6.QtCore import Qt, QLocale
from .CellValue import CellValue
from PySide6.QtGui import QFont, QColor
from .NumericFormat import NumericFormat
from .AppGlobals import AppGlobals

class StringCellValue(CellValue):
    def __init__(self, text: str, row = -1, col = -1):
        super().__init__(row, col)
        self.serialize_type = "StringCellValue"
        self.text = text

        if -1 != col and -1 != row:
            item = AppGlobals.table.item(row, col)
            if item:
                item.setText(self.to_string())

    def to_string(self, row = -1, col = -1):
        return self.text
    
    def value(self, row = -1, col = -1):
        return self.text