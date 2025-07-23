import math
from .AngleUnit import AngleUnit

class GraUnit(AngleUnit):

    def to_deg(self, a:float):
        return 9.0 * a / 10.0

    def to_rad(self, a:float):
        return math.pi * a / 200.0

    def to_gra(self, a:float):
        return a

    def from_rad(self, rad:float):
        return rad * 200.0 / math.pi

    def angle_symbol(self):
        return "GRA"

    def to_deg_with_protocol(self, a:float):
        pass  # No implementation here    

    def to_rad_with_protocol(self, a:float):
        pass  # No implementation here    

    def to_gra_with_protocol(self, a:float):
        pass  # No implementation here    