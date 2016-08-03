#!/bin/python

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


__appname__ = "Dialog Application"


class Program(QDialog):
    """ This class creates a window with 4 buttones (Open, Close, Save, Other). """

    def __init__(self, parent=None):
        """ Constructor. """

        super(Program, self).__init__(parent)

        openButton = QPushButton("Open")
        saveButton = QPushButton("Save")
        dirButton = QPushButton("Other")
        closeButton = QPushButton("Close")

        self.connect(saveButton, SIGNAL("clicked()"), self.saveMethod)
        self.connect(openButton, SIGNAL("clicked()"), self.openMethod)
        #openButton.clicked.connect(self.openDif)

        layout = QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(saveButton)
        layout.addWidget(dirButton)
        layout.addWidget(closeButton)
        self.setLayout(layout)
    # END def __init__

    def openMethod(self):
        """ This method opens a text file. """
#
        dir = "."
        fileObj = QFileDialog.getOpenFileName(self, __appname__ + " Open File Dialog", dir=dir, filter="Text files (*.txt)")
        print fileObj
        print type(fileObj)

        fileName = fileObj[0]

        fileWork = open(fileName, "r")
        readFile = fileWork.read()
        fileWork.close()
        print readFile
    # END def openMethod

    def saveMethod(self):
        """ This method save a text file. """

        dir = "."
        fileObj = QFileDialog.getSaveFileName(self, __appname__, dir=dir, filter="Text files (*.txt)")
        print fileObj
        print type(fileObj)

        contents = "Hello Remus!"

        fileName = fileObj[0]
        open(fileName, mode="w").write(contents)
    # END def saveMethod

    
# END class Program



def main():
    app = QApplication(sys.argv)
    form = Program()
    form.show()
    app.exec_()
# END def main


if __name__ == '__main__':
    main()
# END if