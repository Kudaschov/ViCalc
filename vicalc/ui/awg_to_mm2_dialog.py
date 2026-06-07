# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'awg_to_mm2_dialog.ui'
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

class Ui_awg_to_mm2_dialog(object):
    def setupUi(self, awg_to_mm2_dialog):
        if not awg_to_mm2_dialog.objectName():
            awg_to_mm2_dialog.setObjectName(u"awg_to_mm2_dialog")
        awg_to_mm2_dialog.resize(320, 240)
        self.buttonBox = QDialogButtonBox(awg_to_mm2_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(awg_to_mm2_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 12, 49, 16))
        self.awgLineEdit = QLineEdit(awg_to_mm2_dialog)
        self.awgLineEdit.setObjectName(u"awgLineEdit")
        self.awgLineEdit.setGeometry(QRect(130, 10, 120, 21))
        self.label_2 = QLabel(awg_to_mm2_dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 62, 91, 16))
        self.diameterInchLineEdit = QLineEdit(awg_to_mm2_dialog)
        self.diameterInchLineEdit.setObjectName(u"diameterInchLineEdit")
        self.diameterInchLineEdit.setGeometry(QRect(130, 60, 120, 21))
        self.diameterInchLineEdit.setReadOnly(True)
        self.label_3 = QLabel(awg_to_mm2_dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 92, 111, 16))
        self.diameterMmLineEdit = QLineEdit(awg_to_mm2_dialog)
        self.diameterMmLineEdit.setObjectName(u"diameterMmLineEdit")
        self.diameterMmLineEdit.setGeometry(QRect(130, 90, 120, 21))
        self.diameterMmLineEdit.setReadOnly(True)
        self.label_4 = QLabel(awg_to_mm2_dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 122, 101, 16))
        self.areaKcmilLineEdit = QLineEdit(awg_to_mm2_dialog)
        self.areaKcmilLineEdit.setObjectName(u"areaKcmilLineEdit")
        self.areaKcmilLineEdit.setGeometry(QRect(130, 120, 120, 21))
        self.areaKcmilLineEdit.setReadOnly(True)
        self.label_5 = QLabel(awg_to_mm2_dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 152, 111, 16))
        self.areaMm2LineEdit = QLineEdit(awg_to_mm2_dialog)
        self.areaMm2LineEdit.setObjectName(u"areaMm2LineEdit")
        self.areaMm2LineEdit.setGeometry(QRect(130, 150, 120, 21))
        self.areaMm2LineEdit.setReadOnly(True)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.awgLineEdit)
        self.label_2.setBuddy(self.diameterInchLineEdit)
        self.label_3.setBuddy(self.diameterMmLineEdit)
        self.label_4.setBuddy(self.areaKcmilLineEdit)
        self.label_5.setBuddy(self.areaMm2LineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(awg_to_mm2_dialog)
        self.buttonBox.accepted.connect(awg_to_mm2_dialog.accept)
        self.buttonBox.rejected.connect(awg_to_mm2_dialog.reject)

        QMetaObject.connectSlotsByName(awg_to_mm2_dialog)
    # setupUi

    def retranslateUi(self, awg_to_mm2_dialog):
        awg_to_mm2_dialog.setWindowTitle(QCoreApplication.translate("awg_to_mm2_dialog", u"American wire gauge (AWG) to mm2", None))
        self.label.setText(QCoreApplication.translate("awg_to_mm2_dialog", u"&AWG", None))
        self.label_2.setText(QCoreApplication.translate("awg_to_mm2_dialog", u"Diameter [&in]", None))
        self.label_3.setText(QCoreApplication.translate("awg_to_mm2_dialog", u"&Diameter [mm]", None))
        self.label_4.setText(QCoreApplication.translate("awg_to_mm2_dialog", u"A&rea [kcmil]", None))
        self.label_5.setText(QCoreApplication.translate("awg_to_mm2_dialog", u"&Area [mm2]", None))
    # retranslateUi

