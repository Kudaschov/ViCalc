# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'num_format_dialog.ui'
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
    QGroupBox, QLabel, QRadioButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_FormatDialog(object):
    def setupUi(self, FormatDialog):
        if not FormatDialog.objectName():
            FormatDialog.setObjectName(u"FormatDialog")
        FormatDialog.resize(320, 439)
        self.buttonBox = QDialogButtonBox(FormatDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 400, 301, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.groupBox = QGroupBox(FormatDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 301, 211))
        self.precisionSpinBox = QSpinBox(self.groupBox)
        self.precisionSpinBox.setObjectName(u"precisionSpinBox")
        self.precisionSpinBox.setGeometry(QRect(90, 180, 42, 22))
        self.precisionSpinBox.setMinimum(0)
        self.precisionSpinBox.setMaximum(16)
        self.precisionSpinBox.setValue(5)
        self.engRadioButton = QRadioButton(self.groupBox)
        self.engRadioButton.setObjectName(u"engRadioButton")
        self.engRadioButton.setGeometry(QRect(20, 150, 89, 20))
        self.sciRadioButton = QRadioButton(self.groupBox)
        self.sciRadioButton.setObjectName(u"sciRadioButton")
        self.sciRadioButton.setGeometry(QRect(20, 120, 89, 20))
        self.generalRadioButton = QRadioButton(self.groupBox)
        self.generalRadioButton.setObjectName(u"generalRadioButton")
        self.generalRadioButton.setGeometry(QRect(20, 60, 89, 20))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 183, 71, 16))
        self.fixRadioButton = QRadioButton(self.groupBox)
        self.fixRadioButton.setObjectName(u"fixRadioButton")
        self.fixRadioButton.setGeometry(QRect(20, 90, 89, 20))
        self.normRadioButton = QRadioButton(self.groupBox)
        self.normRadioButton.setObjectName(u"normRadioButton")
        self.normRadioButton.setGeometry(QRect(20, 30, 89, 20))
        self.groupBox_2 = QGroupBox(FormatDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 240, 301, 151))
        self.groupBox_2.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.binaryRadioButton = QRadioButton(self.groupBox_2)
        self.binaryRadioButton.setObjectName(u"binaryRadioButton")
        self.binaryRadioButton.setGeometry(QRect(20, 30, 89, 20))
        self.octalRadioButton = QRadioButton(self.groupBox_2)
        self.octalRadioButton.setObjectName(u"octalRadioButton")
        self.octalRadioButton.setGeometry(QRect(20, 60, 89, 20))
        self.decimalRadioButton = QRadioButton(self.groupBox_2)
        self.decimalRadioButton.setObjectName(u"decimalRadioButton")
        self.decimalRadioButton.setGeometry(QRect(20, 90, 89, 20))
        self.hexadecimalRadioButton = QRadioButton(self.groupBox_2)
        self.hexadecimalRadioButton.setObjectName(u"hexadecimalRadioButton")
        self.hexadecimalRadioButton.setGeometry(QRect(20, 120, 89, 20))
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.precisionSpinBox)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(FormatDialog)
        self.buttonBox.accepted.connect(FormatDialog.accept)
        self.buttonBox.rejected.connect(FormatDialog.reject)

        QMetaObject.connectSlotsByName(FormatDialog)
    # setupUi

    def retranslateUi(self, FormatDialog):
        FormatDialog.setWindowTitle(QCoreApplication.translate("FormatDialog", u"Numeric Format in History", None))
        self.groupBox.setTitle(QCoreApplication.translate("FormatDialog", u"Numeric Format", None))
        self.engRadioButton.setText(QCoreApplication.translate("FormatDialog", u"&Engineering", None))
        self.sciRadioButton.setText(QCoreApplication.translate("FormatDialog", u"&Scientific", None))
        self.generalRadioButton.setText(QCoreApplication.translate("FormatDialog", u"&General", None))
        self.label.setText(QCoreApplication.translate("FormatDialog", u"&Precision:", None))
        self.fixRadioButton.setText(QCoreApplication.translate("FormatDialog", u"&Fixed point", None))
        self.normRadioButton.setText(QCoreApplication.translate("FormatDialog", u"&Normal", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("FormatDialog", u"Show Logical Operations in History as", None))
        self.binaryRadioButton.setText(QCoreApplication.translate("FormatDialog", u"&Binary", None))
        self.octalRadioButton.setText(QCoreApplication.translate("FormatDialog", u"&Octal", None))
        self.decimalRadioButton.setText(QCoreApplication.translate("FormatDialog", u"&Decimal", None))
        self.hexadecimalRadioButton.setText(QCoreApplication.translate("FormatDialog", u"He&xadecimal", None))
    # retranslateUi

