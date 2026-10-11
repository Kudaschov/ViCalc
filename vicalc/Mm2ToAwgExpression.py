from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class Mm2ToAwgExpression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self, number: float)-> float:
        self.insert_scroll_table()
        self.protocol("AWG: ")
        result: float = AppGlobals.mm2_to_awg_calculation(number)
        self.protocol_result(result)
        self.protocol(" / ⌀: ")
        diameter_inch = AppGlobals.mm2_to_diameter_inch_calculation(number)
        self.protocol(diameter_inch, 1)
        self.protocol(" in / ⌀: ")
        diameter_mm = AppGlobals.mm2_to_diameter_mm_calculation(number)
        self.protocol(diameter_mm, 2)
        self.protocol(" mm / ")
        area_kcmil = AppGlobals.mm2_to_kcmil_calculation(number)
        self.protocol(area_kcmil, 3)
        self.protocol(" kcmil / ")
        self.protocol(number, 4)
        self.protocol(" mm²")
        return result
