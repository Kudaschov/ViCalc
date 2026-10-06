from PySide6.QtCore import QLocale, Qt
from PySide6.QtGui import QBrush, QColor, QFont
from .AppGlobals import AppGlobals
from .CellValue import CellValue
from .NumericFormat import NumericFormat


class NumericCellValue(CellValue):

    def __init__(
        self,
        number: float,
        row: int = -1,
        col: int = -1,
        is_bold: bool = False,
        font_size: int = AppGlobals.history_number_font_size,
    ):
        super().__init__(row, col, is_bold, font_size)
        self.number: float = number

        AppGlobals.current_row = row
        AppGlobals.current_column = col

        # Append HTML formatted entry directly to QTextBrowser
        AppGlobals.history.insertHtml(self.to_html())

    def to_string(self, row: int = -1, col: int = -1):
        return AppGlobals.to_format_string(self.number)

    def value(self, row: int = -1, col: int = -1):
        return self.number

    def to_html(self) -> str:
        """Generates clickable HTML fragment for QTextBrowser with font size and color formatting."""
        display_text = self.to_string()
        full_precision = self.number

        # Determine font color for negative values
        if AppGlobals.different_view_negative_number and self.number < 0:
            color = AppGlobals.color_negative_number
        else:
            color = "#1a5fb4"

        # Apply bold styling if enabled
        bold_start = "<b>" if self.is_bold else ""
        bold_end = "</b>" if self.is_bold else ""

        # Construct CSS font size rule if font_size is explicitly provided
        font_size_style = (
            f"font-size: {self.font_size}pt; text-decoration: underline;" if self.font_size > 0 else ""
        )

        return (
            f'<a href="calc:{full_precision}"'
            f'style="color: {color}; text-decoration: none; {font_size_style}">'
            f"{bold_start}{display_text}{bold_end}</a>"
        )