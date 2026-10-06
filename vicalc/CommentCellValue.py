from .AppGlobals import AppGlobals
from .StringCellValue import StringCellValue
from PySide6.QtGui import QColor

class CommentCellValue(StringCellValue):

    def __init__(
        self,
        text: str,
        row: int = -1,
        col: int = -1,
        is_bold: bool = False,
        font_size: int = AppGlobals.history_string_font_size,
    ):
        super().__init__(text, row, col, is_bold, font_size)

    def to_html(self) -> str:
        """Generates formatted HTML fragment for comment text using AppGlobals.color_comment."""
        display_text = self.to_string()

        # HTML entity escaping
        display_text = (
            display_text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace(" ", "&nbsp;")  # Preserve spaces in HTML rendering
        )

        font_size_style = (
            f"font-size: {self.font_size}pt; " if self.font_size > 0 else ""
        )
        bold_start = "<b>" if self.is_bold else ""
        bold_end = "</b>" if self.is_bold else ""

        # Extract hex color string if AppGlobals.color_comment is a QColor object
        color_val = AppGlobals.color_comment
        color_hex = color_val.name() if isinstance(color_val, QColor) else str(color_val)

        return (
            f'<span style="color: {color_hex}; {font_size_style}">'
            f"{bold_start}{display_text}{bold_end}</span>"
        )