# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_rectangular_form.ui'
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

class Ui_InputComplexNumberInRectangularFormDialog(object):
    def setupUi(self, InputComplexNumberInRectangularFormDialog):
        if not InputComplexNumberInRectangularFormDialog.objectName():
            InputComplexNumberInRectangularFormDialog.setObjectName(u"InputComplexNumberInRectangularFormDialog")
        InputComplexNumberInRectangularFormDialog.resize(361, 240)
        InputComplexNumberInRectangularFormDialog.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.buttonBox = QDialogButtonBox(InputComplexNumberInRectangularFormDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 200, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(InputComplexNumberInRectangularFormDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 38, 16, 16))
        self.realPartLineEdit = DotLineEdit(InputComplexNumberInRectangularFormDialog)
        self.realPartLineEdit.setObjectName(u"realPartLineEdit")
        self.realPartLineEdit.setGeometry(QRect(30, 37, 131, 21))
        self.label_2 = QLabel(InputComplexNumberInRectangularFormDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 38, 16, 16))
        self.imagPartLineEdit = DotLineEdit(InputComplexNumberInRectangularFormDialog)
        self.imagPartLineEdit.setObjectName(u"imagPartLineEdit")
        self.imagPartLineEdit.setGeometry(QRect(190, 37, 131, 21))
        self.label_3 = QLabel(InputComplexNumberInRectangularFormDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 38, 16, 16))
        self.rLineEdit = QLineEdit(InputComplexNumberInRectangularFormDialog)
        self.rLineEdit.setObjectName(u"rLineEdit")
        self.rLineEdit.setGeometry(QRect(30, 98, 131, 21))
        self.rLineEdit.setReadOnly(True)
        self.thetaLineEdit = QLineEdit(InputComplexNumberInRectangularFormDialog)
        self.thetaLineEdit.setObjectName(u"thetaLineEdit")
        self.thetaLineEdit.setGeometry(QRect(30, 138, 131, 21))
        self.thetaLineEdit.setReadOnly(True)
        self.label_4 = QLabel(InputComplexNumberInRectangularFormDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 100, 16, 16))
        self.label_5 = QLabel(InputComplexNumberInRectangularFormDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 140, 16, 16))
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.realPartLineEdit)
        self.label_3.setBuddy(self.imagPartLineEdit)
        self.label_4.setBuddy(self.rLineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(InputComplexNumberInRectangularFormDialog)
        self.buttonBox.accepted.connect(InputComplexNumberInRectangularFormDialog.accept)
        self.buttonBox.rejected.connect(InputComplexNumberInRectangularFormDialog.reject)

        QMetaObject.connectSlotsByName(InputComplexNumberInRectangularFormDialog)
    # setupUi

    def retranslateUi(self, InputComplexNumberInRectangularFormDialog):
        InputComplexNumberInRectangularFormDialog.setWindowTitle(QCoreApplication.translate("InputComplexNumberInRectangularFormDialog", u"Input Complex Number in Rectangular Form", None))
        self.label.setText(QCoreApplication.translate("InputComplexNumberInRectangularFormDialog", u"&(", None))
        self.label_2.setText(QCoreApplication.translate("InputComplexNumberInRectangularFormDialog", u"+", None))
        self.label_3.setText(QCoreApplication.translate("InputComplexNumberInRectangularFormDialog", u"&i)", None))
        self.label_4.setText(QCoreApplication.translate("InputComplexNumberInRectangularFormDialog", u"&r", None))
        self.label_5.setText(QCoreApplication.translate("InputComplexNumberInRectangularFormDialog", u"\u03b8", None))
    # retranslateUi

