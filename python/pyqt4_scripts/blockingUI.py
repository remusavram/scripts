#!/usr/bin/python

'''
@package   blockingUI
@brief     2 examples: - bloking UI
                       - no-bloking UI
@details   An example of how one should avoid blocking the main
            GUI thread, and make use of signal/slot notifications.
@author    Remus Avram
@date      2014.12
'''

import sys
import os
import subprocess

from PyQt4 import QtCore, QtGui


class BlockingTest(object):
    
    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        
        self.win = QtGui.QWidget()
        self.win.resize(300,200)
        
        layout = QtGui.QVBoxLayout(self.win)
        
        blocking_button = QtGui.QPushButton("Block")
        blocking_button.clicked.connect(self.blocking)
        layout.addWidget(blocking_button)
        
        signal_button = QtGui.QPushButton("Signals")
        signal_button.clicked.connect(self.not_blocking)
        layout.addWidget(signal_button)
        
        self.output = QtGui.QLineEdit()
        layout.addWidget(self.output)
        
        clear_button = QtGui.QPushButton("Clear")
        clear_button.clicked.connect(self.output.clear)
        layout.addWidget(clear_button)
        
        self.win.show()
        self.win.raise_()
        
        app.exec_()
        
    def finished(self, returnCode):
        self.setMessage("Return code: %s" %returnCode)
        
    def setMessage(self, msg):
        print msg
        self.output.setText(msg)
    
    def blocking(self):
        self.setMessage("Starting blocing sleep")
        
        process = subprocess.Popen(['sleep', '5'])
        ret = process.wait()
        self.finished(ret)
    
    def not_blocking(self):
        self.setMessage("Starting not blocking signal")
        
        process = QtCore.QProcess(self.win)
        process.finished.connect(self.finished)
        process.start('sleep', ['5'])
# end class BlockingTest

def main():
    blockingObject = BlockingTest()

if __name__ == '__main__': main()
