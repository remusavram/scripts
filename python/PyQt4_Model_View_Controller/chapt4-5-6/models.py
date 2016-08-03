#!/usr/bin/python

'''
@package   sceneGraphModel
@brief     
@details
@author    Remus Avram
@date      2014.12
'''

from PyQt4 import QtGui, QtCore
from node import Node, TransformNode, CameraNode, LightNode


class SceneGraphModel(QtCore.QAbstractItemModel):
    
    sortRole   = QtCore.Qt.UserRole
    filterRole = QtCore.Qt.UserRole + 1
    
    def __init__(self, root, parent=None):
        """INPUTS: Node, QObject"""
        super(SceneGraphModel, self).__init__(parent)
        self._rootNode = root
    # END def __init__
    
    def rowCount(self, parent):
        """IMPUTS: QModelIndex"""
        """OUTPUT: int"""
        if not parent.isValid():
            parentNode = self._rootNode
        else:
            parentNode = parent.internalPointer()
        return parentNode.childCount()
    # END def rowCount
    
    def columnCount(self, parent):
        """IMPUTS: QModelIndex"""
        """OUTPUT: int"""
        return 1
    # END def columnCount
    
    def data(self, index, role):
        """INPUTS: QModelIndex, int"""
        """OUTPUTS: QVariant, strings are cast to QString which is a QVariant"""
        if not index.isValid():
            return None
        
        node = index.internalPointer()
        typeInfo = node.typeInfo()
        
        if (role == QtCore.Qt.DisplayRole) or (role == QtCore.Qt.EditRole):
            if index.column() == 0:
                return node.name()
        
            if index.column() == 1:
                return node.typeInfo()
            
            if typeInfo == "CAMERA":
                if index.column() == 2:
                    return node.motionBlur()
                if index.column() == 3:
                    return node.shakeIntensity()
            
            if typeInfo == "LIGHT":
                if index.column() == 2:
                    return node.lightIntensity()
                if index.column() == 3:
                    return node.nearRange()
                if index.column() == 4:
                    return node.farRange()
                if index.column() == 5:
                    return node.castShadows()
            
            if typeInfo == "TRANSFORM":
                if index.column() == 2:
                    return node.x()
                if index.column() == 3:
                    return node.y()
                if index.column() == 4:
                    return node.z()
        
        if role == QtCore.Qt.DecorationRole:
            if index.column() == 0:
                typeInfo = node.typeInfo()
                
                if typeInfo == "LIGHT":
                    return QtGui.QIcon(QtGui.QPixmap(":/Light.png"))
                if typeInfo == "TRANSFORM":
                    return QtGui.QIcon(QtGui.QPixmap(":/Transform.png"))
                if typeInfo == "CAMERA":
                    return QtGui.QIcon(QtGui.QPixmap(":/Camera.png"))
        
        if role == SceneGraphModel.sortRole:
            return node.typeInfo()
        
        if role == SceneGraphModel.filterRole:
            return node.typeInfo()
    # END def data
    
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        """INPUTS: QModelIndex, QVariant, int (flag)"""
        if index.isValid():
            node = index.internalPointer()
            typeInfo = node.typeInfo()
            
            if role == QtCore.Qt.EditRole:
                if index.column() == 0:
                    node.setName(str(value.toString()))
                    
                if typeInfo == "CAMERA":
                    if index.column() == 2:
                        node.setMotionBlur(value.toString())
                    if index.column() == 3:
                        node.setShakeIntensity(value.toString())
                
                if typeInfo == "LIGHT":
                    if index.column() == 2:
                        node.setLightIntensity(value.toString())
                    if index.column() == 3:
                        node.setNearRange(value.toString())
                    if index.column() == 4:
                        node.setFarRange(value.toString())
                    if index.column() == 5:
                        node.setCastShadows(value.toString())
                
                if typeInfo == "TRANSFORM":
                    if index.column() == 2:
                        node.setX(value.toString())
                    if index.column() == 3:
                        node.setY(value.toString())
                    if index.column() == 4:
                        node.setZ(value.toString())
                    
                    self.dataChanged.emit(index, index)
                return True
        return False
    # END def setData

    def headerData(self, section, orientation, role):
        """INPUTS: int, Qt""Orientation, int"""
        """OUTPUTS: QVariant, strings are cast to QString which is a QVariant"""
        if role == QtCore.Qt.DisplayRole:
            if section == 0:
                return "Scenegraph"
            else:
                return "Typeinfo"
    # END def headerData
    
    def flags(self, index):
        """IMPUTS: QModelIndex"""
        """OUTPUT: int(flag)"""
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
    # END def flags
    
    def parent(self, index):
        """INPUTS: QModelIndex"""
        """OUTPUT: QModelIndex"""
        """Should return the parent of the node with the given QModelIndex"""
        node = self.getNode(index)
        parentNode = node.parent()
        
        if parentNode == self._rootNode:
            return QtCore.QModelIndex()
        
        return self.createIndex(parentNode.row(), 0, parentNode)
    # END def parent
    
    def index(self, row, column, parent):
        """INPUTS: int, int, QModelIndex"""
        """OUTPUT: QModelIndex"""
        """Should return a QModelIndex that corresponds to the given row, column and parent node"""
        
        parentNode = self.getNode(parent)
        
        childItem = parentNode.child(row)
        
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()
    # END def index
    
    def getNode(self, index):
        """CUSTOM"""
        """INPUTS: QModelIndex"""
        if index.isValid():
            node = index.internalPointer()
            if node:
                return node
        return self._rootNode
    # END def getNode
    
    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        """INPUTS: int, int, QMoldeIndex"""
        
        parentNode = self.getNode(parent)
        
        self.beginInsertRows(parent, position, position + rows - 1)
        
        for row in range(rows):
            childCount = parentNode.childCount()
            childNode = Node("untitled" + str(childCount))
            success = parentNode.insertChild(position, childNode)
        
        self.endInsertRows()
        
        return success
    # END def insertRows
    
    def insertLights(self, position, rows, parent=QtCore.QModelIndex()):
        """INPUTS: int, int, QMoldeIndex"""
        
        parentNode = self.getNode(parent)
        
        self.beginInsertRows(parent, position, position + rows - 1)
        
        for row in range(rows):
            childCount = parentNode.childCount()
            childNode = LightNode("light" + str(childCount))
            success = parentNode.insertChild(position, childNode)
        
        self.endInsertRows()
        
        return success
    # END def insertLights
    
    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        """INPUTS: int, int, QMoldeIndex"""
        
        parentNode = self.getNode(parent)
        
        self.beginRemoveRows(parent, position, position + rows - 1)
        
        for row in range(rows):
            success = parentNode.removeChild(position)
        
        self.endRemoveRows()
        
        return success
    # END def removeRows
# END class SceneGraphModel


def main():
    '''Only for tests'''
    nodeObject = Node("hips")
    graphModelObject = SceneGraphModel(nodeObject)
# END def main

if __name__ == '__main__': main()
