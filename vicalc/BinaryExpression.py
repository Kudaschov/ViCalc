import cmath
from typing import Any
from .AppGlobals import AppGlobals
from .UnaryExpression import UnaryExpression
from .CalcMode import CalcMode
from .ComplexNumberForm import ComplexNumberForm

class BinaryExpression(UnaryExpression):
    """Base class for binary operations involving two operands."""

    first_number: float | complex

    def __init__(self, first_number: float | complex, table_widget: Any = None) -> None:
        super().__init__(table_widget)
        self.first_number = first_number

    def first_number_to_string(self) -> str:
        """Format the first operand based on current calculator mode and representation."""
        if AppGlobals.calc_mode == CalcMode.complex_numbers:
            if AppGlobals.complex_number_form == ComplexNumberForm.rectangular:
                real_str = AppGlobals.to_format_string(self.first_number.real)
                imag_str = AppGlobals.to_format_string(self.first_number.imag)
                if self.first_number.imag <0:
                    return f"({real_str}{imag_str}i)"
                else:
                    return f"({real_str}+{imag_str}i)"
            
            r, theta = cmath.polar(self.first_number)
            r_s = AppGlobals.to_format_string(r)
            theta_s = AppGlobals.to_format_string(AppGlobals.angle_unit.from_rad(theta))
            return f"({r_s}∠{theta_s})"
        
        return AppGlobals.to_format_string(self.first_number)