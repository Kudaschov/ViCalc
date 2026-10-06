from abc import ABC, abstractmethod
from typing import Any
from .CalcPrios import CalcPrios
from .AppGlobals import AppGlobals

class CalcExpression(ABC):
    """Abstract base class representing a mathematical calculation expression."""

    def __init__(self, table_widget: Any = None) -> None:
        self.operation_prio = CalcPrios.Min
        self.prev_expression: CalcExpression | None = None
        self.next_expression: CalcExpression | None = None
        self.locale = AppGlobals.locale
        self.row: int = 0  # Row index in TableWidget

    def text(self) -> str:
        """Return text representation of the expression operator."""
        return "- - -"

    @abstractmethod
    def calculate(self, number: float | complex) -> float | complex:
        """Perform calculation and record steps to the output table."""
        pass

    def toString(self, number: float | complex) -> str:
        """Convert a number to its formatted string representation."""
        return AppGlobals.to_normal_string(number)

    def insert_scroll_table(self) -> None:
        """Insert a new row into the global output table and scroll to bottom."""
        AppGlobals.history.append("")