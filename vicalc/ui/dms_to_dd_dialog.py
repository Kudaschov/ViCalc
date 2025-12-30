# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dms_to_dd_dialog.ui'
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

class Ui_DMStoDD_Dialog(object):
    def setupUi(self, DMStoDD_Dialog):
        if not DMStoDD_Dialog.objectName():
            DMStoDD_Dialog.setObjectName(u"DMStoDD_Dialog")
        DMStoDD_Dialog.resize(244, 151)
        self.buttonBox = QDialogButtonBox(DMStoDD_Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 110, 221, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(DMStoDD_Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 12, 81, 16))
        self.degreesLineEdit = QLineEdit(DMStoDD_Dialog)
        self.degreesLineEdit.setObjectName(u"degreesLineEdit")
        self.degreesLineEdit.setGeometry(QRect(92, 10, 141, 21))
        self.label_2 = QLabel(DMStoDD_Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 42, 81, 16))
        self.minutesLineEdit = QLineEdit(DMStoDD_Dialog)
        self.minutesLineEdit.setObjectName(u"minutesLineEdit")
        self.minutesLineEdit.setGeometry(QRect(92, 40, 141, 21))
        self.label_3 = QLabel(DMStoDD_Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 72, 81, 16))
        self.secondsLineEdit = QLineEdit(DMStoDD_Dialog)
        self.secondsLineEdit.setObjectName(u"secondsLineEdit")
        self.secondsLineEdit.setGeometry(QRect(92, 70, 141, 21))
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.degreesLineEdit)
        self.label_2.setBuddy(self.minutesLineEdit)
        self.label_3.setBuddy(self.secondsLineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.degreesLineEdit, self.minutesLineEdit)
        QWidget.setTabOrder(self.minutesLineEdit, self.secondsLineEdit)

        self.retranslateUi(DMStoDD_Dialog)
        self.buttonBox.accepted.connect(DMStoDD_Dialog.accept)
        self.buttonBox.rejected.connect(DMStoDD_Dialog.reject)

        QMetaObject.connectSlotsByName(DMStoDD_Dialog)
    # setupUi

    def retranslateUi(self, DMStoDD_Dialog):
        DMStoDD_Dialog.setWindowTitle(QCoreApplication.translate("DMStoDD_Dialog", u"DMS to Decimal Degrees (DD)", None))
        self.label.setText(QCoreApplication.translate("DMStoDD_Dialog", u"&Degrees:", None))
        self.label_2.setText(QCoreApplication.translate("DMStoDD_Dialog", u"&Minutes:", None))
        self.label_3.setText(QCoreApplication.translate("DMStoDD_Dialog", u"&Seconds:", None))
    # retranslateUi

