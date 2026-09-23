from enum import Enum, auto

class CalcMode(Enum):
    scientific = auto()
    base_n = auto()
    complex_numbers = auto()

    def next(self):
        # Convert enum members to a list
        modes = list(CalcMode)
        # Find current index, increment, and wrap around using modulo
        next_index = (modes.index(self) + 1) % len(modes)
        return modes[next_index]
    
    @property
    def status_text(self) -> str:
        """Text displayed in the status bar."""
        mapping = {
            CalcMode.scientific: "Scientific",
            CalcMode.base_n: "Programmer",
            CalcMode.complex_numbers: "Complex",
        }
        return mapping[self]
