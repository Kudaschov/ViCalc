import math
from PySide6.QtWidgets import QTableWidgetItem
from AngleUnit import AngleUnit

class RadUnit(AngleUnit):

    def to_deg(self, a:float):
         return 180.0 * a / math.pi
    
    def to_rad(self, a:float):
        return a

    def to_gra(self, a:float):
        return 200.0 * a / math.pi

    def from_rad(self, rad:float):
        return rad

    def angle_symbol(self):
        return "RAD"

    def to_deg_with_protocol(self, a:float):
        pass  # No implementation here    

    def to_rad_with_protocol(self, a:float):
        pass  # No implementation here    

    def to_gra_with_protocol(self, a:float):
        pass  # No implementation here    

