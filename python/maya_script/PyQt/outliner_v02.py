'''
@package   
@brief     
@details   
@author    Remus Avram
@date      2014.12
'''

from PyQt4 import QtCore, QtGui
import sip

import maya.cmds as cmds
import maya.OpenMaya as om
import maya.OpenMayaUI as mui

from mQtUtil import getMainWindow


class Outliner(QtGui.QDialog):
    '''
    Custom dialog widget that emulates a few basic features
    of the Maya Outliner.
    '''
    
    def __init__(self, *args, **kwargs):
        super(Outliner, self).__init__(*args, **kwargs)
        
        self.resize(200,500)
        self.setObjectName("CustomOutliner")
        
        self.layout = QtGui.QVBoxLayout(self)
        self.layout.setMargin(2)
        
        self.menu = QtGui.QMenuBar()
        displayMenu = self.menu.addMenu('Display')
        sortMenu = displayMenu.addMenu('Sort Order')
        
        self.sortActions = QtGui.QActionGroup(sortMenu)
        
        self.sortAction1 = self.sortActions.addAction('Scene Hierarchy')
        self.sortAction1.setCheckable(True)
        self.sortAction1.setChecked(True)
        sortMenu.addAction(self.sortAction1)
        
        self.sortAction2 = self.sortActions.addAction('Alpabetical Within Type')
        self.sortAction2.setCheckable(True)
        sortMenu.addAction(self.sortAction2)
        self.layout.addWidget(self.menu)
        
        self.model = QtGui.QStandardItemModel()
        self.model.setItemPrototype(DagTreeItem())
        
        self.sortModel = QtGui.QSortFilterProxyModel()
        self.sortModel.setSourceModel(self.model)
        self.sortModel.setDynamicSortFilter(True)
        self.sortModel.setSortRole(QtCore.Qt.UserRole)
        
        view = QtGui.QTreeView()
        view.setModel(self.sortModel)
        view.header().setVisible(False)
        view.setEditTriggers(view.NoEditTriggers)
        view.setSelectionMode(view.ExtendedSelection)
        
        self.view = view
        self.layout.addWidget(self.view)
        
        QtCore.QTimer.singleShot(1, self.initDisplay)
        
        #self.view.expanded.connect(self.nodeExpanded)
        #self.view.selectionModel().selectionChanged.connect(self.selectionChanged)
        
        self.sortActions.triggered.connect(self.sortMethodChaged)
    # END def __init__
    
    def initDisplay(self):
        ''' Initialize the model with the root world items'''
        self.model.clear()
        
        excludes = set([
            '|growndPlane_transform',
            '|Mainpulator1',
            '|UniversalMainp',
            '|CubeCompass'
            ])
        
        roots = self.scanDag(mindepth=1, maxdepth=4, exclude=excludes)
        if roots:
            self.model.appendColumn(roots)
    # END def initDisplay
    
    """
    def nodeExpanded(self, idx):
        '''
        Slot to handle an item in the list being expanded.
        Populates the children of this items immediate children.
        '''
        idx = self.sortModel.mapToSource(idx)
        item = self.model.itemFromIndex(idx)
        if item.hasChildren():
            for row in xrange(item.rowCount()):
                child = item.child(row)
                child.removeRows(0, child.rowCount())
                grandChildren = self.scanDag(child)
                if grandChildren:
                    child.appendRows(grandChildren)
    # END def nodeExpanded
    
    
    def selectionChanged(self):
        '''
        Slot called when the selection of the view has changed.
        Selects the corresponding nodes in the Maya scene that
        match the selected view items.
        '''
        sel = (self.sortModel.mapToSoruce(i) for i in self.view.selectedIndexes())
        nodes = [self.model.itemFromIndex(1).fullname for i in self.view.selectedIndexes()]
        if nodes:
            cmds.select(nodes, replace=True)
        else:
            cmds.select(clear=True)
    # END def selectionChanged
    """
    
    def sortMethodChaged(self):
        '''
        Slot called when the sort method has changed in the UI
        and the model should have it's sort node changed.
        '''
        action = self.sortActions.checkedAction()
        if action is self.sortAction1:
            self.sortModel.sort(-1)
        elif action is self.sortAction2:
            self.sortModel.sort(0)
    # END def sortMethodChaged
    
    @staticmethod
    def scanDag(root=None, mindepth=1, maxdepth=1, exclude=None):
        '''
        Walks the DAG tree from a starting root, through a given depth
        range. Returns a list of the top level children of the root at
        DagTreeItem's Decendents of these items already haven been added
        as bagfreeitem children.
        '''
        if isinstance(root, DagTreeItem):
            root = root.dagObj
        
        dagIt = om.MItDag()
        root = root or dagIt.root()
        exclude = exclude or set()
        
        dagIt.reset(root, om.MItDag.kDepthFirst)
        
        nodes = []
        itemMap = {}
        
        while not dagIt.isDone():
            depth = dagIt.depth()
            if (maxdepth > -1) and (depth > maxdepth):
                dagIt.prune()
            elif depth >= mindepth:
                dagPath = om.MDagPath()
                dagIt.getPath(dagPath)
                path = dagPath.fullPathName()
                
                if path and path not in exclude:
                    item = DagTreeItem(dagPath)
                    itemMap[item.fullname] = item
                    parent = itemMap.get(item.parentname)
                    if parent:
                        parent.appendRow(item)
                    else:
                        nodes.append(item)
                else:
                    dagIt.prune()
            dagIt.next()
        return nodes                    
    # END def scanDag
# END class Outliner


class DagTreeItem(QtGui.QStandardItem):
    '''QStandardItem subclass that represents a Dag node'''
    
    def __init__(self, dagObj=None):
        super(DagTreeItem, self).__init__()
        
        self.dagObj = dagObj
        self.apiType = om.MFn.kInvalid
        self.setText(self.name)
        self.setData(self.sortKey, QtCore.Qt.UserRole)
    # END def __init__
    
    def __repr__(self):
        return "<%s: %s>" %(self.__class__.__name__, self.name)
    
    @property
    def sortKey(self):
        '''
        Computed property that builds a sort key based on a
        combination to attributes.
        Allows sorting to consider multiple keys.
        '''
        if self.dagObj:
            dagCopy = om.MDagPath(self.dagObj)
            
            try:
                dagCopy.extendToShape()
                self.apiType = dagCopy.apiType()
            except RuntimeError:
                self.apiType = self.dagObj.apiType()
        key = '{0}{1}'.format(self.apiType, self.name)
        return key
    # END def sortKey
    
    @property
    def fullname(self):
        if not self.dagObj:
            return ''
        return self.dagObj.fullPathName()
    # END def fullname
    
    @property
    def name(self):
        return self.fullname.rsplit('|', 1)[-1]
    
    @property
    def parentname(self):
        return self.fullname.rsplit('|', 1)[0]
# END class DagTreeItem



'''
Run in Maya:
================================================================================
import sys
from PyQt4 import QtGui

pathToDir = r"D:\Programare\PySide-PyQt\Tutorials\cmivfx - PyQt4 UI Development for Maya\PyQt for Maya"

if pathToDir not in sys.path:
    sys.path.append(pathToDir)

try:
    reload(outliner_v02)
except:
    import outliner_v02

o = outliner_v02.Outliner()
o.show()
================================================================================
'''
