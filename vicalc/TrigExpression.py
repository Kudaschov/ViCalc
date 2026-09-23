from .UnaryExpression import UnaryExpression
from .AngleUnit import AngleUnit

class TrigExpression(UnaryExpression):
    def __init__(self, tableWidget = None):
        super().__init__(tableWidget)
