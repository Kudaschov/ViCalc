from abc import ABC, abstractmethod
from functools import singledispatchmethod
from PySide6.QtCore import QLocale
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QTableWidgetItem
from .AppGlobals import AppGlobals
from .ResultCellValue import ResultCellValue
from .StringCellValue import StringCellValue
from .FloatCellValue import FloatCellValue

class AngleUnit(ABC):
    def __init__(self):
        self.locale = QLocale()
        self.resultFont = QFont()
        self.resultFont.setBold(True)
        self.row = None

    def toString(self, number:float):
        return AppGlobals.to_format_string(number)
    
    @abstractmethod
    def to_deg(self, a:float):
        pass  # No implementation here    

    @abstractmethod
    def to_deg_with_protocol(self, a:float):
        pass  # No implementation here    

    @abstractmethod
    def to_rad(self, a:float):
        pass  # No implementation here    

    @abstractmethod
    def to_rad_with_protocol(self, a:float):
        pass  # No implementation here    

    @abstractmethod
    def to_gra(self, a:float):
        pass  # No implementation here

    @abstractmethod
    def to_gra_with_protocol(self, a:float):
        pass  # No implementation here

    @abstractmethod
    def from_rad(self, rad:float):
        pass  # No implementation here

    @abstractmethod
    def angle_symbol(self):
        pass  # No implementation here    

    def insert_scroll_table(self):
        self.row = AppGlobals.table.rowCount()
        AppGlobals.table.insertRow(self.row)        
        AppGlobals.table.scrollToBottom()

    def protocol_result(self, result: float, column_number: int):
        ResultCellValue(result, self.row, column_number) 

    @singledispatchmethod
    def protocol(self, arg, column_number):
        """
        Generic report method.
        """
        raise NotImplementedError(f"Reporting not implemented for type {type(arg)}")
    
    @protocol.register(str)
    def _(self, arg: str, column_number: int):
        StringCellValue(arg, self.row, column_number)

    @protocol.register(float)
    def _(self, arg: float, column_number: int):
        FloatCellValue(arg, self.row, column_number)

