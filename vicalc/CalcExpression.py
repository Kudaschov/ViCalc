from abc import ABC, abstractmethod
from PySide6.QtCore import QLocale
from PySide6.QtGui import QFont
from .CalcPrios import CalcPrios
from .AppGlobals import AppGlobals

class CalcExpression(ABC):
    def __init__(self, tableWidget = None):
        self.operation_prio = CalcPrios.Min
        self.prev_expression = None
        self.next_expression = None
        self.locale = QLocale(QLocale.C)
        self.resultFont = QFont()
        self.resultFont.setBold(True)
        self.row = 0 # row in TableWidget

    def text(self):
        return "- - -"

    @abstractmethod
    def calculate(self, number:float):
        pass  # No implementation here

    def toString(self, number:float):
        return AppGlobals.to_normal_string(number)

    def insert_scroll_table(self):
        self.row = AppGlobals.table.rowCount()
        AppGlobals.table.insertRow(self.row)        
        AppGlobals.table.scrollToBottom()