# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\calcWidget.ui'
#
# Created: Tue Dec 23 11:13:23 2014
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

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName(_fromUtf8("Calculator"))
        Calculator.resize(537, 122)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(Calculator)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.inputA = QtGui.QLineEdit(Calculator)
        self.inputA.setObjectName(_fromUtf8("inputA"))
        self.horizontalLayout.addWidget(self.inputA)
        self.operatorBox = QtGui.QComboBox(Calculator)
        self.operatorBox.setObjectName(_fromUtf8("operatorBox"))
        self.horizontalLayout.addWidget(self.operatorBox)
        self.inputB = QtGui.QLineEdit(Calculator)
        self.inputB.setObjectName(_fromUtf8("inputB"))
        self.horizontalLayout.addWidget(self.inputB)
        self.label = QtGui.QLabel(Calculator)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.result = QtGui.QLineEdit(Calculator)
        self.result.setReadOnly(True)
        self.result.setObjectName(_fromUtf8("result"))
        self.horizontalLayout.addWidget(self.result)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.calcButton = QtGui.QPushButton(Calculator)
        self.calcButton.setObjectName(_fromUtf8("calcButton"))
        self.horizontalLayout_2.addWidget(self.calcButton)
        self.clearButton = QtGui.QPushButton(Calculator)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout_2.addWidget(self.clearButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(_translate("Calculator", "Form", None))
        self.label.setText(_translate("Calculator", "=", None))
        self.calcButton.setText(_translate("Calculator", "Calculate", None))
        self.clearButton.setText(_translate("Calculator", "Clear", None))

