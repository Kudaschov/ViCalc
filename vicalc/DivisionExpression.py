from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class DivisionExpression(BinaryExpression):
    def __init__(self, number, tableWidget = None):
        super().__init__(number, tableWidget)
        self.operation_prio = CalcPrios.Multiplication

    def text(self):
        return self.first_number_to_string() + " / "
    
    def calculate(self, number: float):
        result: float = self.first_number / number
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(self.first_number, " / ", False)
            self.protocol_complex(number, " = ", False)
            self.protocol_complex(result, "", True)
        else:
            self.protocol(self.first_number, -1)
            self.protocol(" / ", -1)
            self.protocol(number, -1)
            self.protocol(" = ", -1)
            self.protocol_result(result, -1)
        
        return result
