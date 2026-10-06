from typing import Any
from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression
from .AppGlobals import AppGlobals
from .CalcMode import CalcMode

class AdditionExpression(BinaryExpression):
    """Expression executing addition."""

    def __init__(self, first_number: float | complex, table_widget: Any = None) -> None:
        super().__init__(first_number, table_widget)
        self.operation_prio = CalcPrios.Addition

    def text(self) -> str:
        return f"{self.first_number_to_string()} + "
    
    def calculate(self, number: float):
        result = self.first_number + number
        self.insert_scroll_table()

        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(self.first_number, " + ", False)
            self.protocol_complex(number, " = ", False)
            self.protocol_complex(result, "", True)
        else:
            self.protocol(self.first_number, 0)
            self.protocol(" + ", 1)
            self.protocol(number, 2)
            self.protocol(" = ", 3)
            self.protocol_result(result, 4)
        return result