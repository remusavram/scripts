# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\pickAnOS.ui'
#
# Created: Sun Sep 14 14:01:17 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

# command:
# D:\Programare\PySide\Tutoriale Scripts\PythonGUIPackage> pyside-uic.exe .\resources\pickAnOS.ui -o pickAnOS.py

from PySide import QtCore, QtGui

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.resize(386, 252)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/app-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainDialog.setWindowIcon(icon)
        self.archButton = QtGui.QPushButton(mainDialog)
        self.archButton.setGeometry(QtCore.QRect(30, 100, 91, 71))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/arch-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.archButton.setIcon(icon1)
        self.archButton.setObjectName("archButton")
        self.fedoraButton = QtGui.QPushButton(mainDialog)
        self.fedoraButton.setGeometry(QtCore.QRect(140, 100, 91, 71))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/fedora-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fedoraButton.setIcon(icon2)
        self.fedoraButton.setObjectName("fedoraButton")
        self.windowButton = QtGui.QPushButton(mainDialog)
        self.windowButton.setGeometry(QtCore.QRect(260, 100, 91, 71))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/windows-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.windowButton.setIcon(icon3)
        self.windowButton.setObjectName("windowButton")

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(QtGui.QApplication.translate("mainDialog", "Pick on OS", None, QtGui.QApplication.UnicodeUTF8))
        self.archButton.setText(QtGui.QApplication.translate("mainDialog", "Load Arch", None, QtGui.QApplication.UnicodeUTF8))
        self.fedoraButton.setText(QtGui.QApplication.translate("mainDialog", "Load Fedora", None, QtGui.QApplication.UnicodeUTF8))
        self.windowButton.setText(QtGui.QApplication.translate("mainDialog", "Load Window", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
