from PySide6.QtCore import QRect, Qt, Signal
from PySide6.QtGui import QPainter, QMouseEvent
from PySide6.QtWidgets import QLabel
from .ClickableLabel import ClickableLabel

class VerticalLabel(ClickableLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # 1. Translate origin to the bottom-left of the widget
        painter.translate(0, self.height())

        # 2. Rotate 90 degrees counter-clockwise
        painter.rotate(-90)

        # 3. Create bounding box
        rect = QRect(0, 0, self.height(), self.width())

        # 4. DETERMINE CORRECT COLOR (Handles Disabled State & StyleSheets)
        # Check if widget is disabled -> use Disabled palette group
        if not self.isEnabled():
            text_color = self.palette().color(
                self.palette().ColorGroup.Disabled,
                self.palette().ColorRole.WindowText,
            )
        else:
            # Current color based on active state / stylesheet
            text_color = self.palette().color(
                self.palette().currentColorGroup(),
                self.palette().ColorRole.WindowText,
            )

        painter.setPen(text_color)

        # 5. Draw text
        display_text = self.text() if self.text() else "- - -"
        align_flags = Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter

        painter.drawText(rect, align_flags, display_text)