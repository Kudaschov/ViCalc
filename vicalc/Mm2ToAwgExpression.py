from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class Mm2ToAwgExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self, number: float)-> float:
        self.insert_scroll_table()
        self.protocol_result("AWG", 0)
        self.protocol_result("⌀ [in]", 1)
        self.protocol_result("⌀ [mm]", 2)
        self.protocol_result("Area [kcmil]", 3)
        self.protocol_result("Area [mm²]", 4)
        self.insert_scroll_table()
        result: float = AppGlobals.mm2_to_awg_calculation(number)
        self.protocol(result, 0)
        diameter_inch = AppGlobals.mm2_to_diameter_inch_calculation(number)
        self.protocol(diameter_inch, 1)
        diameter_mm = AppGlobals.mm2_to_diameter_mm_calculation(number)
        self.protocol(diameter_mm, 2)
        area_kcmil = AppGlobals.mm2_to_kcmil_calculation(number)
        self.protocol(area_kcmil, 3)
        self.protocol(number, 4)
        return result
