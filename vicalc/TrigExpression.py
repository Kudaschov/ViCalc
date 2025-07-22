from UnaryExpression import UnaryExpression
from AngleUnit import AngleUnit

class TrigExpression(UnaryExpression):
    def __init__(self, tableWidget, angle_unit:AngleUnit):
        super().__init__(tableWidget)
        self.angle_unit = angle_unit