import sys
from PySide6.QtWidgets import QApplication, QDialog
from ui.comment_dialog_box import Ui_CommentDialog  # Import your generated UI class

class CommentDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CommentDialog()
        self.ui.setupUi(self)

        # Set initial focus to lineEdit
        self.ui.lineEdit.setFocus()

    def get_comment(self):
        return self.ui.lineEdit.text()