from PySide6.QtCore import Qt
from .CellValue import CellValue
from PySide6.QtGui import QFont, QColor, QBrush
from .AppGlobals import AppGlobals
from .StringCellValue import StringCellValue

class ResultStringCellValue(StringCellValue):

    def __init__(
        self,
        text: str,
        row: int = -1,
        col: int = -1,
        font_size: int = AppGlobals.history_string_font_size
    ):
        # Pass is_bold=True and font_size to parent class StringCellValue
        super().__init__(
            text, row, col, is_bold=True, font_size=font_size
        )
