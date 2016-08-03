'''
@package   mQtUtil   
@brief     
@details   
@author    Remus Avram
@date      2014.12
'''

from PyQt4 import QtCore, QtGui
import sip

import maya.cmds as cmds
import maya.OpenMayaUI as mui


def getMainWindow():
    ptr = mui.MQtUtil.mainWindow()
    mainWin = sip.wrapinstance(long(ptr), QtCore.QObject)
    return mainWin

def getWindowUnderPointer():
    panel = cmds.getPanel(underPointer=True)
    if not panel:
        return None
    
    prt = mui.MQtUtil.findControl(panel)
    widget = sip.wrapinstance(long(prt), QtCore.QObject)
    return widget

def getPathForWidget(widget):
    return sip.unwrapinstance(widget)
