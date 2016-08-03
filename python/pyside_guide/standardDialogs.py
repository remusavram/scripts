#!/usr/python

"""
@brief         Simple Dialog Application
@author        Remus Avram
@email         avram.remus20@yahoo.com
@copyright     private
@date          2014.09.04
"""


from PySide.QtCore import *
from PySide.QtGui import *
import sys


__appName__ = "Standard Dialogs"



class Program(QDialog):
    """ This class create a dialog window for tests."""
    
    def __init__(self, parent=None):
        """ Constructor class. """
        
        super(Program, self).__init__()
        
        self.setWindowTitle(__appName__)
        
        btn = QPushButton("Open Dialog")
        self.mainSpingBox = QSpinBox()
        self.mainCheckBox = QCheckBox("Main CheckBox Value")
        
        layout = QVBoxLayout()
        layout.addWidget(self.mainSpingBox)
        layout.addWidget(self.mainCheckBox)
        layout.addWidget(btn)
        self.setLayout(layout)
        
        self.connect(btn, SIGNAL("clicked()"), self.dialogOpen)
    # END def __init__
    
    
    def dialogOpen(self):
        """ Open the dialog window. """
        
        initValues = {"mainSpinBox":self.mainSpingBox.value(), "mainCheckBox":self.mainCheckBox.isChecked()}
        dialog = Dialog(initValues)
        if dialog.exec_():
            self.mainSpingBox.setValue(dialog.spinBox.value())
            self.mainCheckBox.setChecked(dialog.checkBox.isChecked())
    # END def dialogOpen
# END class Program



class Dialog(QDialog):
    """ This class creates a window dialog for tests. """
    
    def __init__(self, initValues, parent=None):
        """ Constructor class. """
        
        super(Dialog, self).__init__(parent)
        
        self.setWindowTitle("Dialog")
        
        self.checkBox = QCheckBox("Check me out!")
        self.spinBox = QSpinBox()
        buttonOK = QPushButton("OK")
        buttonCancel = QPushButton("Cancel")
        
        layout = QGridLayout()
        layout.addWidget(self.spinBox, 0, 0)
        layout.addWidget(self.checkBox, 0, 1)
        layout.addWidget(buttonOK)
        layout.addWidget(buttonCancel)
        self.setLayout(layout)
        
        #self.spinBox.setValue(1)
        
        self.spinBox.setValue(initValues["mainSpinBox"])
        self.checkBox.setChecked(initValues["mainCheckBox"])
        
        self.connect(buttonOK, SIGNAL("clicked()"), self, SLOT("acceptDialog()"))
        self.connect(buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()"))
    # END __init__ def
    
    
    def acceptDialog(self):
        """ This method checks if the number introduced is between 0 and 5. """
        
        class GreatorThenFive(Exception): pass
        class IsZero(Exception): pass
        
        try:
            if self.spinBox.value() > 5:
                raise GreatorThenFive, ("The SpinBox value cannot be greater then 5")
            elif self.spinBox.value() == 0:
                raise IsZero, ("The SpingBox value cannot be equal to 0")
            else:
                QDialog.accept(self)
        
        except GreatorThenFive, e:
            QMessageBox.warning(self, __appName__, str(e))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return
        
        except IsZero, e:
            QMessageBox.warning(self, __appName__, str(e))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return
    # END def acceptDialog 
# END calss Dialog



def main():
    app = QApplication(sys.argv)
    form = Program()
    form.show()
    app.exec_()
# END def main


if __name__ == '__main__':
    main()
# END if