from abc import ABC, abstractmethod
from functools import singledispatchmethod
from PySide6.QtCore import QLocale
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QTableWidgetItem

class AngleUnit(ABC):
    def __init__(self):
        self.tableWidget = None
        self.locale = QLocale()
        self.resultFont = QFont()
        self.resultFont.setBold(True)
        self.row = None
        

    def toString(self, number:float):
        return self.locale.toString(number, "g", 16)
    
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
        self.row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.row)        
        self.tableWidget.scrollToBottom()

    def protocol_result(self, result: float, column_number: int):
        item = QTableWidgetItem(self.toString(result))
        item.setFont(self.resultFont)
        self.tableWidget.setItem(self.row, column_number, item)
        self.tableWidget.setCurrentCell(self.row, column_number)

    @singledispatchmethod
    def protocol(self, arg, column_number):
        """
        Generic report method.
        """
        raise NotImplementedError(f"Reporting not implemented for type {type(arg)}")
    
    @protocol.register(str)
    def _(self, arg: str, column_number: int):
        self.tableWidget.setItem(self.row, column_number, QTableWidgetItem(arg))

    @protocol.register(float)
    def _(self, arg: float, column_number: int):
        self.tableWidget.setItem(self.row, column_number, QTableWidgetItem(self.toString(arg)))

