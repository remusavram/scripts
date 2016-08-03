#!/usr/bin/python

'''
@package   
@brief     
@details   
@author    Remus Avram
@date      2015.01
'''


from PySide import QtCore, QtGui, QtSql
import sys
from os import path
import qt

import Shiboken
# CONFIGURATION
form_class, base_class = qt.utils.loadUiType(path.join(path.dirname(__file__), 'ui/test.ui'))


class MainWindow(base_class, form_class):
    '''LoadUI. Connect buttons with functions.'''
    
    def __init__(self):
        """Initializes the MainWindow."""
        super(MainWindow, self).__init__()
        self.setupUi(self)
    # END def __init__
# END class MainWindow
        

def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
# END def main


if __name__ == '__main__': main()