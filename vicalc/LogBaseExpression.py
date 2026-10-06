import math, cmath
from .BinaryExpression import BinaryExpression
from .AppGlobals import AppGlobals
from .CalcPrios import CalcPrios
from .CalcMode import CalcMode

class LogBaseExpression(BinaryExpression):
    def __init__(self, first_number: float | complex) -> None:
        super().__init__(first_number)
        self.operation_prio = CalcPrios.Bracket
    
    def text(self) -> str:
        return f"log({self.first_number_to_string()}), base:"

    def calculate(self, number: float | complex)-> float:
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(self.first_number, "; ", False, "Log(")
            self.protocol_complex(number, " = ", False, "base: (")
            result = cmath.log(self.first_number, number)
            self.protocol_complex(result, "", True)
        else:
            self.protocol("Log(")
            self.protocol(self.first_number)
            self.protocol("); base: ")
            self.protocol(number)
            self.protocol(" = ")
            result: float = AppGlobals.log_base_calculation(self.first_number, number)
            self.protocol_result(result)
        return result
