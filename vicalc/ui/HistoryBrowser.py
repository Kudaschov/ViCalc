from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QTextBrowser, QMessageBox
from PySide6.QtGui import QTextCursor
from ..AppGlobals import AppGlobals
from ..CalcMode import CalcMode

class HistoryBrowser(QTextBrowser):
    # Custom signal emitted when Esc key is pressed
    escPressed = Signal()
    enterPressed = Signal()
    # Optional signal if you want to notify other components about pasting
    pasteToInputRequested = Signal(str)
    pasteToInputImagRequested = Signal(str)

    def keyPressEvent(self, event):
        # Check if the pressed key is the Escape key
        if event.key() == Qt.Key.Key_Escape:
            self.escPressed.emit()
            return  # Event process finished
        # Handle Enter / Return key presses
        elif event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            super().keyPressEvent(event)
            self.enterPressed.emit()
            return  # Stop further processing
        # Handle Delete key press for text selection removal
        elif event.key() == Qt.Key.Key_Delete:
            self.delete_selection_with_confirmation()
            return        
        # Pass all other key events to the parent class
        super().keyPressEvent(event)
    
    def setHtml(self, html: str):
        self.scroll_history_to_bottom()
        # Call the base class setHtml implementation
        super().setHtml(html)
        self.scroll_history_to_bottom()

    def insertHtml(self, html: str):
        self.scroll_history_to_bottom()
        super().insertHtml(html)
        self.scroll_history_to_bottom()

    def scroll_history_to_bottom(self):
        # Move cursor to the end of the document
        cursor = AppGlobals.history.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        AppGlobals.history.setTextCursor(cursor)            

    def contextMenuEvent(self, event):
        """Extends default context menu with a 'Delete Selection' action."""
        # Create standard context menu provided by QTextBrowser
        menu = self.createStandardContextMenu()

        # Check if right-click position is over an HTML anchor/link
        click_pos = event.pos()
        anchor_url = self.anchorAt(click_pos)

        cursor = self.textCursor()
        has_selection = cursor.hasSelection()

        # Add a separator before custom action
        menu.addSeparator()

        # Action 1: Paste value under cursor to input box (Active ONLY when over a hyperlink)
        paste_action = menu.addAction("Paste to input box")
        if anchor_url:
            paste_action.setEnabled(True)
            # Pass the anchor URL (e.g., 'calc:0.86603') to handler method
            paste_action.triggered.connect(
                lambda: self.on_paste_to_input(anchor_url)
            )
        else:
            paste_action.setEnabled(False)

        # Action 2: Paste value under cursor to input imagbox (Imag part oActive ONLY when over a hyperlink and calc mode is complex numbers)
        paste_action = menu.addAction("Paste to input box of imag part")
        if anchor_url and AppGlobals.calc_mode is CalcMode.complex_numbers:
            paste_action.setEnabled(True)
            # Pass the anchor URL (e.g., 'calc:0.86603') to handler method
            paste_action.triggered.connect(
                lambda: self.on_paste_to_input_imag(anchor_url)
            )
        else:
            paste_action.setEnabled(False)

        # Action 3
        # Create custom delete action
        delete_action = menu.addAction("Delete Selection")
        delete_action.setEnabled(has_selection)
        delete_action.triggered.connect(
            self.delete_selection_with_confirmation
        )

        # Show context menu at click position
        menu.exec_(event.globalPos())

    def delete_selection_with_confirmation(self):
        """Deletes the currently selected text after user confirmation."""
        cursor = self.textCursor()

        # Ensure there is an active text selection
        if not cursor.hasSelection():
            return

        # Display confirmation dialog
        reply = QMessageBox.question(
            self,
            "Confirm Deletion",
            "Are you sure you want to delete the selected text?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        # Remove selected text if user confirmed
        if reply == QMessageBox.StandardButton.Yes:
            cursor.removeSelectedText()
            self.escPressed.emit()

    def on_paste_to_input(self, anchor_url: str):
        """Extracts exact value from anchor URL and pastes it into the input field."""
        if anchor_url.startswith("calc:"):
            exact_value = anchor_url.split("calc:")[1]
        else:
            exact_value = anchor_url

        # Paste value directly into the main input line edit
        AppGlobals.input_box.setFocus()
        AppGlobals.input_box.setText(exact_value)
        AppGlobals.input_box.selectAll()

        # Emit signal in case external listeners need to process the event
        self.pasteToInputRequested.emit(exact_value)

    def on_paste_to_input_imag(self, anchor_url: str):
        """Extracts exact value from anchor URL and pastes it into the input imag field."""
        if anchor_url.startswith("calc:"):
            exact_value = anchor_url.split("calc:")[1]
        else:
            exact_value = anchor_url

        # Paste value directly into the main input line edit
        # Paste value directly into the main input line edit
        AppGlobals.input_imag_box.setFocus()
        AppGlobals.input_imag_box.setText(exact_value)
        AppGlobals.input_imag_box.selectAll()

        # Emit signal in case external listeners need to process the event
        self.pasteToInputRequested.emit(exact_value)