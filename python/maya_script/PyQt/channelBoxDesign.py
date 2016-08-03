'''
@package   channelBox   
@brief     
@details   
@author    Remus Avram
@date      2014.12
'''

from PyQt4 import QtCore, QtGui
import sip

from functools import partial
from contextlib import contextmanager

import maya.cmds as cmds
import maya.OpenMaya as om
import maya.OpenMayaUI as mui

from mQtUtil import getMainWindow


class ChannelBox(QtGui.QDialog):
    '''
    ChennelBox(QtGui.QDialog)
    
    Custom dialog widget thet emulates a few basic features
    of the Mata Channel Box
    
    1. Follows the scene selection changes
    2. Validates attributes value types
    3. Can set multiple attributes values at once
    '''
    
    def __init__(self, *args, **kwargs):
        super(ChannelBox, self).__init__(*args, **kwargs)
        
        self.resize(300, 500)
        self.setObjectName("CustomChannelBox")
        
        self._currentNode = None
        self._is_updating = False
        
        self.mainLayout = QtGui.QStackedLayout(self)
        self.mainLayout.addWidget(QtGui.QWidget())
        
        table = QtGui.QTableWidget(1,2)
        table.setShowGrid(False)
        table.setSpan(0,0,1,2)
        header = table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        header.setVisible(False)
        editTriggers = table.DoubleClicked|table.SelectedClicked|table.AnyKeyPressed
        table.setEditTriggers(editTriggers)
        
        table.setItemPrototype(AttrItem())
        
        node = QtGui.QTableWidgetItem()
        table.setItem(0,0,node)
        
        self.table = table
        
        self.mainLayout.addWidget(self.table)
        self.mainLayout.setCurrentIndex(1)
        
        self.setStyleSheet('''
            QTabkeWudget {
                background: rgb(65,65,65);
            }
        ''')
        
        self.table.itemChanged.connect(self.itemChanged)
        
        self._sel_cbk_id = om.MEventMessage.addEventCallback(
                                            'SelectionChanged',
                                            self.refreshDisplay)
        
        cbk = partial(om.MMessage.removeCallback, self._sel_cbk_id)
        self.destroyed.connect(cbk)
        
        self.table.installEventFilter(self)
    # END def __init__
        
    def showEvent(self, event):
        super(ChannelBox, self).showEvent(event)
        self.refreshDisplay()
    # END def showEvent
    
    def eventFilter(self, obj, event):
        if obj is self.table:
            if event.type() == event.KeyPress:
                self.table.keyPressEvent(event)
                event.accept()
                return True
        return False
    # END def eventFilter
    
    def itemChanged(self, item):
        '''
        Slot called when an item in the attributes tables is changed.
        Performs validation of the value by checking the recorded types.
        Recursively triggered setting the same value on all other selected
        items if a multiple selection was made.
        '''
        
        row = item.row()
        col = item.column()
        
        if row == 0:
            newname = cmds.rename(self._currentNode, str(item.text()))
            self.showAttributes(newname)
            return
        
        elif col == 1:
            txt = str(item.text())
            attrType = type(item.attrVal)
            try:
                if attrType is bool:
                    attrVal = txt.lower() in ('1', 'on', 'yes', 'y', 'true')
                else:
                    attrVal = attrType(txt)
            except ValueError:
                cmds.worning("'%s' is not a valid attribute type. Expected %s" %(txt, attrType))
                with noSignals(self.table):
                    item.setAttrValue(item.attrVal)
                return
                
            cmds.setAttr(item.attrName, attrVal)
            
            with noSignals(self.table):
                item.setAttrValue(attrVal)
            
            if not self._is_updating == True:
                for i in self.table.selectedItems():
                    if i.column() != 1:
                        continue
                    if i is item:
                        continue
                    i.setAttrValue(attrVal)
                    
                self._is_updating = False
    # END def itemChanged
    
    def refreshDisplay(self, *args, **kwargs):
        '''
        Slot that refreshes the ChannelBox attributes with
        the currently selected item tn the scene.
        '''
        node = ''
        sel = cmds.ls(sl=True, l=True)
        if sel:
            node = sel[-1]
        
        self.showAttributes(node)
    # END def refreshDisplay
    
    def showAttributes(self, node):
        '''
        Set the ChannelBox to view the given node.
        If node is empty or None, the ChannelBox will simply be cleared.
        '''
        with noSignals(self.table):
            while self.table.rowCount() > 1:
                self.table.removeRow(1)
            
            if not node or not cmds.objExists(node):
                self._setTableVisible(False)
                return
            
            self._setTableVisible(True)
            
            self._currentNode = node
            name = node.split('|')[-1]
            self.table.item(0,0).setText(name)
            
            attrs = cmds.listAttr(node, r=True, w=True, v=True, k=True)
            self.table.setRowCount(len(attrs)+1)
            
            for row, name in enumerate(attrs):
                row += 1
                self.table.setRowHeight(row, 20)
                
                attr = '%s.%s' %(node,name)
                niceName = cmds.attributeName(attr)
                
                item = QtGui.QTableWidgetItem(niceName)
                item.setFlags(item.flags()^QtCore.Qt.ItemIsEditable)
                item.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
                self.table.setItem(row, 0, item)
                
                val = cmds.getAttr(attr)
                item = AttrItem()
                item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                item.setBackgroundColor(QtGui.QColor(40,40,40))
                item.attrName = attr
                item.attrVal = val
                item.setAttrValue(val)
                
                self.table.setItem(row, 1, item)
    # END def showAttributes
    
    def _setTableVisible(self, v):
        self.mainLayout.setCurrentIndex(1 if v else 0)
    # END def _setTableVisible
    
    @classmethod
    def showChannelBox(cls):
        '''
        Creates a ChannelBox widget inside of a Maya gockControl.
        Returns the dockControl path, and the ChannelBox widget.
        '''
        win = cls(parent=getMainWindow())
        size = win.size()
        
        name = mui.MQtUtil.fullName(long(sip.unwrapinstance(win)))
        
        dock = cmds.dockControl(
                allowedArea='all',
                area='right',
                floating=True,
                content=name,
                width=size.width(),
                height=size.height(),
                label='Custom ChannelBox')
        return dock, win
    # END def showChannelBox
