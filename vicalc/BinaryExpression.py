from .AppGlobals import AppGlobals
from .CalcPrios import CalcPrios
from .UnaryExpression import UnaryExpression

class BinaryExpression(UnaryExpression):
    first_number: float
    def __init__(self, first_number, tableWidget = None):
        super().__init__(tableWidget)
        self.first_number = first_number

    def first_number_to_string(self):
        return AppGlobals.to_format_string(self.first_number)
