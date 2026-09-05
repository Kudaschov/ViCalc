from .CalcPrios import CalcPrios
from .BinaryExpression import BinaryExpression
from PySide6.QtWidgets import QTableWidgetItem

class IntegerBinaryExpression(BinaryExpression):
    """Base class for two-operand integer operations (e.g., bitwise AND, OR, XOR)."""
    def calculate(self, number: float):
        if not self.first_number.is_integer():
            raise ValueError(f"Invalid value: {self.first_number} is not an integer.")
        
        if not number.is_integer():
            raise ValueError(f"Invalid value: {number} is not an integer.")
