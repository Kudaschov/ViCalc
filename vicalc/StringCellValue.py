from PySide6.QtCore import QLocale, Qt
from PySide6.QtGui import QColor, QFont
from .AppGlobals import AppGlobals
from .CellValue import CellValue
from .NumericFormat import NumericFormat


class StringCellValue(CellValue):

    def __init__(
        self,
        text: str,
        row: int = -1,
        col: int = -1,
        is_bold: bool = False,
        font_size: int = AppGlobals.history_string_font_size,
    ):
        super().__init__(row, col, is_bold, font_size)
        self.text: str = text

        # Append HTML formatted entry directly to QTextBrowser
        AppGlobals.history.insertHtml(self.to_html())

    def to_string(self, row: int = -1, col: int = -1):
        return self.text

    def value(self, row: int = -1, col: int = -1):
        return self.text

    def to_html(self) -> str:
        """Generates formatted HTML fragment for non-clickable text, headers, and operators."""
        display_text = self.to_string()

        # HTML entity escaping for common operators
        display_text = (
            display_text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace(" ", "&nbsp;")  # Preserve spaces in HTML rendering
        )

        # Style options
        font_size_style = (
            f"font-size: {self.font_size}pt; " if self.font_size > 0 else ""
        )
        bold_start = "<b>" if self.is_bold else ""
        bold_end = "</b>" if self.is_bold else ""

        # Regular text or functions (e.g. 'sin' or header text)
        return (
            f'<span style="color: #000000; {font_size_style}">'
            f"{bold_start}{display_text}{bold_end}</span>"
        )