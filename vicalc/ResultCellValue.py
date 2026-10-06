from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QFont
from .AppGlobals import AppGlobals
from .CellValue import CellValue
from .NumericCellValue import NumericCellValue

class ResultCellValue(NumericCellValue):

    def __init__(
        self,
        number: float,
        row: int = -1,
        col: int = -1,
        font_size: int = AppGlobals.history_number_font_size,
    ):
        # Pass is_bold=True and font_size to parent class
        super().__init__(
            number, row, col, is_bold=True, font_size=font_size
        )