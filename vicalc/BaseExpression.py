from abc import ABC, abstractmethod
from PySide6.QtWidgets import QMessageBox
from .UnaryExpression import UnaryExpression

class BaseExpression(UnaryExpression):
    def __init__(self, tableWidget, base: int):
        super().__init__(tableWidget)
        self.base: int = base
        self.i_number: int = 0 #integer number from string with base 2, 8, 10 or 16

    def calculate(self, number:float):
        pass  # Not used here

    @abstractmethod
    def conv_from_string(self, string_number) -> bool:
        pass  # No implementation here

    def to_binary(self):
        return f"{self.i_number:b}"
    
    def to_octal(self):
        return f"{self.i_number:o}"
    
    def to_decimal(self):
        return f"{self.i_number}"
    
    def to_hexadecimal(self):
        return f"{self.i_number:X}"
    
    def conv_from_string(self, string_number):
        try:
           self.i_number = int(string_number, self.base)
           return True
        except Exception as e:
            # QMessageBox.critical(None, "Error", f"{str(e)}")
            return False