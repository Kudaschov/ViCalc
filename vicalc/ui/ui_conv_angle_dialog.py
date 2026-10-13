# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'conv_angle_dialog.ui'
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
    QLabel, QLineEdit, QSizePolicy, QWidget)

from .dot_line_edit import DotLineEdit

class Ui_ConvAngleDialog(object):
    def setupUi(self, ConvAngleDialog):
        if not ConvAngleDialog.objectName():
            ConvAngleDialog.setObjectName(u"ConvAngleDialog")
        ConvAngleDialog.resize(320, 200)
        ConvAngleDialog.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.buttonBox = QDialogButtonBox(ConvAngleDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 160, 301, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.number_label = QLabel(ConvAngleDialog)
        self.number_label.setObjectName(u"number_label")
        self.number_label.setGeometry(QRect(10, 12, 91, 16))
        self.number_label.setTextFormat(Qt.TextFormat.AutoText)
        self.numberLineEdit = DotLineEdit(ConvAngleDialog)
        self.numberLineEdit.setObjectName(u"numberLineEdit")
        self.numberLineEdit.setGeometry(QRect(100, 10, 211, 21))
        self.degLabel = QLabel(ConvAngleDialog)
        self.degLabel.setObjectName(u"degLabel")
        self.degLabel.setGeometry(QRect(10, 62, 91, 16))
        self.degLineEdit = QLineEdit(ConvAngleDialog)
        self.degLineEdit.setObjectName(u"degLineEdit")
        self.degLineEdit.setGeometry(QRect(100, 60, 211, 21))
        self.degLineEdit.setStyleSheet(u"QLineEdit:read-only {\n"
"    background-color: #f0f0f0;\n"
"    color: #333333;\n"
"}")
        self.degLineEdit.setReadOnly(True)
        self.radLineEdit = QLineEdit(ConvAngleDialog)
        self.radLineEdit.setObjectName(u"radLineEdit")
        self.radLineEdit.setGeometry(QRect(100, 90, 211, 21))
        self.radLineEdit.setStyleSheet(u"QLineEdit:read-only {\n"
"    background-color: #f0f0f0;\n"
"    color: #333333;\n"
"}")
        self.radLineEdit.setReadOnly(True)
        self.radLabel = QLabel(ConvAngleDialog)
        self.radLabel.setObjectName(u"radLabel")
        self.radLabel.setGeometry(QRect(10, 92, 91, 16))
        self.graLineEdit = QLineEdit(ConvAngleDialog)
        self.graLineEdit.setObjectName(u"graLineEdit")
        self.graLineEdit.setGeometry(QRect(100, 120, 211, 21))
        self.graLineEdit.setStyleSheet(u"QLineEdit:read-only {\n"
"    background-color: #f0f0f0;\n"
"    color: #333333;\n"
"}")
        self.graLineEdit.setReadOnly(True)
        self.graLabel = QLabel(ConvAngleDialog)
        self.graLabel.setObjectName(u"graLabel")
        self.graLabel.setGeometry(QRect(10, 122, 91, 16))
#if QT_CONFIG(shortcut)
        self.number_label.setBuddy(self.numberLineEdit)
        self.degLabel.setBuddy(self.degLineEdit)
        self.radLabel.setBuddy(self.radLineEdit)
        self.graLabel.setBuddy(self.graLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.numberLineEdit, self.degLineEdit)
        QWidget.setTabOrder(self.degLineEdit, self.radLineEdit)
        QWidget.setTabOrder(self.radLineEdit, self.graLineEdit)

        self.retranslateUi(ConvAngleDialog)
        self.buttonBox.accepted.connect(ConvAngleDialog.accept)
        self.buttonBox.rejected.connect(ConvAngleDialog.reject)

        QMetaObject.connectSlotsByName(ConvAngleDialog)
    # setupUi

    def retranslateUi(self, ConvAngleDialog):
        ConvAngleDialog.setWindowTitle(QCoreApplication.translate("ConvAngleDialog", u"Angle Input", None))
        self.number_label.setText(QCoreApplication.translate("ConvAngleDialog", u"&Angle [\u00b0]:", None))
        self.numberLineEdit.setText(QCoreApplication.translate("ConvAngleDialog", u"0xABCDEF", None))
        self.degLabel.setText(QCoreApplication.translate("ConvAngleDialog", u"&DEG (\u00b0):", None))
        self.radLabel.setText(QCoreApplication.translate("ConvAngleDialog", u"&RAD:", None))
        self.graLabel.setText(QCoreApplication.translate("ConvAngleDialog", u"&GRA:", None))
    # retranslateUi

