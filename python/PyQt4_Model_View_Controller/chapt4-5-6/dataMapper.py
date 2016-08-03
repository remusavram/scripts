#!/usr/bin/python

'''
@package   dataMapper
@brief     Creates a QDataWidgetMapper.
@details
@title     PyQt4 Model View Tutorial Part 06
@URL       https://www.youtube.com/watch?v=EmYby3BB3Kk&index=6&list=PL8B63F2091D787896
@author    Remus Avram
@date      2014.12
'''

from PyQt4 import QtGui, QtCore, uic
import sys
from resources import icons_rc
from node import Node, TransformNode, CameraNode, LightNode
from models import SceneGraphModel



base, form = uic.loadUiType("Views/Window.ui")
propBase, propForm = uic.loadUiType("Views/Editors.ui")
nodeBase, nodeForm = uic.loadUiType("Views/NodeEditor.ui") 
lightBase, lightForm = uic.loadUiType("Views/LightEditor.ui")
cameraBase, cameraForm = uic.loadUiType("Views/CameraEditor.ui")
transformBase, transfromForm = uic.loadUiType("Views/TransformEditor.ui")

class PropertiesEditor(propBase, propForm):
    '''PROPERTIESEDITOR'''
    def __init__(self, parent=None):
        super(propBase, self).__init__(parent)
        self.setupUi(self)
        self._proxyModel = None
        
        self._nodeEditor = NodeEditor(self)
        self._lightEditor = LightEditor(self)
        self._cameraEditor = CameraEditor(self)
        self._transformEditor = TransformEditor(self)
        
        self.layoutNode.addWidget(self._nodeEditor)
        self.layoutSpecs.addWidget(self._lightEditor)
        self.layoutSpecs.addWidget(self._cameraEditor)
        self.layoutSpecs.addWidget(self._transformEditor)
        
        self._lightEditor.setVisible(False)
        self._cameraEditor.setVisible(False)
        self._transformEditor.setVisible(False)
    # END def __init__
    
    def setSelection(self, current, old):
        """INPUTES: QModelIndex, QModelIndex"""
        current = self._proxyModel.mapToSource(current)
        node = current.internalPointer()
        
        if node is not None:
            typeInfo = node.typeInfo()
        
        if typeInfo == "CAMERA":
            self._cameraEditor.setVisible(True)
            self._lightEditor.setVisible(False)
            self._transformEditor.setVisible(False)
        
        elif typeInfo == "LIGHT":
            self._cameraEditor.setVisible(False)
            self._lightEditor.setVisible(True)
            self._transformEditor.setVisible(False)
        
        elif typeInfo == "TRANSFORM":
            self._cameraEditor.setVisible(False)
            self._lightEditor.setVisible(False)
            self._transformEditor.setVisible(True)
        
        else:
            self._cameraEditor.setVisible(False)
            self._lightEditor.setVisible(False)
            self._transformEditor.setVisible(False)
            
        self._nodeEditor.setSelection(current)
        self._cameraEditor.setSelection(current)
        self._lightEditor.setSelection(current)
        self._transformEditor.setSelection(current)
    # END def setSelection
    
    def setModel(self, proxyModel):
        self._proxyModel = proxyModel
        
        self._nodeEditor.setModel(self._proxyModel)
        self._lightEditor.setModel(self._proxyModel)
        self._cameraEditor.setModel(self._proxyModel)
        self._transformEditor.setModel(self._proxyModel)
    # END def setModel
# END class PropertiesEditor

class NodeEditor(nodeBase, nodeForm):
    '''Node'''
    def __init__(self, parent=None):
        super(nodeBase,self).__init__(parent)
        self.setupUi(self)
        self._dataMapper = QtGui.QDataWidgetMapper()
    # END def __init__
    
    def setModel(self, proxyModel):
        self._proxyModel = proxyModel
        self._dataMapper.setModel(proxyModel.sourceModel())
        
        self._dataMapper.addMapping(self.uiName, 0)
        self._dataMapper.addMapping(self.uiType, 1)
    # END def setModel
    
    def setSelection(self, current):
        """INPUTES: QModelIndex"""
        
        parent = current.parent()
        self._dataMapper.setRootIndex(parent)
        self._dataMapper.setCurrentModelIndex(current)
    # END def setSelection
# END class NodeEditor


