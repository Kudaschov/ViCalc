from functools import singledispatchmethod
from PySide6.QtWidgets import QTableWidgetItem
from .CalcPrios import CalcPrios
from .CalcExpression import CalcExpression
from .FloatCellValue import FloatCellValue
from .ResultCellValue import ResultCellValue
from .StringCellValue import StringCellValue
from .ResultStringCellValue import ResultStringCellValue

class UnaryExpression(CalcExpression):
    def __init__(self, tableWidget = None):
        super().__init__(tableWidget)
    
    @singledispatchmethod
    def protocol_result(self, arg, column_number):
        """
        Generic report method for protocol_results.
        """
        raise NotImplementedError(f"Reporting not implemented for type {type(arg)}")

    @protocol_result.register(float)
    def _(self, arg: float, column_number: int):
        ResultCellValue(arg, self.row, column_number)

    @protocol_result.register(str)
    def _(self, arg: str, column_number: int):
        ResultStringCellValue(arg, self.row, column_number)

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

