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
        
        self.model = QtGui.QStandardItemModel()
        self.model.setItemPrototype(DagTreeItem())
        
        view = QtGui.QTreeView()
        view.setModel(self.model)
        view.header().setVisible(False)
        view.setEditTriggers(view.NoEditTriggers)
        view.setSelectionMode(view.ExtendedSelection)
        
        self.view = view
        self.layout.addWidget(self.view)
        
        QtCore.QTimer.singleShot(1, self.initDisplay)
        
        #self.view.expanded.connect(self.nodeExpanded)
        #self.view.selectionModel().selectionChanged.connect(self.selectionChanged)
    # END def __init__
    
    def initDisplay(self):
        ''' Initialize the modul with the root world items'''
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
        nodes = [self.model.itemFromIndex(1).fullname for i in self.view.selectedIndexes()]
        if nodes:
            cmds.select(nodes, replace=True)
        else:
            cmds.select(clear=True)
    # END def selectionChanged
    """
    
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
        self.setText(self.name)
    # END def __init__
    
    def __repr__(self):
        return "<%s: %s>" %(self.__class__.__name__, self.name)
    
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
    reload(outliner)
except:
    import outliner

o = outliner.Outliner()
o.show()
================================================================================
'''
