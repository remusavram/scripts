# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI\showDialog.ui'
#
# Created: Tue Sep 09 21:37:22 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.resize(360, 62)
        self.nameEdit = QtGui.QLineEdit(mainDialog)
        self.nameEdit.setGeometry(QtCore.QRect(10, 20, 221, 28))
        self.nameEdit.setObjectName("nameEdit")
        self.showButton = QtGui.QPushButton(mainDialog)
        self.showButton.setGeometry(QtCore.QRect(250, 20, 98, 28))
        self.showButton.setObjectName("showButton")

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(QtGui.QApplication.translate("mainDialog", "Main Dialog ", None, QtGui.QApplication.UnicodeUTF8))
        self.nameEdit.setPlaceholderText(QtGui.QApplication.translate("mainDialog", "Enter your name!", None, QtGui.QApplication.UnicodeUTF8))
        self.showButton.setText(QtGui.QApplication.translate("mainDialog", "Show!", None, QtGui.QApplication.UnicodeUTF8))

