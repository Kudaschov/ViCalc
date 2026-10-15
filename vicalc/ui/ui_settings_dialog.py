# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QWidget)

from .dot_line_edit import DotLineEdit

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(320, 78)
        SettingsDialog.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 40, 301, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.taxRateLabel = QLabel(SettingsDialog)
        self.taxRateLabel.setObjectName(u"taxRateLabel")
        self.taxRateLabel.setGeometry(QRect(10, 12, 91, 16))
        self.taxRateLabel.setTextFormat(Qt.TextFormat.AutoText)
        self.taxRateLineEdit = DotLineEdit(SettingsDialog)
        self.taxRateLineEdit.setObjectName(u"taxRateLineEdit")
        self.taxRateLineEdit.setGeometry(QRect(140, 10, 171, 21))
#if QT_CONFIG(shortcut)
        self.taxRateLabel.setBuddy(self.taxRateLineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.taxRateLabel.setText(QCoreApplication.translate("SettingsDialog", u"&Tax rate [%]", None))
        self.taxRateLineEdit.setText(QCoreApplication.translate("SettingsDialog", u"- - -", None))
    # retranslateUi

