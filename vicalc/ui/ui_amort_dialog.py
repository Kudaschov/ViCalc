# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'amort_dialog.ui'
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
    QGroupBox, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

from .dot_line_edit import DotLineEdit

class Ui_amortDialog(object):
    def setupUi(self, amortDialog):
        if not amortDialog.objectName():
            amortDialog.setObjectName(u"amortDialog")
        amortDialog.resize(401, 549)
        self.buttonBox = QDialogButtonBox(amortDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 510, 381, 32))
        self.buttonBox.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.groupBox = QGroupBox(amortDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 191, 71))
        self.groupBox.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.beginRadioButton = QRadioButton(self.groupBox)
        self.beginRadioButton.setObjectName(u"beginRadioButton")
        self.beginRadioButton.setGeometry(QRect(20, 20, 89, 20))
        self.endRadioButton = QRadioButton(self.groupBox)
        self.endRadioButton.setObjectName(u"endRadioButton")
        self.endRadioButton.setGeometry(QRect(20, 40, 89, 20))
        self.label = QLabel(amortDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 92, 211, 16))
        self.p_yLineEdit = DotLineEdit(amortDialog)
        self.p_yLineEdit.setObjectName(u"p_yLineEdit")
        self.p_yLineEdit.setGeometry(QRect(250, 90, 141, 21))
        self.label_2 = QLabel(amortDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 122, 231, 16))
        self.c_yLineEdit = DotLineEdit(amortDialog)
        self.c_yLineEdit.setObjectName(u"c_yLineEdit")
        self.c_yLineEdit.setGeometry(QRect(250, 120, 141, 21))
        self.annualRatePctLineEdit = DotLineEdit(amortDialog)
        self.annualRatePctLineEdit.setObjectName(u"annualRatePctLineEdit")
        self.annualRatePctLineEdit.setGeometry(QRect(250, 240, 141, 21))
        self.label_3 = QLabel(amortDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 242, 211, 16))
        self.pvLineEdit = DotLineEdit(amortDialog)
        self.pvLineEdit.setObjectName(u"pvLineEdit")
        self.pvLineEdit.setGeometry(QRect(250, 270, 141, 21))
        self.label_4 = QLabel(amortDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 272, 211, 16))
        self.label_5 = QLabel(amortDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 302, 211, 16))
        self.pmtLineEdit = DotLineEdit(amortDialog)
        self.pmtLineEdit.setObjectName(u"pmtLineEdit")
        self.pmtLineEdit.setGeometry(QRect(250, 300, 141, 21))
        self.pmtLineEdit.setStyleSheet(u"QLineEdit:read-only {\n"
"    background-color: #f0f0f0;\n"
"    color: #333333;\n"
"}")
        self.pmtLineEdit.setReadOnly(True)
        self.p1LineEdit = DotLineEdit(amortDialog)
        self.p1LineEdit.setObjectName(u"p1LineEdit")
        self.p1LineEdit.setGeometry(QRect(250, 180, 141, 21))
        self.label_6 = QLabel(amortDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 182, 211, 16))
        self.label_7 = QLabel(amortDialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 212, 231, 16))
        self.p2LineEdit = DotLineEdit(amortDialog)
        self.p2LineEdit.setObjectName(u"p2LineEdit")
        self.p2LineEdit.setGeometry(QRect(250, 210, 141, 21))
        self.label_8 = QLabel(amortDialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 452, 211, 16))
        self.prnLineEdit = DotLineEdit(amortDialog)
        self.prnLineEdit.setObjectName(u"prnLineEdit")
        self.prnLineEdit.setGeometry(QRect(250, 450, 141, 21))
        self.prnLineEdit.setStyleSheet(u"QLineEdit:read-only {\n"
"    background-color: #f0f0f0;\n"
"    color: #333333;\n"
"}")
        self.prnLineEdit.setReadOnly(True)
        self.label_9 = QLabel(amortDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 392, 211, 16))
        self.prnP1LineEdit = DotLineEdit(amortDialog)
        self.prnP1LineEdit.setObjectName(u"prnP1LineEdit")
        self.prnP1LineEdit.setGeometry(QRect(250, 390, 141, 21))
        self.prnP1LineEdit.setStyleSheet(u"QLineEdit:read-only {\n"
"    background-color: #f0f0f0;\n"
"    color: #333333;\n"
"}")
        self.prnP1LineEdit.setReadOnly(True)
        self.label_10 = QLabel(amortDialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 332, 211, 16))
        self.label_11 = QLabel(amortDialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 422, 211, 16))
        self.balLineEdit = DotLineEdit(amortDialog)
        self.balLineEdit.setObjectName(u"balLineEdit")
        self.balLineEdit.setGeometry(QRect(250, 330, 141, 21))
        self.balLineEdit.setStyleSheet(u"QLineEdit:read-only {\n"
"    background-color: #f0f0f0;\n"
"    color: #333333;\n"
"}")
        self.balLineEdit.setReadOnly(True)
        self.intLineEdit = DotLineEdit(amortDialog)
        self.intLineEdit.setObjectName(u"intLineEdit")
        self.intLineEdit.setGeometry(QRect(250, 420, 141, 21))
        self.intLineEdit.setStyleSheet(u"QLineEdit:read-only {\n"
"    background-color: #f0f0f0;\n"
"    color: #333333;\n"
"}")
        self.intLineEdit.setReadOnly(True)
        self.intP1LineEdit = DotLineEdit(amortDialog)
        self.intP1LineEdit.setObjectName(u"intP1LineEdit")
        self.intP1LineEdit.setGeometry(QRect(250, 360, 141, 21))
        self.intP1LineEdit.setStyleSheet(u"QLineEdit:read-only {\n"
"    background-color: #f0f0f0;\n"
"    color: #333333;\n"
"}")
        self.intP1LineEdit.setReadOnly(True)
        self.label_12 = QLabel(amortDialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 362, 231, 16))
        self.historyPushButton = QPushButton(amortDialog)
        self.historyPushButton.setObjectName(u"historyPushButton")
        self.historyPushButton.setGeometry(QRect(120, 480, 101, 24))
        self.solvePushButton = QPushButton(amortDialog)
        self.solvePushButton.setObjectName(u"solvePushButton")
        self.solvePushButton.setGeometry(QRect(10, 480, 101, 24))
        self.solvePushButton.setAutoDefault(False)
        self.nLineEdit = DotLineEdit(amortDialog)
        self.nLineEdit.setObjectName(u"nLineEdit")
        self.nLineEdit.setGeometry(QRect(250, 150, 141, 21))
        self.label_13 = QLabel(amortDialog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 152, 211, 16))
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.p_yLineEdit)
        self.label_2.setBuddy(self.c_yLineEdit)
        self.label_3.setBuddy(self.annualRatePctLineEdit)
        self.label_4.setBuddy(self.pvLineEdit)
        self.label_5.setBuddy(self.pmtLineEdit)
        self.label_6.setBuddy(self.p1LineEdit)
        self.label_7.setBuddy(self.p2LineEdit)
        self.label_8.setBuddy(self.prnLineEdit)
        self.label_9.setBuddy(self.prnP1LineEdit)
        self.label_10.setBuddy(self.balLineEdit)
        self.label_11.setBuddy(self.intLineEdit)
        self.label_12.setBuddy(self.intP1LineEdit)
        self.label_13.setBuddy(self.nLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.beginRadioButton, self.endRadioButton)
        QWidget.setTabOrder(self.endRadioButton, self.p_yLineEdit)
        QWidget.setTabOrder(self.p_yLineEdit, self.c_yLineEdit)
        QWidget.setTabOrder(self.c_yLineEdit, self.nLineEdit)
        QWidget.setTabOrder(self.nLineEdit, self.p1LineEdit)
        QWidget.setTabOrder(self.p1LineEdit, self.p2LineEdit)
        QWidget.setTabOrder(self.p2LineEdit, self.annualRatePctLineEdit)
        QWidget.setTabOrder(self.annualRatePctLineEdit, self.pvLineEdit)
        QWidget.setTabOrder(self.pvLineEdit, self.pmtLineEdit)
        QWidget.setTabOrder(self.pmtLineEdit, self.balLineEdit)
        QWidget.setTabOrder(self.balLineEdit, self.intP1LineEdit)
        QWidget.setTabOrder(self.intP1LineEdit, self.prnP1LineEdit)
        QWidget.setTabOrder(self.prnP1LineEdit, self.intLineEdit)
        QWidget.setTabOrder(self.intLineEdit, self.prnLineEdit)
        QWidget.setTabOrder(self.prnLineEdit, self.solvePushButton)
        QWidget.setTabOrder(self.solvePushButton, self.historyPushButton)

        self.retranslateUi(amortDialog)
        self.buttonBox.accepted.connect(amortDialog.accept)
        self.buttonBox.rejected.connect(amortDialog.reject)

        QMetaObject.connectSlotsByName(amortDialog)
    # setupUi

    def retranslateUi(self, amortDialog):
        amortDialog.setWindowTitle(QCoreApplication.translate("amortDialog", u"Amortization", None))
        self.groupBox.setTitle(QCoreApplication.translate("amortDialog", u"Payment Period", None))
        self.beginRadioButton.setText(QCoreApplication.translate("amortDialog", u"&Begin", None))
        self.endRadioButton.setText(QCoreApplication.translate("amortDialog", u"En&d", None))
        self.label.setText(QCoreApplication.translate("amortDialog", u"N&umber of Annual Payments (P/Y)", None))
        self.label_2.setText(QCoreApplication.translate("amortDialog", u"Number of Annual &Compoundings (C/Y)", None))
        self.label_3.setText(QCoreApplication.translate("amortDialog", u"Annual &Interest Rate (I/Y) [%]", None))
        self.label_4.setText(QCoreApplication.translate("amortDialog", u"Present Value (&PV)", None))
        self.label_5.setText(QCoreApplication.translate("amortDialog", u"Payment Amount (P&MT)", None))
        self.label_6.setText(QCoreApplication.translate("amortDialog", u"Starting payment (P&1)", None))
        self.label_7.setText(QCoreApplication.translate("amortDialog", u"Ending payment (P&2)", None))
        self.label_8.setText(QCoreApplication.translate("amortDialog", u"Princip&al paid (PRN)", None))
        self.label_9.setText(QCoreApplication.translate("amortDialog", u"P&rincipal paid of payment P1", None))
        self.label_10.setText(QCoreApplication.translate("amortDialog", u"Ba&lance (BAL)", None))
        self.label_11.setText(QCoreApplication.translate("amortDialog", u"Int&erest paid (INT)", None))
        self.label_12.setText(QCoreApplication.translate("amortDialog", u"In&terest paid of payment P1", None))
        self.historyPushButton.setText(QCoreApplication.translate("amortDialog", u"Add to &History", None))
        self.solvePushButton.setText(QCoreApplication.translate("amortDialog", u"&Solve", None))
        self.label_13.setText(QCoreApplication.translate("amortDialog", u"Number of Payments (&N)", None))
    # retranslateUi

