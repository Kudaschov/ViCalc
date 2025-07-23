from .CalcPrios import CalcPrios
from .CalcExpression import CalcExpression
from .UnaryExpression import UnaryExpression

class BracketExpression(UnaryExpression):
    def __init__(self, tableWidget):
        super().__init__(tableWidget)

    def text(self):
        return " ( "
    
    def calculate(self, number: float):
        # just give the number further
        result: float = number
        return result    
