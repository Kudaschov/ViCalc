from enum import Enum, auto

class WordSize(Enum):
    BIT8 = auto()
    BIT16 = auto()
    BIT32 = auto()
    BIT64 = auto()

    @property
    def status_text(self) -> str:
        """Text displayed in the status bar."""
        mapping = {
            WordSize.BIT8: "Byte",
            WordSize.BIT16: "Word",
            WordSize.BIT32: "DWord",
            WordSize.BIT64: "QWord",
        }
        return mapping[self]

    @property
    def bits(self) -> int:
        """Returns the number of bits for the word size."""
        mapping = {
            WordSize.BIT8: 8,
            WordSize.BIT16: 16,
            WordSize.BIT32: 32,
            WordSize.BIT64: 64,
        }
        return mapping[self]    

    @property
    def mask(self) -> int:
        """Returns the bitmask for restricting values (e.g., 0xFF for 8-bit)."""
        return (1 << self.bits) - 1    