from PySide6.QtCore import Qt

from vicalc.IntegerCellValue import IntegerCellValue
from .CellValue import CellValue
from PySide6.QtGui import QFont, QColor, QBrush
from .AppGlobals import AppGlobals

class IntegerResultCellValue(IntegerCellValue):
    def __init__(self, number: int, row = -1, col = -1):
        super().__init__(number, row, col)
        self.serialize_type = "IntegerResultCellValue"

    def to_string(self, row = -1, col = -1):
        if -1 != col and -1 != row:
            item = AppGlobals.table.item(row, col)
            if item:
                resultFont = QFont()
                resultFont.setBold(True)
                if AppGlobals.different_view_negative_number and self.number < 0:
                    item.setForeground(QBrush(QColor(AppGlobals.color_negative_number)))
                item.setFont(resultFont)

        return super().to_string(row, col)
