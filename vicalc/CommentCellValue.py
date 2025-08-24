from PySide6.QtCore import Qt, QLocale
from .StringCellValue import StringCellValue
from PySide6.QtGui import QFont, QColor, QBrush
from .NumericFormat import NumericFormat
from .AppGlobals import AppGlobals

class CommentCellValue(StringCellValue):
    def __init__(self, text: str, row = -1, col = -1):
        super().__init__(text, row, col)
        self.serialize_type = "CommentCellValue"

        if -1 != col and -1 != row:
            item = AppGlobals.table.item(row, col)
            if item:
                item.setForeground(QBrush(QColor(AppGlobals.color_comment)))
                item.setText(self.to_string())
