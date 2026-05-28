# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ratio_d_dialog.ui'
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
    QFrame, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_ratio_d_dialog(object):
    def setupUi(self, ratio_d_dialog):
        if not ratio_d_dialog.objectName():
            ratio_d_dialog.setObjectName(u"ratio_d_dialog")
        ratio_d_dialog.resize(340, 240)
        self.buttonBox = QDialogButtonBox(ratio_d_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 200, 321, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.frame = QFrame(ratio_d_dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 141, 80))
        self.frame.setFrameShape(QFrame.Shape.HLine)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.bLineEdit = QLineEdit(self.frame)
        self.bLineEdit.setObjectName(u"bLineEdit")
        self.bLineEdit.setGeometry(QRect(20, 50, 113, 21))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 52, 49, 16))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 12, 49, 16))
        self.aLineEdit = QLineEdit(self.frame)
        self.aLineEdit.setObjectName(u"aLineEdit")
        self.aLineEdit.setGeometry(QRect(20, 10, 113, 21))
        self.bLineEdit.raise_()
        self.label.raise_()
        self.aLineEdit.raise_()
        self.label_2.raise_()
        self.label_3 = QLabel(ratio_d_dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 40, 49, 16))
        self.frame_2 = QFrame(ratio_d_dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(190, 10, 141, 80))
        self.frame_2.setFrameShape(QFrame.Shape.HLine)
        self.frame_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.cLineEdit = QLineEdit(self.frame_2)
        self.cLineEdit.setObjectName(u"cLineEdit")
        self.cLineEdit.setGeometry(QRect(20, 10, 113, 21))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 52, 49, 16))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 12, 49, 16))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.xLineEdit = QLineEdit(ratio_d_dialog)
        self.xLineEdit.setObjectName(u"xLineEdit")
        self.xLineEdit.setGeometry(QRect(40, 148, 113, 21))
        self.label_6 = QLabel(ratio_d_dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 152, 49, 16))
        self.frame.raise_()
        self.buttonBox.raise_()
        self.label_3.raise_()
        self.frame_2.raise_()
        self.xLineEdit.raise_()
        self.label_6.raise_()
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.bLineEdit)
        self.label.setBuddy(self.aLineEdit)
        self.label_4.setBuddy(self.bLineEdit)
        self.label_5.setBuddy(self.aLineEdit)
        self.label_6.setBuddy(self.aLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.aLineEdit, self.bLineEdit)
        QWidget.setTabOrder(self.bLineEdit, self.cLineEdit)
        QWidget.setTabOrder(self.cLineEdit, self.xLineEdit)

        self.retranslateUi(ratio_d_dialog)
        self.buttonBox.accepted.connect(ratio_d_dialog.accept)
        self.buttonBox.rejected.connect(ratio_d_dialog.reject)

        QMetaObject.connectSlotsByName(ratio_d_dialog)
    # setupUi

    def retranslateUi(self, ratio_d_dialog):
        ratio_d_dialog.setWindowTitle(QCoreApplication.translate("ratio_d_dialog", u"Ratio Calculation: Unknown D", None))
        self.label_2.setText(QCoreApplication.translate("ratio_d_dialog", u"b", None))
        self.label.setText(QCoreApplication.translate("ratio_d_dialog", u"a", None))
        self.label_3.setText(QCoreApplication.translate("ratio_d_dialog", u"=", None))
        self.label_4.setText(QCoreApplication.translate("ratio_d_dialog", u"d", None))
        self.label_5.setText(QCoreApplication.translate("ratio_d_dialog", u"c", None))
        self.label_6.setText(QCoreApplication.translate("ratio_d_dialog", u"d", None))
    # retranslateUi

