'''
Created on Sep 10, 2014

@author: remusav
'''


from PySide import QtGui  
from PySide import QtCore
from PySide import QtUiTools

uiFileName = "resource/login.ui"

class MyWidget(QtGui.QMainWindow):
    def __init__(self, *args):  
        apply(QtGui.QMainWindow.__init__, (self,) + args)

        loader = QtUiTools.QUiLoader()
        fileUi = QtCore.QFile(uiFileName)
        fileUi.open(QtCore.QFile.ReadOnly)
        self.myWidget = loader.load(fileUi, self)
        fileUi.close()

        self.setCentralWidget(self.myWidget)

if __name__ == '__main__':  
    import sys  
    import os
    print("Running in " + os.getcwd() + " .\n")

    app = QtGui.QApplication(sys.argv)  

    win  = MyWidget()  
    win.show()

    app.connect(app, QtCore.SIGNAL("lastWindowClosed()"),
               app, QtCore.SLOT("quit()"))
    app.exec_()