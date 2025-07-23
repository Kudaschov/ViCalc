import math
from PySide6.QtWidgets import QTableWidgetItem
from .AngleUnit import AngleUnit

class DegUnit(AngleUnit):

    def to_deg(self, a:float):
        return a

    def to_rad(self, a):
        return math.pi * a / 180.0
    
    def to_gra(self, a:float):
        return 10.0 * a / 9.0
    
    def from_rad(self, rad:float):
        return rad * 180.0 / math.pi

    def angle_symbol(self):
        return "°"

    def to_deg_with_protocol(self, a:float):
        pass  # No implementation here    

    def to_rad_with_protocol(self, a:float):
        pass  # No implementation here    

    def to_gra_with_protocol(self, a:float):
        pass  # No implementation here    