import math
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
        self.protocol(number)
        self.protocol(" = ")
        self.protocol_result(degrees)
        self.protocol("° ", 5)
        self.protocol_result(minutes)
        self.protocol("\' ", 5)
        self.protocol_result(seconds)
        self.protocol("\"", 5)

        return number