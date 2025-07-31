from PySide6.QtCore import Qt, QLocale
from .CellValue import CellValue
from .NumericFormat import NumericFormat
from .AppGlobals import AppGlobals

class NumericCellValue(CellValue):
    def __init__(self, number: float, row = -1, col = -1):
        super().__init__(row, col)
        self.serialize_type = "NumericCellValue"
        self.number: float = number

        if -1 != col and -1 != row:
            AppGlobals.current_row = row
            AppGlobals.current_column = col
            item = AppGlobals.table.item(row, col)
            if item:
                item.setText(self.to_string(row, col))

    def to_string(self, row = -1, col = -1):
        return AppGlobals.to_format_string(self.number)
            
    def value(self, row = -1, col = -1):
        return self.number