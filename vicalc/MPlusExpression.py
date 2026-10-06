from .MemoryExpression import MemoryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class MPlusExpression(MemoryExpression):
    def calculate(self, number: float | complex):
        result: float | complex = self.first_number + number
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(self.first_number, " + ", False)
            self.protocol_complex(number, " = ", False)
            self.protocol_complex(result, " Memory", True, "")
        else:
            self.protocol(self.first_number, 0)
            self.protocol(" + ", 1)
            self.protocol(number, 2)
            self.protocol(" = ", 3)
            self.protocol_result(result, 4)
            self.protocol(" Memory", 5)
        return result