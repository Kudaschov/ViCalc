# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_polar_form.ui'
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

class Ui_InputComplexNumberInPolarFormDialog(object):
    def setupUi(self, InputComplexNumberInPolarFormDialog):
        if not InputComplexNumberInPolarFormDialog.objectName():
            InputComplexNumberInPolarFormDialog.setObjectName(u"InputComplexNumberInPolarFormDialog")
        InputComplexNumberInPolarFormDialog.resize(361, 240)
        InputComplexNumberInPolarFormDialog.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.buttonBox = QDialogButtonBox(InputComplexNumberInPolarFormDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 200, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(InputComplexNumberInPolarFormDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 150, 16, 16))
        self.realPartLineEdit = QLineEdit(InputComplexNumberInPolarFormDialog)
        self.realPartLineEdit.setObjectName(u"realPartLineEdit")
        self.realPartLineEdit.setGeometry(QRect(30, 149, 131, 21))
        self.realPartLineEdit.setReadOnly(True)
        self.label_2 = QLabel(InputComplexNumberInPolarFormDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 150, 16, 16))
        self.imagPartLineEdit = QLineEdit(InputComplexNumberInPolarFormDialog)
        self.imagPartLineEdit.setObjectName(u"imagPartLineEdit")
        self.imagPartLineEdit.setGeometry(QRect(190, 149, 131, 21))
        self.imagPartLineEdit.setReadOnly(True)
        self.label_3 = QLabel(InputComplexNumberInPolarFormDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 150, 16, 16))
        self.rLineEdit = DotLineEdit(InputComplexNumberInPolarFormDialog)
        self.rLineEdit.setObjectName(u"rLineEdit")
        self.rLineEdit.setGeometry(QRect(30, 28, 131, 21))
        self.rLineEdit.setReadOnly(False)
        self.thetaLineEdit = DotLineEdit(InputComplexNumberInPolarFormDialog)
        self.thetaLineEdit.setObjectName(u"thetaLineEdit")
        self.thetaLineEdit.setGeometry(QRect(30, 68, 131, 21))
        self.thetaLineEdit.setReadOnly(False)
        self.label_4 = QLabel(InputComplexNumberInPolarFormDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 30, 16, 16))
        self.label_5 = QLabel(InputComplexNumberInPolarFormDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 70, 16, 16))
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.realPartLineEdit)
        self.label_3.setBuddy(self.imagPartLineEdit)
        self.label_4.setBuddy(self.rLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.rLineEdit, self.thetaLineEdit)
        QWidget.setTabOrder(self.thetaLineEdit, self.realPartLineEdit)
        QWidget.setTabOrder(self.realPartLineEdit, self.imagPartLineEdit)

        self.retranslateUi(InputComplexNumberInPolarFormDialog)
        self.buttonBox.accepted.connect(InputComplexNumberInPolarFormDialog.accept)
        self.buttonBox.rejected.connect(InputComplexNumberInPolarFormDialog.reject)

        QMetaObject.connectSlotsByName(InputComplexNumberInPolarFormDialog)
    # setupUi

    def retranslateUi(self, InputComplexNumberInPolarFormDialog):
        InputComplexNumberInPolarFormDialog.setWindowTitle(QCoreApplication.translate("InputComplexNumberInPolarFormDialog", u"Input Complex Number in Polar Form", None))
        self.label.setText(QCoreApplication.translate("InputComplexNumberInPolarFormDialog", u"&(", None))
        self.label_2.setText(QCoreApplication.translate("InputComplexNumberInPolarFormDialog", u"+", None))
        self.label_3.setText(QCoreApplication.translate("InputComplexNumberInPolarFormDialog", u"&i)", None))
        self.label_4.setText(QCoreApplication.translate("InputComplexNumberInPolarFormDialog", u"&r", None))
        self.label_5.setText(QCoreApplication.translate("InputComplexNumberInPolarFormDialog", u"\u03b8", None))
    # retranslateUi

