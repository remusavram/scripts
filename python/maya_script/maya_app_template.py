'''
@package   maya_app_template    
@brief     
@details   
@author    Remus Avram
@date      2014.12
'''

from PyQt4 import QtCore, QtGui
import sip

import maya.cmds as cmds
import maya.OpenMayaUI as mui

class Window(QtGui.QDialog):
    
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        
        # custom code here
        self.resize(800,600)
    # END def __init__
# END class Window

def getMainWindow():
    ptr = mui.MQtUtil.mainWindow()
    mainWin = sip.wrapinstance(long(ptr), QtCore.QObject)
    return mainWin

def show():
    win = Window(parent=getMainWindow())
    win.show()
    win.raise_()
    return win    


"""
In Maya we call the script:

================================================================================
import sys

pathToDir = r"D:\Programare\PySide-PyQt\Tutorials\cmivfx - PyQt4 UI Development for Maya\PyQt for Maya"

if pathToDir not in sys.path:
    sys.path.append(pathToDir)

try:
    reload(maya_app_template)
except:
    import maya_app_template

win = maya_app_template.show()
win.parent()
================================================================================
"""