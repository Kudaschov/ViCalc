from PySide6.QtCore import Qt

from vicalc.IntegerCellValue import IntegerCellValue
from .CellValue import CellValue
from PySide6.QtGui import QFont, QColor, QBrush
from .AppGlobals import AppGlobals

class IntegerResultCellValue(IntegerCellValue):
    def __init__(self, number: int, row = -1, col = -1):
        super().__init__(number, row, col, is_bold=True)
