from enum import IntEnum, auto

class CalcPrios(IntEnum):
    Min = auto()
    OR = auto()
    XOR = auto()
    AND = auto()
    Addition = auto()
    Multiplication = auto()
    Power = auto()
    Bracket = auto()