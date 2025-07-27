# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convert_from_base_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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

class Ui_ConvertFromBaseDialog(object):
    def setupUi(self, ConvertFromBaseDialog):
        if not ConvertFromBaseDialog.objectName():
            ConvertFromBaseDialog.setObjectName(u"ConvertFromBaseDialog")
        ConvertFromBaseDialog.resize(320, 240)
        self.buttonBox = QDialogButtonBox(ConvertFromBaseDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.number_label = QLabel(ConvertFromBaseDialog)
        self.number_label.setObjectName(u"number_label")
        self.number_label.setGeometry(QRect(10, 12, 91, 16))
        self.number_label.setTextFormat(Qt.TextFormat.AutoText)
        self.numberLineEdit = QLineEdit(ConvertFromBaseDialog)
        self.numberLineEdit.setObjectName(u"numberLineEdit")
        self.numberLineEdit.setGeometry(QRect(100, 10, 211, 21))
        self.label = QLabel(ConvertFromBaseDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 62, 91, 16))
        self.binaryLineEdit = QLineEdit(ConvertFromBaseDialog)
        self.binaryLineEdit.setObjectName(u"binaryLineEdit")
        self.binaryLineEdit.setGeometry(QRect(100, 60, 211, 21))
        self.binaryLineEdit.setReadOnly(True)
        self.label_2 = QLabel(ConvertFromBaseDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 152, 91, 16))
        self.octalLineEdit = QLineEdit(ConvertFromBaseDialog)
        self.octalLineEdit.setObjectName(u"octalLineEdit")
        self.octalLineEdit.setGeometry(QRect(100, 90, 211, 21))
        self.octalLineEdit.setReadOnly(True)
        self.label_3 = QLabel(ConvertFromBaseDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 92, 91, 16))
        self.decimalLineEdit = QLineEdit(ConvertFromBaseDialog)
        self.decimalLineEdit.setObjectName(u"decimalLineEdit")
        self.decimalLineEdit.setGeometry(QRect(100, 120, 211, 21))
        self.decimalLineEdit.setReadOnly(True)
        self.label_4 = QLabel(ConvertFromBaseDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 122, 91, 16))
        self.hexadecimalLineEdit = QLineEdit(ConvertFromBaseDialog)
        self.hexadecimalLineEdit.setObjectName(u"hexadecimalLineEdit")
        self.hexadecimalLineEdit.setGeometry(QRect(100, 150, 211, 21))
        self.hexadecimalLineEdit.setReadOnly(True)
#if QT_CONFIG(shortcut)
        self.number_label.setBuddy(self.numberLineEdit)
        self.label.setBuddy(self.binaryLineEdit)
        self.label_2.setBuddy(self.hexadecimalLineEdit)
        self.label_3.setBuddy(self.octalLineEdit)
        self.label_4.setBuddy(self.decimalLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.numberLineEdit, self.binaryLineEdit)
        QWidget.setTabOrder(self.binaryLineEdit, self.octalLineEdit)
        QWidget.setTabOrder(self.octalLineEdit, self.decimalLineEdit)
        QWidget.setTabOrder(self.decimalLineEdit, self.hexadecimalLineEdit)

        self.retranslateUi(ConvertFromBaseDialog)
        self.buttonBox.accepted.connect(ConvertFromBaseDialog.accept)
        self.buttonBox.rejected.connect(ConvertFromBaseDialog.reject)

        QMetaObject.connectSlotsByName(ConvertFromBaseDialog)
    # setupUi

    def retranslateUi(self, ConvertFromBaseDialog):
        ConvertFromBaseDialog.setWindowTitle(QCoreApplication.translate("ConvertFromBaseDialog", u"Dialog", None))
        self.number_label.setText(QCoreApplication.translate("ConvertFromBaseDialog", u"He&xadecimal:", None))
        self.numberLineEdit.setText(QCoreApplication.translate("ConvertFromBaseDialog", u"0xABCDEF", None))
        self.label.setText(QCoreApplication.translate("ConvertFromBaseDialog", u"B&inary:", None))
        self.label_2.setText(QCoreApplication.translate("ConvertFromBaseDialog", u"&Hexadecimal:", None))
        self.label_3.setText(QCoreApplication.translate("ConvertFromBaseDialog", u"Oc&tal:", None))
        self.label_4.setText(QCoreApplication.translate("ConvertFromBaseDialog", u"D&ecimal", None))
    # retranslateUi

