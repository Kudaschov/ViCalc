import math
from .UnaryExpression import UnaryExpression

class DDExpression(UnaryExpression):
    def calculate(self, degrees: int, minutes: int, seconds: float) -> float:
        result: float = degrees + (seconds / 60.0 + minutes) / 60.0
        self.insert_scroll_table()
        self.protocol(degrees)
        self.protocol("° ")
        self.protocol(minutes)
        self.protocol("\' ")
        self.protocol(seconds)
        self.protocol("\" = ")
        self.protocol_result(result)
        return result
        