class LightEditor(lightBase, lightForm):
    '''Light'''
    def __init__(self, parent=None):
        super(lightBase, self).__init__(parent)
        self.setupUi(self)
        self._dataMapper = QtGui.QDataWidgetMapper()
    # END def __init__
    
    def setModel(self, proxyModel):
        self._proxyModel = proxyModel
        self._dataMapper.setModel(proxyModel.sourceModel())
        
        self._dataMapper.addMapping(self.uiLightIntensity, 2)
        self._dataMapper.addMapping(self.uiNear, 3)
        self._dataMapper.addMapping(self.uiFar, 4)
        self._dataMapper.addMapping(self.uiShadow, 5)
    # END def setModel
    
    def setSelection(self, current):
        """INPUTES: QModelIndex"""
        
        parent = current.parent()
        self._dataMapper.setRootIndex(parent)
        self._dataMapper.setCurrentModelIndex(current)
    # END def setSelection
# END class LightEditor


class CameraEditor(cameraBase, cameraForm):
    '''Camera'''
    def __init__(self, parent=None):
        super(cameraBase, self).__init__(parent)
        self.setupUi(self)
        self._dataMapper = QtGui.QDataWidgetMapper()
    # END def __init__
    
    def setModel(self, proxyModel):
        self._proxyModel = proxyModel
        self._dataMapper.setModel(proxyModel.sourceModel())
        
        self._dataMapper.addMapping(self.uiMotionBlur, 2)
        self._dataMapper.addMapping(self.uiShakeIntensity, 3)
    # END def setModel
    
    def setSelection(self, current):
        """INPUTES: QModelIndex"""
        
        parent = current.parent()
        self._dataMapper.setRootIndex(parent)
        self._dataMapper.setCurrentModelIndex(current)
    # END def setSelection
# END class CameraEditor


class TransformEditor(transformBase, transfromForm):
    '''Camera'''
    def __init__(self, parent=None):
        super(transformBase, self).__init__(parent)
        self.setupUi(self)
        self._dataMapper = QtGui.QDataWidgetMapper()
    # END def __init__
    
    def setModel(self, proxyModel):
        self._proxyModel = proxyModel
        self._dataMapper.setModel(proxyModel.sourceModel())
        
        self._dataMapper.addMapping(self.uiX, 2)
        self._dataMapper.addMapping(self.uiY, 3)
        self._dataMapper.addMapping(self.uiZ, 4)
    # END def setModel
    
    def setSelection(self, current):
        """INPUTES: QModelIndex"""
        
        parent = current.parent()
        self._dataMapper.setRootIndex(parent)
        self._dataMapper.setCurrentModelIndex(current)
    # END def setSelection
# END class TransformEditor


class WindTutorial06(base, form):
    
    def __init__(self, parent=None):
        super(base, self).__init__(parent)
        self.setupUi(self)
        
        # creates some nodes
        rootNode = Node("hips")
        childNode0 = TransformNode("a",      rootNode)
        childNode1 = LightNode("b",          rootNode)
        childNode2 = CameraNode("c",         rootNode)
        childNode3 = TransformNode("d",      rootNode)
        childNode4 = LightNode("e",          rootNode)
        childNode5 = CameraNode("f",         rootNode)
        childNode6 = TransformNode("g",      rootNode)
        childNode7 = LightNode("h",          rootNode)
        childNode8 = CameraNode("i",         rootNode)
        
        self._proxyModel = QtGui.QSortFilterProxyModel(self)
        
        """VIEW <-------> PROXY MODEL <-------> DATA MODEL """
        
        self._model = SceneGraphModel(rootNode, self)
        
        self._proxyModel.setSourceModel(self._model)
        self._proxyModel.setDynamicSortFilter(True)
        self._proxyModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        
        self._proxyModel.setSortRole(SceneGraphModel.sortRole)
        self._proxyModel.setFilterRole(SceneGraphModel.filterRole)
        self._proxyModel.setFilterKeyColumn(0)
        
        self.uiTree.setModel(self._proxyModel)
        
        QtCore.QObject.connect(self.uiFilter, QtCore.SIGNAL("textChanged(QString)"), self._proxyModel.setFilterRegExp)
        
        self.uiTree.setSortingEnabled(True)
        
        self._propEditor = PropertiesEditor(self)
        self.layoutMain.addWidget(self._propEditor)
        self._propEditor.setModel(self._proxyModel)
        
        QtCore.QObject.connect(self.uiTree.selectionModel(), QtCore.SIGNAL("currentChanged(QModelIndex, QModelIndex)"), self._propEditor.setSelection)
    # END def __init__
# END class WindTutorial06



def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanlooks")
    wind = WindTutorial06()
    wind.show()
    sys.exit(app.exec_())
# END def main

if __name__ == '__main__': main()
