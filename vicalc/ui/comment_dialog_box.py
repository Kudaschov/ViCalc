# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comment_dialog_box.ui'
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
    QLineEdit, QSizePolicy, QWidget)

class Ui_CommentDialog(object):
    def setupUi(self, CommentDialog):
        if not CommentDialog.objectName():
            CommentDialog.setObjectName(u"CommentDialog")
        CommentDialog.resize(320, 77)
        self.buttonBox = QDialogButtonBox(CommentDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 40, 301, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.lineEdit = QLineEdit(CommentDialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 301, 21))

        self.retranslateUi(CommentDialog)
        self.buttonBox.accepted.connect(CommentDialog.accept)
        self.buttonBox.rejected.connect(CommentDialog.reject)

        QMetaObject.connectSlotsByName(CommentDialog)
    # setupUi

    def retranslateUi(self, CommentDialog):
        CommentDialog.setWindowTitle(QCoreApplication.translate("CommentDialog", u"Comment for Log", None))
    # retranslateUi

