# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QSizePolicy, QWidget)

class Ui_optionsDialog(object):
    def setupUi(self, optionsDialog):
        if not optionsDialog.objectName():
            optionsDialog.setObjectName(u"optionsDialog")
        optionsDialog.resize(410, 240)
        self.buttonBox = QDialogButtonBox(optionsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 200, 391, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.timestampCheckBox = QCheckBox(optionsDialog)
        self.timestampCheckBox.setObjectName(u"timestampCheckBox")
        self.timestampCheckBox.setGeometry(QRect(20, 20, 291, 20))
        self.copyCheckBox = QCheckBox(optionsDialog)
        self.copyCheckBox.setObjectName(u"copyCheckBox")
        self.copyCheckBox.setGeometry(QRect(20, 50, 381, 20))
        self.pasteCheckBox = QCheckBox(optionsDialog)
        self.pasteCheckBox.setObjectName(u"pasteCheckBox")
        self.pasteCheckBox.setGeometry(QRect(20, 80, 381, 20))
        self.inputReplacePointcheckBox = QCheckBox(optionsDialog)
        self.inputReplacePointcheckBox.setObjectName(u"inputReplacePointcheckBox")
        self.inputReplacePointcheckBox.setGeometry(QRect(20, 110, 381, 20))
        self.NumlockACcheckBox = QCheckBox(optionsDialog)
        self.NumlockACcheckBox.setObjectName(u"NumlockACcheckBox")
        self.NumlockACcheckBox.setGeometry(QRect(20, 140, 381, 20))
        self.convertAngleCheckBox = QCheckBox(optionsDialog)
        self.convertAngleCheckBox.setObjectName(u"convertAngleCheckBox")
        self.convertAngleCheckBox.setGeometry(QRect(20, 170, 381, 20))

        self.retranslateUi(optionsDialog)
        self.buttonBox.accepted.connect(optionsDialog.accept)
        self.buttonBox.rejected.connect(optionsDialog.reject)

        QMetaObject.connectSlotsByName(optionsDialog)
    # setupUi

    def retranslateUi(self, optionsDialog):
        optionsDialog.setWindowTitle(QCoreApplication.translate("optionsDialog", u"Dialog", None))
        self.timestampCheckBox.setText(QCoreApplication.translate("optionsDialog", u"&Automatically date and time stamp at start", None))
        self.copyCheckBox.setText(QCoreApplication.translate("optionsDialog", u"On &copy to clipboard: replace comma (,) with decimal point (.)", None))
        self.pasteCheckBox.setText(QCoreApplication.translate("optionsDialog", u"On &paste from clipboard: replace decimal point (.) with comma (,)", None))
        self.inputReplacePointcheckBox.setText(QCoreApplication.translate("optionsDialog", u"Convert decimal point (.) to comma (,) on &input", None))
        self.NumlockACcheckBox.setText(QCoreApplication.translate("optionsDialog", u"&Numlock as AC/C - All Clear / Clear Key", None))
#if QT_CONFIG(tooltip)
        self.convertAngleCheckBox.setToolTip(QCoreApplication.translate("optionsDialog", u"Convert angle automatically when changing units.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.convertAngleCheckBox.setWhatsThis(QCoreApplication.translate("optionsDialog", u"If this checkbox is checked, the angle value will be converted automatically when you switch between degrees (D), radians (R), or grads (G). If unchecked, only the unit label changes.", None))
#endif // QT_CONFIG(whatsthis)
        self.convertAngleCheckBox.setText(QCoreApplication.translate("optionsDialog", u"Con&vert Angle on Unit Change", None))
    # retranslateUi

