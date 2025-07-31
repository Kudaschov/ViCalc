from PySide6.QtCore import Qt
from .CellValue import CellValue
from PySide6.QtGui import QFont, QColor
from .AppGlobals import AppGlobals
from .NumericCellValue import NumericCellValue

class ResultCellValue(NumericCellValue):
    def __init__(self, number: float, row = -1, col = -1):
        super().__init__(number, row, col)
        self.serialize_type = "ResultCellValue"

    def to_string(self, row = -1, col = -1):
        if -1 != col and -1 != row:
            item = AppGlobals.table.item(row, col)
            if item:
                resultFont = QFont()
                resultFont.setBold(True)
                item.setFont(resultFont)

        return super().to_string(row, col)
