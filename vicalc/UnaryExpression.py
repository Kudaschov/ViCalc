from functools import singledispatchmethod
from PySide6.QtWidgets import QTableWidgetItem
from .CalcPrios import CalcPrios
from .CalcExpression import CalcExpression

class UnaryExpression(CalcExpression):
    def __init__(self, tableWidget):
        super().__init__(tableWidget)
    
    def protocol_result(self, result, column_number):
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
