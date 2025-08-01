import sys
import pickle
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt, Signal
from ..NumericFormat import NumericFormat
from ..CellValue import CellValue
from ..AppGlobals import AppGlobals
from ..FloatCellValue import FloatCellValue
from ..ResultCellValue import ResultCellValue
from ..StringCellValue import StringCellValue

class CalcTableWidget(QTableWidget):
    enterPressed = Signal(int, int)
    escPressed = Signal()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            row = self.currentRow()
            col = self.currentColumn()
            item = self.item(row, col)
            if item:
                self.enterPressed.emit(row, col)
        if event.key() == Qt.Key.Key_Escape:
            self.escPressed.emit()
        else:
            # Standardverhalten beibehalten (z. B. Navigation mit Pfeiltasten)
            super().keyPressEvent(event)

    def get_serializable_data(self):
        data = []
        for row in range(self.rowCount()):
            row_data = []
            for col in range(self.columnCount()):
                item = self.item(row, col)
                if not item:
                    row_data.append("")
                    continue

                val = item.data(Qt.UserRole)

                if isinstance(val, CellValue):
                    row_data.append({"type": val.serialize_type, "value": val.value()})
                else:
                    # Leave raw string/number unwrapped
                    if val:
                        row_data.append(str(val))
                    else:
                        row_data.append(item.text())
            data.append(row_data)
        return data
    
    def load_serialized_data(self, matrix):
        float_cell = FloatCellValue(0)
        result_cell = ResultCellValue(0)
        string_cell = StringCellValue("")

        parsed = []
        for row_idx, row_data in enumerate(matrix):
            if self.rowCount() <= row_idx:
                self.setRowCount(row_idx + 1)
            row_objs = []
            for col_idx, entry in enumerate(row_data):
                if (self.columnCount() <= col_idx):
                    self.setColumnCount(col_idx + 1)
                if isinstance(entry, dict) and "type" in entry and "value" in entry:
                    if entry["type"] == float_cell.serialize_type:
                        row_objs.append(FloatCellValue(entry["value"], row_idx, col_idx))
                    elif entry["type"] == string_cell.serialize_type:
                        row_objs.append(StringCellValue(entry["value"], row_idx, col_idx))
                    elif entry["type"] == result_cell.serialize_type:
                        row_objs.append(ResultCellValue(entry["value"], row_idx, col_idx))
                    else:
                        item = self.item(row_idx, col_idx)
                        if item:
                            item.setText(str(entry["value"]))
                        else:
                            if len(str(entry["value"])) > 0:
                                item = QTableWidgetItem(str(entry["value"]))
                                self.setItem(row_idx, col_idx, item)
                else:
                    item = self.item(row_idx, col_idx)
                    if item:
                        self.item(row_idx, col_idx).setText(str(entry))
                    else:
                        if len(str(entry)) > 0:
                            item = QTableWidgetItem(str(entry))
                            self.setItem(row_idx, col_idx, item)

            parsed.append(row_objs)

    def save_to_file(self, filepath):
        """Save table content to file using pickle."""
        data = self.get_serializable_data()
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)

    def load_from_file(self, filepath):
        """Load table content from a pickle file."""
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
        self.load_serialized_data(data)