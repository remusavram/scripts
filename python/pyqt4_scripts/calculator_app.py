#!/usr/bin/python

'''
@package   calculator_app    
@brief     
@details   
@author    Remus Avram
@date      2014.12
'''

import sys
import os
import operator
from PyQt4 import QtCore, QtGui

from calculatorWinUI import Ui_CalculatorWindow
from calcWidgetUI import Ui_Calculator


class Window(QtGui.QMainWindow, Ui_CalculatorWindow):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        
        self.setupUi(self)
        
        self.calcWidget = Calculator()
        self.setCentralWidget(self.calcWidget)
        
        self.actionClear.triggered.connect(self.calcWidget.clear)
    # END def __init__
# END class Window
 

class Calculator(QtGui.QWidget):
    
    OPS = {
           '+': operator.add,
           '-': operator.sub,
           '/': operator.div,
           '*': operator.mul
           }
    
    def __init__(self, *args, **kwargs):
        super(Calculator, self).__init__(*args, **kwargs)
        
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
    
        self.ui.inputA.setValidator(QtGui.QDoubleValidator(self))
        self.ui.inputB.setValidator(QtGui.QDoubleValidator(self))
        
        self.ui.operatorBox.clear()
        self.ui.operatorBox.addItems(self.OPS.keys())
        
        self.ui.clearButton.clicked.connect(self.clear)
        
        self.ui.inputA.textEdited.connect(self.calc)
        self.ui.inputB.textEdited.connect(self.calc)
        
        self.ui.operatorBox.currentIndexChanged.connect(self.calc)
    # END def __init__
    
    def clear(self):
        ''' Slot to clear the fors fields'''
        self.ui.inputA.clear()
        self.ui.inputB.clear()
        self.ui.result.clear()
    # END def clear
    
    def calc(self):
        op_str = str(self.ui.operatorBox.currentText())
        op = self.OPS.get(op_str)
        if not op:
            return
        
        inputA = self.ui.inputA.text()
        inputB = self.ui.inputB.text()
        
        if not (inputA and inputB):
            return
        
        try:
            i1 = float(inputA)
            i2 = float(inputB)
            result = op(i1, i2)
            
        except Exception, e:
            QtGui.QMessageBox.warning(self, "Could not calculate result", 
                                            "Result: \n%s" %e)
        else:
            self.ui.result.setText(str(result))
# END class Calculator


def main():
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.show()
    win.raise_()
    sys.exit(app.exec_())
    

if __name__ == "__main__": main()