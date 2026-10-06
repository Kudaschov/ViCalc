import math
from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression

class ModExpression(BinaryExpression):
    def __init__(self, number):
        super().__init__(number)
        self.operation_prio = CalcPrios.Multiplication

    def text(self):
        return self.first_number_to_string() + " mod "
    
    def calculate(self, number: float):
        result: float = math.fmod(self.first_number, number)
        self.insert_scroll_table()
        self.protocol(self.first_number)
        self.protocol(" mod ")
        self.protocol(number)
        self.protocol(" = ")
        self.protocol_result(result)
        
        return result
