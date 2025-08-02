# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rectangular_to_polar_dialog.ui'
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

class Ui_RectangularToPolarDialog(object):
    def setupUi(self, RectangularToPolarDialog):
        if not RectangularToPolarDialog.objectName():
            RectangularToPolarDialog.setObjectName(u"RectangularToPolarDialog")
        RectangularToPolarDialog.resize(254, 170)
        self.buttonBox = QDialogButtonBox(RectangularToPolarDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 130, 231, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(RectangularToPolarDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 12, 49, 16))
        self.xLineEdit = QLineEdit(RectangularToPolarDialog)
        self.xLineEdit.setObjectName(u"xLineEdit")
        self.xLineEdit.setGeometry(QRect(90, 10, 151, 21))
        self.label_2 = QLabel(RectangularToPolarDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 42, 49, 16))
        self.yLineEdit = QLineEdit(RectangularToPolarDialog)
        self.yLineEdit.setObjectName(u"yLineEdit")
        self.yLineEdit.setGeometry(QRect(90, 40, 151, 21))
        self.label_3 = QLabel(RectangularToPolarDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 72, 71, 16))
        self.distanceLineEdit = QLineEdit(RectangularToPolarDialog)
        self.distanceLineEdit.setObjectName(u"distanceLineEdit")
        self.distanceLineEdit.setGeometry(QRect(90, 70, 151, 21))
        self.distanceLineEdit.setReadOnly(True)
        self.label_4 = QLabel(RectangularToPolarDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 102, 49, 16))
        self.angleLineEdit = QLineEdit(RectangularToPolarDialog)
        self.angleLineEdit.setObjectName(u"angleLineEdit")
        self.angleLineEdit.setGeometry(QRect(90, 100, 151, 21))
        self.angleLineEdit.setReadOnly(True)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.xLineEdit)
        self.label_2.setBuddy(self.yLineEdit)
        self.label_3.setBuddy(self.distanceLineEdit)
        self.label_4.setBuddy(self.angleLineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(RectangularToPolarDialog)
        self.buttonBox.accepted.connect(RectangularToPolarDialog.accept)
        self.buttonBox.rejected.connect(RectangularToPolarDialog.reject)

        QMetaObject.connectSlotsByName(RectangularToPolarDialog)
    # setupUi

    def retranslateUi(self, RectangularToPolarDialog):
        RectangularToPolarDialog.setWindowTitle(QCoreApplication.translate("RectangularToPolarDialog", u"Rectangular to Polar Coordinates", None))
        self.label.setText(QCoreApplication.translate("RectangularToPolarDialog", u"&X:", None))
        self.label_2.setText(QCoreApplication.translate("RectangularToPolarDialog", u"&Y:", None))
        self.label_3.setText(QCoreApplication.translate("RectangularToPolarDialog", u"&Radius:", None))
        self.label_4.setText(QCoreApplication.translate("RectangularToPolarDialog", u"&Angle:", None))
    # retranslateUi

