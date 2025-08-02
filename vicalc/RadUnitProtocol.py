import math
from PySide6.QtWidgets import QTableWidgetItem
from .DegUnit import DegUnit
from .RadUnit import RadUnit
from .GraUnit import GraUnit
from .AppGlobals import AppGlobals

class RadUnitProtocol(RadUnit):
    def to_deg_with_protocol(self, a:float):
        result = self.to_deg(a)
    
        if AppGlobals.table != None:
            self.insert_scroll_table()
            self.protocol(a, 0)
            self.protocol(self.angle_symbol() + " =", 1)
            self.protocol_result(result, 2)
            self.protocol(DegUnit().angle_symbol(), 3)
        return result
    
    def to_rad_with_protocol(self, a:float):
        return self.to_rad(a)
    
    def to_gra_with_protocol(self, a:float):
        result = self.to_gra(a)
    
        if AppGlobals.table != None:
            self.insert_scroll_table()
            self.protocol(a, 0)
            self.protocol(self.angle_symbol() + " =", 1)
            self.protocol_result(result, 2)
            self.protocol(GraUnit().angle_symbol(), 3)

        return result