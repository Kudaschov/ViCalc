# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'linear_y_from_x_dialog.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_linear_y_from_x_dialog(object):
    def setupUi(self, linear_y_from_x_dialog):
        if not linear_y_from_x_dialog.objectName():
            linear_y_from_x_dialog.setObjectName(u"linear_y_from_x_dialog")
        linear_y_from_x_dialog.resize(320, 240)
        self.buttonBox = QDialogButtonBox(linear_y_from_x_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(linear_y_from_x_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 42, 91, 16))
        self.aLineEdit = QLineEdit(linear_y_from_x_dialog)
        self.aLineEdit.setObjectName(u"aLineEdit")
        self.aLineEdit.setGeometry(QRect(110, 40, 120, 21))
        self.label_2 = QLabel(linear_y_from_x_dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 72, 91, 16))
        self.bLineEdit = QLineEdit(linear_y_from_x_dialog)
        self.bLineEdit.setObjectName(u"bLineEdit")
        self.bLineEdit.setGeometry(QRect(110, 70, 120, 21))
        self.fromTwoPointsPushButton = QPushButton(linear_y_from_x_dialog)
        self.fromTwoPointsPushButton.setObjectName(u"fromTwoPointsPushButton")
        self.fromTwoPointsPushButton.setGeometry(QRect(10, 10, 301, 24))
        self.label_3 = QLabel(linear_y_from_x_dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 102, 49, 16))
        self.xLineEdit = QLineEdit(linear_y_from_x_dialog)
        self.xLineEdit.setObjectName(u"xLineEdit")
        self.xLineEdit.setGeometry(QRect(110, 100, 120, 21))
        self.label_4 = QLabel(linear_y_from_x_dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 132, 49, 16))
        self.yLineEdit = QLineEdit(linear_y_from_x_dialog)
        self.yLineEdit.setObjectName(u"yLineEdit")
        self.yLineEdit.setGeometry(QRect(110, 130, 120, 21))
        self.yLineEdit.setReadOnly(True)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.aLineEdit)
        self.label_2.setBuddy(self.bLineEdit)
        self.label_3.setBuddy(self.xLineEdit)
        self.label_4.setBuddy(self.yLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.fromTwoPointsPushButton, self.aLineEdit)
        QWidget.setTabOrder(self.aLineEdit, self.bLineEdit)
        QWidget.setTabOrder(self.bLineEdit, self.xLineEdit)
        QWidget.setTabOrder(self.xLineEdit, self.yLineEdit)

        self.retranslateUi(linear_y_from_x_dialog)
        self.buttonBox.accepted.connect(linear_y_from_x_dialog.accept)
        self.buttonBox.rejected.connect(linear_y_from_x_dialog.reject)

        QMetaObject.connectSlotsByName(linear_y_from_x_dialog)
    # setupUi

    def retranslateUi(self, linear_y_from_x_dialog):
        linear_y_from_x_dialog.setWindowTitle(QCoreApplication.translate("linear_y_from_x_dialog", u"Calculate Y from Linear Function", None))
        self.label.setText(QCoreApplication.translate("linear_y_from_x_dialog", u"Slope (&a)", None))
        self.label_2.setText(QCoreApplication.translate("linear_y_from_x_dialog", u"Intercept (&b)", None))
        self.fromTwoPointsPushButton.setText(QCoreApplication.translate("linear_y_from_x_dialog", u"&Slope and Intercept from Two Points...", None))
        self.label_3.setText(QCoreApplication.translate("linear_y_from_x_dialog", u"&x", None))
        self.label_4.setText(QCoreApplication.translate("linear_y_from_x_dialog", u"&y", None))
    # retranslateUi

