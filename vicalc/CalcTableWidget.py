from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt, Signal
import sys

class CalcTableWidget(QTableWidget):
    enterPressed = Signal(str)
    escPressed = Signal()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            row = self.currentRow()
            col = self.currentColumn()
            item = self.item(row, col)
            if item:
                self.enterPressed.emit(item.text())
        if event.key() == Qt.Key.Key_Escape:
            self.escPressed.emit()
        else:
            # Standardverhalten beibehalten (z. B. Navigation mit Pfeiltasten)
            super().keyPressEvent(event)