# END class ChannelBox
        

@contextmanager
def noSignals(obj):
    ''' Context for blocking signals on a QDbject'''
    obj.blockSignals(True)
    yield
    obj.blockSignals(False)
# END def noSignals

        
class AttrItem(QtGui.QTableWidgetItem):
    '''
    Custom table widget item subclass for storing
    Maya attribute names and values
    Bacause we can set attribtes to whatever type we want,
    we can avoid dealing with QVariant objects throguh the 
    more common Qt approach of calling setData()/data()
    '''
    
    def __init__(self, val=None):
        super(AttrItem, self).__init__(self.UserType)
        
        self.attrName = ''
        self.attrVal = None
        
        if val is not None:
            self.setAttrValue(val)
    # END def __init__
            
    def setAttrValue(self, val):
        '''
        Set the value for this item.
        Checks the type of the value against the initial
        value type for this item when it was created.
        '''
        if self.attrVal is not None:
            typ = type(self.attrVal)
            try:
                val = typ(val)
            except ValueError:
                val = self.attrVal
            else:
                self.attrVal = val
            
            if isinstance(val, float):
                self.setText('%0.3f' %val)
            else:
                self.setText(str(val))
    # END def setAttrValue
# END class AttrItem


'''
Start in Maya with this command:

================================================================================
import sys

pathToDir = r"D:\Programare\PySide-PyQt\Tutorials\cmivfx - PyQt4 UI Development for Maya\PyQt for Maya"

if pathToDir not in sys.path:
    sys.path.append(pathToDir)

try:
    reload(channelBoxDesign)
except:
    import channelBoxDesign

dock, chan = channelBoxDesign.ChannelBox.showChannelBox()
================================================================================
'''
