from enum import Enum, auto

class PaymentPeriod(Enum):
    BEGIN = auto()
    END = auto()

    @property
    def label(self) -> str:
        """Returns the human-readable label for the payment period."""
        mapping = {
            PaymentPeriod.BEGIN: "Begin",
            PaymentPeriod.END: "End",
        }
        return mapping[self]