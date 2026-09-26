from enum import Enum, auto

class ShiftRotateOperation(Enum):
    arithmetic = auto()
    logical = auto()
    circular = auto()
    circular_carry_bit = auto()

    @property
    def status_text(self) -> str:
        """Abbreviated text displayed in status bar"""
        mapping = {
            ShiftRotateOperation.arithmetic: "Ash",
            ShiftRotateOperation.logical: "Lsh",
            ShiftRotateOperation.circular: "Ro",
            ShiftRotateOperation.circular_carry_bit: "RoC"
        }
        return mapping[self]