# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_base_dialog.ui'
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

class Ui_log_base_dialog(object):
    def setupUi(self, log_base_dialog):
        if not log_base_dialog.objectName():
            log_base_dialog.setObjectName(u"log_base_dialog")
        log_base_dialog.resize(339, 127)
        self.buttonBox = QDialogButtonBox(log_base_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 90, 301, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.numberLineEdit = QLineEdit(log_base_dialog)
        self.numberLineEdit.setObjectName(u"numberLineEdit")
        self.numberLineEdit.setGeometry(QRect(60, 10, 120, 21))
        self.baseLineEdit = QLineEdit(log_base_dialog)
        self.baseLineEdit.setObjectName(u"baseLineEdit")
        self.baseLineEdit.setGeometry(QRect(30, 32, 120, 21))
        self.label = QLabel(log_base_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 49, 21))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_2 = QLabel(log_base_dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 20, 49, 16))
        self.resultLineEdit = QLineEdit(log_base_dialog)
        self.resultLineEdit.setObjectName(u"resultLineEdit")
        self.resultLineEdit.setGeometry(QRect(210, 20, 120, 21))
        self.resultLineEdit.setReadOnly(True)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.numberLineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(log_base_dialog)
        self.buttonBox.accepted.connect(log_base_dialog.accept)
        self.buttonBox.rejected.connect(log_base_dialog.reject)

        QMetaObject.connectSlotsByName(log_base_dialog)
    # setupUi

    def retranslateUi(self, log_base_dialog):
        log_base_dialog.setWindowTitle(QCoreApplication.translate("log_base_dialog", u"Logarithm to Base", None))
        self.numberLineEdit.setText(QCoreApplication.translate("log_base_dialog", u"888", None))
        self.baseLineEdit.setText(QCoreApplication.translate("log_base_dialog", u"888", None))
        self.label.setText(QCoreApplication.translate("log_base_dialog", u"lo&g", None))
        self.label_2.setText(QCoreApplication.translate("log_base_dialog", u"=", None))
    # retranslateUi

