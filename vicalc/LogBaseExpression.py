from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class LogBaseExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self, number: float)-> float:
        self.insert_scroll_table()
        self.protocol("Logarithm", 0)
        self.protocol(number, 1)
        self.protocol("Base", 2)
        self.protocol(AppGlobals.log_base, 3)
        self.protocol("=", 4)
        result: float = AppGlobals.log_base_calculation(number, AppGlobals.log_base)
        self.protocol_result(self.toString(result), 5)
        return result
