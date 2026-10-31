from enum import Enum, auto

class DaysInYear(Enum):
    days360 = auto()
    days365 = auto()

    @property
    def days(self) -> int:
        mapping = {
            DaysInYear.days360: 360,
            DaysInYear.days365: 365,
        }
        return mapping[self]