# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'combination_dialog.ui'
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

class Ui_combinationDialog(object):
    def setupUi(self, combinationDialog):
        if not combinationDialog.objectName():
            combinationDialog.setObjectName(u"combinationDialog")
        combinationDialog.resize(210, 135)
        self.buttonBox = QDialogButtonBox(combinationDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(-10, 90, 201, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(combinationDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 22, 49, 16))
        self.nLineEdit = QLineEdit(combinationDialog)
        self.nLineEdit.setObjectName(u"nLineEdit")
        self.nLineEdit.setGeometry(QRect(80, 20, 113, 21))
        self.label_2 = QLabel(combinationDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 52, 49, 16))
        self.rLineEdit = QLineEdit(combinationDialog)
        self.rLineEdit.setObjectName(u"rLineEdit")
        self.rLineEdit.setGeometry(QRect(80, 50, 113, 21))
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.nLineEdit)
        self.label_2.setBuddy(self.rLineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(combinationDialog)
        self.buttonBox.accepted.connect(combinationDialog.accept)
        self.buttonBox.rejected.connect(combinationDialog.reject)

        QMetaObject.connectSlotsByName(combinationDialog)
    # setupUi

    def retranslateUi(self, combinationDialog):
        combinationDialog.setWindowTitle(QCoreApplication.translate("combinationDialog", u"Combination nCr", None))
        self.label.setText(QCoreApplication.translate("combinationDialog", u"&n:", None))
        self.label_2.setText(QCoreApplication.translate("combinationDialog", u"&r:", None))
    # retranslateUi

