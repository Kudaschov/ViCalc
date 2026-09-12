from PySide6.QtWidgets import QLineEdit

class DotLineEdit(QLineEdit):
    """QLineEdit subclass that replaces commas with dots using textChanged signal."""

    def __init__(self, parent=None):
        super().__init__(parent)
        # Connect textChanged signal to the replacement handler
        self.textChanged.connect(self._replace_comma)

    def _replace_comma(self, text: str):
        if "," in text:
            # 1. Block signals temporarily to prevent an infinite recursion loop
            self.blockSignals(True)

            # 2. Save current cursor position before text modification
            cursor_pos = self.cursorPosition()

            # 3. Replace comma with dot and update text
            self.setText(text.replace(",", "."))

            # 4. Restore cursor position
            self.setCursorPosition(cursor_pos)

            # 5. Re-enable signals
            self.blockSignals(False)