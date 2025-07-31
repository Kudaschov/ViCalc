from abc import ABC, abstractmethod
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem
from .AppGlobals import AppGlobals

class CellValue(ABC):
    def __init__(self, row = -1, col = -1):
        self.serialize_type = "CellValue"

        if -1 != col and -1 != row:
            table_item = QTableWidgetItem()
            table_item.setFlags(table_item.flags() ^ Qt.ItemIsEditable)
            table_item.setData(Qt.UserRole, self)
            AppGlobals.table.setItem(row, col, table_item)

    @abstractmethod
    def to_string(self, row = -1, col = -1):
        pass 

    @abstractmethod
    def value(self, row = -1, col = -1):
        pass