from .UnaryExpression import UnaryExpression
from .AppGlobals import AppGlobals

class AwgToMm2Expression(UnaryExpression):
    def __init__(self):
        super().__init__()
    
    def calculate(self, number: float)-> float:
        self.insert_scroll_table()
        self.protocol("AWG: ")
        self.protocol(number)
        diameter_inch = AppGlobals.awg_to_diameter_inch_calculation(number)
        self.protocol(" / ⌀: ")
        self.protocol(diameter_inch)
        self.protocol(" in / ⌀: ")
        diameter_mm = AppGlobals.awg_to_diameter_mm_calculation(number)
        self.protocol(diameter_mm)
        self.protocol(" mm / ")
        area_kcmil = AppGlobals.awg_to_kcmil_calculation(number)
        self.protocol(area_kcmil)
        self.protocol(" kcmil / ")
        result: float = AppGlobals.awg_to_mm2_calculation(number)
        self.protocol_result(result)
        self.protocol(" mm²")
        return result
