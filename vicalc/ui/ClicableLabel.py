from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt, Signal, QEvent
from PySide6.QtGui import QMouseEvent

class ClickableLabel(QLabel):
    clicked = Signal()  # Custom signal

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor) # show hand cursor on hover
        self._bg_color = "#F0F0F0"
        self._update_style()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()  # Emit signal when label is clicked

    # --- Python Getter ---
    @property
    def bg_color(self) -> str:
        """Gets the current background color."""
        return self._bg_color

    # --- Python Setter ---
    @bg_color.setter
    def bg_color(self, color: str):
        """Sets the background color and updates the stylesheet."""
        if self._bg_color != color:
            self._bg_color = color
            self._update_style()

    def _update_style(self):
        """Resets the style if the label is empty; otherwise applies custom styling."""
        if not self.text().strip():
            self.reset_style()
        else:
            self._apply_custom_style()

# --- Override Text Setters for Auto-Monitoring ---
    def setText(self, text: str):
        """Overrides setText to trigger style checks automatically when text changes."""
        super().setText(text)
        self._update_style()

    def clear(self):
        """Overrides clear to trigger style reset when label content is cleared."""
        super().clear()
        self._update_style()

    def _apply_custom_style(self):
        """Applies the current background color and border styles."""
        self.setStyleSheet(f"""
            ClickableLabel {{
                background-color: {self._bg_color};
                color: #000000;
                border: 1px solid #717171;
                border-radius: 3px;
                padding: 2px 6px;
            }}
        """)        

    def reset_style(self):
        """Resets the stylesheet to the system default and forces a re-polish."""
        self.setStyleSheet("")
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()