import maya.cmds as cmds
from functools import partial


class myWin(object):
    def __init__(self):
       self.buildWin()
    
    def buildWin(self):
        self.win = cmds.window()
        self.layout = cmds.columnLayout(parent = self.win)
        self.button = cmds.button(label = 'refresh', command = partial(self.refreshList, self.win))
        self.button = cmds.button(label = 'close', command = partial(self.closeWin, self.win))
        cmds.showWindow(self.win)
    
    def refreshList(self, window=None, arg=None):
        if cmds.window(self.win, exists = True):
          cmds.deleteUI(self.win, window=True)
        self.buildWin()
    
    def closeWin(self, window=None, arg=None):
        if cmds.window(self.win, exists = True):
            cmds.deleteUI(self.win, window=True)
    

a = myWin()
