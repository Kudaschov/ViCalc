from functools import singledispatchmethod
from typing import Any

from vicalc.IntegerCellValue import IntegerCellValue
from vicalc.IntegerResultCellValue import IntegerResultCellValue
from .CalcExpression import CalcExpression
from .FloatCellValue import FloatCellValue
from .ResultCellValue import ResultCellValue
from .StringCellValue import StringCellValue
from .ResultStringCellValue import ResultStringCellValue
import cmath
from .AppGlobals import AppGlobals
from .ComplexNumberForm import ComplexNumberForm
from .CalcMode import CalcMode

class UnaryExpression(CalcExpression):
    """Base class for unary operations supporting multi-type table protocol output."""

    def __init__(self, table_widget: Any = None) -> None:
        super().__init__(table_widget)
    
    @singledispatchmethod
    def protocol_result(self, arg: Any, column_number: int) -> None:
        """Generic report method for result cells."""
        raise NotImplementedError(f"Reporting not implemented for type {type(arg)}")

    @protocol_result.register(float)
    def _(self, arg: float, column_number: int) -> None:
        if arg.is_integer():
            IntegerResultCellValue(int(arg), self.row, column_number)
        else:
            ResultCellValue(arg, self.row, column_number)

    @protocol_result.register(str)
    def _(self, arg: str, column_number: int) -> None:
        ResultStringCellValue(arg, self.row, column_number)

    @protocol_result.register(int)
    def _(self, arg: int, column_number: int) -> None:
        IntegerResultCellValue(arg, self.row, column_number)

    @singledispatchmethod
    def protocol(self, arg: Any, column_number: int) -> None:
        """Generic report method for input/operand cells."""
        raise NotImplementedError(f"Reporting not implemented for type {type(arg)}")
    
    @protocol.register(str)
    def _(self, arg: str, column_number: int) -> None:
        StringCellValue(arg, self.row, column_number)

    @protocol.register(float)
    def _(self, arg: float, column_number: int) -> None:
        if arg.is_integer():
            IntegerCellValue(int(arg), self.row, column_number)
        else:
            FloatCellValue(arg, self.row, column_number)

    @protocol.register(int)
    def _(self, arg: int, column_number: int) -> None:
        IntegerCellValue(arg, self.row, column_number)

    def protocol_complex_rect(self, num: complex, suffix: str, is_result: bool = False, prefix: str = "") -> None:
        """Helper method to format and protocol rectangular complex numbers."""
        method = self.protocol_result if is_result else self.protocol

        if prefix == "":
            method("(", 0)
        else:
            method(prefix, 0)
            
        method(num.real, 1)
        next_col = 2
        if num.imag >= 0:
            method("+", next_col)
            next_col += 1
        method(num.imag, next_col)
        next_col += 1
        method(f"i){suffix}", next_col)

    def protocol_complex_polar(self, num: complex, suffix: str, is_result: bool = False, prefix: str = "") -> None:
        """Helper method to format and protocol polar complex numbers."""
        method = self.protocol_result if is_result else self.protocol
        r, theta = cmath.polar(num)
        angle_val = AppGlobals.angle_unit.from_rad(theta)
        unit_str = AppGlobals.angle_unit.angle_symbol()

        if prefix == "":
            method("(", 0)
        else:
            method(prefix, 0)
        method(r, 1)
        method("∠", 2)
        method(angle_val, 3)
        method(f"{unit_str}){suffix}", 4)

    def protocol_complex(self, num: complex, suffix: str, is_result: bool = False, prefix: str = "") -> None:
        if AppGlobals.complex_number_form is ComplexNumberForm.rectangular:
            self.protocol_complex_rect(num, suffix, is_result, prefix)
        else:
            self.protocol_complex_polar(num, suffix, is_result, prefix)

    def calculate(self, number: float | complex) -> float | complex:
        self.insert_scroll_table()
        if AppGlobals.calc_mode is CalcMode.complex_numbers:
            self.protocol_complex(number, "", True)
        else:
            self.protocol_result(number, 0)