from PySide6.QtCore import Qt
from .CellValue import CellValue
from .NumericCellValue import NumericCellValue
from .AppGlobals import AppGlobals

class FloatCellValue(NumericCellValue):
    def __init__(self, number: float, row = -1, col = -1):
        super().__init__(number, row, col)
        self.serialize_type = "FloatCellValue"
