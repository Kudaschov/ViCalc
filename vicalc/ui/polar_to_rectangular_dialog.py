# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'polar_to_rectangular_dialog.ui'
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

class Ui_PolarToRectangularDialog(object):
    def setupUi(self, PolarToRectangularDialog):
        if not PolarToRectangularDialog.objectName():
            PolarToRectangularDialog.setObjectName(u"PolarToRectangularDialog")
        PolarToRectangularDialog.resize(255, 170)
        self.buttonBox = QDialogButtonBox(PolarToRectangularDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 130, 231, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(PolarToRectangularDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 12, 49, 16))
        self.radiusLineEdit = QLineEdit(PolarToRectangularDialog)
        self.radiusLineEdit.setObjectName(u"radiusLineEdit")
        self.radiusLineEdit.setGeometry(QRect(90, 10, 151, 21))
        self.label_2 = QLabel(PolarToRectangularDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 42, 49, 16))
        self.angleLineEdit = QLineEdit(PolarToRectangularDialog)
        self.angleLineEdit.setObjectName(u"angleLineEdit")
        self.angleLineEdit.setGeometry(QRect(90, 40, 151, 21))
        self.label_3 = QLabel(PolarToRectangularDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 72, 49, 16))
        self.xLineEdit = QLineEdit(PolarToRectangularDialog)
        self.xLineEdit.setObjectName(u"xLineEdit")
        self.xLineEdit.setGeometry(QRect(90, 70, 151, 21))
        self.xLineEdit.setReadOnly(True)
        self.label_4 = QLabel(PolarToRectangularDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 102, 49, 16))
        self.yLineEdit = QLineEdit(PolarToRectangularDialog)
        self.yLineEdit.setObjectName(u"yLineEdit")
        self.yLineEdit.setGeometry(QRect(90, 100, 151, 21))
        self.yLineEdit.setReadOnly(True)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.radiusLineEdit)
        self.label_2.setBuddy(self.angleLineEdit)
        self.label_3.setBuddy(self.xLineEdit)
        self.label_4.setBuddy(self.yLineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(PolarToRectangularDialog)
        self.buttonBox.accepted.connect(PolarToRectangularDialog.accept)
        self.buttonBox.rejected.connect(PolarToRectangularDialog.reject)

        QMetaObject.connectSlotsByName(PolarToRectangularDialog)
    # setupUi

    def retranslateUi(self, PolarToRectangularDialog):
        PolarToRectangularDialog.setWindowTitle(QCoreApplication.translate("PolarToRectangularDialog", u"Polar to Rectangular Coordinates", None))
        self.label.setText(QCoreApplication.translate("PolarToRectangularDialog", u"&Radius:", None))
        self.label_2.setText(QCoreApplication.translate("PolarToRectangularDialog", u"&Angle:", None))
        self.label_3.setText(QCoreApplication.translate("PolarToRectangularDialog", u"&X:", None))
        self.label_4.setText(QCoreApplication.translate("PolarToRectangularDialog", u"&Y:", None))
    # retranslateUi

