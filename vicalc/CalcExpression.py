from abc import ABC, abstractmethod
from PySide6.QtCore import QLocale
from PySide6.QtGui import QFont
from .CalcPrios import CalcPrios

class CalcExpression(ABC):
    next_result: float # result from next node

    def __init__(self, tableWidget):
        self.operation_prio = CalcPrios.Min
        self.prev_expression = None
        self.next_expression = None
        self.locale = QLocale()
        self.tableWidget = tableWidget
        self.resultFont = QFont()
        self.resultFont.setBold(True)
        self.next_result = None
        self.row = 0 # row in TableWidget

    def text(self):
        return "- - -"

    @abstractmethod
    def calculate(self, number:float):
        pass  # No implementation here

    def toString(self, number:float):
        return self.locale.toString(number, "g", 16)

    def insert_scroll_table(self):
        self.row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.row)        
        self.tableWidget.scrollToBottom()