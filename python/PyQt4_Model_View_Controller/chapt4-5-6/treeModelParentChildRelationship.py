#!/usr/bin/python

'''
@package   treeModelParentChildRelationship
@brief     Creates a treeView model using a parent-child relationship.
@details
@title     PyQt4 Model View Tutorial Part 04
@URL       https://www.youtube.com/watch?v=pr1M3mP7qfI
@author    Remus Avram
@date      2014.12
'''

from PyQt4 import QtGui, QtCore, uic
import sys
from resources import icons_rc
from node import Node, TransformNode, CameraNode, LightNode
from models import SceneGraphModel
    

def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanlooks")

    rootNode = Node("Hips")
    childNode0 = TransformNode("RightPirateLeg",        rootNode)
    childNode1 = Node("RightPirateLeg_END",             childNode0)
    childNode2 = CameraNode("LeftFemur",                rootNode)
    childNode3 = Node("LeftTibia",                      childNode2)
    childNode4 = Node("LeftFoot",                       childNode3)
    childNode5 = LightNode("LeftFoot_END",              childNode4)
    
    print rootNode
    
    model = SceneGraphModel(rootNode)
    
    treeView = QtGui.QTreeView()
    treeView.show()
    
    treeView.setModel(model)
    
    rightPirateLeg = model.index(0, 0, QtCore.QModelIndex())
    
    model.insertRows(1, 5, rightPirateLeg)
    model.insertLights(1, 5, rightPirateLeg)
    
    #model.removeRows(1,5)
    #model.removeRows(1,5)
    
    sys.exit(app.exec_())
# END def main

if __name__ == '__main__': main()
