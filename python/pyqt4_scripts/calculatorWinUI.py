# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\calculatorWin.ui'
#
# Created: Tue Dec 23 11:13:24 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CalculatorWindow(object):
    def setupUi(self, CalculatorWindow):
        CalculatorWindow.setObjectName(_fromUtf8("CalculatorWindow"))
        CalculatorWindow.resize(612, 151)
        self.centralwidget = QtGui.QWidget(CalculatorWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        CalculatorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(CalculatorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        CalculatorWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(CalculatorWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CalculatorWindow.setStatusBar(self.statusbar)
        self.actionClear = QtGui.QAction(CalculatorWindow)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.menuFile.addAction(self.actionClear)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(CalculatorWindow)
        QtCore.QMetaObject.connectSlotsByName(CalculatorWindow)

    def retranslateUi(self, CalculatorWindow):
        CalculatorWindow.setWindowTitle(_translate("CalculatorWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("CalculatorWindow", "File", None))
        self.actionClear.setText(_translate("CalculatorWindow", "Clear", None))

