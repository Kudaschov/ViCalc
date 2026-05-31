# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quadratic_equation_dialog.ui'
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

class Ui_quadratic_equation_dialog(object):
    def setupUi(self, quadratic_equation_dialog):
        if not quadratic_equation_dialog.objectName():
            quadratic_equation_dialog.setObjectName(u"quadratic_equation_dialog")
        quadratic_equation_dialog.resize(320, 256)
        self.buttonBox = QDialogButtonBox(quadratic_equation_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 220, 301, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(quadratic_equation_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 12, 49, 16))
        self.aLineEdit = QLineEdit(quadratic_equation_dialog)
        self.aLineEdit.setObjectName(u"aLineEdit")
        self.aLineEdit.setGeometry(QRect(130, 10, 121, 21))
        self.label_2 = QLabel(quadratic_equation_dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 42, 49, 16))
        self.bLineEdit = QLineEdit(quadratic_equation_dialog)
        self.bLineEdit.setObjectName(u"bLineEdit")
        self.bLineEdit.setGeometry(QRect(130, 40, 121, 21))
        self.label_3 = QLabel(quadratic_equation_dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 72, 49, 16))
        self.cLineEdit = QLineEdit(quadratic_equation_dialog)
        self.cLineEdit.setObjectName(u"cLineEdit")
        self.cLineEdit.setGeometry(QRect(130, 70, 121, 21))
        self.label_4 = QLabel(quadratic_equation_dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 122, 111, 16))
        self.DLineEdit = QLineEdit(quadratic_equation_dialog)
        self.DLineEdit.setObjectName(u"DLineEdit")
        self.DLineEdit.setGeometry(QRect(130, 120, 121, 21))
        self.DLineEdit.setReadOnly(True)
        self.label_5 = QLabel(quadratic_equation_dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 152, 49, 16))
        self.x1LineEdit = QLineEdit(quadratic_equation_dialog)
        self.x1LineEdit.setObjectName(u"x1LineEdit")
        self.x1LineEdit.setGeometry(QRect(130, 150, 181, 21))
        self.x1LineEdit.setReadOnly(True)
        self.label_6 = QLabel(quadratic_equation_dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 182, 49, 16))
        self.x2LineEdit = QLineEdit(quadratic_equation_dialog)
        self.x2LineEdit.setObjectName(u"x2LineEdit")
        self.x2LineEdit.setGeometry(QRect(130, 180, 181, 21))
        self.x2LineEdit.setReadOnly(True)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.aLineEdit)
        self.label_2.setBuddy(self.bLineEdit)
        self.label_3.setBuddy(self.cLineEdit)
        self.label_4.setBuddy(self.DLineEdit)
        self.label_5.setBuddy(self.x1LineEdit)
        self.label_6.setBuddy(self.x2LineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(quadratic_equation_dialog)
        self.buttonBox.accepted.connect(quadratic_equation_dialog.accept)
        self.buttonBox.rejected.connect(quadratic_equation_dialog.reject)

        QMetaObject.connectSlotsByName(quadratic_equation_dialog)
    # setupUi

    def retranslateUi(self, quadratic_equation_dialog):
        quadratic_equation_dialog.setWindowTitle(QCoreApplication.translate("quadratic_equation_dialog", u"Quadratic Equation", None))
        self.label.setText(QCoreApplication.translate("quadratic_equation_dialog", u"&a", None))
        self.label_2.setText(QCoreApplication.translate("quadratic_equation_dialog", u"&b", None))
        self.label_3.setText(QCoreApplication.translate("quadratic_equation_dialog", u"&c", None))
        self.label_4.setText(QCoreApplication.translate("quadratic_equation_dialog", u"&Discriminant (D)", None))
        self.label_5.setText(QCoreApplication.translate("quadratic_equation_dialog", u"x&1", None))
        self.label_6.setText(QCoreApplication.translate("quadratic_equation_dialog", u"&x2", None))
    # retranslateUi

