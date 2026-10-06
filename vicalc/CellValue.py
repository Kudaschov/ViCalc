from abc import ABC, abstractmethod

class CellValue(ABC):
    def __init__(
        self,
        row: int = -1,
        col: int = -1,
        is_bold: bool = False,
        font_size: int = -1,
    ):
        """Base class for history cells supporting row/col indices, bold styling, and font size."""
        self.row = row
        self.col = col
        self.is_bold = is_bold
        self.font_size = font_size

    @abstractmethod
    def to_string(self, row: int = -1, col: int = -1):
        pass

    @abstractmethod
    def value(self, row: int = -1, col: int = -1):
        pass