from enum import Enum, auto

class NumberBase(Enum):
    BIN = auto()
    OCT = auto()
    DEC = auto()
    HEX = auto()

    @property
    def status_text(self) -> str:
        """Text displayed in the status bar."""
        mapping = {
            NumberBase.BIN: "BIN",
            NumberBase.OCT: "OCT",
            NumberBase.DEC: "DEC",
            NumberBase.HEX: "HEX",
        }
        return mapping[self]
