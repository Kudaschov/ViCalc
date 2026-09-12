from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QMouseEvent
from ..NumberBase import NumberBase
from ..AppGlobals import AppGlobals
from .ClicableLabel import ClickableLabel

class NumberBaseLabel(ClickableLabel):
    clicked = Signal()  # Custom signal

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor) # show hand cursor on hover

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()  # Emit signal when label is clicked

    def set_base(self, base: NumberBase):
        """Updates the label background color based on the selected NumberBase."""
        self.bg_color = AppGlobals.BASE_COLORS.get(base, "#FFFFFF")
