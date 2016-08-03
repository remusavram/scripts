#!/usr/bin/python

'''
@package   palletListViewMVC
@brief     
@details
@title     PyQt4 Model View Tutorial Part 02
@URL       https://www.youtube.com/watch?v=mCHVI8OXDxw&list=PL8B63F2091D787896
@author    Remus Avram
@date      2014.12
'''

from PyQt4 import QtGui, QtCore, uic
import sys


class PaletteListModel(QtCore.QAbstractListModel):
    ''' '''
    
    def __init__(self, colors=[], parent=None):
        '''Initializes the PaletteListModel.'''
        QtCore.QAbstractListModel.__init__(self,parent)
        self.__colors = colors
    # END def __init__
    
    def headerData(self, section, orientation, role):
        ''' '''
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return QtCore.QString("Palette")
            else:
                return QtCore.QString("Color %1").arg(section)
    # END def headerData
        
    def rowCount(self, parent):
        return len(self.__colors)
    # END def rowCount
    
    def data(self, index, role):
        ''' '''
        if role == QtCore.Qt.EditRole:
            return self.__colors[index.row()].name()
        
        if role == QtCore.Qt.ToolTipRole:
            return "Hex code: " + self.__colors[index.row()].name()
        
        if role == QtCore.Qt.DecorationRole:
            row = index.row()
            value =self.__colors[row]
            pixmap = QtGui.QPixmap(26,26)
            pixmap.fill(value)
            icon = QtGui.QIcon(pixmap)
            return icon
        
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value =self.__colors[row]
            return value.name()
    # END def data
    
    def flags(self, index):
        ''' '''
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
    # END def flags
    
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        ''' '''
        if role == QtCore.Qt.EditRole:
            row = index.row()
            color = QtGui.QColor(value)
            if color.isValid():
                self.__colors[row] = color
                self.dataChanged.emit(index, index)
                return True
        return False
    # END def setData
    
    
    #======================================================================#
    # INSERTING & REMOVING
    #======================================================================#
    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginInsertRows(QtCore.QModelIndex(), position, position + rows-1)
        for i in range(rows):
            self.__colors.insert(position, QtGui.QColor("#000000"))
        self.endInsertRows()
        return True
    # END def insertRows
    
    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(QtCore.QModelIndex(), position, position + rows-1)
        for i in range(rows):
            value = self.__colors[position]
            self.__colors.remove(value)
        self.endRemoveRows()
        return True
    # END def removeRows
    
# END class PaletteListModel



def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanlooks")
    
    
    # All OF OUR VIEWS
    listView = QtGui.QListView()
    listView.show()
    
    treeView = QtGui.QTreeView()
    treeView.show()
    
    comboBox = QtGui.QComboBox()
    comboBox.show()
    
    tableView = QtGui.QTableView()
    tableView.show()
    
    red   = QtGui.QColor(255,0,0)
    green = QtGui.QColor(0,255,0)
    blue  = QtGui.QColor(0,0,255)
    
    model = PaletteListModel([red, green, blue])
    
    listView.setModel(model)
    treeView.setModel(model)
    comboBox.setModel(model)
    tableView.setModel(model)
    
    model.insertRows(2, 5)
    model.removeRows(2, 5)
    
    sys.exit(app.exec_())
# END def main


if __name__ == '__main__': main()