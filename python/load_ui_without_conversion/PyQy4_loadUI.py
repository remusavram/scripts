#!/usr/bin/python

'''
@package   2014.12_loadUIDinamically
@brief     Loads a ui file dinamically in PyQt.
@details   
@author    Remus Avram
@date      2014.12
'''

from PyQt4 import QtCore, QtGui, uic
import sys


uiFileName = "resource/login.ui"


class LoginInterface(QtGui.QWidget):
    """ This class connects the fields form login.ui with commands. """
    
    def __init__(self):
        """ Initializes LoginInterface."""
    
        super(LoginInterface, self).__init__()
        #somewhere in constructor:
        uic.loadUi(uiFileName, self)
        self.loginPushButton.clicked.connect(self.loginButton)
    
    def loginButton(self):
        print "ok"


def main():
    app = QtGui.QApplication(sys.argv)
    form = LoginInterface()
    form.show()
    sys.exit(app.exec_())
# END def main


if __name__ == '__main__':
    main()
# END if
