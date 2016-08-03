#!/usr/python

"""
@brief         Working with Signals and Slots
@author        Remus Avram
@email         avram.remus20@yahoo.com
@copyright     private
@date          2014.09.04
"""


from PySide.QtCore import *
from PySide.QtGui import *
import sys



class ZeroSpinBox(QSpinBox):

    # global variables
    zeros = 0

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)

        self.connect(self, SIGNAL("valueChanged(int)"), self.checkzero)
    # END def __init__



    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.nulls = 5
            self.emit(SIGNAL("atzero(int, int)"), self.zeros, self.nulls)
# END class ZeroSpinBox



class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        dial = QDial()
        dial.setNotchesVisible(True)

        zeroSpinbox = ZeroSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(zeroSpinbox)
        self.setLayout(layout)

        self.connect(dial, SIGNAL("valueChanged(int)"), zeroSpinbox.setValue)
        self.connect(zeroSpinbox, SIGNAL("valueChanged(int)"), dial.setValue)
        self.connect(zeroSpinbox, SIGNAL("atzero(int, int)"), self.announce)

        self.setWindowTitle("Signals and Slots")


    def announce(self, zeros, nulls):
        print "ZeroSpinBox has been at zero " + str(zeros) + " times!"
        print "The constant nulls is: " + str(nulls)

    # END def __init__
# END class Form



def main():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
# END def main


if __name__ == '__main__':
    main()
# END if