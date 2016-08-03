#!/usr/python


'''
Created on Sep 10, 2014

@author: remusav
'''



from PySide import QtCore, QtGui
from PyQt4 import Qt
import sys
import os



# keep the path to the uiFile in a variable
uiFile = os.path.join(os.path.dirname(__file__), 'resource/login.ui')

form_class, base_class = Qt.u

# keep the changeable names in variables
windowObject = 'Login'

class LoginInterface(QtGui.QMainWindow):
    """ This class connects the fields form login.ui with commands. """
    
    def __init__(self, parent=None):
        """ This methods is a constructor. """
        super(LoginInterface, self).__init__(parent)
        
        
        
    # END def __init__
# END class LoginInterface



def main():
    app = QtGui.QApplication(sys.argv)
    form = LoginInterface()
    form.show()
    app.exec_()
# END def main


if __name__ == '__main__':
    main()
# END if