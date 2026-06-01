# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'linear_system_dialog.ui'
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

class Ui_linear_system_dialog(object):
    def setupUi(self, linear_system_dialog):
        if not linear_system_dialog.objectName():
            linear_system_dialog.setObjectName(u"linear_system_dialog")
        linear_system_dialog.resize(598, 213)
        self.buttonBox = QDialogButtonBox(linear_system_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(260, 170, 321, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(linear_system_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 22, 41, 16))
        self.a1LineEdit = QLineEdit(linear_system_dialog)
        self.a1LineEdit.setObjectName(u"a1LineEdit")
        self.a1LineEdit.setGeometry(QRect(40, 20, 121, 21))
        self.label_2 = QLabel(linear_system_dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 22, 41, 16))
        self.b1LineEdit = QLineEdit(linear_system_dialog)
        self.b1LineEdit.setObjectName(u"b1LineEdit")
        self.b1LineEdit.setGeometry(QRect(220, 20, 121, 21))
        self.label_3 = QLabel(linear_system_dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(430, 22, 41, 16))
        self.c1LineEdit = QLineEdit(linear_system_dialog)
        self.c1LineEdit.setObjectName(u"c1LineEdit")
        self.c1LineEdit.setGeometry(QRect(460, 20, 121, 21))
        self.label_4 = QLabel(linear_system_dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 52, 41, 16))
        self.label_5 = QLabel(linear_system_dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 52, 41, 16))
        self.b2LineEdit = QLineEdit(linear_system_dialog)
        self.b2LineEdit.setObjectName(u"b2LineEdit")
        self.b2LineEdit.setGeometry(QRect(220, 50, 121, 21))
        self.label_6 = QLabel(linear_system_dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(430, 52, 41, 16))
        self.a2LineEdit = QLineEdit(linear_system_dialog)
        self.a2LineEdit.setObjectName(u"a2LineEdit")
        self.a2LineEdit.setGeometry(QRect(40, 50, 121, 21))
        self.c2LineEdit = QLineEdit(linear_system_dialog)
        self.c2LineEdit.setObjectName(u"c2LineEdit")
        self.c2LineEdit.setGeometry(QRect(460, 50, 121, 21))
        self.label_7 = QLabel(linear_system_dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 142, 41, 16))
        self.xLineEdit = QLineEdit(linear_system_dialog)
        self.xLineEdit.setObjectName(u"xLineEdit")
        self.xLineEdit.setGeometry(QRect(130, 140, 121, 21))
        self.xLineEdit.setReadOnly(True)
        self.label_8 = QLabel(linear_system_dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 172, 41, 16))
        self.yLineEdit = QLineEdit(linear_system_dialog)
        self.yLineEdit.setObjectName(u"yLineEdit")
        self.yLineEdit.setGeometry(QRect(130, 170, 121, 21))
        self.yLineEdit.setReadOnly(True)
        self.label_9 = QLabel(linear_system_dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 110, 101, 16))
        self.DLineEdit = QLineEdit(linear_system_dialog)
        self.DLineEdit.setObjectName(u"DLineEdit")
        self.DLineEdit.setGeometry(QRect(130, 110, 121, 21))
        self.DLineEdit.setReadOnly(True)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.a1LineEdit)
        self.label_2.setBuddy(self.b1LineEdit)
        self.label_3.setBuddy(self.c1LineEdit)
        self.label_4.setBuddy(self.a2LineEdit)
        self.label_5.setBuddy(self.b2LineEdit)
        self.label_6.setBuddy(self.c2LineEdit)
        self.label_7.setBuddy(self.xLineEdit)
        self.label_8.setBuddy(self.yLineEdit)
        self.label_9.setBuddy(self.DLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.a1LineEdit, self.b1LineEdit)
        QWidget.setTabOrder(self.b1LineEdit, self.c1LineEdit)
        QWidget.setTabOrder(self.c1LineEdit, self.a2LineEdit)
        QWidget.setTabOrder(self.a2LineEdit, self.b2LineEdit)
        QWidget.setTabOrder(self.b2LineEdit, self.c2LineEdit)
        QWidget.setTabOrder(self.c2LineEdit, self.DLineEdit)
        QWidget.setTabOrder(self.DLineEdit, self.xLineEdit)
        QWidget.setTabOrder(self.xLineEdit, self.yLineEdit)

        self.retranslateUi(linear_system_dialog)
        self.buttonBox.accepted.connect(linear_system_dialog.accept)
        self.buttonBox.rejected.connect(linear_system_dialog.reject)

        QMetaObject.connectSlotsByName(linear_system_dialog)
    # setupUi

    def retranslateUi(self, linear_system_dialog):
        linear_system_dialog.setWindowTitle(QCoreApplication.translate("linear_system_dialog", u"System of Linear Equations with Two Unknowns", None))
        self.label.setText(QCoreApplication.translate("linear_system_dialog", u"&a1", None))
        self.label_2.setText(QCoreApplication.translate("linear_system_dialog", u"&b1", None))
        self.label_3.setText(QCoreApplication.translate("linear_system_dialog", u"c&1", None))
        self.label_4.setText(QCoreApplication.translate("linear_system_dialog", u"a&2", None))
        self.label_5.setText(QCoreApplication.translate("linear_system_dialog", u"b2", None))
        self.label_6.setText(QCoreApplication.translate("linear_system_dialog", u"&c2", None))
        self.label_7.setText(QCoreApplication.translate("linear_system_dialog", u"&x", None))
        self.label_8.setText(QCoreApplication.translate("linear_system_dialog", u"&y", None))
        self.label_9.setText(QCoreApplication.translate("linear_system_dialog", u"&Discriminant (D)", None))
    # retranslateUi

