import math
from PySide6.QtWidgets import QTableWidgetItem
from .UnaryExpression import UnaryExpression

class DMSExpression(UnaryExpression):
    def calculate(self, number: float):

        is_negative = number < 0
        decimal_deg = abs(number)
        degrees = int(decimal_deg)
        minutes_float = (decimal_deg - degrees) * 60
        minutes = int(minutes_float)
        seconds = (minutes_float - minutes) * 60
        if is_negative:
            degrees = -1 * degrees

        self.insert_scroll_table()
        self.protocol(number, 0)
        self.protocol("=", 1)
        self.protocol_result(float(degrees), 2)
        self.protocol_result(float(minutes), 3)
        self.protocol_result(seconds, 4)
        self.protocol("° \' \"", 5)

        return number