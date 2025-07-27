from PySide6.QtWidgets import QDialog
from .ui.about_dialog import Ui_AboutDialog
from PySide6.QtCore import QUrl
import webbrowser

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)

        # Disable default handling
        self.ui.textBrowser.setOpenExternalLinks(False)

        # Connect signal to instance method
        self.ui.textBrowser.anchorClicked.connect(self.handle_link_clicked)

    def handle_link_clicked(self, url: QUrl):
        webbrowser.open(url.toString())
        
        # Prevent QTextBrowser from trying to load it
        self.ui.textBrowser.setSource(QUrl())
