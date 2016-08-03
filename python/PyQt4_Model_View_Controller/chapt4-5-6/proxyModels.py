#!/usr/bin/python

'''
@package   proxyModels
@brief     Creates a proxy model.
@details
@title     PyQt4 Model View Tutorial Part 05
@URL       https://www.youtube.com/watch?v=Dp-BRJer5CQ
@author    Remus Avram
@date      2014.12
'''

from PyQt4 import QtGui, QtCore, uic
import sys
from resources import icons_rc
from node import Node, TransformNode, CameraNode, LightNode
from models import SceneGraphModel


base, form = uic.loadUiType("Views/Window.ui")


class WindTutorial05(base, form):
    
    def __init__(self, parent=None):
        super(base, self).__init__(parent)
        self.setupUi(self)
        
        rootNode = Node("Hips")
        childNode0 = TransformNode("RightPirateLeg",        rootNode)
        childNode1 = Node("RightPirateLeg_END",             childNode0)
        childNode2 = CameraNode("LeftFemur",                rootNode)
        childNode3 = Node("LeftTibia",                      childNode2)
        childNode4 = Node("LeftFoot",                       childNode3)
        childNode5 = LightNode("LeftFoot_END",              childNode4)
        
        self._proxyModel = QtGui.QSortFilterProxyModel()
        
        """VIEW <-------> PROXY MODEL <-------> DATA MODEL """
        
        self._model = SceneGraphModel(rootNode)
        self._model.insertLights(0, 10)
        
        self._proxyModel.setSourceModel(self._model)
        self._proxyModel.setDynamicSortFilter(True)
        self._proxyModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        
        self.uiTree.setModel(self._proxyModel)
        
        QtCore.QObject.connect(self.uiFilter, QtCore.SIGNAL("textChanged(QString)"), self._proxyModel.setFilterRegExp)
        
        self.uiTree.setSortingEnabled(True)
    # END def __init__
# END class WindTutorial05


def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanlooks")
    wind = WindTutorial05()
    wind.show()
    
    sys.exit(app.exec_())
# END def main

if __name__ == '__main__': main()
