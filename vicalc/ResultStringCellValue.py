from PySide6.QtCore import Qt
from .CellValue import CellValue
from PySide6.QtGui import QFont, QColor, QBrush
from .AppGlobals import AppGlobals
from .StringCellValue import StringCellValue

class ResultStringCellValue(StringCellValue):
    def __init__(self, text: str, row = -1, col = -1):
        super().__init__(text, row, col)
        self.serialize_type = "ResultStringCellValue"

    def to_string(self, row = -1, col = -1):
        if -1 != col and -1 != row:
            item = AppGlobals.table.item(row, col)
            if item:
                resultFont = QFont()
                resultFont.setBold(True)
                item.setFont(resultFont)

        return super().to_string(row, col)
