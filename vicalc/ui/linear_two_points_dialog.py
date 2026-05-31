# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'linear_two_points_dialog.ui'
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

class Ui_linear_two_points_dialog(object):
    def setupUi(self, linear_two_points_dialog):
        if not linear_two_points_dialog.objectName():
            linear_two_points_dialog.setObjectName(u"linear_two_points_dialog")
        linear_two_points_dialog.resize(330, 240)
        linear_two_points_dialog.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.buttonBox = QDialogButtonBox(linear_two_points_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(20, 200, 301, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(linear_two_points_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 12, 49, 16))
        self.x0LineEdit = QLineEdit(linear_two_points_dialog)
        self.x0LineEdit.setObjectName(u"x0LineEdit")
        self.x0LineEdit.setGeometry(QRect(30, 10, 120, 21))
        self.label_2 = QLabel(linear_two_points_dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 12, 49, 16))
        self.y0LineEdit = QLineEdit(linear_two_points_dialog)
        self.y0LineEdit.setObjectName(u"y0LineEdit")
        self.y0LineEdit.setGeometry(QRect(200, 10, 120, 21))
        self.label_3 = QLabel(linear_two_points_dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 42, 49, 16))
        self.x1LineEdit = QLineEdit(linear_two_points_dialog)
        self.x1LineEdit.setObjectName(u"x1LineEdit")
        self.x1LineEdit.setGeometry(QRect(30, 40, 120, 21))
        self.label_4 = QLabel(linear_two_points_dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 42, 49, 16))
        self.y1LineEdit = QLineEdit(linear_two_points_dialog)
        self.y1LineEdit.setObjectName(u"y1LineEdit")
        self.y1LineEdit.setGeometry(QRect(200, 40, 120, 21))
        self.aLabel = QLabel(linear_two_points_dialog)
        self.aLabel.setObjectName(u"aLabel")
        self.aLabel.setGeometry(QRect(10, 102, 81, 16))
        self.aLineEdit = QLineEdit(linear_two_points_dialog)
        self.aLineEdit.setObjectName(u"aLineEdit")
        self.aLineEdit.setGeometry(QRect(120, 100, 120, 21))
        self.aLineEdit.setReadOnly(True)
        self.label_6 = QLabel(linear_two_points_dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 132, 81, 16))
        self.bLineEdit = QLineEdit(linear_two_points_dialog)
        self.bLineEdit.setObjectName(u"bLineEdit")
        self.bLineEdit.setGeometry(QRect(120, 130, 120, 21))
        self.bLineEdit.setReadOnly(True)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.x0LineEdit)
        self.label_2.setBuddy(self.y0LineEdit)
        self.label_3.setBuddy(self.x1LineEdit)
        self.label_4.setBuddy(self.y1LineEdit)
        self.aLabel.setBuddy(self.aLineEdit)
        self.label_6.setBuddy(self.bLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.x0LineEdit, self.y0LineEdit)
        QWidget.setTabOrder(self.y0LineEdit, self.x1LineEdit)
        QWidget.setTabOrder(self.x1LineEdit, self.y1LineEdit)
        QWidget.setTabOrder(self.y1LineEdit, self.aLineEdit)
        QWidget.setTabOrder(self.aLineEdit, self.bLineEdit)

        self.retranslateUi(linear_two_points_dialog)
        self.buttonBox.accepted.connect(linear_two_points_dialog.accept)
        self.buttonBox.rejected.connect(linear_two_points_dialog.reject)

        QMetaObject.connectSlotsByName(linear_two_points_dialog)
    # setupUi

    def retranslateUi(self, linear_two_points_dialog):
        linear_two_points_dialog.setWindowTitle(QCoreApplication.translate("linear_two_points_dialog", u"Linear Function from Two Points", None))
        self.label.setText(QCoreApplication.translate("linear_two_points_dialog", u"&x0", None))
        self.label_2.setText(QCoreApplication.translate("linear_two_points_dialog", u"y&0", None))
        self.label_3.setText(QCoreApplication.translate("linear_two_points_dialog", u"x&1", None))
        self.label_4.setText(QCoreApplication.translate("linear_two_points_dialog", u"&y1", None))
        self.aLabel.setText(QCoreApplication.translate("linear_two_points_dialog", u"Slope (&a)", None))
        self.label_6.setText(QCoreApplication.translate("linear_two_points_dialog", u"Intercept (&b)", None))
    # retranslateUi

