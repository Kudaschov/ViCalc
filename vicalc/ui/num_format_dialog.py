# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'num_format_dialog.ui'
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
    QLabel, QRadioButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_FormatDialog(object):
    def setupUi(self, FormatDialog):
        if not FormatDialog.objectName():
            FormatDialog.setObjectName(u"FormatDialog")
        FormatDialog.resize(320, 240)
        self.buttonBox = QDialogButtonBox(FormatDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.normRadioButton = QRadioButton(FormatDialog)
        self.normRadioButton.setObjectName(u"normRadioButton")
        self.normRadioButton.setGeometry(QRect(20, 20, 89, 20))
        self.generalRadioButton = QRadioButton(FormatDialog)
        self.generalRadioButton.setObjectName(u"generalRadioButton")
        self.generalRadioButton.setGeometry(QRect(20, 50, 89, 20))
        self.fixRadioButton = QRadioButton(FormatDialog)
        self.fixRadioButton.setObjectName(u"fixRadioButton")
        self.fixRadioButton.setGeometry(QRect(20, 80, 89, 20))
        self.sciRadioButton = QRadioButton(FormatDialog)
        self.sciRadioButton.setObjectName(u"sciRadioButton")
        self.sciRadioButton.setGeometry(QRect(20, 110, 89, 20))
        self.engRadioButton = QRadioButton(FormatDialog)
        self.engRadioButton.setObjectName(u"engRadioButton")
        self.engRadioButton.setGeometry(QRect(20, 140, 89, 20))
        self.label = QLabel(FormatDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 173, 71, 16))
        self.precisionSpinBox = QSpinBox(FormatDialog)
        self.precisionSpinBox.setObjectName(u"precisionSpinBox")
        self.precisionSpinBox.setGeometry(QRect(90, 170, 42, 22))
        self.precisionSpinBox.setMinimum(0)
        self.precisionSpinBox.setMaximum(16)
        self.precisionSpinBox.setValue(5)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.precisionSpinBox)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(FormatDialog)
        self.buttonBox.accepted.connect(FormatDialog.accept)
        self.buttonBox.rejected.connect(FormatDialog.reject)

        QMetaObject.connectSlotsByName(FormatDialog)
    # setupUi

    def retranslateUi(self, FormatDialog):
        FormatDialog.setWindowTitle(QCoreApplication.translate("FormatDialog", u"Numeric Format", None))
        self.normRadioButton.setText(QCoreApplication.translate("FormatDialog", u"&Normal", None))
        self.generalRadioButton.setText(QCoreApplication.translate("FormatDialog", u"&General", None))
        self.fixRadioButton.setText(QCoreApplication.translate("FormatDialog", u"&Fixed", None))
        self.sciRadioButton.setText(QCoreApplication.translate("FormatDialog", u"&Scientific", None))
        self.engRadioButton.setText(QCoreApplication.translate("FormatDialog", u"&Engineering", None))
        self.label.setText(QCoreApplication.translate("FormatDialog", u"&Precision:", None))
    # retranslateUi

