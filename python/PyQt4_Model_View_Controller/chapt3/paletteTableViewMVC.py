#!/usr/bin/python

'''
@package   palletTableViewMVC
@brief     
@details
@title     PyQt4 Model View Tutorial Part 03
@URL       https://www.youtube.com/watch?v=mCHVI8OXDxw&list=PL8B63F2091D787896
@author    Remus Avram
@date      2014.12
'''

from PyQt4 import QtGui, QtCore, uic
import sys

class PaletteTableModel(QtCore.QAbstractTableModel):
    ''' '''
    
    def __init__(self, colors=[[]],headers=[], parent=None):
        '''Initializes the PaletteListModel.'''
        QtCore.QAbstractTableModel.__init__(self,parent)
        self.__colors = colors
        self.__headers = headers
    # END def __init__
    
    def headerData(self, section, orientation, role):
        ''' '''
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section < len(self.__headers):
                    return self.__headers[section]
                else:
                    return "not implemented"
            else:
                return QtCore.QString("Color %1").arg(section)
    # END def headerData
    
    def rowCount(self, parent):
        return len(self.__colors)
    # END def rowCount
    
    def columnCount(self, parent):
        return len(self.__colors[0])
    # END def columnCount
    
    def data(self, index, role):
        ''' '''
        row = index.row()
        column = index.column()
        
        if role == QtCore.Qt.EditRole:
            return self.__colors[row][column].name()
        
        if role == QtCore.Qt.ToolTipRole:
            return "Hex code: " + self.__colors[row][column].name()
        
        if role == QtCore.Qt.DecorationRole:
            value =self.__colors[row][column]
            pixmap = QtGui.QPixmap(26,26)
            pixmap.fill(value)
            icon = QtGui.QIcon(pixmap)
            return icon
        
        if role == QtCore.Qt.DisplayRole:
            value =self.__colors[row][column]
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
            column = index.column()
            color = QtGui.QColor(value)
            if color.isValid():
                self.__colors[row][column] = color
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
            defaultValues = [QtGui.QColor("#000000") for i in range(self.columnCount(None))]
            self.__colors.insert(position, defaultValues)
        self.endInsertRows()
        return True
    # END def insertRows

    def insertColumns(self, position, columns, parent=QtCore.QModelIndex()):
        self.beginInsertColumns(QtCore.QModelIndex(), position, position + columns-1)
        rowCount = len(self.__colors)
        for i in range(columns):
            for j in range(rowCount):
                self.__colors[j].insert(position, QtGui.QColor("#000000"))
        self.endInsertColumns()
        return True
    # END def insertColumns
    
    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(QtCore.QModelIndex(), position, position + rows-1)
        for i in range(rows):
            value = self.__colors[position]
            self.__colors.remove(value)
        self.endRemoveRows()
        return True
    # END def removeRows
    
    def removeColumns(self, position, columns, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(QtCore.QModelIndex(), position, position + columns-1)
        rowCount = len(self.__colors)
        for i in range(columns):
            for j in range(rowCount):
                value = self.__colors[j][position]
                self.__colors[j].remove(value)
        self.endRemoveRows()
        return True
    # END def removeColumns
# END class PaletteTableModel



def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanlooks")
    
    tableView = QtGui.QTableView()
    tableView.show()
    
    rowCount    = 4
    columnCount = 6
    
    headers = ["Pallete0", "Colors", "Brushes", "Omg", "Technical", "Artist"]
    tableData0  = [ [QtGui.QColor("#FFFF00") for i in range(columnCount)] for j in range(rowCount)]
    
    model = PaletteTableModel(tableData0, headers)
    model.insertRows(3, 3)
    model.insertColumns(0, 5)
    model.removeRows(2, 2)
    model.removeColumns(2, 5)
    
    tableView.setModel(model)
    
    sys.exit(app.exec_())
# END def main


if __name__ == '__main__': main()
