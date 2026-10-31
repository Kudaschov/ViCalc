# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_interest_dlg.ui'
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
    QGroupBox, QLabel, QRadioButton, QSizePolicy,
    QWidget)

from .dot_line_edit import DotLineEdit

class Ui_SimpleInterestDialog(object):
    def setupUi(self, SimpleInterestDialog):
        if not SimpleInterestDialog.objectName():
            SimpleInterestDialog.setObjectName(u"SimpleInterestDialog")
        SimpleInterestDialog.resize(392, 320)
        self.buttonBox = QDialogButtonBox(SimpleInterestDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 280, 371, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.groupBox = QGroupBox(SimpleInterestDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 191, 80))
        self.groupBox.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.days360RadioButton = QRadioButton(self.groupBox)
        self.days360RadioButton.setObjectName(u"days360RadioButton")
        self.days360RadioButton.setGeometry(QRect(20, 30, 89, 20))
        self.days365RadioButton = QRadioButton(self.groupBox)
        self.days365RadioButton.setObjectName(u"days365RadioButton")
        self.days365RadioButton.setGeometry(QRect(20, 50, 89, 20))
        self.label = QLabel(SimpleInterestDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 102, 211, 16))
        self.daysLineEdit = DotLineEdit(SimpleInterestDialog)
        self.daysLineEdit.setObjectName(u"daysLineEdit")
        self.daysLineEdit.setGeometry(QRect(230, 100, 141, 21))
        self.label_2 = QLabel(SimpleInterestDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 132, 211, 16))
        self.annualRatePctLineEdit = DotLineEdit(SimpleInterestDialog)
        self.annualRatePctLineEdit.setObjectName(u"annualRatePctLineEdit")
        self.annualRatePctLineEdit.setGeometry(QRect(230, 130, 141, 21))
        self.label_3 = QLabel(SimpleInterestDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 162, 211, 16))
        self.pvLineEdit = DotLineEdit(SimpleInterestDialog)
        self.pvLineEdit.setObjectName(u"pvLineEdit")
        self.pvLineEdit.setGeometry(QRect(230, 160, 141, 21))
        self.groupBox_2 = QGroupBox(SimpleInterestDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 190, 371, 81))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 22, 191, 16))
        self.siLineEdit = DotLineEdit(self.groupBox_2)
        self.siLineEdit.setObjectName(u"siLineEdit")
        self.siLineEdit.setGeometry(QRect(220, 20, 141, 21))
        self.siLineEdit.setStyleSheet(u"QLineEdit:read-only {\n"
"    background-color: #f0f0f0;\n"
"    color: #333333;\n"
"}")
        self.siLineEdit.setReadOnly(True)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 52, 191, 16))
        self.sfvLineEdit = DotLineEdit(self.groupBox_2)
        self.sfvLineEdit.setObjectName(u"sfvLineEdit")
        self.sfvLineEdit.setGeometry(QRect(220, 50, 141, 21))
        self.sfvLineEdit.setStyleSheet(u"QLineEdit:read-only {\n"
"    background-color: #f0f0f0;\n"
"    color: #333333;\n"
"}")
        self.sfvLineEdit.setReadOnly(True)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.daysLineEdit)
        self.label_2.setBuddy(self.annualRatePctLineEdit)
        self.label_3.setBuddy(self.pvLineEdit)
        self.label_4.setBuddy(self.siLineEdit)
        self.label_5.setBuddy(self.sfvLineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(SimpleInterestDialog)
        self.buttonBox.accepted.connect(SimpleInterestDialog.accept)
        self.buttonBox.rejected.connect(SimpleInterestDialog.reject)

        QMetaObject.connectSlotsByName(SimpleInterestDialog)
    # setupUi

    def retranslateUi(self, SimpleInterestDialog):
        SimpleInterestDialog.setWindowTitle(QCoreApplication.translate("SimpleInterestDialog", u"Simple Interest", None))
        self.groupBox.setTitle(QCoreApplication.translate("SimpleInterestDialog", u"Days in Year", None))
        self.days360RadioButton.setText(QCoreApplication.translate("SimpleInterestDialog", u"&360", None))
        self.days365RadioButton.setText(QCoreApplication.translate("SimpleInterestDialog", u"36&5", None))
        self.label.setText(QCoreApplication.translate("SimpleInterestDialog", u"Interest Period [&Days]", None))
        self.label_2.setText(QCoreApplication.translate("SimpleInterestDialog", u"&Annual Interest Rate [%]", None))
        self.label_3.setText(QCoreApplication.translate("SimpleInterestDialog", u"Present &Value (PV)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SimpleInterestDialog", u"Results", None))
        self.label_4.setText(QCoreApplication.translate("SimpleInterestDialog", u"&Simple Interest (SI)", None))
        self.label_5.setText(QCoreApplication.translate("SimpleInterestDialog", u"&Future Value (FV)", None))
    # retranslateUi

